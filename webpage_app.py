import streamlit as st
import pandas as pd
import altair as alt

# Load the telco data
telco_data = pd.read_csv('satisfaction_data.csv')

# Set page configuration
st.set_page_config(layout="wide")

# Add a title to your app
st.title("Telco Data Dashboard")

# Display some basic information about the data
st.write("### Data Overview")
st.write(telco_data.head(10))

# Check if 'Session Frequency' and 'Total Duration' columns exist in the data
if 'Session Frequency' in telco_data.columns and 'Total Duration' in telco_data.columns:
    # Create a scatter plot using Altair
    st.write("### Scatter Plot")
    scatter_chart = alt.Chart(telco_data).mark_circle().encode(
        x='Total Duration',
        y='Session Frequency',
        color='Satisfaction:N',  # Adjust if 'Satisfaction' is not categorical
        tooltip=['Total Duration', 'Session Frequency']
    ).properties(
        width=600,
        height=400
    )
    st.altair_chart(scatter_chart, use_container_width=True)

# Display summary statistics
st.write("### Summary Statistics")
st.write(telco_data.describe().round(2))

# Display the DataFrame
st.write("### Telco Data")
st.write(telco_data)