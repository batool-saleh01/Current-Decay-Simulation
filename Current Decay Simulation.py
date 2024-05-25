from numpy import zeros, linspace
import matplotlib.pyplot as plt

# Initial conditions
i_0 = 10  # Initial current (in amperes)
J = 2     # Given parameter J
dt = 1     # Time step
tau = 10   # Time constant
time = 120  # Total time duration
Nt = int(round(time / dt))  # Number of time steps
i = zeros(Nt + 1)  # Array to store current values
t = linspace(0, Nt * dt, Nt + 1)  # Time array
i[0] = i_0
i[1] = i[0] - dt * i[0] / tau - J  # Modified initial condition with J

# Iteratively calculate current values
for n in range(1, Nt):
    i[n + 1] = i[n] - dt * i[n] / tau - J

# Plotting results
plt.plot(t, i)
plt.xlabel('Time')
plt.ylabel('i(t)')
plt.title('Current Decay Over Time')
plt.grid(True)
plt.show()
