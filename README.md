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
apps_per_lead: Ratio of applications per lead.
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