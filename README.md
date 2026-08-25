# M.E.S. Polytechnic, Madhugiri (Code 347)
### Official Institutional Web Application

Modern, animated, full-stack college web application for **M.E.S. Polytechnic, Madhugiri** (Madhugiri Education Society) built with Django, Tailwind CSS, and AOS scroll animations.

---

## 🚀 Quick Start Guide (Run Locally on Any PC)

### 1. Prerequisites
Ensure you have **Python 3.10 or higher** installed on your computer:
- **Windows:** Download from [python.org](https://www.python.org/downloads/) *(⚠️ Check the box **"Add Python to PATH"** during installation)*.
- **Mac/Linux:** Python is usually pre-installed. Verify with `python3 --version`.

---

### 2. Setup & Run in 3 Easy Steps

#### 🪟 On Windows (Command Prompt / PowerShell):
```cmd
# 1. Open Command Prompt inside the unzipped folder and create a virtual environment:
python -m venv venv

# 2. Activate the virtual environment:
venv\Scripts\activate

# 3. Install dependencies:
pip install -r requirements.txt

# 4. Start the development server:
python manage.py runserver
```

---

#### 🍎 On macOS / 🐧 Linux (Terminal):
```bash
# 1. Open Terminal inside the unzipped folder and create a virtual environment:
python3 -m venv venv

# 2. Activate the virtual environment:
source venv/bin/activate

# 3. Install dependencies:
pip install -r requirements.txt

# 4. Start the development server:
python manage.py runserver
```

---

### 🌐 3. Open in Your Browser
Once the terminal displays `Starting development server at http://127.0.0.1:8000/`, open your browser and navigate to:

- **Public Website:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Faculty Directory:** [http://127.0.0.1:8000/faculty/](http://127.0.0.1:8000/faculty/)
- **Staff Administration Portal:** [http://127.0.0.1:8000/staff-dashboard/](http://127.0.0.1:8000/staff-dashboard/)
- **Django Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

### 🔐 Staff & Administrator Login Credentials
- **Username:** `admin`
- **Password:** `admin123`

*(To create an additional administrator account, run `python manage.py createsuperuser` in your activated terminal).*

---

### 📁 Project Highlights
- **Pre-populated Real Data:** All 33 official faculty members, HODs, real toppers with photos, and AICTE/DTE circular PDFs are pre-loaded in the database (`db.sqlite3`).
- **Staff Portal:** Add, edit, or delete department programs, intake seats, faculty pictures, notices, quick downloads, and academic achievers.
- **Branding Assets:** Powered by **ABCX** ([https://abcx.co.in/](https://abcx.co.in/)).
