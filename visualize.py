from main import Monopoly
import matplotlib.pyplot as plt

simulations = 100
turns = 10000
total_turns = simulations * turns

for simulation in range(simulations):
    monopoly = Monopoly()
    monopoly.run(turns)

# Calculate the frequency of landing on each space
spaces = [space.space.name.replace("_", " ") for space in Monopoly.BOARD]
frequency = [space.counter / total_turns for space in Monopoly.BOARD]

# Visualize the results using a bar chart
plt.figure(figsize=(16,7))
plt.bar(spaces, frequency, edgecolor="black")
plt.xticks(rotation=90)
plt.xlabel("Board Space")
plt.ylabel("Landing Probability")
plt.title("Monopoly Landing Probabilities")
plt.show()
