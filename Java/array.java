import java.util.*; //needed for List

class myArray {
    static public void main(String[] args) {
        System.out.println("Arrays:");
        int arr[] = new int[5]; //Java doesn allow array length modification
        for (int i=0; i<=4; i++) {
            arr[i] = i + 1;
        }
        for (int i: arr) {
            System.out.print(i);
        }
        System.out.print("\n");
        String arr2[] = {"A", "B", "C", "D", "E"}; //Short definition of list, where elements are already known
        for (String i: arr2) {
            System.out.print(i);
        }
        System.out.print("i\n\nLists:\n");
        List<Integer> mylist = new ArrayList<Integer>();
        for (int i=1; i<=5; i++) {
            mylist.add(i);
        }
        System.out.println("Length of list before: " + mylist.size());
        mylist.remove(4);
        System.out.println("Length of list after: " + mylist.size());
        mylist.set(0, 13); //replace 1st element in list with value 4
        System.out.println(mylist.get(0));
        System.out.println("\nMultidimensional arrays:");
        int[][] myintgrid = {{1,2,3},{4,5,6}};
        String[][] mystrgrid = new String[5][2];
        String abc = "ABCDE";
        for (int i=0; i<5; i++) {
            mystrgrid[i][0] = "Letter on position " + Integer.toString(i + 1) + " is: ";
            mystrgrid[i][1] = Character.toString(abc.charAt(i));
        }
        for (int i=0; i<5; i++) {
            System.out.println(mystrgrid[i][0] + mystrgrid[i][1]);
        }
    }
}        
