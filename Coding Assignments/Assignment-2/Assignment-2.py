#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Sri Rupin Potula

#Define Union Find Data Structure
class union_find:
    def __init__(self, total_nodes):
        self.parent_node = list(range(total_nodes))
        self.rank_node = [1] * total_nodes
    
    def find_node(self, node):
        if self.parent_node[node] != node:
            self.parent_node[node] = self.find_node(self.parent_node[node])
        return self.parent_node[node]
        
    def union_operation(self, node_1, node_2):
        root_node_1 = self.find_node(node_1)
        root_node_2 = self.find_node(node_2)
        
        if root_node_1 != root_node_2:
            if self.rank_node[root_node_1] > self.rank_node[root_node_2]:
                self.parent_node[root_node_2] = root_node_1
            elif self.rank_node[root_node_1] < self.rank_node[root_node_2]:
                self.parent_node[root_node_1] = root_node_2
            else:
                self.parent_node[root_node_2] = root_node_1
                self.rank_node[root_node_1] += 1


# Function to perform Kruskal's algorithm for single link k-clustering
def greedy_clustering_kruskal(distance_matrix, k):

    n = len(distance_matrix)
    node_tree = []
    
    # Convert distance matrix into an edge list
    for i in range(n):
        for j in range(i + 1, n):
            node_tree.append((distance_matrix[i][j], i, j))
    
    # Sort edges based on their distance (weight)
    node_tree.sort()
    total_clusters = n
    unionFind = union_find(n)
    mst_trees = []

    # Apply Kruskal's algorithm to build MST and stop when we have k clusters
    for weight, u, v in node_tree:
        if unionFind.find_node(u) != unionFind.find_node(v):
            unionFind.union_operation(u, v)
            mst_trees.append((weight, u, v))
            total_clusters -= 1
            if total_clusters == k:
                break
    
    # Form clusters based on the resulting Union-Find structure
    clusters = {}
    for i in range(n):
        root_node = unionFind.find_node(i)
        if root_node not in clusters:
            clusters[root_node] = []
        clusters[root_node].append(i)
    return list(clusters.values())  # Return the clusters


# Use this input 
distance_matrix = [
    [0, 38, 17, 28, 88, 59, 13],
    [38, 0, 52, 49, 83, 91, 59],
    [17, 52, 0, 46, 34, 77, 80],
    [28, 49, 46, 0, 5, 53, 62],
    [88, 83, 34, 5, 0, 43, 33],
    [59, 91, 77, 53, 43, 0, 27],
    [13, 59, 80, 62, 33, 27, 0]
]

# Set k=2 for number of clusters
k = 2  
clusters = greedy_clustering_kruskal(distance_matrix, k)

# Print the resulting clusters
print("Resulting Clusters:", clusters)
