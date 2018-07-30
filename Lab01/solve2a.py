import matplotlib.pyplot as plt

def function(x):
    ca0 = 42
    cb0 = 28
    cc0 = 4
    k = 0.016
    return ((cc0 + x) / (pow((ca0 - 2 * x), 2) * (cb0 - x))) - k

print(' x     f(x)')

graph=[]
for i in range(1,21):
    graph.append(function(i))
    print('%2d %10.5f'%(i, function(i)))

plt.ylabel('f(x)')
plt.xlabel('x')
plt.plot(graph)
plt.savefig('solve2/a.png')
plt.show()