# Calorie Counter App

A simple, fast, and responsive web application built with **Django** and **Tailwind CSS** that helps users log daily food consumption, calculate total calorie intake, and manage meal entries.

---

## Features

- **Food Logging:** Easily log food items along with their respective calorie counts.
- **Dynamic Calorie Total:** Calculates total daily intake efficiently in memory using Python generator expressions.
- **Individual Entry Deletion:** Remove individual meal items safely via secure `POST` requests protected by CSRF tokens.
- **Daily Reset:** Clear all daily entries with a single click ("Reset Day") to start fresh for a new day.
- **Responsive UI:** Modern, clean interface styled with Tailwind CSS, supporting mobile and desktop views.

---

## Tech Stack

- **Backend:** Python 3.x, Django 5.x
- **Database:** SQLite
- **Frontend:** HTML5, Tailwind CSS (via CDN), Django Templating Engine

---

## Project Layout

The application utilizes a flat app-level template structure:

```text
calorie_counter_project/
├── calorie_counter_app/
│   ├── templates/             # App-level templates (flat layout)
│   │   ├── base.html          # Global layout template
│   │   └── tracker.html       # Calorie tracker interface
│   ├── forms.py               # FoodItemForm definition
│   ├── models.py              # FoodItem schema
│   ├── urls.py                # App routing (tracker, delete, reset)
│   └── views.py               # Controller logic
├── calorie_counter_project/
│   ├── settings.py            # Project settings
│   ├── urls.py                # Global routing
│   └── wsgi.py
├── db.sqlite3                 # Local SQLite database
├── manage.py
└── requirements.txt
```

---

## How to Set Up and Run on Another Machine

Follow these step-by-step instructions to clone and run this project on any fresh setup or remote machine.

### Prerequisites

Ensure the target machine has the following installed:
* **Python 3.10+** (verify with `python --version` or `python3 --version`)
* **Git** (verify with `git --version`)

---

### Step-by-Step Setup Guide

#### 1. Clone the Repository
Open your terminal or command prompt and clone the project:
```bash
git clone https://github.com/lameckkipsang/calorie_counter.git
cd calorie-counter-project
```

#### 2. Set Up a Virtual Environment
Isolate project dependencies by creating and activating a virtual environment:

- **Windows (Git Bash / Command Prompt):**
  ```bash
  python -m venv venv
  source venv/Scripts/activate     # Git Bash
  # OR
  venv\Scripts\activate            # Command Prompt / PowerShell
  ```

- **Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

#### 3. Install Dependencies
Install Django inside your active virtual environment:
```bash
pip install -r requirements.txt
```
*(If `requirements.txt` is not present, run `pip install django`)*

#### 4. Apply Database Migrations
Initialize your local SQLite database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Start the Django Development Server
Run the local development server:
```bash
python manage.py runserver
```

#### 6. Open in Browser
Open your web browser and navigate to:
```text
http://127.0.0.1:8000/
```

---

## Security Practices

- **CSRF Protection:** All state-changing actions (`Delete` and `Reset Day`) utilize HTML forms sending `POST` requests containing Django's `{% csrf_token %}` to prevent Cross-Site Request Forgery vulnerabilities.
- **Resource Cleanup:** Employs Django's `get_object_or_404` helper to gracefully return 404 HTTP errors for non-existent records during deletion operations.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.