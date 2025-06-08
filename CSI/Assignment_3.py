import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("C:\\Users\\acer\\Downloads\\indian_patient_sentiment_data.csv")

# Set seaborn style
sns.set(style="whitegrid")

# 1. Emotion distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Emotion', order=df['Emotion'].value_counts().index, palette="Set2")
plt.title('Distribution of Patient Emotions')
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Satisfaction Score distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='SatisfactionScore', palette='coolwarm')
plt.title('Distribution of Satisfaction Scores')
plt.xlabel('Satisfaction Score')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 3. Average satisfaction score by department
plt.figure(figsize=(10, 6))
dept_scores = df.groupby("Department")["SatisfactionScore"].mean().sort_values()
sns.barplot(x=dept_scores.values, y=dept_scores.index, palette="viridis")
plt.title("Average Satisfaction Score by Department")
plt.xlabel("Average Satisfaction Score")
plt.ylabel("Department")
plt.tight_layout()
plt.show()

# 4. Correlation heatmap between numerical features
plt.figure(figsize=(8, 6))
numerical_cols = ['Cleanliness', 'StaffFriendliness', 'Billing', 'SatisfactionScore']
corr = df[numerical_cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
