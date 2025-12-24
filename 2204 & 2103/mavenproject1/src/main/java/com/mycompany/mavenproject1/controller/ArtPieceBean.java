package com.mycompany.mavenproject1.controller;

import java.io.IOException;
import java.io.InputStream;
import java.io.Serializable;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.primefaces.model.file.UploadedFile;

import com.mycompany.mavenproject1.dao.ArtPieceDAO;
import com.mycompany.mavenproject1.model.ArtPiece;

import jakarta.annotation.PostConstruct;
import jakarta.faces.application.FacesMessage;
import jakarta.faces.context.FacesContext;
import jakarta.faces.view.ViewScoped;
import jakarta.inject.Named;
import jakarta.servlet.http.HttpSession;

@Named("artPieceBean")
@ViewScoped
public class ArtPieceBean implements Serializable {

    private List<ArtPiece> allArtPieces = new ArrayList<>();
    private List<ArtPiece> filteredArtPieces = new ArrayList<>();
    private String filterStatus = "All"; 
    private List<String> statusOptions;

    private ArtPiece newArtPiece = new ArtPiece();
    private UploadedFile file;

    @PostConstruct
    public void init() {
        try {
            allArtPieces = ArtPieceDAO.getAllArtPieces();
            filteredArtPieces.addAll(allArtPieces); 
        } catch (SQLException e) {
            e.printStackTrace();
            FacesContext.getCurrentInstance().addMessage(null, new FacesMessage(FacesMessage.SEVERITY_ERROR, "Error", "Could not load art pieces."));
        }
        statusOptions = Arrays.asList("All", "AVAILABLE", "SOLD", "NOT_FOR_SALE");
    }

    public void onFilterChange() {
        if (filterStatus == null || filterStatus.equals("All")) {
            filteredArtPieces = new ArrayList<>(allArtPieces);
        } else {
            List<ArtPiece> resultList = new ArrayList<>();

            for (ArtPiece art : allArtPieces) {
                if (art.getStatus().name().equals(filterStatus)) {
                    resultList.add(art);
                }
            }

            filteredArtPieces = resultList;
        }
    }

    public String createArtPiece() {
        FacesContext facesContext = FacesContext.getCurrentInstance();
        HttpSession session = (HttpSession) facesContext.getExternalContext().getSession(false);
        Integer artistId = (session != null) ? (Integer) session.getAttribute("loggedInUserId") : null;

        if (artistId == null) {
            facesContext.addMessage(null, new FacesMessage(FacesMessage.SEVERITY_ERROR, "Not Logged In", "You must be logged in to post art."));
            return null;
        }

        if (file != null && file.getFileName() != null && !file.getFileName().isEmpty()) {
            try (InputStream input = file.getInputStream()) {
                byte[] imageData = input.readAllBytes();
                newArtPiece.setImageData(imageData);
            } catch (IOException e) {
                e.printStackTrace();
                facesContext.addMessage(null, new FacesMessage(FacesMessage.SEVERITY_ERROR, "File Read Failed", e.getMessage()));
                return null;
            }
        } else {
             facesContext.addMessage(null, new FacesMessage(FacesMessage.SEVERITY_ERROR, "File Required", "Please select an image to upload."));
             return null;
        }

        try {
            newArtPiece.setArtistId(artistId);
            newArtPiece.setStatus(ArtPiece.Status.AVAILABLE);
            ArtPieceDAO.createArtPiece(newArtPiece);
            return "gallery?faces-redirect=true";
        } catch (SQLException e) {
            e.printStackTrace();
            facesContext.addMessage(null, new FacesMessage(FacesMessage.SEVERITY_ERROR, "Database Error", "Could not save the art piece."));
            return null;
        }
    }


    public List<ArtPiece> getFilteredArtPieces() {
        return filteredArtPieces;
    }

    public String getFilterStatus() {
        return filterStatus;
    }

    public void setFilterStatus(String filterStatus) {
        this.filterStatus = filterStatus;
    }

    public List<String> getStatusOptions() {
        return statusOptions;
    }

    public ArtPiece getNewArtPiece() {
        return newArtPiece;
    }

    public void setNewArtPiece(ArtPiece newArtPiece) {
        this.newArtPiece = newArtPiece;
    }

    public UploadedFile getFile() {
        return file;
    }

    public void setFile(UploadedFile file) {
        this.file = file;
    }
}
