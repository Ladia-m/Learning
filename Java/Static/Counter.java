public class Counter {
    public static int COUNT=0;
    public int num = 0;
    Counter() {
        COUNT++;
        num++;
    }
    public void setCount(int n) {
        COUNT += n;
    }
    public void setNum(int n) {
        num += n;
    }
}
