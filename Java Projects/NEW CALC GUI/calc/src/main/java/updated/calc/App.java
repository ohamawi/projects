package updated.calc;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class App extends Application {
    private TextField display;
    private double firstOperand = 0;
    private String operator = "";
    private boolean startNewInput = true;

    @Override
    public void start(Stage primaryStage) {
        // display for the numbers
        display = new TextField();
        display.setEditable(false);
        display.setAlignment(Pos.CENTER_RIGHT);
        display.setStyle("-fx-font-size: 20px;");
        
        // button grid
        GridPane grid = new GridPane();
        grid.setPadding(new Insets(10));
        grid.setHgap(5);
        grid.setVgap(5);
        grid.setAlignment(Pos.CENTER);
        
        // buttons for numbers and operations
        String[] buttonLabels = {
            "7", "8", "9", "/", 
            "4", "5", "6", "*", 
            "1", "2", "3", "-", 
            "C", "0", "=", "+"
        };

        int row = 1;
        int col = 0;

        for (String label : buttonLabels) {
            Button button = new Button(label);
            button.setStyle("-fx-font-size: 18px; -fx-min-width: 60px; -fx-min-height: 60px;");
            button.setOnAction(e -> handleButtonClick(label));
            grid.add(button, col, row);

            col++;
            if (col == 4) {
                col = 0;
                row++;
            }
        }


        GridPane root = new GridPane();
        root.setPadding(new Insets(10));
        root.setVgap(10);
        root.add(display, 0, 0, 4, 1);
        root.add(grid, 0, 1);

        Scene scene = new Scene(root, 300, 400);
        primaryStage.setTitle("Calculator");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void handleButtonClick(String label) {
        switch (label) {
            case "C":
                display.clear();
                firstOperand = 0;
                operator = "";
                startNewInput = true;
                break;
            case "=":
                calculateResult();
                startNewInput = true;
                break;
            case "+": case "-": case "*": case "/":
                operator = label;
                firstOperand = Double.parseDouble(display.getText());
                startNewInput = true;
                break;
            default: // this is what lets you write numbers
                if (startNewInput) {
                    display.clear();
                    startNewInput = false;
                }
                display.appendText(label);
        }
    }

    private void calculateResult() {
        if (!operator.isEmpty() && !display.getText().isEmpty()) {
            double secondOperand = Double.parseDouble(display.getText());
            double result = 0;
            
            switch (operator) {
                case "+": result = firstOperand + secondOperand; break;
                case "-": result = firstOperand - secondOperand; break;
                case "*": result = firstOperand * secondOperand; break;
                case "/": 
                    if (secondOperand != 0) {
                        result = firstOperand / secondOperand;
                    } else {
                        display.setText("Error: /0");
                        return;
                    }
                    break;
            }

            display.setText(String.valueOf(result));
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
