import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.ArrayList;
import java.util.Scanner; // Import the Scanner class to read text files

public class ReadFile {
    

    public ReadFile(String gcValue) {
        this.gcValue = gcValue;
        this.firstTime = true;
    }
    public void readFile(String fileName, int linesToRead) {
    try {
        // For more security.
        // try catch
        String secureFilename;
        try {
          secureFilename = fileName.split(".")[0];
        } catch (ArrayIndexOutOfBoundsException e) {
          System.out.println("Error: Filename must have an extension.");
          secureFilename = fileName;
        }
        
        File myObj = new File(secureFilename);
        Scanner myReader = new Scanner(myObj);
        // this secures aginst overflow, by limiting the number of lines to read
        while (myReader.hasNextLine() || gcCount < linesToRead) {

        }
    } catch (FileNotFoundException e) {
        System.out.println("An error occurred.");
        e.printStackTrace();
    }
    }   
}