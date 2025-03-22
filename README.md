# 💰 Expense Tracker Web Application

A full-stack web application built with Flask to track personal expenses and manage spending categories.

![Expense Tracker Screenshot](/assets/main.PNG)

## 🌟 Features

- **Add Expenses**: Track expenses with amount, category, and description
- **Expense List**: View all expenses in chronological order
- **Category Breakdown**: See spending distribution across categories
- **Delete Expenses**: Remove unwanted entries
- **Category Management**: Add/remove spending categories
- **Responsive UI**: Mobile-friendly Bootstrap interface
- **Data Persistence**: SQLite database storage

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Database**: SQLAlchemy, SQLite
- **Frontend**: HTML5, Bootstrap 5, Jinja2 templating
- **Form Handling**: Flask-WTF, WTForms
- **Environment Management**: python-dotenv

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
    ```
2. **Create virtual environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure environment**
    Create .env file in project root:
    ```bash
    SECRET_KEY=your-secret-key-here
    DATABASE_URL=sqlite:///app.db
5. **Initialize database**
    ```bash
    flask shell
    >>> from app import db, create_app
    >>> app = create_app()
    >>> with app.app_context():
    ...     db.create_all()
    ... 
    >>> exit()
    ```
6. **Run the application**
    ```bash
    flask run
    ```
    Visit http://localhost:5000 in your browser.

## 🚀 Usage
1.**Home Page (/)**

    - View all expenses

    - See total spending and category breakdown

    - Delete existing entries

2.**Add Expense (/add)**

    - Enter amount, select category, add        description

    - Form validation ensures correct data entry

3.**Manage Categories (/categories)**

    - Add new spending categories

    - Remove existing categories

## 📂 Project Structure

![Expense Tracker Structure](/assets/structure.PNG)