# Sale-Team-Performance-Analysis-Using-LLM 

# Dataset Description

```bash
The CSV data you've uploaded contains various columns related to sales performance. Here's a summary of the key columns:

employee_id: Unique identifier for each sales representative.
employee_name: Name of the sales representative.
lead_taken: Number of leads taken by the employee.
tours_booked: Number of tours booked.
applications: Number of applications made.
tours_per_lead: Ratio of tours booked per lead taken.
apps_per_tour: Ratio of applications per tour booked.
apps_per_lead: Ratio of applications per lead.
fri_call, sat_call, ... sun_call: Number of calls made on specific days of the week.
fri_text, sat_text, ... sun_text: Number of texts sent on specific days of the week.
This dataset includes detailed sales and communication performance metrics for each sales representative. It will allow you to calculate important metrics such as:

Target achievement: Using ratios like tours per lead or apps per tour.
Growth trends: By comparing the performance across different time periods.
```


# How to run?
### STEPS:

# Clone the repository

```bash
Project repo: https://github.com/
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


```bash
# perform EDA and Integrate LLM Model

```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
uvicorn a pp:app --reload
```


### Techstack Used:

- Python
- Fast API
- GPT
-