/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pkg2103_assignment3.pkg1;

/**
 *
 * @author ponlawatchangto
 */
public class Baggage {
    
    private int id ;
    private String type ;
    private String passengerID ;
//    private float cost ;
    
//    Type of baggage
//    carryOnBackpack   max 8.5kg   900฿ 400/kg
//    personalBag       max 10kg    500฿ 200/kg
//    checkedBag        max 35kg    700฿ 300/kg
//    largeDuffel       max 32kg    1500฿ 600/kg
    
    public Baggage() {
        type = "Not assigned" ;
        passengerID = "Not assigned" ;
    }
    public Baggage(int id ,String type , String passengerID , float weight) {
        this.id = id ;
        this.type = type ;
        this.passengerID = passengerID ;
    }
    
    public void setID(int id) { this.id = id ; }
    public int getID() { return id ; }
    
    public void setType(String type) { this.type = type; }
    public String getType() { return this.type ; }
    
    public void setPassengerID(String passengerID) { this.passengerID = passengerID ; }
    public String getPassengerID() { return passengerID ; }
    
}
