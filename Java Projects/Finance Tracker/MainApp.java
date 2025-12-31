package com.example;

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

        // Load transactions
        transactions = FXCollections.observableArrayList();
        List<Transaction> loaded = FileManager.load();
        if (loaded != null) {
            transactions.addAll(loaded);
        }

        // Table
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
                        d.getValue().getCategory().getDisplayName()
                )
        );

        TableColumn<Transaction, String> amtCol = new TableColumn<>("Amount");
        amtCol.setCellValueFactory(d ->
                new javafx.beans.property.SimpleStringProperty(
                        String.format("%.2f", d.getValue().getAmount())
                )
        );

        table.getColumns().addAll(dateCol, descCol, catCol, amtCol);
        table.setColumnResizePolicy(TableView.CONSTRAINED_RESIZE_POLICY);

        // Buttons
        Button addBtn = new Button("Add");
        Button deleteBtn = new Button("Delete");

        addBtn.setOnAction(e -> {
            Transaction t = TransactionDialog.showAndWait();
            if (t != null) {
                transactions.add(t);
            }
        });

        deleteBtn.setOnAction(e -> {
            Transaction selected = table.getSelectionModel().getSelectedItem();
            if (selected != null) {
                transactions.remove(selected);
            }
        });

        HBox buttonBox = new HBox(10, addBtn, deleteBtn);
        buttonBox.setPadding(new Insets(10));

        // Summary
        SummaryPane summaryPane = new SummaryPane(transactions);

        // Layout
        BorderPane root = new BorderPane();
        root.setTop(summaryPane);
        root.setCenter(table);
        root.setBottom(buttonBox);

        stage.setScene(new Scene(root, 800, 500));
        stage.setTitle("Personal Finance Manager");

        stage.setOnCloseRequest(e -> FileManager.save(transactions));

        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
