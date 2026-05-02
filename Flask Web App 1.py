#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template_string, request, redirect, session
import threading
import json
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# ---------------- USERS ----------------
USERS = {
    "admin": "pass",
    "user": "pass2"
}

# ---------------- CATEGORIES ----------------
CATEGORIES = {
    "Salary": True,
    "Freelance": True,
    "Other Income": True,
    "Food": False,
    "Rent": False,
    "Utilities": False,
    "Entertainment": False
}

# ---------------- SAFE SESSION CHECK ----------------
def is_logged_in():
    return session.get("logged_in") and session.get("user")

# ---------------- FILE HANDLING ----------------
def get_file():
    user = session.get("user")
    if not user:
        return None
    return f"{user}_transactions.json"

def load_data():
    file = get_file()
    if not file:
        return []

    if os.path.exists(file):
        try:
            with open(file, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_data(data):
    file = get_file()
    if not file:
        return

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# ---------------- HTML TEMPLATES ----------------
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
<p>Logged in as: {{ user }}</p>
<a href="/logout">Logout</a>

<hr>

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
    <input type="date" name="date" required>

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
<th>Edit</th>
</tr>

{% for t in transactions %}
<tr>
<td>{{ t.date }}</td>
<td>{{ t.description }}</td>
<td>{{ t.category }}</td>
<td>{{ t.amount }}</td>
<td><a href="/edit/{{ loop.index0 }}">Edit</a></td>
</tr>
{% endfor %}
</table>
"""

EDIT_HTML = """
<h2>Edit Transaction</h2>

<form method="POST">
    <input name="description" value="{{ t.description }}" required>

    <select name="category">
        {% for c in categories %}
        <option {% if c == t.category %}selected{% endif %}>{{ c }}</option>
        {% endfor %}
    </select>

    <input type="number" step="0.01" name="amount" value="{{ t.amount }}" required>
    <input type="date" name="date" value="{{ t.date }}" required>

    <button type="submit">Save</button>
</form>

<a href="/dashboard">Back</a>
"""

# ---------------- ROUTES ----------------

@app.route("/", methods=["GET", "POST"])
def login():

    # SAFE redirect check (prevents loop)
    if is_logged_in():
        return redirect("/dashboard")

    error = ""

    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if user in USERS and USERS[user] == pwd:
            session["logged_in"] = True
            session["user"] = user
            return redirect("/dashboard")
        else:
            error = "Invalid credentials"

    return render_template_string(LOGIN_HTML, error=error)


@app.route("/dashboard")
def dashboard():

    if not is_logged_in():
        session.clear()
        return redirect("/")

    transactions = load_data()

    income = sum(t["amount"] for t in transactions if t["is_income"])
    expenses = sum(t["amount"] for t in transactions if not t["is_income"])
    balance = income - expenses

    return render_template_string(
        MAIN_HTML,
        transactions=transactions,
        income=income,
        expenses=expenses,
        balance=balance,
        categories=CATEGORIES.keys(),
        user=session.get("user")
    )


@app.route("/add", methods=["POST"])
def add():

    if not is_logged_in():
        return redirect("/")

    transactions = load_data()

    category = request.form["category"]

    transactions.append({
        "date": request.form["date"],
        "description": request.form["description"],
        "category": category,
        "amount": float(request.form["amount"]),
        "is_income": CATEGORIES[category]
    })

    save_data(transactions)
    return redirect("/dashboard")


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):

    if not is_logged_in():
        return redirect("/")

    transactions = load_data()

    if index >= len(transactions):
        return redirect("/dashboard")

    if request.method == "POST":
        category = request.form["category"]

        transactions[index] = {
            "date": request.form["date"],
            "description": request.form["description"],
            "category": category,
            "amount": float(request.form["amount"]),
            "is_income": CATEGORIES[category]
        }

        save_data(transactions)
        return redirect("/dashboard")

    return render_template_string(
        EDIT_HTML,
        t=transactions[index],
        categories=CATEGORIES.keys()
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------------- RUN (JUPYTER SAFE) ----------------
def run_app():
    app.run(port=5000)

thread = threading.Thread(target=run_app)
thread.daemon = True
thread.start()

print("App running at http://127.0.0.1:5000")


# In[ ]:




