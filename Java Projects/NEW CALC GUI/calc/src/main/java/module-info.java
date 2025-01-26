module updated.calc {
    requires javafx.controls;
    requires javafx.fxml;

    opens updated.calc to javafx.fxml;
    exports updated.calc;
}
