import requests
import datetime
import csv
import json

# Store the carpark information with the carpark name as the dictionary key
hdb_carpark_info = dict()
with open("hdb-carpark-information.csv") as f:
    array = csv.reader(f, delimiter=',', quotechar='"')
    for line in array:
        hdb_carpark_info[line[0]] = line[1:]

def map_carpark_name_to_latlng(name):
    try:
        info = hdb_carpark_info[name]
    except KeyError:
        return (None, None)

    # Some custom coordinate system
    x_coord = float(info[1])
    y_coord = float(info[2])

    # Perform linear interpolation

    # BLOCK 728 ANG MO KIO AVE 6
    # x = 29283.7324 -> long = 103.8456739
    # y = 39647.8906 -> lat  = 1.3727031
    posA = (29283.7324, 39647.8906, 103.8456739, 1.3727031)

    # BLK 517B JURONG WEST STREET 52
    # x = 15461.2578 -> long = 103.7206833
    # y = 36356.8719 -> lat  = 1.3451942
    posB = (15461.2578, 36356.8719, 103.7206833, 1.3451942)

    lat  = (y_coord - posA[1]) / (posB[1] - posA[1]) * (posB[3] - posA[3]) + posA[3]
    long = (x_coord - posA[0]) / (posB[0] - posA[0]) * (posB[2] - posA[2]) + posA[2]
    return (lat, long)

def get_carpark_data():
    today = datetime.datetime.today()

    # Call the API
    params = {
        "date_time": today.replace(microsecond=0).isoformat() # ISO8601 date format (without microsecond)
    }
    response = requests.get('https://api.data.gov.sg/v1/transport/carpark-availability', params=params)
    data = response.json()
    if response.status_code == 200:
        print("Data received successfully")
    else:
        print(response.status_code)
        print("Error")

    payload = []
    carpark_data = data['items'][0]['carpark_data']
    for entry in carpark_data:
        # get spaces available
        lots = entry['carpark_info'][0] # conveniently ignore non-cars
        total_spaces = int(lots['total_lots']) # by "lots" you mean parking spaces?
        available_spaces = int(lots['lots_available'])

        # stop processing if carpark has no spaces at all
        if total_spaces <= 0:
            continue
        availability = available_spaces / total_spaces

        # Convert carpark name into GPS coordinates
        carpark_name = entry['carpark_number']
        lat, long = map_carpark_name_to_latlng(carpark_name)

        # if we could not map it then conveniently ignore it
        if (not lat) or (not long):
            continue

        # Save to payload
        payload.append((carpark_name, lat, long, available_spaces, total_spaces, availability))
    return payload

# If not imported as a library, run test case
if __name__ == '__main__':
    import parking_map
    payload = get_carpark_data()
    user = (103.92432685169994, 1.3339179186421388)
    rad = 5
    parking_map.generate_map(user, payload, rad)
