from great_circle_calculator.great_circle_calculator import distance_between_points


def get_coords(trkpt):
    lat = float(trkpt.attrib['lat'])
    lon = float(trkpt.attrib['lon'])
    return lon, lat


def get_time_sec(string):
    time_split = string.split(':')
    seconds = 60 * int(time_split[0]) + int(time_split[1])
    return seconds


def get_total_distance(trkseg):
    total_distance = 0
    trkpt_list = zip(list(trkseg), list(trkseg)[1:])
    for prev_trkpt, current_trkpt in trkpt_list:
        p1 = get_coords(prev_trkpt)
        p2 = get_coords(current_trkpt)
        d = distance_between_points(p1, p2)
        total_distance += d
    return total_distance
