import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class PartTwo {
    private int totalFuel;
    private int mass;
    private int fuel;
    private ArrayList<Integer> massArrayList = new ArrayList<Integer>();
    private boolean firstTime;
    public PartTwo() {
        this.totalFuel = 0;
        this.mass = 0;
        this.fuel = 0;
        this.firstTime = true;
        
    }

    // Read file
    public void readFile(){
        try {
            // For more security.
            // try catch

            File myObj = new File("test.txt");
            Scanner myReader = new Scanner(myObj);
            // this secures aginst overflow, by limiting the number of lines to read
            while (myReader.hasNextLine()) {
                try {
                    int mass = myReader.nextInt();
                    System.out.println("inital mass: " + mass);
                    solveTotalFuel(mass);

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

    public void solveTotalFuel(int mass){
        if (firstTime == true){
            this.fuel = (int) (Math.floor(mass/3) - 2);
            System.out.println("DEBUG FIRST FIRST: " + fuel);
            firstTime = false;
            solveTotalFuel(this.fuel);
        }
        else {
        System.out.println("DEBUG FUEL:" + mass);
        this.mass = mass;
        this.fuel = 0;
        if ((int) (Math.floor(mass/3) - 2) <= 0){
            this.totalFuel += this.fuel;
            massArrayList.add(this.totalFuel);
            System.out.println("DEBUG123123123 :" + this.totalFuel);
        }
        else {
            this.fuel = (int) (Math.floor(mass/3) - 2);
            this.totalFuel += this.fuel;
            solveTotalFuel(this.fuel);
        }
        this.fuel = (int) Math.floor(mass/3) - 2;
        
        
        //System.out.println(this.fuel);
    }

    }

    public static void main(String[] args) {
        PartTwo partTwo = new PartTwo();
        partTwo.readFile();
        int sum = 0;
        for (int i = 0; i < partTwo.massArrayList.size(); i++){
            sum += partTwo.massArrayList.get(i);
        }
        System.out.println("SUM FINAL:" + sum);
    }
}
