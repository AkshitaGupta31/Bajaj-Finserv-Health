VIT BFHL – FastAPI Implementation

This project implements the Bajaj Finserv Health Ltd (BFHL) API assignment using FastAPI and deployed on Render.
It processes input arrays to classify numbers, alphabets, and special characters, while also computing sums and concatenated strings.

Live API

Base URL:

https://bajaj-finserv-health-wd0q.onrender.com


Endpoint:

POST /bfhl

How to Run Locally
1. Clone Repo
git clone <your-repo-url>
cd <your-repo-name>

2. Install Dependencies
pip install -r requirements.txt

3. Run Server
uvicorn main:app --reload


API will be available at:

http://127.0.0.1:8000/bfhl

Deployment (Render)

Push repo to GitHub.

On Render
 → Create New Web Service.

Connect your repo.

Use:

Build Command: pip install -r requirements.txt

Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT

Add Environment Variables:

FULL_NAME → "Your Name"

DOB_DDMMYYYY → "ddmmyyyy"

EMAIL → "your_email@example.com"

ROLL_NUMBER → "YourRollNumber"

Example Request

POST /bfhl

{
  "data": ["a","1","334","4","R","$"]
}


Response:

{
  "is_success": true,
  "user_id": "akshita_gupta_31012004",
  "email": "akshita31012004@gmail.com",
  "roll_number": "22BCE0248",
  "odd_numbers": ["1"],
  "even_numbers": ["334","4"],
  "alphabets": ["A","R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}


<img width="1638" height="927" alt="image" src="https://github.com/user-attachments/assets/b476e421-cad4-4dfb-9d42-fc104d2669d7" />



<img width="1918" height="406" alt="image" src="https://github.com/user-attachments/assets/4720e2c9-9e07-41d0-a161-b863044df337" />


Tech Stack

- Python 3.11

- FastAPI

- Uvicorn

- Render (deployment)





