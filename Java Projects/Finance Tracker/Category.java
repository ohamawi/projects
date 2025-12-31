package com.example;

public enum Category {

    // Income categories
    SALARY("Salary", true),
    FREELANCE("Freelance", true),
    OTHER_INCOME("Other Income", true),

    // Expense categories
    FOOD("Food", false),
    RENT("Rent", false),
    UTILITIES("Utilities", false),
    ENTERTAINMENT("Entertainment", false),
    TRANSPORTATION("Transportation", false),
    OTHER_EXPENSE("Other Expense", false);

    private final String displayName;
    private final boolean income;

    Category(String displayName, boolean income) {
        this.displayName = displayName;
        this.income = income;
    }

    public String getDisplayName() {
        return displayName;
    }

    public boolean isIncome() {
        return income;
    }

    @Override
    public String toString() {
        return displayName;
    }
}
