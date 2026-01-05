package com.example;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.DirectoryChooser;
import javafx.stage.Stage;

import java.io.File;

public class MainApp extends Application {

    private Label directoryLabel;
    private TextField searchField;
    private ListView<String> resultsList;
    private Label statusLabel;

    @Override
    public void start(Stage stage) {

        // ---- Directory Selection ----
        Button chooseDirButton = new Button("Choose Directory");
        directoryLabel = new Label("No directory selected");

        chooseDirButton.setOnAction(e -> {
            DirectoryChooser chooser = new DirectoryChooser();
            File selected = chooser.showDialog(stage);
            if (selected != null) {
                directoryLabel.setText(selected.getAbsolutePath());
            }
        });

        VBox directoryBox = new VBox(5, chooseDirButton, directoryLabel);

        // ---- Search Input ----
        searchField = new TextField();
        searchField.setPromptText("Enter search term");

        Button searchButton = new Button("Search");

        searchButton.setOnAction(e -> {
            // Placeholder logic
            resultsList.getItems().clear();
            resultsList.getItems().add("Searching for: " + searchField.getText());
            statusLabel.setText("Search completed (mock)");
        });

        HBox searchBox = new HBox(10, searchField, searchButton);
        HBox.setHgrow(searchField, Priority.ALWAYS);

        // ---- Results ----
        resultsList = new ListView<>();

        // ---- Status Bar ----
        statusLabel = new Label("Ready");

        // ---- Layout ----
        VBox root = new VBox(12,
                directoryBox,
                searchBox,
                resultsList,
                statusLabel
        );
        root.setPadding(new Insets(10));

        stage.setScene(new Scene(root, 700, 500));
        stage.setTitle("Local File Search");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
