# Heaviside step function

def heaviside(x):
    """Heaviside step function"""

    theta = None
    if x < 0:
        theta = 0.
    elif x == 0:
        theta = 0.5
    else:
        theta = 1.

    return theta


# generate list
xvalues = []
for i in range(-8,9,1):
    xvalues.append(i/2)

#print(xvalues)


thetas = []
# Print list
print("x and thetas")
for i in range(0,len(xvalues),1):
    thetas.append(heaviside(xvalues[i]))
#print(thetas)
    print(xvalues[i], thetas[i])

import matplotlib.pyplot as plt
plt.plot(xvalues, thetas, '-o', color="red", linewidth=2)
plt.show()
