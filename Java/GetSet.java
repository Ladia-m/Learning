class Car {
    private int horsepower;
    private String speed;
    public void setHorsepower(int hp) { //to set value for variable from outside of class, you need to use set function
        this.horsepower = hp;
        if (horsepower < 100) {
            speed = "slow";
        } else if (horsepower < 200) {
            speed = "moderate";
        } else if (horsepower < 500) {
            speed = "fast";
        } else if (horsepower < 1000) {
            speed = "superfast";
        } else {
            speed = "ludicrous";
        }
    }
    public String getSpeed() { //to retrieve class variable from outside of class, you need to set get function
        return speed;
    }
    void coment() {
        if (horsepower < 100) {
            System.out.println("Isn't bicycle faster?");
        } else if (horsepower < 200) {
            System.out.println("So what?");
        } else if (horsepower < 500) {
            System.out.println("Nice ride!");
        } else if (horsepower < 1000) {
            System.out.println("WOW!");
        } else {
            System.out.println("are you crazy?");
        }
    }
}

class Show_off {  //This class should be public because it contains main code, and therefore written in its own file
    public static void main(String[] args) {
        Car mycar = new Car();
        mycar.setHorsepower(540);
        String speed = mycar.getSpeed();
        System.out.println("Speed of your car is " + speed);
        mycar.coment();
    }
}
