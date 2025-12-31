package com.example;

import javafx.collections.ListChangeListener;
import javafx.collections.ObservableList;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.geometry.Insets;

public class SummaryPane extends GridPane {

    private final Label incomeValue = new Label("$0.00");
    private final Label expenseValue = new Label("$0.00");
    private final Label balanceValue = new Label("$0.00");

    private final ObservableList<Transaction> transactions;

    public SummaryPane(ObservableList<Transaction> transactions) {
        this.transactions = transactions;

        setPadding(new Insets(10));
        setHgap(15);
        setVgap(10);

        add(new Label("Total Income:"), 0, 0);
        add(incomeValue, 1, 0);

        add(new Label("Total Expenses:"), 0, 1);
        add(expenseValue, 1, 1);

        add(new Label("Balance:"), 0, 2);
        add(balanceValue, 1, 2);

        recalculate();

        transactions.addListener((ListChangeListener<Transaction>) change -> recalculate());
    }

    private void recalculate() {
        double income = 0;
        double expenses = 0;

        for (Transaction t : transactions) {
            if (t.isIncome()) {
                income += t.getAmount();
            } else {
                expenses += Math.abs(t.getAmount());
            }
        }

        double balance = income - expenses;

        incomeValue.setText(String.format("$%.2f", income));
        expenseValue.setText(String.format("$%.2f", expenses));
        balanceValue.setText(String.format("$%.2f", balance));
    }
}
