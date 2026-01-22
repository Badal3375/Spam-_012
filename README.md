👤 Author

Badal Singh


Machine Learning & Django Developer

Email -singh.badal3375@gmail.com <br>

If you have received the code and all the files related to this project, please comment or send an email.



📧 Spam Detection Web Application (ML + Django)
📌 Project Overview

This project is a Spam Detection Web Application built using Machine Learning and Django. The application allows users to enter a message or email text and predicts whether it is Spam or Not Spam using a trained machine learning model. The system demonstrates the complete integration of an ML model into a web application.

🎯 Objectives

Detect spam messages using machine learning techniques

Integrate ML model with Django backend

Provide a simple and user-friendly web interface

Demonstrate real-world ML deployment

🛠️ Technologies Used
🔹 Backend

Python 3.x

Django

Scikit-learn

Pickle

🔹 Frontend

HTML

CSS

Bootstrap

🔹 Machine Learning

TF-IDF Vectorizer

Naive Bayes / Logistic Regression (or any ML model used)

Text preprocessing (tokenization, stopword removal)

📂 Project Structure
spam_detection/
│
├── spam_app/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── spam_detection/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/spam-detection-django.git
cd spam-detection-django

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the Server
python manage.py runserver

6️⃣ Open Browser
http://127.0.0.1:8000/

🧠 Machine Learning Workflow

Data Collection

Text Cleaning & Preprocessing

Feature Extraction using TF-IDF

Model Training

Model Evaluation

Model Saving using Pickle

Model Integration with Django

📊 Model Performance

Accuracy: ~95% (depends on dataset and model)

Algorithm Used: Naive Bayes / Logistic Regression

Vectorizer: TF-IDF

🖥️ Application Features

Input message/email text

Real-time prediction

Displays result as Spam or Not Spam

Clean and responsive UI

🔮 Future Enhancements

Add deep learning models (LSTM / BERT)

User authentication

Store prediction history

Deploy on cloud (AWS / Heroku / Render)

📚 Learning Outcomes

End-to-end ML project implementation

Django and ML model integration

Real-world web application development

Deployment-ready ML solution

 
