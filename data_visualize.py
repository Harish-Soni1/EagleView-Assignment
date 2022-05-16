import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./yolov5/runs/train/exp5/results.csv")

fig, ax = plt.subplots(2, 5, figsize=(12, 6), tight_layout=True)
ax = ax.ravel()

x = df.values[:, 0]
s = [x.strip() for x in df.columns]

for i, j in enumerate([1, 2, 3, 4, 5, 8, 9, 10, 6, 7]):
    y = df.values[:, j].astype('float')
    ax[i].plot(x, y, marker='.', linewidth=2, markersize=8)
    ax[i].set_title(s[j], fontsize=12)


plt.savefig("metrics.png")

