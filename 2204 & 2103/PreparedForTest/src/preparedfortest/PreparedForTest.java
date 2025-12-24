/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package preparedfortest;

/**
 *
 * @author ponlawatchangto
 */
public class PreparedForTest {
    
    int[] queue = {0,0,0,0,0,0,0,0,20,0} ;
    int front = 8 ;
    int rear = 8 ;
    int n = 10 ;
    int count = 1 ;
    
    void enqueue(int input) {
        if(count == n){
            System.out.print("Full");
            return ;
        }
        
        rear = (rear+1) % n ;
        count++ ;
        queue[rear] = input ;
    }

    void show() {
        System.out.print("{");
        for(int i = 0 ; i < n ; i++) {
            System.out.print(queue[i]);
            if (i != n-1) {
                System.out.print(",");
            }
        }
        System.out.println("}");
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        PreparedForTest obj = new PreparedForTest() ;
        obj.enqueue(70);
        obj.show();
        obj.enqueue(80);
        obj.show();
        obj.enqueue(45);
        obj.show();
        obj.enqueue(45);
        obj.show();
        obj.enqueue(45);
        obj.show();
        obj.enqueue(45);
        obj.show();
        obj.enqueue(45);
        obj.show();
        obj.enqueue(45);
        obj.show();
        obj.enqueue(45);
        obj.show();
        obj.enqueue(45);
        obj.show();
        obj.enqueue(45);
        obj.show();
        obj.enqueue(45);
        obj.show();
        obj.enqueue(45);
        obj.show();
        
    }
    
}
