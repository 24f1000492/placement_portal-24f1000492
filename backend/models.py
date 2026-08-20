from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Admin(db.Model):
    __tablename__ = 'admin'
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(80),  nullable=False, default='Admin')
    email         = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)


class Company(db.Model):
    __tablename__ = 'companies'
    id              = db.Column(db.Integer, primary_key=True)
    company_name    = db.Column(db.String(150), nullable=False)
    email           = db.Column(db.String(120), unique=True, nullable=False)
    password_hash   = db.Column(db.String(256), nullable=False)
    hr_contact      = db.Column(db.String(120))
    phone           = db.Column(db.String(20))
    website         = db.Column(db.String(200))
    description     = db.Column(db.Text)
    # approval_status: pending | approved | rejected | blacklisted
    approval_status = db.Column(db.String(20), default='pending')
    registered_at   = db.Column(db.DateTime, default=datetime.utcnow)

    drives = db.relationship('PlacementDrive', backref='company',
                             lazy=True, cascade='all, delete-orphan')


class Student(db.Model):
    __tablename__ = 'students'
    id            = db.Column(db.Integer, primary_key=True)
    full_name     = db.Column(db.String(120), nullable=False)
    email         = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    phone         = db.Column(db.String(20))
    branch        = db.Column(db.String(100))
    year          = db.Column(db.String(20))
    cgpa          = db.Column(db.Float)
    skills        = db.Column(db.Text)
    resume_path   = db.Column(db.String(300))
    is_active     = db.Column(db.Boolean, default=True)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)

    applications = db.relationship('Application', backref='student',
                                   lazy=True, cascade='all, delete-orphan')


class PlacementDrive(db.Model):
    __tablename__ = 'placement_drives'
    id                   = db.Column(db.Integer, primary_key=True)
    company_id           = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    job_title            = db.Column(db.String(150), nullable=False)
    job_description      = db.Column(db.Text,        nullable=False)
    eligibility_criteria = db.Column(db.Text)
    location             = db.Column(db.String(100))
    salary_package       = db.Column(db.String(80))
    application_deadline = db.Column(db.Date,        nullable=False)
    # status: pending | approved | rejected | closed
    status               = db.Column(db.String(20), default='pending')
    created_at           = db.Column(db.DateTime, default=datetime.utcnow)

    applications = db.relationship('Application', backref='drive',
                                   lazy=True, cascade='all, delete-orphan')


class Application(db.Model):
    __tablename__ = 'applications'
    id               = db.Column(db.Integer, primary_key=True)
    student_id       = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    drive_id         = db.Column(db.Integer, db.ForeignKey('placement_drives.id'), nullable=False)
    # status: applied | shortlisted | selected | rejected
    status           = db.Column(db.String(20), default='applied')
    application_date = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('student_id', 'drive_id', name='unique_application'),
    )