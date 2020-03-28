from great_circle_calculator.great_circle_calculator import distance_between_points


def get_coords(trkpt):
    lat = float(trkpt.attrib['lat'])
    lon = float(trkpt.attrib['lon'])
    return lon, lat


def get_dist(trkpt1, trkpt2):
    p1 = get_coords(trkpt1)
    p2 = get_coords(trkpt2)
    return distance_between_points(p1, p2)


def get_time_sec(string):
    time_split = string.split(':')
    seconds = 60 * int(time_split[0]) + int(time_split[1])
    return seconds


def get_total_dist(trkpt_list):
    total_dist = 0
    for prev_trkpt, current_trkpt in trkpt_list:
        dist = get_dist(prev_trkpt, current_trkpt)
        total_dist += dist
    return total_dist
