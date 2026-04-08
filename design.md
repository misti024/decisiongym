DecisionGym Design

-----------------------------

Domain 1: Customer Support (Adaptive)

Observation:
- customer query
- sentiment (happy/angry)
- wait time
- order status
- customer patience level (1–10)

Actions:
- apologize
- refund
- escalate
- give discount
- ignore

What happens after action:
- apologize → customer becomes calm
- refund → issue solved but company loses money
- ignore → customer becomes more angry
- escalate → issue transferred to higher support
- customer patience decreases every step

Additional Logic:
- customer anger increases if wrong action
- if patience = 0 → customer leaves (done)

Reward:
- correct response → +1
- partially correct response → +0.5
- wrong response → -1
- refund given unnecessarily → -0.5
- fast resolution (within 2 steps) → +0.5
- customer satisfaction high → +1
- customer becomes very angry → -1

Note:
- reward is calculated at each step (not only at end)

Done:
- problem solved OR 5 steps finished OR patience = 0


-----------------------------

Domain 2: Task Scheduling

Observation:
- list of tasks
- deadlines
- priority (high/medium/low)
- available time (e.g., 8 hours)

Actions:
- do task
- delay task
- skip task
- change priority

What happens:
- time reduces each step
- tasks get completed or delayed
- deadlines approach over time

Reward:
- high priority task completed → +2
- medium priority task → +1
- low priority task → +0.5
- missed deadline → -2
- delayed task → -0.5
- efficient scheduling → +1
- idle/no action → -0.5

Note:
- reward is calculated at each step

Done:
- all tasks completed OR time finished


-----------------------------

Domain 3: Resource Allocation

Observation:
- total budget (e.g., 100)
- options: marketing, hiring, product
- expected returns (varies)

Actions:
- spend on marketing
- spend on hiring
- spend on product
- save money

What happens:
- budget decreases after spending
- returns depend on decision
- bad investment reduces profit

Reward:
- profit generated → +value
- balanced allocation → +1
- overspending budget → -2
- investing in low-return option → -1
- saving money wisely → +0.5
- business growth achieved → +2
- continuous losses → -2

Note:
- reward is calculated at each step

Done:
- budget finished OR 5 steps completed