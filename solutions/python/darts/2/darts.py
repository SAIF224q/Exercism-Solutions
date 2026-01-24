def score(x, y):
    radius = (x**2 + y**2)**0.5
    
    thresholds = [(1, 10), (5, 5), (10, 1)]
    
    for threshold, points in thresholds:
        if radius <= threshold:
            return points
    return 0
