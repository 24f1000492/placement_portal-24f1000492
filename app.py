from flask import Flask
app = None
def create_app():
    app=Flask(__name__)
    return app
create_app()

if __name__ == '__main__':
    app.run(debug=True)
    