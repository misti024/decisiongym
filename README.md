# DecisionGym: Multi-Domain RL Environment

## Overview
DecisionGym is a reinforcement learning environment designed to simulate real-world decision-making scenarios across multiple domains.

## Domains
1. Customer Support
2. Task Scheduling
3. Resource Allocation

## Features
- Multi-domain environment
- Step-based simulation
- Reward-based decision system
- Automated grading
- Rule-based AI agent

## Project Structure
- env.py → environment logic
- grader.py → evaluation system
- runner.py → automated testing
- inference.py → agent simulation
- design.md → system design

## How to Run

### Run evaluation
python runner.py

### Run agent
python inference.py

## Example Use Cases
- AI customer support automation
- Task optimization systems
- Business decision simulation

## Future Scope
- Reinforcement learning training (PPO, DQN)
- UI dashboard (Streamlit)
- More complex domains

## Key Idea
This project models decision-making as a reinforcement learning problem, where an agent interacts with an environment, takes actions, and receives rewards based on performance.