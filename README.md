# 🚀 Quantum Secure Communication using BB84   Protocol and Image Steganography 

A modern full-stack web application that combines **Quantum Key Distribution (QKD)** concepts with **Image Steganography** to securely encrypt and hide messages inside images.

---

## ✨ Features

* 🔐 Quantum-inspired Encryption (QKD)
* 🖼️ Image Steganography (Hide secret messages in images)
* 🔓 Secure Decryption with Key Validation
* ⚡ React Frontend + Flask Backend
* 🎨 Premium UI
* 🚫 Invalid Key Detection

---

## 🛠️ Tech Stack

### Frontend

* React.js
* CSS

### Backend

* Python
* Flask
* Pillow
* Flask-CORS

---

## 📁 Project Structure

```
quantum-stego-ui/
│
├── backend/
│   ├── app.py
│   ├── utils/
│   │   ├── encrypt.py
│   │   ├── decrypt.py
│   │   ├── qkd.py
│   │   ├── stego.py
│   │   └── __init__.py
│
├── src/
│   ├── components/
│   │   ├── Encrypt.js
│   │   ├── Decrypt.js
│   │   └── Navbar.js
│   ├── App.js
│   └── App.css
│
├── package.json
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/quantum-stego-ui.git
cd quantum-stego-ui
```

---

## 🔧 Backend Setup

```bash
cd backend
python -m venv venv
```

### ▶️ Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 📦 Install Dependencies

```bash
pip install flask flask-cors pillow
```

### ▶️ Run Backend

```bash
python app.py
```

👉 Server runs at:
http://127.0.0.1:5000

---

## 💻 Frontend Setup

```bash
npm install
npm start
```

👉 App runs at:
http://localhost:3000

---

## 🔄 How It Works

### 🔐 Encryption Process

1. Enter your secret message
2. Generate Quantum Key (QKD)
3. Encrypt message using XOR
4. Hide encrypted message inside image
5. Download stego image

---

### 🔓 Decryption Process

1. Upload stego image
2. Enter the secret key
3. Extract hidden data
4. Decrypt message

✅ Correct Key → Original Message
❌ Wrong Key → Invalid Key

---

## 🔗 API Endpoints

| Method | Endpoint | Description            |
| ------ | -------- | ---------------------- |
| POST   | /encrypt | Encrypt & hide data    |
| POST   | /decrypt | Extract & decrypt data |

---

## ⚠️ Troubleshooting

### ❌ Module Not Found Error

```js
import Encrypt from "./components/Encrypt";
```

✔️ Make sure file names and paths are correct

---

### ❌ CORS Error (Backend)

```python
from flask_cors import CORS
CORS(app)
```

---

## 🎯 Future Improvements

* 🔬 Real Quantum Cryptography Integration
* ☁️ Cloud Deployment
* 📱 Mobile Responsive UI
* 🖱️ Drag & Drop Image Upload
* 🤖 AI-based Enhancements

---

## 🤝 Contributing

1. Fork the repository
2. Clone your fork
3. Create a new branch
4. Commit your changes
5. Push to GitHub
6. Create a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.


## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🔁 Share it
* 💡 Build more

---
