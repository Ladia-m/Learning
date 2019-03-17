import java.util.Scanner;

class input {
  public static void main(String[] args) {
    Scanner reader = new Scanner(System.in);
    System.out.print("Insert text: ");
    String mystring = reader.next();
    System.out.println(mystring);
    System.out.print("Insert number: ");
    int myint = reader.nextInt();
    System.out.println(myint);
  }
}

