import os
from openai import OpenAI
from env import DecisionGymEnv

# ---------------- ENV VARIABLES ----------------
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
HF_TOKEN = os.getenv("HF_TOKEN", "")

# Create OpenAI client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=os.getenv("OPENAI_API_KEY", "dummy")  # safe fallback
)

# ---------------- LLM FUNCTION ----------------
def get_action_from_llm(state):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are an AI decision-making agent."},
                {"role": "user", "content": f"State: {state}. Give best action."}
            ]
        )

        action = response.choices[0].message.content.strip().lower()
        return action

    except Exception:
        # fallback logic (IMPORTANT)
        if state["domain"] == "customer_support":
            return "refund"
        elif state["domain"] == "task_scheduling":
            return "do_task"
        elif state["domain"] == "resource_allocation":
            return "invest_product"
        return "wait"

# ---------------- RUN EPISODE ----------------
def run_episode(domain, difficulty="medium"):
    env = DecisionGymEnv()

    print("START")
    print(f"DOMAIN: {domain}, DIFFICULTY: {difficulty}")

    state = env.reset(domain, difficulty)
    print("INITIAL_STATE:", state)

    done = False
    step = 1

    while not done:
        print(f"STEP {step}")

        action = get_action_from_llm(state)
        print("ACTION:", action)

        state, reward, done, _ = env.step(action)

        print("REWARD:", reward)
        print("STATE:", state)

        step += 1

    print("END")
    return state


# ---------------- ENTRY ----------------
if __name__ == "__main__":
    run_episode("customer_support")
    run_episode("task_scheduling")
    run_episode("resource_allocation")