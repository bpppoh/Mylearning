package com.mycompany.mavenproject1.controller;

import java.io.Serializable;
import java.sql.SQLException;
import java.util.Map;

import com.mycompany.mavenproject1.dao.ArtPieceDAO;
import com.mycompany.mavenproject1.dao.UserDAO;
import com.mycompany.mavenproject1.model.ArtPiece;
import com.mycompany.mavenproject1.model.User;

import jakarta.annotation.PostConstruct;
import jakarta.faces.application.FacesMessage;
import jakarta.faces.context.FacesContext;
import jakarta.faces.view.ViewScoped;
import jakarta.inject.Named;
import jakarta.servlet.http.HttpSession;

@Named("artPieceDetailBean")
@ViewScoped
public class ArtPieceDetailBean implements Serializable {

    private ArtPiece selectedArtPiece;
    private int artId;
    private User artist; 

    @PostConstruct
    public void init() {
        System.out.println("ArtPieceDetailBean: init() called.");
        Map<String, String> params = FacesContext.getCurrentInstance().getExternalContext().getRequestParameterMap();
        String idStr = params.get("id");
        System.out.println("ArtPieceDetailBean: Received idStr = " + idStr);

        if (idStr != null && !idStr.isEmpty()) {
            try {
                this.artId = Integer.parseInt(idStr);
                System.out.println("ArtPieceDetailBean: Parsed artId = " + this.artId);
                this.selectedArtPiece = ArtPieceDAO.findArtPieceById(artId);
                System.out.println("ArtPieceDetailBean: ArtPieceDAO.findArtPieceById returned " + (this.selectedArtPiece != null ? "NOT NULL" : "NULL"));
                
                // Fetch artist details if art piece is found
                if (this.selectedArtPiece != null) {
                    this.artist = UserDAO.findUserById(this.selectedArtPiece.getArtistId());
                    System.out.println("ArtPieceDetailBean: Artist for ArtPiece ID " + this.artId + " is " + (this.artist != null ? this.artist.getUsername() : "NULL"));
                }
            } catch (NumberFormatException e) {
                System.err.println("ArtPieceDetailBean: NumberFormatException for idStr: " + idStr);
                e.printStackTrace();
            } catch (SQLException e) {
                System.err.println("ArtPieceDetailBean: SQLException while fetching art piece or artist for id: " + this.artId);
                e.printStackTrace();
            }
        } else {
            System.out.println("ArtPieceDetailBean: idStr is null or empty.");
        }
        System.out.println("ArtPieceDetailBean: selectedArtPiece at end of init() is " + (this.selectedArtPiece != null ? "NOT NULL" : "NULL"));
    }

    public String buy() {
        FacesContext facesContext = FacesContext.getCurrentInstance();
        HttpSession session = (HttpSession) facesContext.getExternalContext().getSession(false);
        Integer userId = (session != null) ? (Integer) session.getAttribute("loggedInUserId") : null;

        // 1. Check if user is logged in
        if (userId == null) {
            facesContext.addMessage(null, new FacesMessage(FacesMessage.SEVERITY_WARN, "Login Required", "You must be logged in to purchase an item."));
            // Redirect to login page, but also pass the current art piece ID to return after login
            return "/login.xhtml?faces-redirect=true&from=/artPieceInformation.xhtml?id=" + this.artId;
        }

        // 2. Check if art piece exists and is available
        if (selectedArtPiece == null || selectedArtPiece.getStatus() != ArtPiece.Status.AVAILABLE) {
            facesContext.addMessage(null, new FacesMessage(FacesMessage.SEVERITY_ERROR, "Purchase Failed", "This art piece is no longer available."));
            return null; // Stay on the same page
        }

        // 3. Perform purchase
        try {
            ArtPieceDAO.updateStatus(selectedArtPiece.getId(), ArtPiece.Status.SOLD);
            // Refresh the local object's status
            selectedArtPiece.setStatus(ArtPiece.Status.SOLD);
            facesContext.addMessage(null, new FacesMessage(FacesMessage.SEVERITY_INFO, "Purchase Successful!", "Thank you for your purchase."));
        } catch (SQLException e) {
            e.printStackTrace();
            facesContext.addMessage(null, new FacesMessage(FacesMessage.SEVERITY_FATAL, "Database Error", "Could not complete the purchase. Please try again later."));
        }

        return null; // Stay on the same page to see the updated status
    }

    public ArtPiece getSelectedArtPiece() {
        return selectedArtPiece;
    }

    public void setSelectedArtPiece(ArtPiece selectedArtPiece) {
        this.selectedArtPiece = selectedArtPiece;
    }

    public int getArtId() {
        return artId;
    }

    public void setArtId(int artId) {
        this.artId = artId;
    }
    
    public User getArtist() {
        return artist;
    }

    public void setArtist(User artist) {
        this.artist = artist;
    }
}
