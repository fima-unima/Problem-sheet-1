import numpy as np  # Import packages numpy and matplotlib
import matplotlib.pyplot as plt 

T=5 # Time horizon
N=1000 # Discretization number per time unit

# Create normal distributed random numbers by using random.normal
mu, sigma = 0, np.sqrt(1/N) # Mean and standard deviation 
s = np.random.normal(mu, sigma, N*T) # N*T normal distributed random numbers 

# Construct realization of Brownian Motion 
B=np.zeros(N*T+1)  # Vector creation
for i in range(N*T):
    B[i+1]=B[i]+s[i] # Summig the increments of BM on each time step

# Create the other martingales
X=np.zeros(N*T+1)
Y=np.zeros(N*T+1)
Y[0]=1 # Y starts at 1
Lambda = 0.5
for i in range(N*T):
    X[i+1]=B[i+1]**2-i/N # Definition of X
    Y[i+1]=np.exp(Lambda*B[i+1]-(Lambda**2)/2*(i/N)) # Definition of Y


# Show the realisations of the 3 processes in one Plot
x = np.linspace(0, T, N*T+1)  # Correct discretization of the x-axis
plt.plot(x,B, label='Brownian Motion')  # Plot of the Brownian Motion 
plt.plot(x,X, label='squared BM minus t')
plt.plot(x,Y, label='geometric BM')
plt.xlabel('t') # Labeling x-axis
plt.title('One realization of three stochastic processes') # Plot title
plt.legend(loc='best') # Legend at the position where Python finds it the best
plt.show() # Generate the plot