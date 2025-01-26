import java.util.Scanner;

public class CalcUpdated {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);

        double num1, num2, num3 = 0; // Third variable optional
        boolean hasThirdVariable = false;

        System.out.println("Input your values for the x and y:");
        num1 = scnr.nextDouble();
        num2 = scnr.nextDouble();

        System.out.println("Do you want to include a third value? (yes/no)");
        String response = scnr.next();

        if (response.equalsIgnoreCase("yes")) {
            System.out.println("Input your value for the third variable (z):");
            num3 = scnr.nextDouble();
            hasThirdVariable = true;
        }

        System.out.println("Would you like to add (+), subtract (-), multiply (*), or divide (/)?");
        char userOperation = scnr.next().charAt(0);

        double result;
        switch (userOperation) {
            case '+':
                result = num1 + num2 + (hasThirdVariable ? num3 : 0);
                System.out.println("Result: " + result);
                break;
            case '-':
                result = num1 - num2 - (hasThirdVariable ? num3 : 0);
                System.out.println("Result: " + result);
                break;
            case '*':
                result = num1 * num2 * (hasThirdVariable ? num3 : 1);
                System.out.println("Result: " + result);
                break;
            case '/':
                if (num2 != 0 && (!hasThirdVariable || num3 != 0)) {
                    result = hasThirdVariable ? num1 / num2 / num3 : num1 / num2;
                    System.out.println("Result: " + result);
                } else {
                    System.out.println("Error: Division by zero is not allowed.");
                }
                break;
            default:
                System.out.println("Error: Invalid operation.");
        }
    }
}