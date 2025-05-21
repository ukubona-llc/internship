import pandas as pd
import matplotlib.pyplot as plt

# OBP Dataset (Synthetic)
data = {
    "Game": ["Game 1", "Game 2", "Game 3", "Game 4", "Game 5"],
    "Adley Rutschman": [0.345, 0.400, 0.375, 0.390, 0.410],
    "Gunnar Henderson": [0.320, 0.360, 0.385, 0.405, 0.430]
}

# Melt and plot
df = pd.DataFrame(data)
melted = df.melt(id_vars=["Game"], var_name="Player", value_name="OBP")

for player in melted["Player"].unique():
    plt.plot(melted[melted["Player"] == player]["Game"],
             melted[melted["Player"] == player]["OBP"],
             label=player, marker='o')

plt.title("Orioles OBP Surge: May 2025")
plt.xlabel("Game")
plt.ylabel("On-Base Percentage")
plt.legend()
plt.grid(True)
plt.savefig("assets/interns/jonathan/orioles-analysis.jpeg", dpi=300)
plt.show()