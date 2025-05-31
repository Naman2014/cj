# Coding Ninjas Learning Assistant

This is an AI-powered programming learning companion built with Streamlit and custom agents.

## Features
- Understand programming concepts
- Get help with code
- Create study plans
- Receive motivation

## Deployment (Render)

### 1. Requirements
- Python 3.8+
- All dependencies in `requirements.txt`

### 2. Render Setup
- Add this repository to a new **Web Service** on [Render](https://render.com/).
- Set the build command to `pip install -r requirements.txt` (default).
- Set the start command to:
  ```
  streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
  ```
- Ensure the environment is set to **Python**.

### 3. Files
- `app.py`: Main entry point (Streamlit app)
- `requirements.txt`: Python dependencies
- `Procfile`: Specifies the web service command for Render
- `agents/`: Contains all agent logic

### 4. Usage
- Once deployed, visit the Render-provided URL to interact with the assistant.

---

**Local Development:**
```bash
pip install -r requirements.txt
streamlit run app.py
``` 