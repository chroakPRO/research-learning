import java.util.Scanner;

public class FiboNaci {
    private static int count;
    private static int max;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        FiboNaci.setMax(6);
        System.out.println(FiboNaci.fibonacci(n));
    }

    
   //Create a recursive function that returns the nth Fibonacci number.
    public static long fibonacci(int n) {
        
        
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        if (count == max) {
            return n;
        }
        count++;
        return fibonacci(n - 1) + fibonacci(n - 2);
    } 

    public static void setMax(int max) {
        FiboNaci.max = max;
    }

}

