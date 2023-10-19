# Simulated-Annealing
Used simulated annealing to find the highest point in Minnesota. The data is present in the file mn-srtm-data. It covers the entire state of Minnesota (except for the Northwest Angle, which lies above the 49th parallel)

Used a geometric decrement for the cooling schedule. I sampled from a two-dimensional Gaussian distribution around the current point for the neighboring function. The algorithm also checks whether a point was within the feasible region or not. For each temperature, the code performs 10,000 iterations. 

The coordinates of the best point found by the algorithm were (47.897550156580145, -90.56035967110459) with an elevation of 700 meters.

The python-srtm module is needed for interacting with this data. Set the SRTM1_DIR environment variable to point to the SRTM data directory so python-srtm knows where to find it.
