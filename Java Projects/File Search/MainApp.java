package file.search;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

import java.io.*;
import java.nio.file.*;
import java.util.stream.Stream;

public class MainApp extends Application {

    private static final String DOWNLOADS_PATH =
            System.getProperty("user.home") + File.separator + "Downloads";

    private TextField searchField;
    private ListView<String> resultsList;
    private Label statusLabel;

    @Override
    public void start(Stage stage) {

        Label directoryLabel = new Label("Searching in: " + DOWNLOADS_PATH);

        searchField = new TextField();
        searchField.setPromptText("Enter search term");

        Button searchButton = new Button("Search");

        searchButton.setOnAction(e -> runSearch());

        resultsList = new ListView<>();
        statusLabel = new Label("Ready");

        VBox root = new VBox(
                10,
                directoryLabel,
                searchField,
                searchButton,
                resultsList,
                statusLabel
        );

        root.setPadding(new Insets(10));

        stage.setScene(new Scene(root, 700, 500));
        stage.setTitle("File Search (Downloads Test)");
        stage.show();
    }

    private void runSearch() {
        resultsList.getItems().clear();
        statusLabel.setText("Searching...");

        String query = searchField.getText().toLowerCase();

        if (query.isBlank()) {
            statusLabel.setText("Enter a search term");
            return;
        }

        Path downloads = Paths.get(DOWNLOADS_PATH);

        try (Stream<Path> paths = Files.walk(downloads)) {

            paths
                .filter(Files::isRegularFile)
                .forEach(path -> {
                    if (matches(path, query)) {
                        resultsList.getItems().add(path.toString());
                    }
                });

            statusLabel.setText("Search completed");

        } catch (IOException e) {
            statusLabel.setText("Error scanning files");
        }
    }

    private boolean matches(Path file, String query) {
        // Match file name
        if (file.getFileName().toString().toLowerCase().contains(query)) {
            return true;
        }

        // Match file content (safe text attempt)
        try (BufferedReader reader = Files.newBufferedReader(file)) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.toLowerCase().contains(query)) {
                    return true;
                }
            }
        } catch (Exception ignored) {
            // Ignore binary or unreadable files
        }

        return false;
    }

    public static void main(String[] args) {
        launch(args);
    }
}
