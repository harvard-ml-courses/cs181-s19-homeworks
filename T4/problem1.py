# CS 181, Spring 2017
# Homework 4: Clustering

import numpy as np 
from copy import copy

# The code below gives a bare bones approach for getting the dendogram
# for part 3 of problem 1. You will need to write the dist functions that
# have been left blank and specify the remaining norms (either finding)
# an equivalent numpy function or writing your own function). The program
# will then output how the points merge at each step and the distance at which
# they merge.

def dist_min(cluster_1,cluster_2,norm):
	# Calculate the minimum distance between the two clusters. 
	min_dist = np.inf
	for p1 in cluster_1:
		for p2 in cluster_2:
			n_dist = norm(p1-p2)
			if n_dist < min_dist:
				min_dist = n_dist
	return min_dist


def dist_max(cluster_1,cluster_2,norm):
	# Calculate the maximum distance between the two clusters.
	return 0

def dist_centroid(cluster_1,cluster_2,norm):
	# Calculate the centroid distance between the two clusters.
	return 0

def dist_avg(cluster_1, cluster_2,norm):
	# Calculate the geometric average distance between the two clusters.
	return 0

# Example code below does the L2 norm for min distance.

# List of norms (this currently only has l2 norm)
norms_list = [np.linalg.norm]
norm_names = ["l2 norm"]

# List of distances (this currently only has dist_min)
dist_list = [dist_min]
dist_names = ["min dist"]

#########################################################################
# You should not have to change anything below this line. However, feel free
# to do whatever you find most convenient.

for norm_i in range(len(norms_list)):
	for dist_i in range(len(dist_list)):
		print("Using distance function " + str(dist_names[dist_i]) + 
			"and using norm " + str(norm_names[norm_i]))

		#Initialize clusters, points, and step
		# Define our points and initial clusters
		points = np.array([[[0.1,0.5]],[[0.35,0.75]],[[0.28,1.35]],[[0,1.01]]])
		cluster_1 = np.concatenate((points[0],points[1]))
		cluster_2 = points[2]; cluster_3 = points[3]
		clusters = [cluster_1,cluster_2,cluster_3]
		step = 1

		# Continue until there is only one cluster left in our list of clusters
		while len(clusters)>1:
			print("----------------------------------")
			print("Clusters at step " + str(step))
			for clust in clusters:
				print(list(clust))
			step += 1
			min_dist = np.inf
			merge_i = -1
			merge_j = -1
			# Iterate through all the possible cluster pairs and test distance
			for i in range(len(clusters)):
				for j in range(len(clusters)):
					# If statement ensure i=j will not be tested
					if i<j:
						n_dist = dist_list[dist_i](
							clusters[i],clusters[j],norms_list[norm_i])
						if n_dist < min_dist:
							# Record minimum distance and indices
							min_dist = n_dist
							merge_i = i
							merge_j = j
			# Merge together clusters with the minimum distance
			clusters[merge_i] = np.concatenate((clusters[merge_i],
				clusters[merge_j]),axis=0)
			del clusters[merge_j]
			print("Most recent merge distance " + str(min_dist))

		print("----------------------------------")
		print("Clusters at step" + str(step))
		for clust in clusters:
			print(list(clust))



