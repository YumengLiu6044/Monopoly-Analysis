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

# Sort the spaces and frequencies in descending order
pairs = list(zip(spaces, frequency))
pairs.sort(key=lambda x: x[1], reverse=True)

# split back 
spaces = [pair[0] for pair in pairs]
frequency = [pair[1] for pair in pairs]

# Map Monopoly spaces to Monopoly-style colors
space_colors = {
    "MEDITERRANEAN AVENUE": "purple",
    "BALTIC AVENUE": "purple",

    "ORIENTAL AVENUE": "lightblue",
    "VERMONT AVENUE": "lightblue",
    "CONNECTICUT AVENUE": "lightblue",

    "ST CHARLES PLACE": "pink",
    "STATES AVENUE": "pink",
    "VIRGINIA AVENUE": "pink",

    "ST JAMES PLACE": "orange",
    "TENNESSEE AVENUE": "orange",
    "NEW YORK AVENUE": "orange",

    "KENTUCKY AVENUE": "red",
    "INDIANA AVENUE": "red",
    "ILLINOIS AVENUE": "red",

    "ATLANTIC AVENUE": "yellow",
    "VENTNOR AVENUE": "yellow",
    "MARVIN GARDENS": "yellow",

    "PACIFIC AVENUE": "green",
    "NORTH CAROLINA AVENUE": "green",
    "PENNSYLVANIA AVENUE": "green",

    "PARK PLACE": "darkblue",
    "BOARDWALK": "darkblue",

    "READING RAILROAD": "black",
    "PENNSYLVANIA RAILROAD": "black",
    "B AND O RAILROAD": "black",
    "SHORT LINE RAILROAD": "black",

    "ELECTRIC COMPANY": "gray",
    "WATER WORKS": "gray"
}

# Build a color list in the same sorted order as the bars
colors = [space_colors.get(space, "lightgray") for space in spaces]

# Visualize the results using a bar chart
plt.figure(figsize=(16,10))
plt.bar(spaces, frequency, edgecolor="black", color=colors)
plt.xticks(rotation=90, fontsize=8)
plt.xlabel("Board Space")
plt.ylabel("Landing Probability")
plt.title("Monopoly Landing Probabilities")
plt.tight_layout()
plt.show()
