import matplotlib.pyplot as plt

f = open("nodeValues.txt", "r")

nodes = []

for line in f.readlines():
    vals = line.split(" ")
    nodes.append(int(vals[1].strip("\n")))

print(f"Max nodes: {max(nodes)} for number {nodes.index(max(nodes))+1}")
print(f"Min nodes: {min(nodes)} for number {nodes.index(min(nodes))+1}")

plt.plot(nodes)
plt.show()
