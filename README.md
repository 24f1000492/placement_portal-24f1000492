# Placement Portal

A web-based placement management system built with Flask that connects **Students**, **Companies**, and **College Admins** on a single platform to streamline campus recruitment drives — from posting job openings to tracking applications and final selections.

## Features

### Admin
- Approve, reject, or blacklist company registrations
- Approve or reject placement drives posted by companies
- View, edit, deactivate, or delete student profiles
- Monitor all applications across the platform
- Search across students, companies, and drives

### Company
- Register and manage a company profile (pending admin approval)
- Create, edit, close, or delete placement drives
- View and manage applications received for each drive
- Update applicant status (shortlisted / selected / rejected)

### Student
- Register and manage a personal profile (branch, year, CGPA, skills, resume upload)
- Browse and view details of open placement drives
- Apply to eligible drives
- Track the status of all submitted applications

## Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite via Flask-SQLAlchemy (SQLAlchemy 2.x)
- **Templating:** Jinja2
- **Auth/Security:** Werkzeug password hashing
- **Frontend:** HTML/CSS (Jinja templates)

## Project Structure

```
placement_portalV1/
├── app.py                     # Application entry point & config
├── requirement.txt            # Python dependencies
├── backend/
│   ├── models.py              # SQLAlchemy models (Admin, Company, Student, Drive, Application)
│   └── routes.py               # All application routes/views
├── templates/
│   ├── base.html
│   ├── layout_dashboard.html
│   ├── auth/                  # Login, register, home
│   ├── admin/                 # Admin dashboard & management pages
│   ├── company/               # Company dashboard & drive management
│   └── student/               # Student dashboard & applications
├── static/
│   ├── css/
│   └── uploads/                # Uploaded resumes
└── instance/
    └── placement_portal.db    # SQLite database (auto-generated)
```

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd placement_portalV1
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser at `http://127.0.0.1:5000/`

The database and a default admin account are created automatically on first run.

### Default Admin Credentials
```
Email:    admin@placement.com
Password: admin123
```
> ⚠️ Change these credentials before deploying to production.

## Database Models

| Model            | Purpose                                                   |
|-------------------|------------------------------------------------------------|
| `Admin`           | Portal administrator accounts                              |
| `Company`         | Registered companies (with approval status)                |
| `Student`         | Registered students (profile, resume, active status)        |
| `PlacementDrive`  | Job/drive postings created by companies                    |
| `Application`     | Student applications linked to drives                      |

## Notes

- Max resume upload size is capped at 5 MB (`app.config['MAX_CONTENT_LENGTH']`).
- Companies and drives require admin approval before becoming visible/active.
- Update `SECRET_KEY` and the database URI in `app.py` before deploying.

## License

This project is provided for educational purposes.
