# Dependencies and Setup
import pandas as pd
from pathlib import Path
import pandas as pd

# Path to the CSV file
file_path = 'C:/Users/000154302/OneDrive/dataviz2024/UNC-VIRT-DATA-PT-06-2024-U-LOLC/Homework/Pandas-Challenge/schools_data.csv'

# Read the CSV file into a DataFrame
school_data = pd.read_csv(file_path)

# Calculate the Disctrict Summary
district_summary = {
    "Total Schools": school_data["school_name"].nunique(),
  "Total Students": school_data["student_name"].nunique(),
    "Total Budget": school_data["budget"].sum(),
    "Average Math Score": school_data["math_score"].mean(),
    "Average Reading Score": school_data["reading_score"].mean(),
    "% Passing Math": (school_data["math_score"] >= 70).mean() * 100,
    "% Passing Reading": (school_data["reading_score"] >= 70).mean() * 100,
    "% Overall Passing": ((school_data["math_score"] >= 70) & (school_data["reading_score"] >= 70)).mean() * 100
}

# Print the summary
for key, value in district_summary.items():
    print(f"{key}: {value}")

district_summary_df = pd.DataFrame([district_summary])
# School Summary calculations
school_summary = school_data_complete.groupby("school_name").agg(
    School_Type=('type', 'first'),
    Total_Students=('student_name', 'count'),
    Total_Budget=('budget', 'first'),
    Per_Student_Budget=('budget', 'first') / school_data_complete.groupby("school_name")['student_name'].count(),
    Average_Math_Score=('math_score', 'mean'),
    Average_Reading_Score=('reading_score', 'mean'),
    Percentage_Passing_Math= lambda x: (x['math_score'] >= 70).mean() * 100,
    Percentage_Passing_Reading= lambda x: (x['reading_score'] >= 70).mean() * 100,
    Percentage_Overall_Passing= lambda x: ((x['math_score'] >= 70) & (x['reading_score'] >= 70)).mean() * 100
)

# Rename columns for clarity
school_summary = school_summary.rename(columns={
    "Percentage_Passing_Math": "% Passing Math",
    "Percentage_Passing_Reading": "% Passing Reading",
    "Percentage_Overall_Passing": "% Overall Passing"
})
# Highest-Performing Schools
top_schools = school_summary.sort_values(by="Percentage Overall Passing", ascending=False).head(5)

# Lowest-Performing Schools
bottom_schools = school_summary.sort_values(by="Percentage Overall Passing").head(5)
# Math Scores by Grade
math_scores_by_grade = school_data_complete.groupby(["school_name", "grade"])["math_score"].mean().unstack() # type: ignore

# Reading Scores by Grade
reading_scores_by_grade = school_data_complete.groupby(["school_name", "grade"])["reading_score"].mean().unstack() # type: ignore
# Binning school spending
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]
school_data_complete['Spending Ranges (Per Student)'] = pd.cut(school_data_complete['budget'] / school_data_complete['Total_Students'], bins=spending_bins, labels=labels)

# Calculate mean scores per spending range
spending_summary = school_data_complete.groupby("Spending Ranges (Per Student)").agg(
    Average_Math_Score=('math_score', 'mean'),
    Average_Reading_Score=('reading_score', 'mean'),
    Percentage_Passing_Math= lambda x: (x['math_score'] >= 70).mean() * 100,
    Percentage_Passing_Reading= lambda x: (x['reading_score'] >= 70).mean() * 100,
    Percentage_Overall_Passing= lambda x: ((x['math_score'] >= 70) & (x['reading_score'] >= 70)).mean() * 100
).rename(columns={
    "Percentage_Passing_Math": "Percentage Passing Math",
    "Percentage_Passing_Reading": "Percentage Passing Reading",
    "Percentage_Overall_Passing": "Percentage Overall Passing"
})
# Binning school size
size_bins = [0, 1000, 2000, 5000]
size_labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
school_summary['School Size'] = pd.cut(school_summary['Total_Students'], bins=size_bins, labels=size_labels)

# Calculate metrics by school size
size_summary = school_summary.groupby("School Size").agg(
    Average_Math_Score=('Average_Math_Score', 'mean'),
    Average_Reading_Score=('Average_Reading_Score', 'mean'),
    Percentage_Passing_Math= ('Percentage Passing Math', 'mean'),
    Percentage_Passing_Reading= ('Percentage Passing Reading', 'mean'),
    Percentage_Overall_Passing= ('Percentage Overall Passing', 'mean')
)
# Calculate metrics by school type
type_summary = school_summary.groupby("School_Type").agg(
    Average_Math_Score=('Average_Math_Score', 'mean'),
    Average_Reading_Score=('Average_Reading_Score', 'mean'),
    Percentage_Passing_Math= ('Percentage Passing Math', 'mean'),
    Percentage_Passing_Reading= ('Percentage Passing Reading', 'mean'),
    Percentage_Overall_Passing= ('Percentage Overall Passing', 'mean')
)
