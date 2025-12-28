import java.io.Serializable;
import java.time.LocalDate;

public class Transaction implements Serializable {

    private static final long serialVersionUID = 1L;

    private LocalDate date;
    private String description;
    private Category category;
    private double amount;

    public Transaction(LocalDate date, String description, Category category, double amount) {
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

    public Category getCategory() {
        return category;
    }

    public double getAmount() {
        return amount;
    }

    public boolean isIncome() {
        return category.isIncome();
    }
}
