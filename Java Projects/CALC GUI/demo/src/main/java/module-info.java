module calc.gui {
    requires javafx.controls;
    requires javafx.fxml;

    opens calc.gui to javafx.fxml;
    exports calc.gui;
}
