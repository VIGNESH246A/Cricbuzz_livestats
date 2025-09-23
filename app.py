import streamlit as st
import sys
import os

# Page configuration
st.set_page_config(
    page_title="🏏 Cricbuzz LiveStats",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for a beautiful, modern theme ---
st.markdown("""
<style>
    /* App background - soft cream */
    .stApp {
        background-color: #fffaf0;  /* Floral White */
        color: #333333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Main header with a rich maroon-gold gradient */
    .main-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #800000, #B22222); /* DarkRed to FireBrick */
        color: #FFD700; /* Gold text */
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.25);
        margin-bottom: 2rem;
        font-family: 'Georgia', serif;
    }

    /* Feature Cards - white with golden icon & subtle shadow */
    .feature-card {
        background: #fff;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        padding: 1.2rem;
        text-align: center;
        transition: transform 0.2s, box-shadow 0.2s;
        cursor: pointer;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
    }
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        color: #FFD700; /* Gold accent */
    }

    /* Metric Cards - white with gold metric */
    .metric-card {
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        padding: 1rem;
        text-align: center;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #B8860B; /* Dark Goldenrod */
    }
    .metric-label {
        color: #7f8c8d;
        font-size: 0.9rem;
    }

    /* Buttons styling - maroon to red gradient with gold text */
    div.stButton > button {
        background: linear-gradient(135deg, #B22222, #800000); /* FireBrick to DarkRed */
        color: #FFD700; /* Gold text */
        border: none;
        border-radius: 25px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
        transition: background 0.3s, transform 0.2s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #800000, #B22222); /* reverse gradient on hover */
        transform: translateY(-2px);
        color: #FFF8DC; /* lighter gold on hover */
    }

    /* Sidebar styling */
    .css-1d391kg {  /* default sidebar class in Streamlit 1.24+ */
        background-color: #fffaf0;  /* match app background */
    }
</style>
""", unsafe_allow_html=True)

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    st.markdown("""
    <div class="main-header">
        <h1>🏏 Cricbuzz LiveStats</h1>
        <p>Real-Time Cricket Insights & SQL-Based Analytics</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar navigation
    with st.sidebar:
        st.markdown("<h2 style='text-align: center; color:#B22222;'>🏏 Menu</h2>", unsafe_allow_html=True)
        st.markdown("---")
        page = st.selectbox(
            "🧭 Navigate to:",
            ["🏠 Home", "⚡ Live Matches", "📊 Top Stats", "🔍 SQL Analytics", "🛠️ CRUD Operations"]
        )

    try:
        if page == "🏠 Home":
            show_home()
        elif page == "⚡ Live Matches":
            from pages.live_matches import show_live_matches
            show_live_matches()
        elif page == "📊 Top Stats":
            from pages.top_stats import show_top_stats
            show_top_stats()
        elif page == "🔍 SQL Analytics":
            from pages.sql_queries import show_sql_queries
            show_sql_queries()
        elif page == "🛠️ CRUD Operations":
            from pages.crud_operations import show_crud_operations
            show_crud_operations()
    except ImportError as e:
        st.error(f"Page file not found: {e}")
        st.warning("Create a corresponding file in the `pages` directory.")

def show_home():
    # Feature cards section
    st.subheader("✨ Explore the Dashboard's Key Features")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="feature-card"><div class="feature-icon">⚡</div><h4>Live Matches</h4><p>Real-time scores, updates, and commentary.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="feature-card"><div class="feature-icon">📊</div><h4>Top Stats</h4><p>Leaderboards for top batsmen and bowlers.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="feature-card"><div class="feature-icon">🔍</div><h4>SQL Analytics</h4><p>Run custom queries on the database for deep insights.</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="feature-card"><div class="feature-icon">🛠️</div><h4>CRUD Operations</h4><p>Add, update, and manage your own data.</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # System Architecture Section
    st.subheader("🖼️ System Architecture at a Glance")
    with st.expander("🔌 API Integration"):
        st.code("""
import requests
import json

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"
response = requests.get(url, headers=headers)
data = response.json()
        """, language="python")

    with st.expander("🗄️ Database Schema"):
        st.code("""
CREATE TABLE players (
    player_id INT PRIMARY KEY,
    name VARCHAR(100),
    team_id INT,
    playing_role VARCHAR(50)
);

CREATE TABLE matches (
    match_id INT PRIMARY KEY,
    series_id INT,
    venue VARCHAR(200)
);
        """, language="sql")

    st.markdown("---")

    # Project Statistics
    st.subheader("📊 Project Statistics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><div class="metric-value">12</div><div class="metric-label">📁 Total Files</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><div class="metric-value">7</div><div class="metric-label">🐍 Python Libraries</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><div class="metric-value">25</div><div class="metric-label">🔍 SQL Queries</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><div class="metric-value">14</div><div class="metric-label">🗄️ Database Tables</div></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
