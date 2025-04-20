print("Function :\nf(x)=x^2")  # f(x) = x^2

a = int(input("Enter limits a: "))
b = int(input("Enter limits b: "))
n = int(input("Enter subinterval: "))

h = (b - a) / n

# List to store x and y values
x = [a + i * h for i in range(n + 1)]
y = [xi**2 for xi in x]  # Compute y values for f(x) = x^2

def Trapfun(y, h):
    total = y[0] + y[-1]  # First and last terms
    total += 2 * sum(y[1:-1])  # Sum of intermediate terms

    result = (h / 2) * total
    print("Solution of function is:", result)

# Call the function with computed y values
area_approx = Trapfun(y, h)
print("Approximate solution using Trapezoidal rule:", area_approx)



import numpy as np
import matplotlib.pyplot as plt

#ploting original function (x**2)

x_plot = np.linspace(a, b, 100)  # More points for a smooth curve
y_plot = x_plot**2
plt.plot(x_plot, y_plot, label='f(x) = x^2', color='blue')

# Ploting the trapezoids area
for i in range(n):
    x_coords = [x[i], x[i+1], x[i+1], x[i]]
    y_coords = [0, 0, y[i+1], y[i]]
    plt.fill(x_coords, y_coords, alpha=0.3, color='orange', edgecolor='black', label='Trapezoids' if i == 0 else "")


plt.scatter(x, y, color='red', marker='o', label='Points on f(x)')

plt.title("Trapezoidal Rule Approximation")
plt.xlabel("x")
plt.ylabel("f(x) = x^2")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

