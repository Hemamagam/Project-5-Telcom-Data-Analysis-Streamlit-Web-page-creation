**User Analytics in Telcommunication Industry - (Telcom Data Analysis)**
Project summary
Business Needs

**Task 1 -User Overview Analysis** 
- Data Extraction
- EDA- Exploratory Data Analysis
- Identifying Top 10 handsets used by the customer
- Identify Top 3 Handset Manufacturer
- Identify Top 3 Handset per top 3 Manufacturer
- Overview of users behaviour on applications - xDr Session Duration, Total DL, Total UL etc.

**Task 2 -User Engagement Analysis** 
  - Track the user's engagement using session frequency, Duration of the session, the session total trafic (DL and UL)
  - Top 10 customers per engagement metric
  - Normalizing each engagement metric
  - K-mean cluster (k=3)
  - Min, Max, Average, Total non-normalized metrics for each cluster
  - Top 10 most engaged users per applications
  - Top 3 most used applications
  - k-engagement clusters based on the engagement metrics
    
**Task 3- Experience Analytics**
   - Agregated per customer based on Average TCP Retransmission, Average RTT, Handset type and Average throughput
   - TOp 10 , bottom 10 and most frequent
       - TCP values in dataset
       - RTT values in dataset
       - Throughput values in dataset
    - Distribution of average throughput per handset type
    - Averaged TP retransmission view per handset type
    - Using experience metric performed K-mean clustering (k=3)

**Task 4- Satisfaction Analytics**
  - Engagement score for each user using Euclidean Distance
  - Experience score for each user using Euclidean Distance
  - based on average Engagement and Experience score found the satisfaction score
  - Top 10 Satisfied customers
  - Regression Model- Random Forest Regressor for predict the satisfaction score of a customer
  - Feature importance
  - Prediction for the Satisfaction score
  - K-mean on Engagement and Experience Score
  - Clustering on Engagement and Experience Score
  - Aggregate the average Satisfaction and Experience Score for the cluster
  - Final Conclusion and Recommendation
    
**Web Page Creation**
  - Using Streamlit created web page Dashboard
    
**Power point presenation-Telcom Data analysis report**
  - Objective and Business Needs
  -Top Handsets used by Customers
  -Top Handsets Manufacturers
  -User Engagement Analysis
  -K-Mean Clustering for User Engagement
  -Experience Analysis
  -Less Engaged and Worst Experience Clusters
  -Satisfaction Analysis
  -Top Satisfied Customers
  -Model Building
  -Growth Opportunities and Enhancing User Experience 
