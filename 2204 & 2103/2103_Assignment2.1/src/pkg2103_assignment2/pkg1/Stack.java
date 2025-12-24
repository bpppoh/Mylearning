/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pkg2103_assignment2.pkg1;

/**
 *
 * @author ponlawatchangto
 */


public class Stack {

    int[] stackThing;
    int maxsize;
    int top;

    public Stack() {
        maxsize = 15;
        stackThing = new int[maxsize];
        top = -1;
    }

    public Stack(Stack stack) {
        this.stackThing = stack.stackThing;
        maxsize = stack.maxsize;
        this.top = stack.top;
    }

    public Stack(int size) {
        maxsize = size;
        stackThing = new int[maxsize];
        top = -1;
    }
    void push(int item) {
        if (top == maxsize-1) {
            System.out.println("Stack Overflow");
        } else {
            top = top + 1 ;
            stackThing[top] = item ;
        }
    }
    int pop() {
        if (top == -1) {
            System.out.println("Stack Underflow");
        } else {
            int item = stackThing[top--] ;
            return item ;
        }
        return -1 ;
    }
    boolean checkEmpty() {
        return top == -1 ;
    }
    boolean checkFull() {
        return top == maxsize - 1 ;
    }
}
