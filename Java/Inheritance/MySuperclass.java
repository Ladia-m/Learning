class MySuperclass {
    static protected double x = 1;
    static double pow(double a) {
        return Math.pow(a, x);
    }
}

class MySubclass extends MySuperclass {
    /*with constructor you can modify defined variables of superclass if not defined,
     *  it will use original value from superclass eg. x =1*/
    MySubclass() {
        x = 2;
    }
    // adding more methods in subclass...
    static int sum(int a, int b) {
        return a + b;
    }
    static void info() {
        System.out.println("You can use pow for power of 2 or you can use sum of int variables.");
    }
}
class MySubSubclass extends MySubclass {
    //Overloading: same name, but different parameters (it will choose the best suited method)
    static double sum(double a, double b) {
        return a + b;
    }
    //Overriding: subclass can implement a parent class method based on its requirement
    static void info() {
        System.out.println("You can use pow for power of 2 or you can use sum of int/double variables.");
    }
}

class Main {
    public static void main(String[] agrs) {
        MySubclass myobject1 = new MySubclass();
        myobject1.info();
        System.out.println(myobject1.pow(3));
        System.out.println(myobject1.sum(3, 1));
        MySubSubclass myobject2 = new MySubSubclass();
        myobject2.info();
        System.out.println(myobject2.sum(2, 3));
        System.out.println(myobject2.sum(2.5, 3.7));
    }
}

