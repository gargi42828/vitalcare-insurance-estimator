# VitalCare — Insurance Cost Estimator

A responsive healthcare-inspired web interface for an educational medical insurance cost prediction project. Flask serves the interface and a pre-trained scikit-learn Linear Regression model estimates annual charges from the supplied demographic and lifestyle features.

## Features
- Responsive dashboard with health-and-wellness styling
- Insurance cost estimation form with input validation
- Annual and approximate monthly estimate display
- JSON prediction endpoint (`POST /api/predict`)
- Health check endpoint (`GET /health`) for hosting diagnostics
- Production WSGI server configuration for deployment

## Run locally (Windows PowerShell)
1. Install Python 3.11 (recommended for the supplied model artifact).
2. Open PowerShell in this project folder.
3. Create and activate an environment:
   ```powershell
   py -3.11 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   python app.py
   ```
4. Visit http://127.0.0.1:5000. Check http://127.0.0.1:5000/health for model status.

## Deploy publicly with Render
1. Create a GitHub repository and upload the contents of this folder (including `insurance_model.pkl`). Do not upload private data or credentials.
2. Sign in to Render and choose **New → Web Service**, then connect the repository.
3. Use **Python 3** / Python 3.11 if a version selector is available. Build command: `pip install -r requirements.txt`. Start command: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 60`. The included `Procfile` contains the same start command.
4. Deploy, wait for the build to finish, and open the generated `https://...onrender.com` URL. Check `/health` and submit a test estimate. The exact public URL is assigned by the hosting provider.

## API example
`POST /api/predict` with JSON body:
```json
{
  "age": 29,
  "bmi": 24.5,
  "children": 0,
  "sex": "female",
  "smoker": "no",
  "region": "northeast"
}
```
The response contains `estimated_annual_cost`, `currency`, and a disclaimer.

## Important limitations
This is a student/portfolio demonstration, not a medical service, insurer quote, or financial recommendation. Predictions depend on the quality and limitations of the historical training dataset and model. Do not use it to make real insurance or healthcare decisions. The model artifact was supplied with the original project; its training pipeline should be reviewed and reproduced before production use.
