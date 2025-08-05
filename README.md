# 🔐 Auth Microservice System / # userstory_register_login

A lightweight microservice-based authentication system using **Nameko**, **Flask**, and **MongoDB**. It allows users to sign up and log in securely with hashed passwords.

---

## 📦 Tech Stack

- **Nameko** – Microservices framework (RabbitMQ-based RPC)
- **Flask** – API gateway
- **MongoDB** – Database
- **bcrypt** – Password hashing
- **dotenv** – Environment variable management

---

## 📁 Project Structure

```
.
├── app.py                  # Flask application with CORS and routing
├── authorization.py       # Flask blueprint calling Nameko RPC
├── auth_service.py        # Nameko service for auth logic
├── main.py                # Entry point for running Nameko service
├── mongodbsingleton.py    # Singleton MongoDB connector
├── config.yaml            # Environment configuration
└── api_documentation.ods  # API documentation (spreadsheet format)
```

---

## ⚙️ Setup Instructions

### 1. 🐍 Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. 📥 Install dependencies

```bash
pip install -r requirements.txt
```

(*Make sure your `requirements.txt` includes: nameko, flask, flask-cors, pymongo, python-dotenv, bcrypt*)

### 3. 🐇 Install and run RabbitMQ

Install RabbitMQ and start it (usually runs on port `5672`).

### 4. 🗄️ MongoDB setup

Ensure MongoDB is running locally or update `MONGO_URI` in `.env` or `config.yaml`.

### 5. 🧪 Create `.env` file

```dotenv
AMQP_URI=pyamqp://guest:guest@localhost
MONGO_URI=mongodb://localhost:27017
MONGODB_DATABASE=questdatabase
```

---

## 🚀 Running the Services

### Start the Flask API Gateway

```bash
python app.py
```

### Start the Nameko Auth Service

```bash
nameko run main --config config.yaml
```

---

## 📡 API Endpoints

### POST `/sign-up`

Registers a new user.

**Body:**
```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

---

### GET `/log-in`

Logs in an existing user.

**Body:**
```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

---

## 📊 Documentation

See `api_documentation.ods` for detailed API schema and example calls.

---

## 🔐 Security Notes

- Passwords are hashed using `bcrypt`.
- CORS is open (`*`) – adjust for production use.

