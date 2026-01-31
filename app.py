import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Student Analysis", layout="centered")

# Title
st.title("📊 Student Data Analysis")

# Load data
try:
    df = pd.read_csv('Students_Data.csv')
    st.success("✅ Data loaded successfully!")
except:
    st.error("❌ Could not load data. Make sure 'Students_Data (2).csv' is in the same folder.")
    st.stop()

# Calculate simple metrics
df['Total_Score'] = df['Maths Score'] + df['Reading Score'] + df['Writing Score']
df['Average_Score'] = df['Total_Score'] / 3

# Sidebar - Filter Section
st.sidebar.header("🔍 Filter Data")
selected_gender = st.sidebar.selectbox("Select Gender", ["All"] + list(df['Gender'].unique()))

if selected_gender != "All":
    filtered_df = df[df['Gender'] == selected_gender]
else:
    filtered_df = df

# Sidebar - Author Info Section (ADDED THIS)
st.sidebar.markdown("---")  # Add a divider
st.sidebar.header("📝 About This App")
st.sidebar.info("""
**Created by:** KRRISH GURUNG  
**Email:** krrishgurung1610@gmail.com 
**Date:** 30-jan-2026 
**Version:** 1.0  

**Features:**  
• Student performance analytics  
• Gender-based analysis  
• Interactive visualizations  
• Real-time filtering  
""")

# Show basic stats
st.subheader("📈 Basic Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", len(filtered_df))
col2.metric("Avg Math Score", f"{filtered_df['Maths Score'].mean():.1f}")
col3.metric("Avg Reading Score", f"{filtered_df['Reading Score'].mean():.1f}")

# Visualization 1: Simple histogram
st.subheader("📊 Math Score Distribution")
fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.hist(filtered_df['Maths Score'], bins=20, color='blue', alpha=0.7, edgecolor='black')
ax1.set_xlabel("Math Score")
ax1.set_ylabel("Number of Students")
st.pyplot(fig1)

# Visualization 2: Simple bar chart
st.subheader("📈 Average Scores by Gender")
fig2, ax2 = plt.subplots(figsize=(8, 4))
avg_scores = df.groupby('Gender')[['Maths Score', 'Reading Score', 'Writing Score']].mean()
avg_scores.plot(kind='bar', ax=ax2)
ax2.set_xlabel("Gender")
ax2.set_ylabel("Average Score")
st.pyplot(fig2)

# Show some data
st.subheader("📋 Sample Data (First 10 rows)")
st.dataframe(filtered_df[['Gender', 'Maths Score', 'Reading Score', 'Writing Score']].head(10))

# Footer with additional info
st.markdown("---")
st.markdown("""
### ℹ️ About This Analysis
This application provides insights into student performance data. The analysis includes:

1. **Score Distribution**: Shows how scores are spread across students
2. **Gender Comparison**: Compares average scores between male and female students
3. **Basic Statistics**: Provides key metrics for quick understanding
4. **Interactive Filtering**: Allows filtering by gender for focused analysis

**Data Source:** Student Performance Dataset  
**Tools Used:** Python, Streamlit, Pandas, Matplotlib  

""")
