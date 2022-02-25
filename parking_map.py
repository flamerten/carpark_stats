import matplotlib.pyplot as plt
import numpy as np



def generate_map(data):
    #data is an array of tuples (lat, long, availabiliy)

    #imgxy is the xy cordinates of the image, (Bottom Left Lat Long, Top Right Lat Long)
    imgxy = ((1.210097, 103.597973), (1.512845, 104.088749))
    img = plt.imread("map.png")

    plt.subplots()
    plt.imshow(img, extent=[imgxy[0][1], imgxy[1][1],imgxy[0][0], imgxy[1][0]])

    def mapHelper(data, condition, color):
        data = list(filter(condition, list(data)))

        latAll = list(map(lambda x: x[0], data))
        longAll = list(map(lambda x: x[1], data))
        plt.scatter(
            longAll,
            latAll,
            color = color,
            marker = "*",
            alpha = 0.25)
        return

    mapHelper(data, lambda x: x[2] <= 0.25, "red")
    mapHelper(data, lambda x: 0.25 < x[2] <= 0.5, "yellow")
    mapHelper(data, lambda x: x[2] > 0.5, "green")
    plt.show()

if __name__ == '__main__':
    generate_map([(1.4, 104,0.7)])
