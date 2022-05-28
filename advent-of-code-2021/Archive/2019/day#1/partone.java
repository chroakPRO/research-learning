import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class partone {
    private int mass;
    private int fuel;
    private ArrayList<Integer> massArrayList = new ArrayList<Integer>();
    
    public partone() {
        this.mass = 0;
        this.fuel = 0;
    }

    public void solveProblemOne(int mass){
        this.mass = mass;
        this.fuel = 0;
        this.fuel = (int) Math.floor(mass/3) - 2;
        //System.out.println(this.fuel);
        massArrayList.add(this.fuel);

    }

    public void readFile(String fileName){
        try {
            // For more security.
            // try catch

        
            File myObj = new File("test.txt");
            Scanner myReader = new Scanner(myObj);
            // this secures aginst overflow, by limiting the number of lines to read
            while (myReader.hasNextLine()) {
                try {
                    int mass = myReader.nextInt();
                    solveProblemOne(mass);
                    System.out.println("DEBUG:" + mass);
                } catch (Exception e) {
                    System.out.println("Error: " + e);
                }
            }
            myReader.close();
            System.out.println("DEBUG MASS ARRAY LIST:" + massArrayList);
            int sum = 0;
            for (int i = 0; i < massArrayList.size(); i++){
                sum += massArrayList.get(i);
            }
            System.out.println("DEBUG SUM:" + sum);

        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    public void solveProblemTwo(){
        System.out.println("Problem Two");
    }

    public static void main(String[] args) {
        partone main = new partone();
       // main.solveProblemOne(1969);
        main.readFile("test.txt");
    }
}
