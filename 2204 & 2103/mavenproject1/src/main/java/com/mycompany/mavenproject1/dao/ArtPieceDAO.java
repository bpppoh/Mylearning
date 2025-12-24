package com.mycompany.mavenproject1.dao;

import com.mycompany.mavenproject1.model.ArtPiece;
import com.mycompany.mavenproject1.model.DBConnection;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * ArtPieceDAO handles all database operations related to the ArtPiece entity.
 */
public class ArtPieceDAO {
    
    private static final Logger LOGGER = Logger.getLogger(ArtPieceDAO.class.getName());

    /**
     * Retrieves all art pieces from the database.
     * @return A list of all art pieces.
     * @throws SQLException if a database access error occurs.
     */
    public static List<ArtPiece> getAllArtPieces() throws SQLException {
        List<ArtPiece> artPieces = new ArrayList<>();
        String sql = "SELECT * FROM art_pieces ORDER BY created_at DESC";

        try (Connection conn = DBConnection.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                ArtPiece art = new ArtPiece();
                art.setId(rs.getInt("id"));
                art.setTitle(rs.getString("title"));
                art.setDescription(rs.getString("description"));
                byte[] imageData = rs.getBytes("image_data");
                art.setImageData(imageData); 

                art.setPrice(rs.getBigDecimal("price"));
                art.setStatus(ArtPiece.Status.valueOf(rs.getString("status")));
                art.setArtistId(rs.getInt("artist_id"));
                art.setCreatedAt(rs.getTimestamp("created_at").toLocalDateTime()); // Corrected column name
                art.setUpdatedAt(rs.getTimestamp("updated_at").toLocalDateTime());
                
                artPieces.add(art);
            }
        } catch (Exception e) {
            throw new SQLException("Error retrieving all art pieces.", e);
        }
        return artPieces;
    }

    /**
     * Finds a single art piece by its ID.
     * @param id The ID of the art piece to find.
     * @return An ArtPiece object if found, otherwise null.
     * @throws SQLException if a database access error occurs.
     */
    public static ArtPiece findArtPieceById(int id) throws SQLException {
        String sql = "SELECT * FROM art_pieces WHERE id = ?";
        ArtPiece art = null;

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setInt(1, id);

            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    art = new ArtPiece();
                    art.setId(rs.getInt("id"));
                    art.setTitle(rs.getString("title"));
                    art.setDescription(rs.getString("description"));
                    art.setImageData(rs.getBytes("image_data"));
                    art.setPrice(rs.getBigDecimal("price"));
                    art.setStatus(ArtPiece.Status.valueOf(rs.getString("status")));
                    art.setArtistId(rs.getInt("artist_id"));
                    art.setCreatedAt(rs.getTimestamp("created_at").toLocalDateTime());
                    art.setUpdatedAt(rs.getTimestamp("updated_at").toLocalDateTime());
                }
            }
        } catch (Exception e) {
            throw new SQLException("Error finding art piece by ID.", e);
        }
        
        return art;
    }
    
    /**
     * Updates the status of a specific art piece.
     * @param artId The ID of the art piece to update.
     * @param newStatus The new status to set.
     * @throws SQLException if a database access error occurs.
     */
    public static void updateStatus(int artId, ArtPiece.Status newStatus) throws SQLException {
        String sql = "UPDATE art_pieces SET status = ? WHERE id = ?";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setString(1, newStatus.name());
            pstmt.setInt(2, artId);
            pstmt.executeUpdate();
        } catch (Exception e) {
            throw new SQLException("Error updating art piece status.", e);
        }
    }
    
    /**
     * Creates a new art piece in the database.
     * @param art The art piece object to be created.
     * @throws SQLException if a database access error occurs.
     */
    public static void createArtPiece(ArtPiece art) throws SQLException {
        String sql = "INSERT INTO art_pieces (title, description, image_data, price, status, artist_id) VALUES (?, ?, ?, ?, ?, ?)";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setString(1, art.getTitle());
            pstmt.setString(2, art.getDescription());
            pstmt.setBytes(3, art.getImageData()); // Changed from String to byte array
            pstmt.setBigDecimal(4, art.getPrice());
            pstmt.setString(5, art.getStatus().name());
            pstmt.setInt(6, art.getArtistId());

            pstmt.executeUpdate();
        } catch (Exception e) {
            throw new SQLException("Error creating art piece.", e);
        }
    }

    // Other methods like findArtPieceById, updateArtPiece, etc. can be added here.
}
