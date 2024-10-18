# Sale-Team-Performance-Analysis-Using-LLM 

# Dataset Description


```bash
The Dataset contains various columns related to sales performance. Here is a summary of the key columns:

employee_id: Unique identifier for each sales representative.
employee_name: Name of the sales representative.
lead_taken: Number of leads taken by the employee.
tours_booked: Number of tours booked.
applications: Number of applications made.
tours_per_lead: Ratio of tours booked per lead taken.
apps_per_tour: Ratio of applications per tour booked.
apps_per_lead: Ratio of applications per leads.
fri_call, sat_call, ... sun_call: Number of calls made on specific days of the week.
fri_text, sat_text, ... sun_text: Number of texts sent on specific days of the week.
This dataset includes detailed sales and communication performance metrics for each sales representative. It will allow you to calculate important metrics such as:

Target achievement: Using ratios like tours per lead or apps per tour.
Growth trends: By comparing the performance across different time periods.
```
# Key Observations
```bash
Leads and Tours: Each employee is tracked based on the number of leads they have taken (lead_taken) and how many tours they have booked (tours_booked).

Example: Camilla Ali took 44 leads and booked 2 tours, while Maaz Brown took 27 leads and booked 1 tour.
Performance Metrics:

Tours Per Lead: This is calculated directly in the dataset as tours_per_lead, indicating the efficiency of converting leads into tours.
Apps Per Tour: Similarly, apps_per_tour shows how effective tours are in converting to applications.
Apps Per Lead: Shows how efficient the rep is in converting leads directly into applications, which is a key performance metric for lead quality.
Calls and Texts: There are metrics for communication (both calls and texts) across each day of the week (fri_call, sat_call, etc.), which can give insights into communication patterns and how they might influence sales.

For example, Camilla Ali made 13 calls on Sunday, which was her most active communication day, while Maaz Brown made only 3 calls on Friday and Saturday.
Possible Insights and Calculations:
Target Achievement: You can calculate target achievement by comparing applications or tours booked against leads taken.
Sales Growth Trends: By tracking the performance metrics over multiple weeks or months, we can identify growth or decline patterns.
Communication Patterns: The communication data across different days of the week can be correlated with sales metrics to see if higher engagement on certain days translates into better results.
What’s Next?
For a more in-depth analysis, we can:

Preprocess the data to generate insights such as overall conversion rates, growth trends, and individual performance scores.
Feed the summaries to the LLM to generate qualitative feedback, such as suggestions on improving sales strategy based on performance trends.
```
# Overview of the Sales Team Performance Analysis Project Using LLM
```bash
This project focuses on building a backend system that leverages a Large Language Model (LLM) to analyze sales performance data. The system is designed to provide qualitative and actionable insights into individual sales representatives and the overall team's performance, alongside forecasting sales trends. The project includes data ingestion, preprocessing, integration with an LLM, and the development of multiple RESTful API endpoints to provide performance feedback and sales analysis.
```
# Project Objectives:
```bash
Data Ingestion: Implement a mechanism to load and preprocess sales data from CSV (or JSON) files.
LLM Integration: Utilize a Large Language Model (like GPT) to generate performance insights for individual sales representatives and the sales team as a whole.
REST API Development: Develop multiple API endpoints to query individual and team performance, as well as provide trends and forecasting insights based on the data.
Feedback Generation: Use the LLM to deliver actionable feedback, identify trends, and forecast future performance.
```
# Key Functionalities:
```bash
1. Data Preprocessing:

Load and preprocess the sales data to calculate key performance indicators (KPIs), such as leads taken, tours booked, applications processed, and conversion rates.
Convert the raw sales data into summaries by employee and overall team statistics.
LLM Integration:

2. Integrate a pre-trained Large Language Model (LLM) (such as GPT) to analyze the preprocessed data and generate feedback for each sales representative.
Generate insights, comments, and qualitative performance feedback for individual sales representatives and teams.
3. API Endpoints:

/api/rep_performance: Fetch detailed performance feedback for a specific sales representative based on their ID.
/api/team_performance: Provide a summary of the entire sales team's performance.
/api/performance_trends: Analyze and forecast sales trends over a specified time period (monthly or quarterly).
```

# How to run?
### STEPS:

# Clone the repository

```bash
Project repo: https://github.com/JunaidARahat/Sale-Team-Performance-Analysis-Using-LLM.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n sale python=3.9 -y
```

```bash
conda activate sale
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Write openai credentials as follows:

```bash
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


Now,
```bash
uvicorn app:app --reload
```


### Techstack Used:

- Python
- FastAPI
- GPT
- PostMan
