import streamlit as st
from env import DecisionGymEnv

# -------- PAGE CONFIG --------
st.set_page_config(page_title="DecisionGym", layout="wide")

# -------- CUSTOM DARK CSS --------
st.markdown("""
    <style>
        body {
            background-color: #0E1117;
            color: white;
        }
        .main-title {
            font-size: 42px;
            font-weight: bold;
            text-align: center;
            color: #00FFD1;
        }
        .sub-text {
            text-align: center;
            color: #AAAAAA;
            margin-bottom: 30px;
        }
        .card {
            padding: 20px;
            border-radius: 12px;
            background-color: #1A1D24;
            box-shadow: 0 0 10px rgba(0,255,209,0.2);
        }
    </style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown('<div class="main-title">🧠 DecisionGym RL Simulator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Train AI agents in real-world decision environments</div>', unsafe_allow_html=True)

# -------- LAYOUT --------
col1, col2 = st.columns([1, 2])

# -------- LEFT PANEL (Controls) --------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("⚙️ Configuration")

    domain = st.selectbox(
        "🌍 Select Domain",
        ["customer_support", "task_scheduling", "resource_allocation"]
    )

    difficulty = st.selectbox(
        "🎯 Select Difficulty",
        ["easy", "medium", "hard"]
    )

    run = st.button("🚀 Run Simulation")

    st.markdown('</div>', unsafe_allow_html=True)

# -------- RIGHT PANEL (Output) --------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Simulation Output")

    if run:
        env = DecisionGymEnv()
        state = env.reset(domain, difficulty)

        st.success("Simulation Started")

        st.write("### 🟢 Initial State")
        st.json(state)

        done = False
        step_count = 1

        while not done:

            # -------- AGENT LOGIC --------
            if domain == "customer_support":
                action = "apologize" if state["sentiment"] == "angry" else "refund"

            elif domain == "task_scheduling":
                action = "do_task"

            else:
                action = "invest_product" if state["budget"] > 50 else "save"

            state, reward, done, _ = env.step(action)

            st.write(f"### 🔹 Step {step_count}")
            st.write("👉 Action:", action)
            st.write("💰 Reward:", reward)
            st.json(state)
            st.write("---")

            step_count += 1

        st.success("✅ Simulation Finished")

    else:
        st.info("Click 'Run Simulation' to start")

    st.markdown('</div>', unsafe_allow_html=True)