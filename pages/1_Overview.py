import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Art of War - Welcome", layout="wide")

# Inject custom CSS for welcome page
st.markdown("""
<style>
    .welcome-container {
        background: linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.95)), 
                    url('https://www.armyrecognition.com/images/stories/north_america/united_states/military_equipment/uh-60_black_hawk/UH-60_Black_Hawk_United_States_US_American_army_aviation_helicopter_001.jpg') center/cover no-repeat;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .welcome-title {
        color: #1a237e;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }
    .welcome-text {
        color: #333333;
        font-size: 1.2rem;
        line-height: 1.6;
        text-align: center;
        margin-bottom: 2rem;
    }
       /* Container for stat cards: 3-column grid on wide screens, wraps on smaller screens */
    .stats-container {
      display: grid;
      width=100px;
      gap: 1.5rem;           /* consistent gap between cards */
      margin: 2rem 0;        /* optional: space above/below the card row */
    }
    
    /* Individual stat card styling */
    .stat-card {
      width = 100px;
      background: #f0f0f0;   /* card background color (light gray) */
      padding: 1rem;        /* inner spacing for content */
      text-align: center;   /* center-align text (e.g., numbers/labels) */
      border-radius: 0.5rem; /* rounded corners for aesthetics */
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
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    .feature-card {
        background: rgba(255, 255, 255, 0.9);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
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

# Load military strength data
def load_data():
    return pd.read_csv("data/2024_military_strength_by_country.csv")

military_strength = load_data()

# Compute key statistics
total_countries = len(military_strength)
filtered = military_strength[military_strength['country'] != 'Afghanistan']
filtered = filtered.sort_values('pwr_index', ascending=True)
top_power = filtered.iloc[0]['country'] if not filtered.empty else "N/A"
try:
    total_budget = sum(pd.to_numeric(filtered['national_annual_defense_budgets'], errors='coerce'))
    formatted_budget = f"${total_budget/1e12:.2f}T"
except:
    formatted_budget = "Data unavailable"

# Render welcome container
st.markdown('<div class="welcome-container">', unsafe_allow_html=True)
st.markdown('<h1 class="welcome-title">Military Data Analysis Platform</h1>', unsafe_allow_html=True)
st.markdown('''
<p class="welcome-text">
    Explore comprehensive analysis of global military powers, defense budgets, and international trade data 
    through interactive visualizations and detailed comparisons.
</p>
''', unsafe_allow_html=True)

# Statistics section
st.markdown('<h2 style="text-align:center; color:#1a237e; margin:2rem 0;">Global Military Overview</h2>', unsafe_allow_html=True)
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

# Features section
st.markdown('<h2 style="text-align:center; color:#1a237e; margin:2rem 0;">Available Analysis</h2>', unsafe_allow_html=True)
st.markdown('''
<div class="feature-grid">
    <div class="feature-card">
        <div class="feature-title">Military Strength Comparison</div>
        <div class="feature-description">
            Compare military capabilities between countries with detailed breakdowns of personnel, equipment, and power indices.
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-title">Defense Budget Analysis</div>
        <div class="feature-description">
            Track defense expenditure trends over time and analyze budget allocations across different military sectors.
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-title">Defense Companies</div>
        <div class="feature-description">
            Analyze top defense contractors and their performance in the global military-industrial complex.
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-title">Trade Data</div>
        <div class="feature-description">
            Explore military exports and imports worldwide with detailed trade flow visualizations.
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-title">2047 Predictions</n        </div>
        <div class="feature-description">
            View projections of future military power rankings based on current trends and growth trajectories.
        </div>
    </div>
</div>
''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
