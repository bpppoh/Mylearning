/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package stack;
import java.util.Stack;

/**
 *
 * @author ponlawatchangto
 */
public class Info {

    private Stack<Integer> stackA ;
    private Stack<Integer> stackB ;
    private Stack<Integer> stackC ;
    private int stackSize ;
    
    Info() {
        stackA = new Stack<Integer>() ;
        stackB = new Stack<Integer>() ;
        stackC = new Stack<Integer>() ;
        stackSize = 10 ;
    }
    Info(int size) {
        stackA = new Stack<Integer>() ;
        stackB = new Stack<Integer>() ;
        stackC = new Stack<Integer>() ;
        stackSize = size ;
    }
    
    Stack<Integer> getStackA () {
        return stackA ;
    }
    Stack<Integer> getStackB () {
        return stackB ;
    }
    Stack<Integer> getStackC () {
        return stackC ;
    }
    
    
}
