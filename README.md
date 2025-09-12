# Movie Recommender System

## Project Overview
A **content-based Movie Recommender System** that suggests movies similar to a chosen title by comparing movie metadata (genres, cast, crew, keywords, overview).  
The system precomputes similarity scores and serves recommendations via **FastAPI (backend)** and **Streamlit (demo UI)** or **HTML/CSS/JS frontend**.

---

## Features
- Content-based recommendations (top-5 similar movies)
- Uses metadata: genres, cast (top 3), director, keywords, overview
- Preprocessing pipeline to merge all features into a single `tags` field
- Precomputed similarity matrix for **fast lookups**
- Poster fetching from TMDb API (with caching and fallbacks)
- Multiple UI options:
  - Streamlit prototype  
  - HTML/CSS/JS frontend with FastAPI backend
- Deployable on Render, DigitalOcean, or Docker

---

## Tech Stack
- **Python** (pandas, scikit-learn, numpy)
- **FastAPI** (backend API)
- **Streamlit** (quick demo UI)
- **Requests** (fetch TMDb posters)
- **Pickle** (save processed data & similarity matrix)
- **Frontend**: HTML, CSS, JS (or React/Node as optional upgrade)

---

# Running Locally

## Install dependencies
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Start FastAPI
```bash
uvicorn backend.main:app --reload
```

## Run Streamlit
```bash
streamlit run streamlit_app/app.py
```



