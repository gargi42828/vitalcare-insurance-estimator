# 🩺 VitalCare — AI-Powered Insurance Cost Estimator

<p align="center">
  <strong>Smarter Insights. Better Planning. A Healthier Financial Future.</strong>
</p>

<p align="center">
  A machine learning-powered web application that estimates health insurance charges using demographic and lifestyle-related information.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-0D9488?style=for-the-badge" alt="Machine Learning"/>
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn"/>
</p>

---

## 🌿 About VitalCare

**VitalCare** is a machine learning-based insurance cost estimation application designed to make insurance prediction simple, accessible, and interactive.

The application uses a trained machine learning model to estimate insurance charges based on user-provided information. Its modern, healthcare-inspired interface combines predictive analytics with an intuitive web experience.

## ✨ Features

- 🩺 Modern healthcare-inspired user interface.
- 🤖 Machine learning-based insurance cost prediction.
- 🧮 Personalized estimates using age, BMI, number of children, sex, smoking status, and region.
- ⚡ Instant prediction results through an interactive web form.
- 📊 Data-driven predictions using an insurance dataset.
- 🌐 Browser-based access through a Flask web application.
- 📱 Customizable frontend built with HTML and CSS.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Backend web framework |
| Scikit-learn | Machine learning |
| NumPy | Numerical computations |
| Joblib | Loading the trained model |
| Pandas | Data processing and analysis |
| HTML | Frontend structure |
| CSS | Frontend styling |
| Render | Cloud deployment |

## 🧠 How It Works

1. **User Input:** Enter the required demographic and lifestyle information.
2. **Data Processing:** The application prepares the input in the format expected by the trained model.
3. **Machine Learning:** The model predicts the estimated insurance charges.
4. **Results:** The predicted cost is displayed on the website.

```text
User Input
    ↓
Flask Web Application
    ↓
Input Processing
    ↓
Trained ML Model
    ↓
Insurance Cost Prediction
    ↓
Display Results
```

## 📋 Prediction Parameters

| Parameter | Description |
|---|---|
| Age | Age of the individual |
| BMI | Body Mass Index |
| Children | Number of dependent children |
| Sex | Sex category used by the dataset |
| Smoker | Smoking status |
| Region | Geographical region |

**Target variable:** Insurance charges.

## 📁 Project Structure

```text
VitalCare_Insurance_Estimator/
│
├── app.py
├── insurance.csv
├── insurance_model.pkl
├── requirements.txt
├── runtime.txt
├── Procfile
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── health2 (1).ipynb
```

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/gargi42828/vitalcare-insurance-estimator.git
```

### 2. Navigate to the Project

```bash
cd vitalcare-insurance-estimator
```

If the application files are inside a nested directory, navigate into that directory before continuing.

### 3. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000/

## ☁️ Deployment

VitalCare can be deployed using Render.

1. Upload the project to GitHub.
2. Open [Render](https://render.com/).
3. Select **New + → Web Service**.
4. Connect the GitHub repository.
5. Configure the following settings.

| Setting | Value |
|---|---|
| Runtime | Python |
| Root Directory | Leave blank if files are in the repository root |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

6. Click **Create Web Service**.
7. Wait for the deployment to complete.
8. Open the public URL provided by Render.

The application becomes publicly accessible after a successful deployment.

## 🔮 Future Enhancements

- 📊 Interactive data visualizations and cost analytics.
- 📈 Model comparison and performance evaluation.
- 🗂️ Prediction history and downloadable reports.
- 📱 Enhanced mobile responsiveness.
- 🔐 Secure authentication and improved application security.
- 💡 Prediction explanations and insurance cost insights.

## 🎯 Learning Outcomes

This project demonstrates practical experience in:

- Python programming and data processing.
- Machine learning model integration.
- Flask web application development.
- Connecting frontend forms to backend prediction logic.
- Working with datasets and trained models.
- Deploying Python applications to cloud platforms.

## ⚠️ Disclaimer

VitalCare provides insurance cost estimates for educational and informational purposes only. Predictions depend on the trained model and its underlying dataset. Results are not official insurance quotes, medical advice, or a guarantee of actual insurance charges.

## 👩‍💻 Author

**Gargi Verma**

GitHub: [@gargi42828](https://github.com/gargi42828)

## ⭐ Support

If you find this project useful, consider starring the repository, exploring the code, or contributing ideas for future improvements.

---

<p align="center">
  <strong>VitalCare — Bringing Machine Learning Closer to Healthcare.</strong>
</p>
