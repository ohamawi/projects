import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import javafx.geometry.Insets;

import java.util.List;

public class MainApp extends Application {

    private ObservableList<Transaction> transactions;

    @Override
    public void start(Stage stage) {

        transactions = FXCollections.observableArrayList();

        List<Transaction> loaded = FileManager.load();
        if (loaded != null) {
            transactions.addAll(loaded);
        }

        TableView<Transaction> table = new TableView<>(transactions);

        TableColumn<Transaction, String> dateCol = new TableColumn<>("Date");
        dateCol.setCellValueFactory(d ->
                new javafx.beans.property.SimpleStringProperty(
                        d.getValue().getDate().toString()
                )
        );

        TableColumn<Transaction, String> descCol = new TableColumn<>("Description");
        descCol.setCellValueFactory(d ->
                new javafx.beans.property.SimpleStringProperty(
                        d.getValue().getDescription()
                )
        );

        TableColumn<Transaction, String> catCol = new TableColumn<>("Category");
        catCol.setCellValueFactory(d ->
                new javafx.beans.property.SimpleStringProperty(
                        d.getValue().getCategory()
                )
        );

        TableColumn<Transaction, String> amtCol = new TableColumn<>("Amount");
        amtCol.setCellValueFactory(d ->
                new javafx.beans.property.SimpleStringProperty(
                        String.format("%.2f", d.getValue().getAmount())
                )
        );

        table.getColumns().addAll(dateCol, descCol, catCol, amtCol);

        Button addBtn = new Button("Add");
        addBtn.setOnAction(e -> {
            Transaction t = TransactionDialog.showAndWait();
            if (t != null) {
                transactions.add(t);
            }
        });

        BorderPane root = new BorderPane();
        root.setCenter(table);
        root.setBottom(new HBox(10, addBtn));
        BorderPane.setMargin(root.getBottom(), new Insets(10));

        stage.setScene(new Scene(root, 700, 400));
        stage.setTitle("Personal Finance Manager");

        stage.setOnCloseRequest(e -> FileManager.save(transactions));

        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
