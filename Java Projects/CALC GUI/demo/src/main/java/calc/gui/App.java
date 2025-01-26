package calc.gui;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class App extends Application {
    @Override
    public void start(Stage primaryStage) {
        //this is where the user inputs their variables. 
        Label label1 = new Label("Value for x:");
        TextField textField1 = new TextField();

        Label label2 = new Label("Value for y:");
        TextField textField2 = new TextField();

        CheckBox includeThirdValue = new CheckBox("Include a third value (z)");
        Label label3 = new Label("Value for z:");
        TextField textField3 = new TextField();
        label3.setVisible(false);
        textField3.setVisible(false);

        //this part lets me set the third value as visible or not
        includeThirdValue.setOnAction(e -> {
            boolean isSelected = includeThirdValue.isSelected();
            label3.setVisible(isSelected);
            textField3.setVisible(isSelected);
        });

        //this part lets the user choose the operation they want for their calculation.
        Label operationLabel = new Label("Choose an operation:");
        ComboBox<String> operations = new ComboBox<>();
        operations.getItems().addAll("+ (Add)", "- (Subtract)", "* (Multiply)", "/ (Divide)");
        operations.setValue("+ (Add)");

        //this is where the calculate button is used, and there the result is printed out.
        Button calculateButton = new Button("Calculate");
        Label resultLabel = new Label("Result: ");

        calculateButton.setOnAction(e -> {
            try {
                //the parse here allows for the number string that the user inputs to be turned into a double variable instead of an string.
                double num1 = Double.parseDouble(textField1.getText());
                double num2 = Double.parseDouble(textField2.getText());
                double num3 = includeThirdValue.isSelected() ? Double.parseDouble(textField3.getText()) : 0;
                boolean hasThirdValue = includeThirdValue.isSelected();

                //this checks for the operation given
                String operation = operations.getValue();
                double result;

                //these are the switch cases for the code to check the operation against the switch cases
                switch (operation.charAt(0)) {
                    case '+':
                        result = num1 + num2 + (hasThirdValue ? num3 : 0);
                        resultLabel.setText(String.format("Result: %.2f", result));
                        break;
                    case '-':
                        result = num1 - num2 - (hasThirdValue ? num3 : 0);
                        resultLabel.setText(String.format("Result: %.2f", result));
                        break;
                    case '*':
                        result = num1 * num2 * (hasThirdValue ? num3 : 1);
                        resultLabel.setText(String.format("Result: %.2f", result));
                        break;
                    case '/':
                        if (num2 != 0 && (!hasThirdValue || num3 != 0)) {
                            result = hasThirdValue ? num1 / num2 / num3 : num1 / num2;
                            resultLabel.setText(String.format("Result: %.2f", result));
                        } else {
                            resultLabel.setText("Error: Division by zero is not allowed.");
                        }
                        break;
                    default:
                        resultLabel.setText("Error: Invalid operation.");
                }
            } catch (NumberFormatException ex) {
                resultLabel.setText("Error: Please enter valid numbers.");
            }
        });

        //this part holds the GUIs layout, where VBox is the layout's main holder in Javafx. it makes the layout in a coloumn, and then i indent it by ten spaces with the ten between each, and 20 between the coloumns and the walls of the program. 
        VBox layout = new VBox(10);
        layout.setPadding(new Insets(20));
        layout.setAlignment(Pos.CENTER);
        layout.getChildren().addAll(
                label1, textField1,
                label2, textField2,
                includeThirdValue, label3, textField3,
                operationLabel, operations,
                calculateButton, resultLabel
        );

        // Scene and stage setup
        Scene scene = new Scene(layout, 400, 400);
        primaryStage.setTitle("JavaFX Calculator");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
