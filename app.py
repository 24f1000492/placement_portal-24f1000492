from flask import Flask
from backend.models import db
from backend.models import Admin
from werkzeug.security import generate_password_hash
from backend.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.secret_key = 'placement-portal-secret-2024'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///placement_portal.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB

    db.init_app(app)
    
    register_routes(app)

    with app.app_context():
        db.create_all()
        create_admin()

   
    

    return app


def create_admin():
    
    if not Admin.query.first():
        admin = Admin(
            username      = 'Admin',
            email         = 'admin@placement.com',
            password_hash = generate_password_hash('admin123'),
        )
        db.session.add(admin)
        db.session.commit()
        print('Admin created  →  admin@placement.com  /  admin123')


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)