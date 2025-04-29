import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Art of War - Military Data Analysis", layout="wide")

# --- Data Loading ---
@st.cache_data
def load_data():
    military_strength = pd.read_csv("data/2024_military_strength_by_country.csv")
    defense_budget = pd.read_csv("data/Cleaned_Defence_Budget.csv")
    return military_strength, defense_budget

military_strength, defense_budget = load_data()

# --- Inject Welcome‐Page CSS ---
st.markdown("""
<style>
  .welcome-container {
    background: linear-gradient(rgba(255,255,255,0.95), rgba(255,255,255,0.95)),
                url('https://www.armyrecognition.com/images/stories/north_america/united_states/military_equipment/uh-60_black_hawk/UH-60_Black_Hawk_United_States_US_American_army_aviation_helicopter_001.jpg')
                no-repeat center center fixed;
    background-size: cover;
    padding: 2rem;
    border-radius: 15px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  }
  .welcome-title {
    color: #1a237e;
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 1.5rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
  }
  .welcome-text {
    color: #333333;
    font-size: 1.2rem;
    line-height: 1.6;
    text-align: center;
    margin-bottom: 2rem;
  }
  .stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
  }
  .stat-card {
    background: rgba(255,255,255,0.9);
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    text-align: center;
    transition: transform 0.3s ease;
  }
  .stat-card:hover {
    transform: translateY(-5px);
  }
  .stat-value {
    font-size: 2rem;
    font-weight: 700;
    color: #1a237e;
    margin-bottom: 0.5rem;
  }
  .stat-label {
    color: #555555;
    font-size: 1rem;
    font-weight: 500;
  }
  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
  }
  .feature-card {
    background: rgba(255,255,255,0.9);
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    border-left: 4px solid #1a237e;
  }
  .feature-card:hover {
    transform: translateY(-5px);
  }
  .feature-title {
    color: #1a237e;
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
  }
  .feature-description {
    color: #555555;
    font-size: 1rem;
    line-height: 1.5;
  }
</style>
""", unsafe_allow_html=True)

# --- Welcome Container ---
st.markdown('<div class="welcome-container">', unsafe_allow_html=True)
st.markdown('<h1 class="welcome-title">Military Data Analysis Platform</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="welcome-text">'
    'Explore comprehensive analysis of global military powers, defense budgets, '
    'and international trade data through interactive visualizations and comparisons.'
    '</p>',
    unsafe_allow_html=True
)

# --- Compute Key Statistics ---
total_countries = len(military_strength)
filtered = military_strength[military_strength['country'] != 'Afghanistan']
filtered = filtered.sort_values('pwr_index', ascending=True)
top_power = filtered.iloc[0]['country'] if not filtered.empty else "N/A"

# Sum all year columns in defense_budget
year_cols = [c for c in defense_budget.columns if c.isdigit()]
total_budget = defense_budget[year_cols].sum().sum()
formatted_budget = f"${total_budget/1e12:.2f}T"

# --- Display Statistics ---
st.markdown('<div class="stats-container">', unsafe_allow_html=True)
st.markdown(f'''
  <div class="stat-card">
    <div class="stat-value">{total_countries}</div>
    <div class="stat-label">Countries Analyzed</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{top_power}</div>
    <div class="stat-label">Top Military Power</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{formatted_budget}</div>
    <div class="stat-label">Global Defense Spending</div>
  </div>
''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Features Overview ---
st.markdown('<h2 style="text-align:center; color:#1a237e; margin:2rem 0;">Available Analysis Modules</h2>', unsafe_allow_html=True)
st.markdown('''
<div class="feature-grid">
  <div class="feature-card">
    <div class="feature-title">Military Strength Comparison</div>
    <div class="feature-description">
      Compare capabilities across countries: personnel, equipment, power indices.
    </div>
  </div>
  <div class="feature-card">
    <div class="feature-title">Defense Budget Analysis</div>
    <div class="feature-description">
      Track spending trends and budget allocations over time.
    </div>
  </div>
  <div class="feature-card">
    <div class="feature-title">Defense Companies</div>
    <div class="feature-description">
      Analyze top contractors and their global market share.
    </div>
  </div>
  <div class="feature-card">
    <div class="feature-title">Trade Data</div>
    <div class="feature-description">
      Explore military export-import flows and trade balances.
    </div>
  </div>
  <div class="feature-card">
    <div class="feature-title">2047 Predictions</div>
    <div class="feature-description">
      View projected top military powers based on current trends.
    </div>
  </div>
</div>
''', unsafe_allow_html=True)

# --- Get Started Button ---
if st.button("Begin Analysis"):
    st.write("Navigate to your module of choice via the sidebar.")
