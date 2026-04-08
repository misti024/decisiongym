def grade_customer_support(state):
    if state.get("resolved"):
        return 1
    return 0


def grade_task_scheduling(state):
    completed = 0
    for task in state.get("tasks", []):
        if task.get("done"):
            completed += 1
    return completed


def grade_resource_allocation(state):
    return state.get("profit", 0)