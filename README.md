# ⚡ Discipline | Daily Performance MicroSaaS

**Discipline** is a high-performance, containerized microSaaS designed to help users track their daily habits, fitness, nutrition, and recovery. Built with a "get-it-done" philosophy, it features a modern glassmorphic UI and a robust FastAPI backend.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688)
![React](https://img.shields.io/badge/Frontend-React-61DAFB)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791)

---

## 🚀 Key Modules

The application is structured into four core pillars of self-discipline:

* **✅ Checklists**: Daily habit tracking with persistent task management.
* **🏋️ Workouts**: Log exercises, sets, and reps to track physical progression.
* **🍎 Diet Plans**: Manage meal types and calorie counts for precision nutrition.
* **😴 Sleep Logs**: Track sleep/wake cycles and qualitative recovery scores.

---

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | React.js (Vite), Lucide Icons, Vanilla CSS (Glassmorphism) |
| **Backend** | Python 3.10+, FastAPI, SQLAlchemy |
| **Database** | PostgreSQL 15 |
| **Infrastructure** | Docker, Docker Compose |
| **Documentation** | Swagger / OpenAPI |

---

## 🏗️ Getting Started

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.
* `git` for cloning the repository.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/discipline-app.git](https://github.com/your-username/discipline-app.git)
    cd discipline-app
    ```

2.  **Spin up the environment:**
    The application is fully containerized. Use Docker Compose to build and start the DB, Backend, and Frontend services:
    ```bash
    docker compose up --build
    ```

3.  **Access the application:**
    * **Frontend UI:** [http://localhost:5173](http://localhost:5173)
    * **Backend API:** [http://localhost:8000](http://localhost:8000)
    * **Interactive API Docs (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📊 Database Schema

The system utilizes a relational PostgreSQL schema managed via SQLAlchemy ORM. The core entities include:
* `users`: Identity and authentication.
* `checklists`: Daily task completion (Boolean tracking).
* `workouts`: Exercise logging (Integer-based tracking).
* `diet_plans`: Nutritional data (Text/Integer description).
* `sleep_logs`: Time-based recovery metrics.

---

## 🛠️ API Development

The API follows RESTful principles. Most modules support the following pattern:
* `GET /api/{module}/?request_date=YYYY-MM-DD` - Fetch entries for a specific day.
* `POST /api/{module}/` - Create a new entry.
* `PUT /api/checklists/{id}` - Toggle completion status.

---

## 📝 License

This project is licensed under the MIT License. Feel free to use it as a template for your own MicroSaaS ventures.

---
*Built with focus and discipline.*
