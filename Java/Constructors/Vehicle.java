public class Vehicle {
    private double consumption; // liters/100km
    private int fuel; // liters
    private double distance = 0;
    //define setters:
    public void setConsumption(double con) {
        this.consumption = con;
    }
    public void setFuel(int fuel) {
        this.fuel = fuel;
    }
    // Contructor follows (Name is same as class with capital included):
    Vehicle(double con) {
        this.fuel = 55;
        this.setConsumption(con);
    }
    //define getter:
    public double getDistance() {
        this.distance = this.fuel / this.consumption * 100;
        return this.distance;
    }
}
