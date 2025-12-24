package com.mycompany.mavenproject1.model;

import java.math.BigDecimal;
import java.time.LocalDateTime;

import org.primefaces.model.StreamedContent;

public class ArtPiece {

    public enum Status {
        AVAILABLE,
        SOLD,
        NOT_FOR_SALE
    }

    private int id;
    private String title;
    private String description;
    private byte[] imageData; 
    private BigDecimal price;
    private Status status;
    private int artistId;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    
    private transient StreamedContent image;

    public ArtPiece() {
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public byte[] getImageData() {
        return imageData;
    }

    public void setImageData(byte[] imageData) {
        this.imageData = imageData;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        this.price = price;
    }

    public Status getStatus() {
        return status;
    }

    public void setStatus(Status status) {
        this.status = status;
    }

    public int getArtistId() {
        return artistId;
    }

    public void setArtistId(int artistId) {
        this.artistId = artistId;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }

    public StreamedContent getImage() {
        System.out.println("Model: getImage() called for ArtPiece ID " + this.id + ". Image is " + (this.image != null ? "NOT NULL" : "NULL"));
        return image;
    }

    public void setImage(StreamedContent image) {
        this.image = image;
    }
}
