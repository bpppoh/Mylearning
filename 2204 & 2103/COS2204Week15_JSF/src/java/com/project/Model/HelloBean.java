/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.project.Model;

import jakarta.inject.Named;
import jakarta.enterprise.context.RequestScoped;

/**
 *
 */
@Named(value = "HelloBean") 
@RequestScoped              
public class HelloBean {

    private String message;
    private String name ;

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    /**
     * Creates a new instance of HelloBean
     */
    public HelloBean() {
        this.message = "This message is sent by HelloBean Class object";
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}