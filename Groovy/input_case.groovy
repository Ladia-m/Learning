#!/usr/bin/groovy

/* This is just example showing possible way to use class, method and simple commands */

class SimpleCalculator {
    /* static:
    *  Static methods are available to every instance of a class, cannot access instance 
    *  variables or methods directly, can be accessed without having to create a new object. 
    *  void:
    *  Basicaly means it will not return any output (except output to console via print cmd.
    */
    static void description() {
        println("This is simple calculator!\n\tFirst enter two numbers and then select operation you would like to do");
    }
    static get_input() {
        print "Enter first # : ";
        def x = System.in.newReader().readLine() as Integer;

        print "Enter second # : ";
        def y = System.in.newReader().readLine() as Integer;

        println "What you want to do? \n +\n -\n *\n /";
        def operation = System.in.newReader().readLine() as char;
        return [x, y, operation]
    }
    static void give_result(x = 0, y = 0, operation = '') {
        switch(operation) {
            case '+':
                println x + y;
                break;
            case '-':
                println x - y;
                break;
            case '*':
                println x * y;
                break;
            case '/':
                println x / y;
                break;
            default:
                println "Wrong operation selected, terminating...";
                break;
        }
    }
    static void main(String[] args) {
        description();
        def (x, y, operation) = get_input();
        give_result(x, y, operation);
    }
}
