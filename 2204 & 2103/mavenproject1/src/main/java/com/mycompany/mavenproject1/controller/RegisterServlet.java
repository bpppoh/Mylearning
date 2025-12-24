/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */
package com.mycompany.mavenproject1.controller;

import com.mycompany.mavenproject1.dao.UserDAO;
import com.mycompany.mavenproject1.model.User;
import java.io.IOException;
import java.io.PrintWriter;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.SQLException;

/**
 *
 * @author ponlawatchangto
 */
@WebServlet(name = "NewServlet", urlPatterns = {"/NewServlet"})
public class RegisterServlet extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        
        String username = request.getParameter("username");
        String email = request.getParameter("email");
        String password = request.getParameter("password"); // Storing plain text password as requested.

        // 2. Create a new User object
        User newUser = new User();
        newUser.setUsername(username);
        newUser.setEmail(email);
        newUser.setPassword(password); // In a real app, this MUST be hashed.

        try {
            // 3. Use the DAO to create the user in the database
            UserDAO.createUser(newUser);
            
            // 4. On success, redirect to a login page (we assume login.jsp or login.xhtml will exist)
            // You can add a success message to the session if you want.
            // e.g., request.getSession().setAttribute("successMessage", "Registration successful! Please log in.");
            response.sendRedirect("login.xhtml");

        } catch (SQLException e) {
            // Handle potential database errors (e.g., duplicate username/email)
            // In a real app, you'd provide a more user-friendly error message.
            e.printStackTrace(); // Log the error for the developer
            request.setAttribute("errorMessage", "Registration failed. The username or email may already be in use.");
            request.getRequestDispatcher("/register.xhtml").forward(request, response);
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
