#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import ttk
from datetime import date
import json
import os

# ---- File Path ----
DATA_FILE = "transactions.json"

# ---- Categories ----
CATEGORIES = {
    "Salary": True,
    "Freelance": True,
    "Other Income": True,
    "Food": False,
    "Rent": False,
    "Utilities": False,
    "Entertainment": False,
    "Transportation": False,
    "Other Expense": False
}

# ---- Main App ----
class FinanceApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")

        self.transactions = []

        # ---- Summary ----
        self.income_var = tk.StringVar(value="$0.00")
        self.expense_var = tk.StringVar(value="$0.00")
        self.balance_var = tk.StringVar(value="$0.00")

        summary_frame = tk.Frame(root)
        summary_frame.pack(pady=10)

        tk.Label(summary_frame, text="Income:").grid(row=0, column=0)
        tk.Label(summary_frame, textvariable=self.income_var).grid(row=0, column=1)

        tk.Label(summary_frame, text="Expenses:").grid(row=1, column=0)
        tk.Label(summary_frame, textvariable=self.expense_var).grid(row=1, column=1)

        tk.Label(summary_frame, text="Balance:").grid(row=2, column=0)
        tk.Label(summary_frame, textvariable=self.balance_var).grid(row=2, column=1)

        # ---- Table ----
        self.tree = ttk.Treeview(root, columns=("Date", "Desc", "Category", "Amount"), show="headings")
        for col in ("Date", "Desc", "Category", "Amount"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # ---- Buttons ----
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Add", command=self.open_add_dialog).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_selected).pack(side="left", padx=5)

        # ---- Load Data ----
        self.load_data()
        self.refresh_table()

        # ---- Save on Close ----
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # ---- Add Dialog ----
    def open_add_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Transaction")

        tk.Label(dialog, text="Description").pack()
        desc_entry = tk.Entry(dialog)
        desc_entry.pack()

        tk.Label(dialog, text="Category").pack()
        category_box = ttk.Combobox(dialog, values=list(CATEGORIES.keys()))
        category_box.current(0)
        category_box.pack()

        tk.Label(dialog, text="Amount").pack()
        amount_entry = tk.Entry(dialog)
        amount_entry.pack()

        def save():
            try:
                desc = desc_entry.get()
                category = category_box.get()
                amount = float(amount_entry.get())
                today = date.today().isoformat()

                transaction = {
                    "date": today,
                    "desc": desc,
                    "category": category,
                    "amount": amount,
                    "is_income": CATEGORIES[category]
                }

                self.transactions.append(transaction)
                self.refresh_table()
                dialog.destroy()

            except ValueError:
                print("Invalid amount")

        tk.Button(dialog, text="Save", command=save).pack(pady=5)

    # ---- Delete ----
    def delete_selected(self):
        selected = self.tree.selection()
        for item in selected:
            index = self.tree.index(item)
            self.tree.delete(item)
            self.transactions.pop(index)

        self.update_summary()

    # ---- Refresh Table ----
    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())

        for t in self.transactions:
            self.tree.insert("", "end", values=(
                t["date"],
                t["desc"],
                t["category"],
                f"{t['amount']:.2f}"
            ))

        self.update_summary()

    # ---- Summary ----
    def update_summary(self):
        income = 0
        expenses = 0

        for t in self.transactions:
            if t["is_income"]:
                income += t["amount"]
            else:
                expenses += abs(t["amount"])

        balance = income - expenses

        self.income_var.set(f"${income:.2f}")
        self.expense_var.set(f"${expenses:.2f}")
        self.balance_var.set(f"${balance:.2f}")

    # ---- Save Data ----
    def save_data(self):
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(self.transactions, f, indent=4)
        except Exception as e:
            print("Error saving:", e)

    # ---- Load Data ----
    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return

        try:
            with open(DATA_FILE, "r") as f:
                self.transactions = json.load(f)
        except Exception as e:
            print("Error loading:", e)

    # ---- On Close ----
    def on_close(self):
        self.save_data()
        self.root.destroy()


# ---- Run ----
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = FinanceApp(root)
    root.mainloop()


# In[ ]:




