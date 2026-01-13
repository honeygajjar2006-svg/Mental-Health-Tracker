def predict_risk(model, user_input):
    
    try:
        risk = model.predict([user_input])[0]
    except Exception:
        
        risk = "High" if user_input[1] > 7 else "Moderate" if user_input[1] > 4 else "Low"
    return risk
