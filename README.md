# 🔐 Microservice-Based Authentication System

A lightweight microservice-based authentication system using **Nameko**, **Flask**, and **MongoDB**. It allows users to sign up and log in securely with hashed passwords.


---

## 🗂️ Project Structure

```
server/
├── api_services/
│   ├── app.py                           # Flask entry point
│   └── authorization/
│       └── authorization.py            # Flask Blueprint routes
│
├── nameko_services/
│   ├── config.yaml                     # Nameko config (AMQP)
│   ├── main.py                         # Nameko runner
│   ├── mongodbsingleton.py            # MongoDB singleton connection
│   └── auth_service/
│       └── auth_service.py            # Nameko RPC-based Auth logic
│
└── .env                                # Environment variables (Mongo, AMQP)
```

---

## ⚙️ Technologies Used

- Python 3.8+
- Flask
- Nameko (microservices framework)
- MongoDB
- RabbitMQ (AMQP transport)
- bcrypt (for password hashing)
- python-dotenv

---

## 📦 Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Setup Environment

Create a `.env` file in the `server/` folder with:

```env
MONGO_URI=mongodb://localhost:27017/
MONGODB_DATABASE=questdatabase
AMQP_URI=pyamqp://guest:guest@localhost
```

Make sure both MongoDB and RabbitMQ are running locally.

---

## 🚀 Running the Application

### 1. Start Nameko Auth Service

```bash
cd server/nameko_services
python main.py
```

> Ensure `config.yaml` exists and contains:
> ```yaml
> AMQP_URI: "pyamqp://guest:guest@localhost"
> ```

### 2. Start Flask API Gateway

```bash
cd server/api_services
python app.py
```

---

## 📡 API Endpoints

| Method | Endpoint    | Description         |
|--------|-------------|---------------------|
| POST   | `/sign-up`  | Register a new user |
| POST   | `/log-in`   | Authenticate user   |

---

## 🔐 Sample Requests

### Sign Up

```bash
curl -X POST http://localhost:5000/sign-up \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "secret"}'
```

### Log In

```bash
curl -X POST http://localhost:5000/log-in \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "secret"}'
```



## 📊 Documentation

See `api_documentation.png` for detailed API schema and example calls.

---

## 🔐 Security Notes

- Passwords are hashed using `bcrypt`.
- CORS is open (`*`) – adjust for production use.
