
import pandas as pd

def load_sales_data(file_path):
    sales_data = pd.read_csv(file_path)
    return sales_data

# Example usage
data = load_sales_data('D:\\Sale Performance Analysis September 2024\\Sale-Team-Performance-Analysis-Using-LLM\\data\\sales_performance_data.csv')


def preprocess_data(sales_data):
    # Handle missing values
    sales_data.fillna(0, inplace=True)

    
    # Calculate overall conversion rates
    sales_data['conversion_rate'] = sales_data['applications'] / sales_data['lead_taken'].replace(0, 1)
    return sales_data

processed_data = preprocess_data(data)

def summarize_by_employee(sales_data):
    employee_summary = sales_data.groupby(['employee_id','employee_name']).agg({
        'lead_taken': 'sum',
        'tours_booked': 'sum',
        'applications': 'sum',
        'conversion_rate': 'mean'
    }).reset_index()

    return employee_summary

employee_performance = summarize_by_employee(processed_data)

