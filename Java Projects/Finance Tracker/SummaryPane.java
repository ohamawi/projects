import javafx.collections.ObservableList;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.geometry.Insets;

public class SummaryPane extends GridPane {

    private Label incomeValue;
    private Label expenseValue;
    private Label balanceValue;

    private ObservableList<Transaction> transactions;

    public SummaryPane(ObservableList<Transaction> transactions) {
        this.transactions = transactions;

        setPadding(new Insets(10));
        setHgap(15);
        setVgap(10);

        // ===== Labels =====
        Label incomeLabel = new Label("Total Income:");
        Label expenseLabel = new Label("Total Expenses:");
        Label balanceLabel = new Label("Balance:");

        incomeValue = new Label("$0.00");
        expenseValue = new Label("$0.00");
        balanceValue = new Label("$0.00");

        add(incomeLabel, 0, 0);
        add(incomeValue, 1, 0);

        add(expenseLabel, 0, 1);
        add(expenseValue, 1, 1);

        add(balanceLabel, 0, 2);
        add(balanceValue, 1, 2);

        // Initial calculation (incomplete)
        updateSummary();

        // TODO: Add listeners so summary updates automatically
        // TODO: Replace manual calculation with JavaFX Bindings
    }

    /**
     * Calculates totals manually.
     * Currently incomplete implementation.
     */
    private void updateSummary() {
        double income = 0;
        double expenses = 0;

        for (Transaction t : transactions) {
            // TODO: verify logic for income vs expense
            if (t.getCategory().isIncome()) {
                income += t.getAmount();
            } else {
                expenses += t.getAmount();
            }
        }

        // BUG: expenses may already be negative depending on input
        double balance = income + expenses;

        incomeValue.setText(String.format("$%.2f", income));
        expenseValue.setText(String.format("$%.2f", expenses));
        balanceValue.setText(String.format("$%.2f", balance));
    }
}
