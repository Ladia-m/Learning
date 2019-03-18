public class MyClass {
    public static void main(String[] args) {
        // you can call COUNT because as static it belongs to class
        System.out.println(Counter.COUNT);
        /* next line will not work, you can't call non-static variable before creating instance, because
         * it is bounded to specifici instance. */
        //System.out.println(Counter.num);
        Counter c1 = new Counter();
        Counter c2 = new Counter();
        Counter c3 = new Counter();
        /*COUNT will increase with each new instance, because as static it belongs to class
         * and not to individual instances (it is shared) */
        System.out.println(String.valueOf(c1.COUNT) + " " + String.valueOf(c3.COUNT));
        /*num is not static (shared), therefore each instance of class has its own alocated
         * memory for num variable, so it starts at default value 0 within each instance */
        System.out.println(String.valueOf(c1.num) + " " + String.valueOf(c3.num));
        // add 5 to COUNT and num only to first instance of class (c1)
        c1.setCount(5);
        c1.setNum(5);
        // you can see that COUNT was increased for all instances, but num only for c1
        System.out.println(String.valueOf(c1.COUNT) + " " + String.valueOf(c3.COUNT));
        System.out.println(String.valueOf(c1.num) + " " + String.valueOf(c3.num));
    }
}
