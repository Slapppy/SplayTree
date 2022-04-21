import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv('Results/delete_worst.csv')
df.columns = ['method' , 'elem' , 'time']
plt.plot(df['time'] , df['elem'], 'o-r', alpha=0.7, label="delete_worst", lw=5, mec='b', mew=2, ms=10)

plt.legend()
plt.grid(True)
plt.show()