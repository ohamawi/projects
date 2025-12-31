package com.example;

import java.io.Serializable;
import java.time.LocalDate;

public class Transaction implements Serializable {

    private static final long serialVersionUID = 1L;

    private LocalDate date;
    private String description;
    private String category;
    private double amount;

    public Transaction(LocalDate date, String description, String category, double amount) {
        this.date = date;
        this.description = description;
        this.category = category;
        this.amount = amount;
    }

    public LocalDate getDate() {
        return date;
    }

    public String getDescription() {
        return description;
    }

    public String getCategory() {
        return category;
    }

    public double getAmount() {
        return amount;
    }
}
