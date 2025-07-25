# SPAM-CLASSIFICATION-FASTAPI-APP
This project is an **end-to-end Spam Classification System** that detects whether a given message is **spam or not spam**.  
It combines **Machine Learning**, a **FastAPI backend**, and **Docker** for containerized deployment.
## ⚙️ **Tech Stack**

- **Python 3.11**
- **scikit-learn** — ML model (Naive Bayes)
- **FastAPI** — REST API
- **Uvicorn** — ASGI server
- **Docker** — Containerization

---
## 📌 **Project Overview**

- **Model:** Naive Bayes classifier with TF-IDF vectorization.
- **API:** FastAPI serves a simple `/predict` endpoint for real-time predictions.
- **Deployment:** Docker makes it portable and reproducible across any environment.

---

## ✅ **Features**

- Clean **ML pipeline**: Data loading → Preprocessing → Training → Inference.
- **FastAPI** REST API for easy integration with other services or frontends.
- **Dockerized** for fast, consistent deployment on any OS or cloud.
- Easily extendable for real-world datasets or more advanced NLP models.

---

## 🚀 **Why FastAPI?**

✅ **FastAPI** is a modern, high-performance web framework for Python.  
- **Super-fast:** Built on **ASGI**, async-ready, and very fast.  
- **Easy docs:** Auto-generates interactive Swagger docs.  
- **Developer friendly:** Type hints + validation are built-in.
- **Production-ready:** Runs efficiently with `uvicorn`.

By using FastAPI instead of a basic Flask server or plain Python script, this project:
- Provides a **proper REST API**.
- Makes your model accessible over HTTP.
- Can be integrated with frontend apps, mobile apps, or other services.

---

## 📦 **Why Docker?**

✅ **Docker** packages your code, model, and environment into a single **container image**.  
- **Same everywhere:** Runs the same on your laptop, your server, or the cloud.
- **No “it works on my machine” problem:** Environment conflicts are eliminated.
- **Easy to deploy:** Plug-and-play on any OS with Docker installed.
- **Portable:** You can push your image to Docker Hub or run it on Kubernetes.

With Docker, this project:
- Is **reproducible**.
- Can be deployed to **Hugging Face Spaces**, AWS EC2, Azure, GCP, or a Raspberry Pi with no changes.

