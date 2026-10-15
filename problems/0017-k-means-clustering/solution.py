def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	def calc_distance(pointX: tuple[float, ...], pointY: tuple[float, ...]):
		return sum((e1-e2) ** 2 for e1, e2 in zip(pointX, pointY))

	def calc_centroid(cluster: list[tuple[float, ...]]):
		cluster_size = len(cluster)
		return tuple(sum(dim) / cluster_size for dim in zip(*cluster))

	final_centroids = initial_centroids
	for _ in range(max_iterations):
		final_centroids = []
		# Adding points into clusters
		clusters = [[] for _ in range(k)]
		for point in points:
			distances = [calc_distance(point, centroid) for centroid in initial_centroids]
			clusterIdx = distances.index(min(distances))
			clusters[clusterIdx].append(point)
		
		for cluster in clusters:
			final_centroids.append(calc_centroid(cluster))

		initial_centroids = final_centroids

	return final_centroids