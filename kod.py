# Fonksiyon tanımlama
def euclideanDistance(coordinate1, coordinate2):
    return (((coordinate1[0] - coordinate2[0]) ** 2) + ((coordinate1[1] - coordinate2[1]) ** 2)) ** 0.5


# Tanımlamalar
points = [(2, 3), (5, 7), (7, 2), (8, 4)]
min_distances = float("inf")

# Minimum bulma
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        distances = euclideanDistance(points[i], points[j])
        if distances < min_distances:
            min_distances = distances
# Yazdırma
print("Minimum mesafe:", min_distances)
