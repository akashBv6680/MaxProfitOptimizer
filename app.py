import streamlit as st
from itertools import product
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Max Profit Optimizer",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Styling
st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}
.problem-description {
    background-color: #f0f2f6;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1rem 0;
}
.solution-box {
    background-color: #d4edda;
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 4px solid #28a745;
    margin: 1rem 0;
}
.test-case-box {
    background-color: #fff3cd;
    padding: 1rem;
    border-radius: 8px;
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# Streamlit Header
st.markdown('<h1 class="main-header">💰 Max Profit Optimizer</h1>', unsafe_allow_html=True)
st.markdown('---')

# Problem Details
with st.sidebar:
    st.header("📋 Problem Details")
    st.write("Mr. X owns land on Mars and can build three types of properties.")
    
    with st.expander("Property Details", expanded=True):
        property_data = {
            "Property": ["Theatre", "Pub", "Commercial Park"],
            "Build Time": [5, 4, 10],
            "Land Space": ["2x1", "1x1", "3x1"],
            "Earnings/Unit": [1500, 1000, 2000]
        }
        st.dataframe(property_data, use_container_width=True)
    
    st.write("**Goal:** Find the optimal mix of properties to maximize earnings.")

# Main Content
tab1, tab2, tab3 = st.tabs(["🎯 Solver", "📊 Test Cases", "📖 About"])

with tab1:
    st.markdown('<div class="problem-description">', unsafe_allow_html=True)
    st.write("""
    ### Problem Statement
    Mr. X can build **Theatre (T)**, **Pub (P)**, or **Commercial Park (C)**.
    - He cannot build two properties in parallel
    - After n units of time, calculate total earnings
    - Find the optimal property mix for maximum profit
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Input Section
    st.subheader("⏱️ Input Time Units")
    col1, col2 = st.columns([2, 1])
    with col1:
        time_units = st.slider(
            "Select time units (n):",
            min_value=1,
            max_value=100,
            value=7,
            step=1,
            help="Mr. X has this much time to build properties"
        )
    
    # Solve Button
    if st.button("🚀 Solve for Maximum Profit", use_container_width=True, key="solve_btn"):
        st.subheader("✨ Optimal Solution")
        
        # Properties data
        properties = {
            'T': {'time': 5, 'earnings': 1500},  # Theatre
            'P': {'time': 4, 'earnings': 1000},  # Pub
            'C': {'time': 10, 'earnings': 2000}  # Commercial
        }
        
        best_earnings = 0
        best_combinations = []
        
        # Try all possible combinations
        max_t = time_units // 5
        max_p = time_units // 4
        max_c = time_units // 10
        
        for t in range(max_t + 1):
            for p in range(max_p + 1):
                for c in range(max_c + 1):
                    total_time = t * 5 + p * 4 + c * 10
                    if total_time <= time_units:
                        earnings = t * 1500 + p * 1000 + c * 2000
                        if earnings > best_earnings:
                            best_earnings = earnings
                            best_combinations = [(t, p, c)]
                        elif earnings == best_earnings:
                            best_combinations.append((t, p, c))
        
        # Display Results
        st.markdown(f'<div class="solution-box">', unsafe_allow_html=True)
        st.metric("Maximum Earnings", f"${best_earnings:,}")
        st.write(f"**Time Available:** {time_units} units")
        st.write(f"**Number of Solutions:** {len(best_combinations)}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("🎪 All Optimal Solutions")
        solutions_df = pd.DataFrame(
            [(t, p, c, t*1500 + p*1000 + c*2000) for t, p, c in best_combinations],
            columns=["Theatre (T)", "Pub (P)", "Commercial (C)", "Total Earnings"]
        )
        st.dataframe(solutions_df, use_container_width=True)
        
        # Breakdown
        st.subheader("📊 Breakdown")
        col1, col2, col3 = st.columns(3)
        with col1:
            t, p, c = best_combinations[0]
            st.metric("Theatres Built", t, delta=f"{t*5} time units")
        with col2:
            st.metric("Pubs Built", p, delta=f"{p*4} time units")
        with col3:
            st.metric("Commercial Parks Built", c, delta=f"{c*10} time units")

with tab2:
    st.subheader("📝 Test Cases")
    st.write("Verify the solver with the provided test cases:")
    
    test_cases = [
        {"time": 7, "expected_earnings": 3000, "description": "Test Case 1"},
        {"time": 8, "expected_earnings": 4500, "description": "Test Case 2"},
        {"time": 13, "expected_earnings": 16500, "description": "Test Case 3"}
    ]
    
    for test in test_cases:
        st.markdown(f'<div class="test-case-box">', unsafe_allow_html=True)
        st.write(f"**{test['description']}**")
        st.write(f"Input Time: **{test['time']} units**")
        st.write(f"Expected Maximum Earnings: **${test['expected_earnings']:,}**")
        
        # Calculate
        best_earnings_test = 0
        best_combinations_test = []
        max_t = test['time'] // 5
        max_p = test['time'] // 4
        max_c = test['time'] // 10
        
        for t in range(max_t + 1):
            for p in range(max_p + 1):
                for c in range(max_c + 1):
                    total_time = t * 5 + p * 4 + c * 10
                    if total_time <= test['time']:
                        earnings = t * 1500 + p * 1000 + c * 2000
                        if earnings > best_earnings_test:
                            best_earnings_test = earnings
                            best_combinations_test = [(t, p, c)]
                        elif earnings == best_earnings_test:
                            best_combinations_test.append((t, p, c))
        
        is_correct = best_earnings_test == test['expected_earnings']
        status = "✅ PASSED" if is_correct else "❌ FAILED"
        st.write(f"Calculated Earnings: **${best_earnings_test:,}** {status}")
        
        for t, p, c in best_combinations_test:
            st.write(f"Solution: T={t}, P={p}, C={c}")
        
        st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.subheader("📖 About This Application")
    st.write("""
    This is a dynamic optimization solver for the **Max Profit Problem**.
    
    ### Problem Background
    Mr. X owns a large strip of land on Mars with infinite capacity. He can build:
    - **Theatre** (5 time units, earns 1500/unit)
    - **Pub** (4 time units, earns 1000/unit)
    - **Commercial Park** (10 time units, earns 2000/unit)
    
    ### Algorithm
    The solver uses a **brute-force search** to explore all valid combinations:
    1. Calculate maximum count for each property type based on available time
    2. Iterate through all combinations (Theatre, Pub, Commercial Park)
    3. For each combination, verify total time doesn't exceed available time
    4. Calculate total earnings: (T × 1500) + (P × 1000) + (C × 2000)
    5. Track the combination(s) with maximum earnings
    
    ### Complexity
    - Time Complexity: O(n³) where n is the number of time units
    - Space Complexity: O(1) - stores only the best solution
    
    ### Features
    ✅ Dynamic input for any time unit value
    ✅ Multiple solutions display (if multiple combinations give same max profit)
    ✅ Automatic test case verification
    ✅ Detailed breakdown of earnings and time allocation
    """)

st.markdown('---')
st.markdown("""
<div style='text-align: center; color: #888; margin-top: 2rem;'>
    <p>💻 Built with <b>Streamlit</b> | 🚀 Powered by Python</p>
    <p>GitHub: <b>akashBv6680/MaxProfitOptimizer</b></p>
</div>
""", unsafe_allow_html=True)
