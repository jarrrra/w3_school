#here will only be parts of matplotlib i didn't know yet

import matplotlib.pyplot as plt
import numpy as np

#scattering

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()

#bars

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1, color = "#4CAF50") #for horizontal bars use barh and height instead
plt.show()

#histogram

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

#pie charts

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels,  colors = mycolors, startangle = 90, explode = myexplode, shadow = True)
plt.legend(title = "Four Fruits:")
plt.show() 
