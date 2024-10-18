from fastapi import FastAPI, HTTPException
from src.preprocess.preprocessing import load_sales_data, preprocess_data, summarize_by_employee
from src.model.llm import generate_employee_feedback
import pandas as pd
import os
import uvicorn

app = FastAPI()

# Load and preprocess data once at startup
data = load_sales_data('D:\\Sale Performance Analysis September 2024\\Sale-Team-Performance-Analysis-Using-LLM\\data\\sales_performance_data.csv')
processed_data = preprocess_data(data)
employee_performance = summarize_by_employee(processed_data)

# Function to calculate sales trends
def calculate_trends(sales_data, time_period):
    # Convert the date column to a datetime format
    sales_data['dated'] = pd.to_datetime(sales_data['dated'], errors='coerce')
    
    # Ensure the data is sorted by date
    sales_data = sales_data.sort_values(by='dated')

    # Resample the data based on the specified time period
    if time_period == 'monthly':
        trends = sales_data.resample('M', on='dated').agg({
            'lead_taken': 'sum',
            'tours_booked': 'sum',
            'applications': 'sum',
            'conversion_rate': 'mean'
        }).reset_index()
    elif time_period == 'quarterly':
        trends = sales_data.resample('Q', on='dated').agg({
            'lead_taken': 'sum',
            'tours_booked': 'sum',
            'applications': 'sum',
            'conversion_rate': 'mean'
        }).reset_index()
    else:
        raise HTTPException(status_code=400, detail="Invalid time_period. Use 'monthly' or 'quarterly'.")
    
    return trends

@app.get("/api/rep_performance")
def rep_performance(rep_id: int):
    # Check if rep_id exists in the data
    rep_data = employee_performance.loc[employee_performance['employee_id'] == rep_id]
    
    if rep_data.empty:
        raise HTTPException(status_code=404, detail=f"Sales Rep with ID {rep_id} not found.")
    
    # Get the first record if found
    rep_data = rep_data.iloc[0]
    feedback = generate_employee_feedback(rep_data)
    
    return {"rep_id": rep_id, "feedback": feedback}

@app.get("/api/team_performance")
def team_performance():
    team_summary = employee_performance.to_dict(orient='records')
    return {"team_summary": team_summary}

@app.get("/api/performance_trends")
def performance_trends(time_period: str):
    try:
        trends = calculate_trends(processed_data, time_period)
        return {"message": f"Sales trends for {time_period}", "trends": trends.to_dict(orient='records')}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT is not set
    uvicorn.run("app:app", host="0.0.0.0", port=port)