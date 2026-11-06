import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(page_title="NextGenLearners Dashboard", layout="wide")
st.title("NextGenLearners Program Performance Dashboard")

# Connect to the SQLite database
conn = sqlite3.connect('nextgen.db')
applicants = pd.read_sql("SELECT * FROM applicants;", conn)
interns = pd.read_sql("SELECT * FROM interns;", conn)
scores = pd.read_sql("SELECT * FROM hackathon_scores;", conn)

# Interactive Domain Filter (Required)
domain_list = ['All'] + sorted(applicants['domain'].unique().tolist())
selected_domain = st.selectbox('Filter by Domain', domain_list)

# Filter DataFrames based on dropdown selection
if selected_domain != 'All':
  app_filt = applicants[applicants['domain'] == selected_domain]
  int_filt = interns[interns['domain'] == selected_domain]
  sco_filt = scores[scores['domain'] == selected_domain]
else:
  app_filt = applicants
  int_filt = interns
  sco_filt = scores

# Element 1: Funnel (Total Applicants vs Completed Interns)
st.subheader("1. Funnel Overview")
col1, col2 = st.columns(2)
completed_count = len(int_filt[int_filt['completion_status'] == 'Completed'])
col1.metric("Total Applicants", len(app_filt))
col2.metric("Completed Interns", completed_count)

st.markdown("---")

# Elements 2 & 3: Completion Rate and Average Score Charts
col3, col4 = st.columns(2)

with col3:
  st.subheader("2. Completion Rate per Domain (%)")
  conv_df = pd.read_sql(
      """
    SELECT 
        a.domain,
        ROUND(100.0 * COUNT(DISTINCT i.intern_id) / COUNT(DISTINCT a.applicant_id), 1) AS completion_rate_pct
    FROM applicants a
    LEFT JOIN interns i 
        ON a.applicant_id = i.applicant_id AND i.completion_status = 'Completed'
    GROUP BY a.domain;
    """,
      conn,
  )
  if selected_domain != 'All':
    conv_df = conv_df[conv_df['domain'] == selected_domain]
  st.bar_chart(conv_df.set_index('domain'))

with col4:
  st.subheader("3. Average Hackathon Score per Domain")
  avg_score_df = pd.read_sql(
      """
    SELECT domain, ROUND(AVG(score), 1) AS avg_score
    FROM hackathon_scores
    GROUP BY domain;
    """,
      conn,
  )
  if selected_domain != 'All':
    avg_score_df = avg_score_df[avg_score_df['domain'] == selected_domain]
  st.bar_chart(avg_score_df.set_index('domain'))

st.markdown("---")

# Element 4: Leaderboard of Top 10 Performers
st.subheader("4. Top Performers Leaderboard")
leaderboard = pd.read_sql(
    """
SELECT i.intern_id, a.name, i.domain, h.score
FROM interns i
JOIN applicants a ON i.applicant_id = a.applicant_id
JOIN hackathon_scores h ON i.intern_id = h.intern_id
ORDER BY h.score DESC
LIMIT 10;
""",
    conn,
)
if selected_domain != 'All':
  leaderboard = leaderboard[leaderboard['domain'] == selected_domain]
st.dataframe(leaderboard, use_container_width=True)
