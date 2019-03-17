// do...while loop will always go through the loop at least once

class DoWhile {
    static public void main(String[] args) {
        boolean x = false;
	do {
	    System.out.println("This will be printed even if test is false");
	} while (x == true);
    }
}
