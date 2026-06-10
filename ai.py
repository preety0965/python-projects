import random
import time
import tkinter as tk


class TrafficVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Traffic Light System Reflex Agent Visualization")

        self.canvas = tk.Canvas(self.root, width=250, height=450, bg="white")
        self.canvas.pack()

        self.red = self.canvas.create_oval(75, 50, 175, 150, fill="gray")
        self.yellow = self.canvas.create_oval(75, 170, 175, 270, fill="gray")
        self.green = self.canvas.create_oval(75, 290, 175, 390, fill="gray")

        self.info = tk.Label(self.root, text="", font=("Arial", 12))
        self.info.pack()

    def update(self, density, timer, light):

        self.canvas.itemconfig(self.red, fill="gray")
        self.canvas.itemconfig(self.yellow, fill="gray")
        self.canvas.itemconfig(self.green, fill="gray")

        if light == "Red":
            self.canvas.itemconfig(self.red, fill="red")
        elif light == "Yellow":
            self.canvas.itemconfig(self.yellow, fill="yellow")
        elif light == "Green":
            self.canvas.itemconfig(self.green, fill="green")

        self.info.config(
            text=f"Traffic Density: {density}\nTimer: {timer}\nLight: {light}"
        )

        self.root.update()


class TrafficEnvironment:
    def __init__(self):
        self.traffic_density = "low"
        self.timer = 0
        self.light = "Red"

    def get_percept(self):
        return self.traffic_density, self.timer, self.light

    def update_environment(self):
        self.traffic_density = random.choice(["low", "high"])
        self.timer += 1

    def execute_action(self, action):

        if action == "SwitchToGreen":
            self.light = "Green"
            self.timer = 0
            print("Action: Light switched to Green")

        elif action == "SwitchToRed":
            self.light = "Red"
            self.timer = 0
            print("Action: Light switched to Red")

        elif action == "SwitchToYellow":
            self.light = "Yellow"
            self.timer = 0
            print("Action: Light switched to Yellow")

class TrafficLightAgent:
    def decide(self, traffic_density, timer, current_light):

        # Red -> Yellow when traffic is high
        if current_light == "Red" and traffic_density == "high":
            return "SwitchToYellow"

        # Yellow -> Green
        elif current_light == "Yellow" and traffic_density == "high":
            return "SwitchToGreen"

        # Green -> Yellow when traffic becomes low
        elif current_light == "Green" and traffic_density == "low":
            return "SwitchToYellow"

        # Yellow -> Red
        elif current_light == "Yellow" and traffic_density == "low":
            return "SwitchToRed"

        return None


def simulate_traffic_agent(steps=10):

    print("\n------ Simulating Traffic Agent ------")

    env = TrafficEnvironment()
    agent = TrafficLightAgent()
    visual = TrafficVisualizer()

    for step in range(steps):

        print(f"\nStep: {step + 1}")

        env.update_environment()

        percepts = env.get_percept()

        print(f"Percepts: Density={percepts[0]}, "
            f"Timer={percepts[1]}, Light={percepts[2]}"
        )

        action = agent.decide(*percepts)

        if action:
            env.execute_action(action)

        visual.update(env.traffic_density, env.timer, env.light)

        time.sleep(1)

    visual.root.mainloop()


if __name__ == "__main__":
    simulate_traffic_agent(steps=50)