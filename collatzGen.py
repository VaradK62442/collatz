def applyRule(num, nodeList):
    # print(f"\nStarting number: {num}")
    nodes = 0
    while num != 1:
        if num % 2 == 1:
            num = (3*num) + 1
        else:
            num = num / 2
            
        nodes += 1

    # print(f"Nodes: {nodes}\n")
    nodeList.append(nodes)

    return nodeList


nodeList = []

for i in range(1, 500000):
    nodeList = applyRule(i, nodeList)

maxNodes = max(nodeList)
maxNodeNumbers = []

for i in range(len(nodeList)):
    if maxNodes == nodeList[i]:
        maxNodeNumbers.append(i+1)

# print(f"Maximum nodes: {maxNodes} for {maxNodeNumbers}")

with open ("nodevalues.txt", 'w') as f:
    for i, node in enumerate(nodeList):
        f.writelines(f"{i+1}: {node}\n")

print("done")