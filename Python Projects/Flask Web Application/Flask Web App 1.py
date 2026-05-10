#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template_string, request, redirect, session
import threading
import json
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# ---------------- USER FILE ----------------
USERS_FILE = "users.json"

# ---------------- DEFAULT USERS ----------------
DEFAULT_USERS = {
    "admin": "pass",
    "user": "pass2"
}

# ---------------- LOAD USERS ----------------
def load_users():

    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump(DEFAULT_USERS, f, indent=4)

    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return DEFAULT_USERS

# ---------------- SAVE USERS ----------------
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

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

# ---------------- SAFE LOGIN CHECK ----------------
def is_logged_in():
    return session.get("logged_in") and session.get("user")

# ---------------- USER FILE HANDLING ----------------
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

# ---------------- HTML ----------------

LOGIN_HTML = """
<h2>Login</h2>

<form method="POST">

    <input name="username" placeholder="Username" required><br><br>

    <input
        name="password"
        type="password"
        placeholder="Password"
        required
    ><br><br>

    <button type="submit">Login</button>

</form>

<br>

<a href="/register">Create Account</a>

<p style="color:red;">{{ error }}</p>
"""

REGISTER_HTML = """
<h2>Create Account</h2>

<form method="POST">

    <input name="username" placeholder="New Username" required><br><br>

    <input
        name="password"
        type="password"
        placeholder="New Password"
        required
    ><br><br>

    <button type="submit">Create Account</button>

</form>

<br>

<a href="/">Back to Login</a>

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

    <input
        name="description"
        placeholder="Description"
        required
    >

    <select name="category">

        {% for c in categories %}
            <option>{{ c }}</option>
        {% endfor %}

    </select>

    <input
        type="number"
        step="0.01"
        name="amount"
        placeholder="Amount"
        required
    >

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
<td>
    <a href="/edit/{{ loop.index0 }}">Edit</a>
</td>
</tr>

{% endfor %}

</table>
"""

EDIT_HTML = """
<h2>Edit Transaction</h2>

<form method="POST">

    <input
        name="description"
        value="{{ t.description }}"
        required
    >

    <select name="category">

        {% for c in categories %}

        <option
            {% if c == t.category %}selected{% endif %}
        >
            {{ c }}
        </option>

        {% endfor %}

    </select>

    <input
        type="number"
        step="0.01"
        name="amount"
        value="{{ t.amount }}"
        required
    >

    <input
        type="date"
        name="date"
        value="{{ t.date }}"
        required
    >

    <button type="submit">Save</button>

</form>

<br>

<a href="/dashboard">Back</a>
"""

# ---------------- ROUTES ----------------

@app.route("/", methods=["GET", "POST"])
def login():

    if is_logged_in():
        return redirect("/dashboard")

    error = ""

    if request.method == "POST":

        users = load_users()

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:

            session["logged_in"] = True
            session["user"] = username

            return redirect("/dashboard")

        else:
            error = "Invalid username or password"

    return render_template_string(
        LOGIN_HTML,
        error=error
    )

# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    error = ""

    if request.method == "POST":

        users = load_users()

        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            error = "Username already exists"

        else:

            users[username] = password

            save_users(users)

            # create empty transaction file
            with open(f"{username}_transactions.json", "w") as f:
                json.dump([], f)

            return redirect("/")

    return render_template_string(
        REGISTER_HTML,
        error=error
    )

# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if not is_logged_in():

        session.clear()

        return redirect("/")

    transactions = load_data()

    income = sum(
        t["amount"]
        for t in transactions
        if t["is_income"]
    )

    expenses = sum(
        t["amount"]
        for t in transactions
        if not t["is_income"]
    )

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

# ---------------- ADD TRANSACTION ----------------

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

# ---------------- EDIT TRANSACTION ----------------

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

# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

# ---------------- RUN APP ----------------

def run_app():
    app.run(port=5000)

thread = threading.Thread(target=run_app)
thread.daemon = True
thread.start()

print("App running at http://127.0.0.1:5000")


# In[ ]:




