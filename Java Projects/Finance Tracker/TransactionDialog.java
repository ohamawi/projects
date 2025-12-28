import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Modality;
import javafx.stage.Stage;
import javafx.geometry.Insets;

import java.time.LocalDate;

public class TransactionDialog {

    public static Transaction showAndWait() {
        Stage stage = new Stage();
        stage.initModality(Modality.APPLICATION_MODAL);

        DatePicker datePicker = new DatePicker(LocalDate.now());
        TextField descriptionField = new TextField();
        descriptionField.setPromptText("Description");

        ComboBox<String> categoryBox = new ComboBox<>();
        categoryBox.getItems().addAll(
                "Food", "Rent", "Utilities", "Entertainment", "Income"
        );
        categoryBox.getSelectionModel().selectFirst();

        TextField amountField = new TextField();
        amountField.setPromptText("Amount");

        Button saveBtn = new Button("Save");
        Button cancelBtn = new Button("Cancel");

        final Transaction[] result = new Transaction[1];

        saveBtn.setOnAction(e -> {
            try {
                double amount = Double.parseDouble(amountField.getText());
                result[0] = new Transaction(
                        datePicker.getValue(),
                        descriptionField.getText(),
                        categoryBox.getValue(),
                        amount
                );
                stage.close();
            } catch (NumberFormatException ex) {
                new Alert(Alert.AlertType.ERROR, "Invalid amount").showAndWait();
            }
        });

        cancelBtn.setOnAction(e -> stage.close());

        VBox layout = new VBox(10,
                datePicker,
                descriptionField,
                categoryBox,
                amountField,
                new HBox(10, saveBtn, cancelBtn)
        );
        layout.setPadding(new Insets(10));

        stage.setScene(new Scene(layout, 300, 250));
        stage.setTitle("Add Transaction");
        stage.showAndWait();

        return result[0];
    }
}
