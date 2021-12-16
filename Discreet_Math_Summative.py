
import networkx as nx
from networkx.generators.random_graphs import erdos_renyi_graph
import random
import matplotlib.pyplot as plt

# is the number of vertices we want in the graph
n = 10

# is the probability of the edges between the vertices
p = random.random()

# storing the inbuilt function for generating graphs as  variable x
x = erdos_renyi_graph(n, p)

# We create an empty list where we will append nodes with an even degrees
even_nodes = []

# We append our nodes that have odd degrees
odd_nodes = []

for node in x.nodes:
    if p > 0 and x.degree(node) != 0 and x.degree(node) % 2 == 0:
        even_nodes.append(node)

    elif x.degree(node) == 0:
        print(" This graph is not connected")
        nx.draw_random(x, with_labels=True)
        plt.show()
        exit()
    else:
        odd_nodes.append(node)
even_nodes.sort()
if even_nodes == list(x.nodes):
    print("This is a euler circuit")

# We print the information to the user in the case the even_nodes and the list of vertices are not equal
else:
    print("This graph is a connected graph")
    print(f"This is not an Euler circuit graph because {odd_nodes} have odd degrees")
    print("Please to run the program again!")

# The last part is we are to estimate probability of getting an euler circuit in an infinite sample
# We assume that the number of trials n is 10 for a start
print("\nCalculating the probability of getting an euler circuit ..")
no_of_trials = 10
print((no_of_trials - 1) / 2 ** no_of_trials)

# We draw the random graph
nx.draw_random(x, with_labels=True)
plt.show()
