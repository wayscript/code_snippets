public class Main {
2
    // Ensure the class you would like to run has a "main" method
3
    public static void main(String[] args) {
4
      // Read a value from the variables Map
5
      String var = WayScript.variables.get( "Location" ).toString();
6
      double var2 = (double)WayScript.variables.get( "new_var" );
7
      System.out.println(var2);
8
      WayScript.variables.put( "variable_2", var );
9
    }
10
}