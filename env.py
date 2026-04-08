class DecisionGymEnv:
    def __init__(self):
        self.state = None
        self.steps = 0
        self.difficulty = "easy"

    def reset(self, domain="customer_support", difficulty="easy"):
        import random

        self.steps = 0
        self.difficulty = difficulty

        # -------- CUSTOMER SUPPORT --------
        if domain == "customer_support":
            patience = 5 if difficulty == "easy" else 3 if difficulty == "medium" else 2

            self.state = {
                "domain": "customer_support",
                "sentiment": random.choice(["angry", "neutral"]),
                "patience": patience,
                "resolved": False
            }

        # -------- TASK SCHEDULING --------
        elif domain == "task_scheduling":
            time_left = 5 if difficulty == "easy" else 3 if difficulty == "medium" else 2

            self.state = {
                "domain": "task_scheduling",
                "tasks": [
                    {"name": "A", "priority": "high", "done": False},
                    {"name": "B", "priority": "low", "done": False}
                ],
                "time_left": time_left
            }

        # -------- RESOURCE ALLOCATION --------
        elif domain == "resource_allocation":
            budget = 100 if difficulty == "easy" else 70 if difficulty == "medium" else 50

            self.state = {
                "domain": "resource_allocation",
                "budget": budget,
                "profit": 0
            }

        return self.state

    def step(self, action):
        reward = 0
        done = False
        domain = self.state["domain"]

        # -------- VALID ACTIONS --------
        valid_actions = {
            "customer_support": ["apologize", "refund", "ignore", "escalate", "give_discount"],
            "task_scheduling": ["do_task", "skip"],
            "resource_allocation": ["invest_marketing", "invest_product", "save"]
        }

        # -------- INVALID ACTION --------
        if action not in valid_actions.get(domain, []):
            reward -= 1
            self.steps += 1
            return self.state, reward, False, {"error": "invalid_action"}

        # -------- CUSTOMER SUPPORT --------
        if domain == "customer_support":

            if action == "apologize":
                reward += 1
                self.state["sentiment"] = "calm"

            elif action == "refund":
                reward += 0.5
                self.state["resolved"] = True

            elif action == "ignore":
                reward -= 1
                self.state["patience"] -= 1

            elif action == "escalate":
                reward += 0.3

            elif action == "give_discount":
                reward += 0.2

            # patience always decreases
            self.state["patience"] -= 1

            if self.state["resolved"] or self.state["patience"] <= 0 or self.steps >= 5:
                done = True

        # -------- TASK SCHEDULING --------
        elif domain == "task_scheduling":

            if action == "do_task":
                for task in self.state["tasks"]:
                    if not task["done"]:
                        task["done"] = True
                        reward += 2 if task["priority"] == "high" else 1
                        break

            elif action == "skip":
                reward -= 1

            self.state["time_left"] -= 1

            if self.state["time_left"] <= 0:
                done = True

        # -------- RESOURCE ALLOCATION --------
        elif domain == "resource_allocation":

            if action == "invest_marketing":
                self.state["budget"] -= 20
                self.state["profit"] += 30
                reward += 1

            elif action == "invest_product":
                self.state["budget"] -= 30
                self.state["profit"] += 50
                reward += 2

            elif action == "save":
                reward += 0.5

            if self.state["budget"] <= 0 or self.steps >= 5:
                done = True

        self.steps += 1

        return self.state, reward, done, {}