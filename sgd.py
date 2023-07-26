import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# synthetic data this function is unknown we need to estimate its parameters
def func(x):
    return 0.5+0.8*x

x = np.linspace(0,1, 100)
y = func(x)+np.random.randint(-20, 20, len(x))/ 100. # data for estimation


plt.scatter(x, y)
plt.ylim(0, max(y))
plt.savefig("data.png")


# function to fit
# parameters 

a = 0.01 # fixed parameter for simplicity
b = 0

# calculating residuals
residuals = y - (a*x+b)

sosr = np.sum(np.square(residuals))

#calculating loss
sosrs = []
parameter_pairs = []
lr = 0.001
while True:
    # lr*=0.2
    residuals = np.square(y - (a*x+b))
    
    da = np.sum(-2*x*(y-(a*x+b)))
    db = np.sum(-2*(y-(a*x+b)))
    
    step_size_a = da * lr
    step_size_b = db * lr
    
    a -= step_size_a
    b -= step_size_b
   
    parameter_pairs.append((a,b))
    print(a, b, step_size_a, step_size_b)
    if step_size_b > -0.000000009 and step_size_a > -0.00000009:
        break
    

for a, b in parameter_pairs:
    plt.plot(x, a*x+b)

plt.savefig("fitting.png")
    
# create a figure with a 2x2 grid of subplots
fig = plt.figure(figsize=(10, 8))

gs = fig.add_gridspec(2, 2)

ax_main = fig.add_subplot(gs[:, 0])
ax_a = fig.add_subplot(gs[0, 1])
ax_b = fig.add_subplot(gs[1, 1])

line, = ax_main.plot([], [], lw=2)

a_line, = ax_a.plot([], [], color='blue')
b_line, = ax_b.plot([], [], color='green')


list_of_a_values = [i[0] for i in parameter_pairs]
list_of_b_values = [i[1] for i in parameter_pairs]

def init():
    ax_main.set_xlim(0, np.max(x))  # adjust as needed
    ax_main.set_ylim(0, np.max(y))  # adjust as needed
    ax_main.scatter(x, y, color='red')  # plot the original data

    ax_a.set_xlim(0, len(parameter_pairs))
    ax_a.set_ylim(min(list_of_a_values), max(list_of_a_values))
    ax_a.set_title('Parameter a')

    ax_b.set_xlim(0, len(parameter_pairs))
    ax_b.set_ylim(min(list_of_b_values), max(list_of_b_values))
    ax_b.set_title('Parameter b')

    return line, a_line, b_line
    
def update(i):
    a, b = parameter_pairs[i]
    l = a*x + b
    line.set_data(x, l)

    a_line.set_data(range(i+1), list_of_a_values[:i+1])
    b_line.set_data(range(i+1), list_of_b_values[:i+1])

    return line, a_line, b_line

ani = FuncAnimation(fig, update, frames=range(len(parameter_pairs)), init_func=init, blit=True)
ani.save('animation.mp4', writer='ffmpeg', fps=60)

plt.savefig("result.png")
plt.show()