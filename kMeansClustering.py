
import random
import math
from collections import defaultdict
import copy


class kMeans(object):

    def __init__(self, k: int):
        self.k = k
        self.centroids = [None for _ in range(k)]

    @staticmethod
    def euclidean_distance(p1, p2):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

    def _classify_point(self, point):
        '''
            DESCRIPTION
            --------------------------------
            finds the closest centroid from P

            PARAMETERS
            --------------------------------
            P = Point with x and y coordinates

            RETURNS
            ----------------------------------
            Index of the closest centroid in self.centroids

        '''
        current_min_distance = math.inf

        for index, centroid in enumerate(self.centroids):
            distance = self.euclidean_distance(point, centroid)
            if distance < current_min_distance:
                min_index = index
                current_min_distance = distance
        return min_index

    def _random_assign_points(self, points: list):
        '''
            DESCRIPTION
            -----------------------------------
            randomly assigns each point to a cluster

            PARAMETERS
            ------------------------------------
            points: list of Points

            RETURNS
            ------------------------------------
            a defaultdict where the keys are index from 0 to self.k - 1
            and the values are the points randomly assigned to each index

        '''
        assigned_points = defaultdict(list)

        for p in points:
            random_index = random.randrange(self.k)
            assigned_points[random_index].append(p)
        return assigned_points

    def _calculate_centroids(self, assigned_points):
        '''
            DESCRIPTION
            -----------------------------------
            re-calculates the centroids based on assigned_points
            centroid.x = the mean of the x points of all xs
            centroid.y = the mean of the y points of all ys

            PARAMETERS
            ------------------------------------
            assigned_points: defaultdict where the keys are the indexes from 0 to self.k-1 and the values are the points belonging to this cluster

            RETURNS
            ------------------------------------
            None

        '''
        for index, points in assigned_points.items():
            # return None if no points belong to a cluster
            if points:
                self.centroids[index] = [sum(p) / len(p) for p in zip(*points)]
            else:
                self.centroids[index] = None

    def _assign_points(self, points):
        '''
            DESCRIPTION
            -----------------------------------
            assigns each point in points to the cluster of its closest centroid

            PARAMETERS
            ------------------------------------
            points: list of Points

            RETURNS
            ------------------------------------
            defaultdict where the keys are the indexes from 0 to self.k-1 and the values are the points belonging to this cluster

        '''
        assigned_points = defaultdict(list)

        for p in points:
            centroid_index = self._classify_point(p)
            assigned_points[centroid_index].append(p)
        return assigned_points

    def train(self, points: list):

        '''
            DESCRIPTION
            -------------------------
            Assign the points to the appropriate cluster. Steps taken:
            
                * Start by assigning each point with x and y coordinates to a random cluster
                * Compute the centroids of each cluster
                * Re-assign each point to the closest cluster (based on the distance with the centroids)
                * Repeat steps 2 and 3 until the points are not re-assigned to another cluster
            
            PARAMETERS
            ------------------------
            A list of points, where each element (point) contains x and y coordinates: [4,3] or a tuple (3,1)

            RETURNS
            -----------------------
            defaultdict where the keys are the indexes from 0 to self.k-1 and the values are the points belonging to this cluster. 
            The centroids can be access by looking at the centroids attribute of the class
        '''

        # assign points randomly to a cluster
        assigned_points = self._random_assign_points(points)
        check_assigned_points = defaultdict(list)

        # calculate_centroids
        self._calculate_centroids(assigned_points)

        while True:
            # stop when the points are not assigned to a new cluster
            if assigned_points == check_assigned_points:
                return assigned_points

            check_assigned_points = copy.deepcopy(assigned_points)

            # assign points based on the centroids
            assigned_points = self._assign_points(points)

            # recalculate centroids
            self._calculate_centroids(assigned_points)


if __name__ == '__main__':

    inputs = [[24,22],[12,15],[15,12],[1,1],[2,5],[4,5],[21,23],[14,12],[11,15],[3,2],[19,21],[18,21],[8,12]]

    k = kMeans(3)
    clusters = k.train(inputs)

