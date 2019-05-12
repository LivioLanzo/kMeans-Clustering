# What is k-means clustering?
k-means clustering aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean. Imagine you have the below observations and you wanted to partition the observations and assign them to their appropriate cluster. How would you go about it? This is what we will try to put in place



The algorithm will work in the following way:

    1) Start by assigning each point with x and y coordinates to a random cluster
    2) Compute the centroids of each cluster
    3) Re-assign each point to the closest cluster (based on the distance with the centroids)
    4) Repeat steps 2 and 3 until the points are not re-assigned to another cluster

# Methods

1) __init__ method:
The argument passed to our __init__ method is k, which is the number of clusters we want to identify. 

2) euclidean_distance:
In order to determine the distance between two points, we will use the euclidean formula

3) _random_assign_points:
This method performs the first step of the algorithm which is to assign each point p with x and y coordinates to a random cluster

4) _calculate_centroids:
This method will perform step 2 which is to calculate the centroid of each cluster.

5) _assign_points:
This method will perform step 3 which is to re-assign each point to the closest cluster based on the distance with its centroid

6) train:
This last method will make use of all the former methods and will train our data and assign each point to the appropriate cluster:

