import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Main {

  public static void main(String[] args) {
    
    { 
     try {
    	 File information = new File("sample.txt");
       if (information.createNewFile()){
         System.out.println("Is This working?");
       }else{
         System.out.println("file Written");
       }
         String myData = WayScript.variables.get( "sample_data" ).toString();
       	 FileWriter data = new FileWriter(information);
       	 data.write(myData);	 
       	 data.close();
         
     } catch (IOException e) {
       e.printStackTrace();
 }
    }

    }
}