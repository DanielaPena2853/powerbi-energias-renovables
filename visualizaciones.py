import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("transacciones.csv")

df["fecha"] = pd.to_datetime(df["fecha"])

energia_anual = df.groupby(df["fecha"].dt.year)["energia_mwh"].sum()

plt.figure(figsize=(10, 5))
energia_anual.plot(kind="bar")

plt.title("Energía comercializada por año")
plt.xlabel("Año")
plt.ylabel("Energía (MWh)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
