import folium
import math
#import io
import os
from PIL import Image

def generate_map(user, data, radius = 5):
    def color(availability):
        if availability > 0.50:
            return "green"
        elif availability > 0.25:
            return "orange"
        else:
            return "red"

    def inRadius(datapoint):
        #1 latitude is about 111km
        _, lat, long, _, _, _ = datapoint
        return math.pow(
            math.pow(lat - user[1], 2) + math.pow(long - user[0], 2),
            0.5) * 111 < radius

    data = list(filter( inRadius, data))

    map = folium.Map(
        location=[user[1], user[0]],
        zoom_start=17
        )

    for carpark_name, lat, long, available_spaces, total_spaces, availability in data:
        folium.Marker(
            location = [lat, long],
            popup = carpark_name,
            icon = folium.Icon(
                color = color(availability),
                icon_color = "white",
                icon = 'car',
                prefix = 'fa'
            )
        ).add_to(map)

    folium.Marker(
        location= [user[1],user[0]],
        popup= "You Are Here!",
        icon = folium.Icon(
                color = "blue",
                icon_color = "white",
                icon = 'car',
                prefix = 'fa'
            )
        ).add_to(map)

    img_data = map._to_png(3)
    #img = Image.open(io.BytesIO(img_data))
    #img.save('image.png')
    #print("Image Saved")
    os.remove("geckodriver.log")
    return img_data

if __name__ == '__main__':
    generate_map(
        (103.81930441307954, 1.2926372991098132),
        [('HE12', 1.2926372991098132, 103.81930441307954, 0, 105, 0.0)],
        5
        )
