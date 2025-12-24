package com.mycompany.mavenproject1.controller;

import com.mycompany.mavenproject1.dao.ArtPieceDAO;
import com.mycompany.mavenproject1.model.ArtPiece;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.faces.context.FacesContext;
import jakarta.faces.event.PhaseId;
import jakarta.inject.Named;
import org.primefaces.model.DefaultStreamedContent;
import org.primefaces.model.StreamedContent;

import java.io.ByteArrayInputStream;
import java.sql.SQLException;

@Named("imageStreamer")
@ApplicationScoped
public class ImageStreamer {

    public StreamedContent getImage() {
        FacesContext context = FacesContext.getCurrentInstance();

        // Check if we are in the RENDER_RESPONSE phase, if so, return a dummy content
        if (context.getCurrentPhaseId() == PhaseId.RENDER_RESPONSE) {
            return new DefaultStreamedContent();
        }
        
        // In the resource-loading phase, get the artId from the request parameters
        String artIdStr = context.getExternalContext().getRequestParameterMap().get("artId");
        if (artIdStr == null) {
            return null;
        }
        int artId = Integer.parseInt(artIdStr);

        try {
            ArtPiece art = ArtPieceDAO.findArtPieceById(artId);
            if (art != null && art.getImageData() != null) {
                System.out.println("ImageStreamer: Streaming image for artId: " + artId);
                return DefaultStreamedContent.builder()
                        .contentType("image/jpeg") // Or another appropriate content type
                        .stream(() -> new ByteArrayInputStream(art.getImageData()))
                        .build();
            } else {
                System.out.println("ImageStreamer: No image found for artId: " + artId);
                return null; // Or return a default "image not found" placeholder
            }
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }
    }
}
