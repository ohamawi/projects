package com.example;

import java.io.*;
import java.nio.file.*;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class FileManager {

    private static final Path DATA_DIR =
            Paths.get(System.getProperty("user.home"), ".finance-app");

    private static final Path DATA_FILE =
            DATA_DIR.resolve("transactions.txt");

    // Save transactions to file
    public static void save(List<Transaction> transactions) {
        try {
            // Create directory if missing
            Files.createDirectories(DATA_DIR);

            try (BufferedWriter writer = Files.newBufferedWriter(DATA_FILE)) {
                for (Transaction t : transactions) {
                    writer.write(
                            t.getDate() + "|" +
                            t.getDescription() + "|" +
                            t.getCategory().name() + "|" +
                            t.getAmount()
                    );
                    writer.newLine();
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Load transactions from file
    public static List<Transaction> load() {
        List<Transaction> transactions = new ArrayList<>();

        if (!Files.exists(DATA_FILE)) {
            return transactions; // first run: no file yet
        }

        try (BufferedReader reader = Files.newBufferedReader(DATA_FILE)) {
            String line;

            while ((line = reader.readLine()) != null) {
                String[] parts = line.split("\\|");

                LocalDate date = LocalDate.parse(parts[0]);
                String description = parts[1];
                Category category = Category.valueOf(parts[2]);
                double amount = Double.parseDouble(parts[3]);

                transactions.add(
                        new Transaction(date, description, category, amount)
                );
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        return transactions;
    }
}
