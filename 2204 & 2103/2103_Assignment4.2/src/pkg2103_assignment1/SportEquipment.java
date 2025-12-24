/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pkg2103_assignment1;

/**
 *
 * @author ponlawatchangto
 */
public class SportEquipment {
    
    private int id ;
    private String name ;
    private int type ;
    private float price ;
    private String image ;
    
    SportEquipment(int id , String name , int type , float price , String image) {
        this.id = id ;
        this.name = name ;
        this.type = type ;
        this.price = price ;
        this.image = image ;
    }
    int getID(){
        return id ;
    }
    void setID(int id) {
        this.id = id ;
    }
    String getName() {
        return this.name ;
    }
    void setName(String name) {
        this.name = name ;
    }
    int getType() {
        return this.type ;
    }
    void setType(int type) {
        this.type = type ;
    }
    float getPrice() {
        return this.price ;
    }
    void setPrice(float price) {
        this.price = price ;
    }
    String getImage() {
        return this.image ;
    }
    void setImage(String image) {
        this.image = image ;
    }
    
}
