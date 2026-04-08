from env import DecisionGymEnv

env = DecisionGymEnv()

domain = input("Choose domain (customer_support / task_scheduling / resource_allocation): ")

state = env.reset(domain)
print("Initial State:", state)

done = False

while not done:
    action = input("Enter action: ")
    state, reward, done, _ = env.step(action)

    print("State:", state)
    print("Reward:", reward)
    print("Done:", done)
    print("-----")