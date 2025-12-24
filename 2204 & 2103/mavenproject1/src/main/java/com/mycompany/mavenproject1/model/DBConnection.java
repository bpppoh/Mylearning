package com.mycompany.mavenproject1.model;
import java.sql.Connection;
import java.sql.DriverManager;

/**
 *
 * @author ponlawatchangto
 */ 

public class DBConnection {
    private static String jdbcURL = "jdbc:mysql://localhost/jsf?allowPublicKeyRetrieval=true&useSSL=false";
    private static String jdbcUsername = "root";
    private static String jdbcPassword = "651616";
    
    public static Connection getConnection() throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver") ;
        return DriverManager.getConnection(jdbcURL, jdbcUsername, jdbcPassword);
    }
}
