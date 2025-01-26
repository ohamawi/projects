import java.util.Scanner;  // this is how i can get user input

public class MyClass {
  public static void main(String args[]) {
      
    Scanner scnr = new Scanner(System.in);
    
    double num1;
    double num2;
    
    System.out.println("Input your values for the x and y");
    
    num1 = scnr.nextDouble();
    
    num2 = scnr.nextDouble();
    
    System.out.println("Would you like to add (+), subtract (-), multiply (*) or division (/)");
   
    char userOperation = scnr.next().charAt(0);
    
    double result;
    
    switch (userOperation) {
        case '+':
            result = num1 + num2;
            System.out.println("Result: " + result);
            break;
        case '-':
            result = num1 - num2;
            System.out.println("Result: " + result);
            break;
        case '*':
            result = num1 * num2;
            System.out.println("Result: " + result);
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
                System.out.println("Result: " + result);
                }
            else {
                System.out.println("Error: Division by zero is not allowed.");
                }
                break;
        default:
            System.out.println("Error: Invalid operation.");
        }
  }
}