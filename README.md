# 📦 Inventory Management System

An **Inventory Management System** developed as a learning and practical project using **Python and Streamlit**.

The goal of this project is to create a simple system for managing inventory, products, stock, and related information.

---

## 🚀 Project Status

**Current Status:** In Development

This project will be improved step by step as new features are added.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Git
* GitHub
* VS Code

---

## 📁 Project Structure

```text
inventory-managemnet-
│
├── README.md
│
├── streamlit/
│   └── 01_app_test/
│       ├── app.py
│       └── workflo.drawio
│
└── ...
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/aneelaaltaf007/inventory-managemnet-.git
```

## 2. Go to the Project Folder

```bash
cd inventory-managemnet-
```

## 3. Create a Virtual Environment

### Using Conda

```bash
conda create -n inventory python=3.12
```

Activate it:

```bash
conda activate inventory
```

### Or using Python venv

```bash
python -m venv inventory_env
```

Activate on Windows:

```bash
inventory_env\Scripts\activate
```

---

# 📦 Install Dependencies

If you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If you don't have one yet, you can install the main packages:

```bash
pip install streamlit pandas numpy matplotlib
```

---

# ▶️ Run the Streamlit Application

Go to the app folder:

```bash
cd streamlit/01_app_test
```

Run:

```bash
streamlit run app.py
```

Or:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

# 🔄 Git & GitHub Commands

These commands will be useful whenever you continue working on the project.

## Check Git Status

```bash
git status
```

## See Current Branch

```bash
git branch
```

## See Remote Repository

```bash
git remote -v
```

## Download Latest Changes

```bash
git pull origin main
```

## Add All Changes

```bash
git add .
```

## Commit Changes

```bash
git commit -m "Your commit message"
```

## Push Changes to GitHub

```bash
git push origin main
```

---

# 🔁 Normal Git Workflow

Whenever you make changes to your project:

```bash
git status
git add .
git commit -m "Describe your changes"
git push origin main
```

For example:

```bash
git add .
git commit -m "Add inventory dashboard"
git push origin main
```

---

# 🌿 Branch Commands

Create a new branch:

```bash
git checkout -b feature-name
```

Switch to another branch:

```bash
git checkout main
```

See all branches:

```bash
git branch
```

Push a new branch:

```bash
git push -u origin feature-name
```

---

# 🔙 Undo / Recovery Commands

See previous commits:

```bash
git log --oneline
```

See changes that have not been committed:

```bash
git diff
```

Undo changes in a file that have not been committed:

```bash
git restore filename
```

Unstage a file:

```bash
git restore --staged filename
```

---

# 📌 Useful Git Commands

Check the current repository:

```bash
git status
```

Check commit history:

```bash
git log --oneline
```

Check remote URL:

```bash
git remote -v
```

Update your local repository:

```bash
git pull origin main
```

Push your work:

```bash
git push origin main
```

---

# 📊 Planned Features

Future versions may include:

* [ ] Add products
* [ ] Delete products
* [ ] Update products
* [ ] Search products
* [ ] Stock management
* [ ] Low-stock alerts
* [ ] Sales management
* [ ] Purchase management
* [ ] Dashboard
* [ ] Data visualization
* [ ] Database integration
* [ ] User authentication
* [ ] Admin panel
* [ ] AI-based inventory predictions
* [ ] NLP-based inventory assistant

---

# 🤖 Future AI Features

As an AI student, this project can later be expanded with AI features such as:

### Machine Learning

* Demand prediction
* Sales forecasting
* Stock prediction
* Product recommendation
* Inventory optimization

### NLP

An NLP assistant could allow users to ask questions such as:

```text
"Which products are low in stock?"
```

```text
"Show me products sold this month."
```

```text
"Which product has the highest sales?"
```

---

# 🗄️ Future Database

The project can later use a database such as:

* MySQL
* PostgreSQL
* SQLite

Possible tables:

```text
Products
Customers
Suppliers
Sales
Purchases
Users
Inventory
```

---

# 🧪 Testing

Before pushing changes to GitHub:

```bash
python -m py_compile app.py
```

Check whether Streamlit starts correctly:

```bash
python -m streamlit run app.py
```

---

# 📋 Requirements File

After installing your project packages, you can create:

```bash
pip freeze > requirements.txt
```

Then another person can install the same dependencies using:

```bash
pip install -r requirements.txt
```

---

# 💾 Saving Your Work

Before closing your project, check:

```bash
git status
```

Then:

```bash
git add .
git commit -m "Save project progress"
git push origin main
```

---

# 👩‍💻 Author

**Aneela Altaf**

Artificial Intelligence Student

GitHub:

https://github.com/aneelaaltaf007

---

# 📜 License

This project is created for educational and learning purposes.

---

## ⭐ Project Goal

The long-term goal is to develop this project into a complete **AI-powered Inventory Management System** that combines:

**Python + Streamlit + Database + Machine Learning + NLP**

```text
Inventory Management
        ↓
     Database
        ↓
   Data Analysis
        ↓
 Machine Learning
        ↓
   AI Prediction
        ↓
    NLP Assistant
```

---

## 📌 Important Note

Keep this README updated whenever you add a major feature to the project.

For example:

```bash
git add .
git commit -m "Add product search feature"
git push origin main
```
