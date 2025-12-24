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
    
    Stack stackA ;
    Stack stackB ;
    Stack stackC ;
    int stackSize = 10 ;
    
    Info() {
        stackA = new Stack(stackSize) ;
        stackB = new Stack(stackSize) ;
        stackC = new Stack(stackSize) ;
    }
    Info(int size) {
        stackSize = size ;
        stackA = new Stack(stackSize) ;
        stackB = new Stack(stackSize) ;
        stackC = new Stack(stackSize) ;
    }
    

    class Stack {
        private int size = 10 ;
        private int top = -1 ;
        private int[] array ;
        
        Stack() {
            array = new int[size] ;
        }
        Stack(int size) {
            array = new int[this.size = size] ;
        }
        
        int push(int input) {
            array[++top] = input ;
            return input ;
        }
        int pop() {
            return array[top--] ;
        }
        int getTop() {
            return top ;
        }
        Boolean isEmpty() {
            return (top == -1) ;
        }
        Boolean isFull() {
            return (top >= size-1) ;
        }
        int[] getArray() {
            return array ;
        }
    }
    
}
