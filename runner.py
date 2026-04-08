from env import DecisionGymEnv
from grader import (
    grade_customer_support,
    grade_task_scheduling,
    grade_resource_allocation
)

def run_episode(domain, actions):
    env = DecisionGymEnv()
    state = env.reset(domain)

    done = False

    for action in actions:
        state, reward, done, _ = env.step(action)
        if done:
            break

    # grading
    if domain == "customer_support":
        score = grade_customer_support(state)

    elif domain == "task_scheduling":
        score = grade_task_scheduling(state)

    elif domain == "resource_allocation":
        score = grade_resource_allocation(state)

    else:
        score = 0

    return state, score


# 🔥 THIS PART IS MISSING IN YOUR CODE
if __name__ == "__main__":

    # Domain 1
    state, score = run_episode(
        "customer_support",
        ["apologize", "refund"]
    )
    print("Customer Support Score:", score)

    # Domain 2
    state, score = run_episode(
        "task_scheduling",
        ["do_task", "do_task"]
    )
    print("Task Scheduling Score:", score)

    # Domain 3
    state, score = run_episode(
        "resource_allocation",
        ["invest_product", "save"]
    )
    print("Resource Allocation Score:", score)