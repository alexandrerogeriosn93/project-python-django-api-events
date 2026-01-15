# EventIn API - Events Management System

EventIn is a Django-based REST API designed for managing events, registrations, and participants. This project provides a robust backend for event organization, including features like participant management and event registration.

## 🛠️ Technologies Used

- **Python**: The core programming language.
- **Django**: The high-level Python web framework.
- **Django REST Framework**: For building the RESTful API.
- **Django-filter**: For filtering API results.
- **Faker**: Used to generate realistic dummy data for testing.
- **SQLite**: Default database for development.
- **validate-docbr**: For validating Brazilian documents (CPF/CNPJ).

## 📂 Project Structure

Below is the directory structure of the project (excluding `.github`):

```text
.
├── eventin/                # Main application folder
│   ├── management/         # Custom management commands
│   │   └── commands/
│   │       └── populate.py # Scripts to seed the database
│   ├── migrations/         # Database migrations
│   ├── admin.py            # Django admin configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Database models (Events, Participants, etc.)
│   ├── serializers.py      # DRF serializers
│   ├── tests.py            # Unit tests
│   ├── validators.py       # Custom data validation logic
│   └── views.py            # API ViewSets and logic
├── setup/                  # Project configuration folder
│   ├── asgi.py             # ASGI entry point
│   ├── settings.py         # Global project settings
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI entry point
├── .gitignore              # Files excluded from version control
├── db.sqlite3              # Local SQLite database
├── manage.py               # Django's command-line utility
├── requirements.txt        # List of project dependencies
└── README.md               # Project documentation
```

## 🚀 How to Execute the Project

### 1. Prerequisites

Ensure you have **Python 3.10+** installed.

### 2. Create and Activate a Virtual Environment

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate it (Linux/macOS)
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
python3 manage.py migrate
```

### 5. (Optional) Seed the Database

To populate the database with dummy data for testing:

```bash
python3 manage.py populate
```

### 6. Start the Development Server

```bash
python3 manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## 🔒 Non-versioned Files

The following files and directories are ignored by Git and will not be versioned:

- `.venv/`: The local Python virtual environment.
- `__pycache__/`: Python compiled files.
- `db.sqlite3`: The local database file containing development data.
