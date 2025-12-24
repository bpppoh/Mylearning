package com.mycompany.mavenproject1.controller;

import java.sql.SQLException;

import com.mycompany.mavenproject1.dao.UserDAO;
import com.mycompany.mavenproject1.model.User;

import jakarta.enterprise.context.RequestScoped;
import jakarta.faces.application.FacesMessage;
import jakarta.faces.context.FacesContext;
import jakarta.inject.Named;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

@Named("userBean")
@RequestScoped
public class UserBean {

    private String username;
    private String email;
    private String password;

    public String register() {
        User newUser = new User();
        newUser.setUsername(username);
        newUser.setEmail(email);
        newUser.setPassword(password);

        try {
            UserDAO.createUser(newUser);
            FacesContext.getCurrentInstance().getExternalContext().getFlash().setKeepMessages(true);
            FacesContext.getCurrentInstance().addMessage(null, new FacesMessage(FacesMessage.SEVERITY_INFO, "Registration Successful!", "You can now log in."));
            return "login?faces-redirect=true";
        } catch (SQLException e) {
            FacesContext.getCurrentInstance().addMessage(null, 
                new FacesMessage(FacesMessage.SEVERITY_ERROR, "Registration Failed", "Username or email may already exist."));
            e.printStackTrace();
            return null;
        }
    }

    public String login() {
        try {
            User user = UserDAO.findUserByUsername(username);

            if (user != null && user.getPassword().equals(password)) {
                FacesContext facesContext = FacesContext.getCurrentInstance();
                
                HttpSession session = (HttpSession) facesContext.getExternalContext().getSession(true);
                session.setAttribute("loggedInUserId", user.getId());

                HttpServletResponse response = (HttpServletResponse) facesContext.getExternalContext().getResponse();
                Cookie userCookie = new Cookie("username", user.getUsername());
                userCookie.setMaxAge(60 * 60 * 24); // Cookie expires in 1 day
                response.addCookie(userCookie);

                return "index?faces-redirect=true";
            } else {
                FacesContext.getCurrentInstance().addMessage(null,
                        new FacesMessage(FacesMessage.SEVERITY_ERROR, "Login Failed", "Invalid username or password."));
                return null;
            }
        } catch (SQLException e) {
            FacesContext.getCurrentInstance().addMessage(null,
                    new FacesMessage(FacesMessage.SEVERITY_FATAL, "Database Error", "An error occurred while trying to log in."));
            e.printStackTrace();
            return null;
        }
    }

    public String logout() {
        FacesContext facesContext = FacesContext.getCurrentInstance();
        
        HttpSession session = (HttpSession) facesContext.getExternalContext().getSession(false);
        if (session != null) {
            session.invalidate();
        }

        HttpServletResponse response = (HttpServletResponse) facesContext.getExternalContext().getResponse();
        Cookie userCookie = new Cookie("username", null);
        userCookie.setMaxAge(0); // Set max age to 0 to delete the cookie
        response.addCookie(userCookie);

        return "index?faces-redirect=true";
    }

    public String getPostArtOutcome() {
        if (isLoggedIn()) {
            return "/add_art.xhtml?faces-redirect=true";
        } else {
            return "/login.xhtml?faces-redirect=true";
        }
    }

    public boolean isLoggedIn() {
        FacesContext facesContext = FacesContext.getCurrentInstance();
        HttpSession session = (HttpSession) facesContext.getExternalContext().getSession(false);
        return session != null && session.getAttribute("loggedInUserId") != null;
    }

    // --- Standard Getters and Setters ---

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
