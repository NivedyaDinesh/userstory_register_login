from flask import Flask
from flask_cors import CORS
from authorization.authorization import auth_bp

app = Flask(__name__)

# Configure CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Register the Blueprint
app.register_blueprint(auth_bp, url_prefix='/')

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(debug=True, port=5000)
