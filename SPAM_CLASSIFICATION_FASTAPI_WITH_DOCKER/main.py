import pickle
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Annotated
with open('spam_model.pkl','rb') as f:
    model=pickle.load(f)
with open('tfidf_vectorizer.pkl','rb') as f:
    vectorizer=pickle.load(f)



app = FastAPI()

class EmailRequest(BaseModel):
    content: str

# 4️⃣ Predict route
@app.get('/')    # Ist endpoint
def show():
    return "Welcome to the ML Page"

@app.post("/predict")    # 2nd endpoint
@app.post("/predict")
def predict_spam(request: EmailRequest):
    try:
        if not request.content or len(request.content.strip()) == 0:
            raise HTTPException(status_code=400, detail="Input text is empty.")
        
        text = [request.content]
        vectorized = vectorizer.transform(text)
        prediction = model.predict(vectorized)[0]
        result = "Spam" if prediction == 1 else "Not Spam"
        return {"prediction": result}

    except HTTPException as e:
        raise e

    except Exception as e:
        # Catch other unexpected errors
        raise HTTPException(status_code=500, detail=str(e))

