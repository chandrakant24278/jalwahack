# jalwa_predictor_api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PeriodRequest(BaseModel):
    period_number: int

def get_color(number):
    if number in [0, 5]:
        return "Violet"
    elif number % 2 == 0:
        return "Green"
    else:
        return "Red"

def get_size(number):
    return "Small" if number <= 4 else "Big"

@app.post("/predict")
def predict_result(req: PeriodRequest):
    num = req.period_number % 10
    return {
        "period": req.period_number,
        "predicted_number": num,
        "predicted_color": get_color(num),
        "predicted_size": get_size(num)
    }
