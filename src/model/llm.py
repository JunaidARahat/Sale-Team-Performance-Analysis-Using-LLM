

import openai
from src.preprocess.preprocessing import employee_performance

openai.api_key = ""


def get_feedback(text_summary):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI specialized in analyzing sales performance."},
                {"role": "user", "content": f"Analyze this sales performance data and provide insights:\n\n{text_summary}"}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error generating feedback: {e}")
        return "Unable to generate feedback at this time."


 
# Function to generate employee feedback summary
def generate_employee_feedback(employee_data):
    try:
        summary = (
            f"Sales Rep {employee_data['employee_name']} took {employee_data['lead_taken']} leads, "
            f"booked {employee_data['tours_booked']} tours, and made {employee_data['applications']} applications."
        )
        return get_feedback(summary)
    except KeyError as e:
        print(f"Missing data for employee: {e}")
        return "Data missing for feedback generation."

# Iterating through employee performance data
for index, row in employee_performance.iterrows():
    feedback = generate_employee_feedback(row)
    print(f"Feedback for {row['employee_name']}: {feedback}")