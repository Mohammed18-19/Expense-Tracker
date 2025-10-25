# 💰 Expense Tracker  

A clean and minimal **Flask web app** that helps you manage and analyze your daily expenses.  
Built with **Python, Flask, SQLAlchemy, and SQLite**, this project demonstrates backend and frontend integration, CRUD operations, and a simple but functional user interface.

---

## 📋 Table of Contents
- [✨ Features](#-features)
- [🧠 Tech Stack](#-tech-stack)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [📁 Folder Structure](#-folder-structure)
- [🖼️ Screenshots](#️-screenshots)
- [🌱 Future Enhancements](#-future-enhancements)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👨‍💻 Author](#-author)

---

## ✨ Features

- ➕ Add, edit, and delete expenses  
- 📊 View all expenses with total calculation  
- 🔍 Filter expenses by category or date  
- ⚡ Flash messages for real-time feedback  
- 💾 Persistent data storage with SQLite  
- 🧩 Structured Flask app with models, routes, and templates  
- 🎨 Responsive design using HTML, CSS (and optionally TailwindCSS)

---

## 🧠 Tech Stack

| Category | Technology |
|-----------|-------------|
| **Language** | Python 3.x |
| **Framework** | Flask |
| **Database** | SQLite with SQLAlchemy ORM |
| **Frontend** | HTML, CSS, Jinja2 |
| **Environment** | Virtualenv / venv |

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Mohammed18-19/Expense-Tracker.git
cd Expense-Tracker


2. Create and Activate a Virtual Environment

python3 -m venv venv
source venv/bin/activate       # macOS / Linux
# or
venv\Scripts\activate          # Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the App
flask run

Your app should now be running at
👉 http://127.0.0.1:5000


🚀 Usage

1. Open the web app in your browser.
2. Add new expenses (description, amount, category, and date).
3. Edit or delete entries as needed.
4. Filter by date or category to view spending trends.
5. Stay aware of your daily and monthly expenses easily.


📁 Folder Structure

Expense-Tracker/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── add.html
│   │   └── edit.html
│   └── static/
│       └── style.css
│
├── requirements.txt
├── config.py
├── run.py
└── README.md


🤝 Contributing

Contributions and suggestions are always welcome!

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request


👨‍💻 Author

Mohammed Aintomar
💼 Github Profile: https://github.com/Mohammed18-19
📧 [aintomar.mohamed19@gmail.com]