#!/usr/bin/env groovy

class Global_local {
    static String myglobal = 'This is example of global variable defined inside class, but outside of method.';
    static void define_local() {
        String mylocal = 'This is example of local variable defined inside method.';
        println "Printing local variable inside its method:";
        println mylocal;
    }
    static void change_variables() {
        println "Printing global variable:";
        println this.myglobal;
        println "Changing global variable inside method:";
        this.myglobal = "New value of global variable.";
        println "Printing changed global variable:";
        println this.myglobal;
        print "\n";
        println "Trying to print local variable outside its method:";
        try {
            println this.mylocal;
        } catch(Exception) {
            println "Printing of local variable failed.";
        }
    }
    static void main(String[] args) {
        define_local();
        change_variables();
    }
}
