import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

x = pd.DataFrame({"day": [1, 2, 3, 4, 5, 6, 7], "grocery": [30, 80, 45, 23, 51, 46, 76], "clothes": [13, 40, 34, 23, 54, 67, 90], "utensils": [12, 32, 27, 33, 61, 13, 23]})
y = pd.DataFrame({"day": [8, 9, 10, 11, 12, 13, 14], "grocery": [30, 90, 45, 23, 51, 48, 76], "clothes": [13, 49, 34, 23, 54, 67, 90], "utensils": [12, 65, 89, 54, 23, 20, 10]})

# Extract the variables you want to visualize
x_grocery = x["grocery"],['day'],["clothes"],['utensils']
y_grocery = y["grocery"],['day'],["clothes"],['utensils']

# Create a joint plot between x_grocery and y_grocery
with sns.axes_style("white"):
    sns.jointplot(x=x_grocery, y=y_grocery, kind="kde", color="b")

plt.show()