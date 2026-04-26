#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template_string, request, redirect, session
from datetime import date
import threading
import json
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for sessions

DATA_FILE = "transactions.json"

transactions = []

CATEGORIES = {
    "Salary": True,
    "Freelance": True,
    "Other Income": True,
    "Food": False,
    "Rent": False,
    "Utilities": False,
    "Entertainment": False
}

# ---- Load Data ----
def load_data():
    global transactions
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                transactions = json.load(f)
        except:
            transactions = []

# ---- Save Data ----
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)

# ---- Templates ----
LOGIN_HTML = """
<h2>Login</h2>
<form method="POST">
    <input name="username" placeholder="Username" required><br>
    <input name="password" type="password" placeholder="Password" required><br>
    <button type="submit">Login</button>
</form>
<p style="color:red;">{{ error }}</p>
"""

MAIN_HTML = """
<h1>Finance Tracker</h1>

<a href="/logout">Logout</a>

<h3>Summary</h3>
<p>Income: ${{ income }}</p>
<p>Expenses: ${{ expenses }}</p>
<p>Balance: ${{ balance }}</p>

<hr>

<h3>Add Transaction</h3>
<form method="POST" action="/add">
    <input name="description" placeholder="Description" required>

    <select name="category">
        {% for c in categories %}
        <option>{{ c }}</option>
        {% endfor %}
    </select>

    <input type="number" step="0.01" name="amount" placeholder="Amount" required>

    <button type="submit">Add</button>
</form>

<hr>

<h3>Transactions</h3>
<table border="1">
<tr>
<th>Date</th>
<th>Description</th>
<th>Category</th>
<th>Amount</th>
</tr>

{% for t in transactions %}
<tr>
<td>{{ t.date }}</td>
<td>{{ t.description }}</td>
<td>{{ t.category }}</td>
<td>{{ t.amount }}</td>
</tr>
{% endfor %}

</table>
"""

# ---- Routes ----
@app.route("/", methods=["GET", "POST"])
def login():
    if session.get("logged_in"):
        return redirect("/dashboard")

    error = ""

    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "pass":
            session["logged_in"] = True
            return redirect("/dashboard")
        else:
            error = "Invalid credentials"

    return render_template_string(LOGIN_HTML, error=error)


@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/")

    income = sum(t["amount"] for t in transactions if t["is_income"])
    expenses = sum(t["amount"] for t in transactions if not t["is_income"])
    balance = income - expenses

    return render_template_string(
        MAIN_HTML,
        transactions=transactions,
        income=income,
        expenses=expenses,
        balance=balance,
        categories=CATEGORIES.keys()
    )


@app.route("/add", methods=["POST"])
def add():
    if not session.get("logged_in"):
        return redirect("/")

    transactions.append({
        "date": date.today().isoformat(),
        "description": request.form["description"],
        "category": request.form["category"],
        "amount": float(request.form["amount"]),
        "is_income": CATEGORIES[request.form["category"]]
    })

    save_data()
    return redirect("/dashboard")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---- Run in Thread ----
def run_app():
    load_data()
    app.run(port=5000)

thread = threading.Thread(target=run_app)
thread.daemon = True
thread.start()

print("App running at http://127.0.0.1:5000")


# In[ ]:




