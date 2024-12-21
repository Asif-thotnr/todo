# Flask To-Do List Application

This is a simple Flask-based To-Do List application that demonstrates CRUD operations using Flask and SQLAlchemy.

## Features

- Add tasks to your to-do list.
- Mark tasks as complete.
- View completed and incomplete tasks.
- Styled using a simple CSS file for better user experience.

---

## Prerequisites

Ensure you have the following installed on your system:

- Python (version 3.7 or above)
- pip (Python package manager)

---

## Setup Instructions

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-todo-list.git
cd flask-todo-list

Flask Todo List Application

Overview

This is a simple Todo List application built using Python, Flask, and SQLite. The application allows users to create, view, and manage their todo items through a web interface.

Getting Started

1. Clone the Repository

Clone the project repository to your local machine:

git clone <repository_url>
cd flask-todo-list

Instructions:-
2. Create a Virtual Environment

To keep dependencies organized, it's recommended to use a virtual environment.

For Windows:

python -m venv venv

For macOS/Linux:

python3 -m venv venv

3. Activate the Virtual Environment

For Windows:

.\venv\Scripts\activate

For macOS/Linux:

source venv/bin/activate

4. Install Dependencies

Install the required Python libraries using pip:

pip install -r requirements.txt

5. Set Up the Database

Initialize the SQLite database by running the following commands:

Open a Python shell in the project directory:

python

Run the following Python commands:

from app import app, db

# Push the application context and create the database
with app.app_context():
    db.create_all()

Exit the Python shell:

exit()

6. Run the Application

Start the Flask development server:

python run.py

7. Access the Application

Open your browser and navigate to:

http://127.0.0.1:5000/

Project Structure

flask-todo-list/
├── app/
│   ├── __init__.py       # App initialization and configuration
│   ├── routes.py         # App routes and view functions
│   ├── models.py         # Database models
│   ├── templates/
│   │   └── index.html    # HTML template for the application
│   ├── static/
│       └── main.css      # CSS for styling
├── run.py                # Entry point to run the application
├── requirements.txt      # List of project dependencies
└── README.md             # Project documentation

Important Commands

Create a Virtual Environment

Windows: python -m venv venv

macOS/Linux: python3 -m venv venv

Activate the Virtual Environment

Windows: .env\Scripts\activate

macOS/Linux: source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

Initialize the Database

from app import app, db

# Push the application context
with app.app_context():
    db.create_all()

Technologies Used

Python: Backend logic.

Flask: Web framework for routing and app structure.

SQLAlchemy: ORM for database operations.

HTML/CSS: Frontend templates and styling.

