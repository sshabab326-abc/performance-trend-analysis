import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Player": ["Messi", "Ronaldo", "Neymar", "Mbappe", "Haaland"],
    "Goals": [25, 22, 18, 24, 30],
    "Assists": [12, 8, 15, 10, 6]
}

df = pd.DataFrame(data)
plt.bar(df["Player"],df["Goals"])
plt.title("Goal by pleyer")
plt.xlabel("players")
plt.ylabel("goals")
plt.show()
plt.plot(df["Player"],df["Assists"])
plt.title("assists by players")
plt.xlabel("PLayers")
plt.ylabel("Assists")
plt.show()
plt.pie(df["Goals"],labels=df["Player"],autopct="1%.1f%%")
plt.title("goals distribution bye players")
plt.show()