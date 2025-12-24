/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */

import java.io.IOException;
import java.io.PrintWriter;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;

/**
 *
 * @author ponlawatchangto
 */
@WebServlet(urlPatterns = {"/ShowDB"})
public class ShowDB extends HttpServlet {

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
        PrintWriter out = response.getWriter();
        try {
            try {
                Class.forName("com.mysql.cj.jdbc.Driver") ;
            } catch (Exception e) {e.printStackTrace();}
            try {
                Connection c = DriverManager.getConnection("jdbc:mysql://localhost/shirts_db?autoRecconnect=true&useSSL=false", "root", "651616");
                Statement s = c.createStatement();
                ResultSet r = s.executeQuery("Select * from resume");
//                out.print("**********************************************************<br>");
//                out.print("     ID        Name           Surname        Address      <br>");
//                out.print("**********************************************************<br>");
                while (r.next()) {
                    out.print("  " + r.getString("shirt_id") + "   " + r.getString("article") + "     " + r.getString("color")
                            + "        " + r.getString("shirt_size") + "        " + r.getString("last_worn") + "<br>");
                }
                s.close();
                r.close();
            } catch (SQLException e) {e.printStackTrace();}
        } finally { 
            out.close();
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
