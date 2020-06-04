# web_app/__init__.py

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

'''
What is @?
What is http protocol?
Why __init__ file?
Why __name__?
What is  http://127.0.0.1:5000/?
Flask versus Django?
'''