# CoordinatePairs.py
# A list of coordinate pairs and a helper to compute centroids.

coords = [(0,0), (2,2), (4,0), (2, -2)]

def centroid(points):
    if not points:
        return None
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return (sum(xs)/len(xs), sum(ys)/len(ys))

if __name__ == '__main__':
    print("Coordinates:", coords)
    print("Centroid:", centroid(coords))