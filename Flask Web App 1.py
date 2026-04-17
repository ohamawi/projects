#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, render_template_string, request, redirect
from datetime import date
import threading

app = Flask(__name__)

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

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Finance Tracker</title>
</head>
<body>

<h1>Finance Tracker</h1>

<h3>Summary</h3>
<p>Income: ${{ income }}</p>
<p>Expenses: ${{ expenses }}</p>
<p>Balance: ${{ balance }}</p>

<hr>

<h3>Add Transaction</h3>
<form method="POST" action="/add">
    <input type="text" name="description" placeholder="Description" required>

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

</body>
</html>
"""

@app.route("/")
def index():
    income = sum(t["amount"] for t in transactions if t["is_income"])
    expenses = sum(t["amount"] for t in transactions if not t["is_income"])
    balance = income - expenses

    return render_template_string(
        HTML,
        transactions=transactions,
        income=income,
        expenses=expenses,
        balance=balance,
        categories=CATEGORIES.keys()
    )

@app.route("/add", methods=["POST"])
def add():
    desc = request.form["description"]
    category = request.form["category"]
    amount = float(request.form["amount"])

    transactions.append({
        "date": date.today().isoformat(),
        "description": desc,
        "category": category,
        "amount": amount,
        "is_income": CATEGORIES[category]
    })

    return redirect("/")


def run_app():
    app.run(port=5000)

# Start Flask in a thread
thread = threading.Thread(target=run_app)
thread.daemon = True
thread.start()

print("Flask app running at http://127.0.0.1:5000")


# In[ ]:




