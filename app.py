from flask import Flask
from backend.models import db

app = None
def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///placement_portal.db.sqlite3'
    db.init_app(app)
    app.app_context().push()
    return app


create_app()

from backend.routes import*

if __name__ == '__main__':
    app.run(debug=True)
    