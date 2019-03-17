//Java.lang.Math;

class Vehicle_range {
    public static void main(String[] args) {
        Vehicle mycar = new Vehicle(6.5);
        double range = mycar.getDistance();
        long rounded_range = Math.round(range);
        System.out.println("Your range is " + String.valueOf(rounded_range) + "km.");
    }
}
