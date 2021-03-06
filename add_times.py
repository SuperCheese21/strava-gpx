from datetime import datetime, timedelta
from sys import argv
from utils import *
import xml.etree.ElementTree as ElementTree


namespace = 'http://www.topografix.com/GPX/1/1'
ElementTree.register_namespace("", namespace)


def main():
    # Check command line args
    if len(argv) != 4:
        print('Usage: python add_times.py <gpx_path> <start_time> <time>')
        print('Example: python add_times.py route.gpx 2020-03-25T18:00:00 34:30')
        exit(1)

    # Parse command line args
    filename = argv[1]
    start_time = argv[2]
    time_string = argv[3]

    # Parse input GPX file
    tree = ElementTree.parse(filename)
    root = tree.getroot()
    trk = root.find('{' + namespace + '}trk')
    trkseg = trk.find('{' + namespace + '}trkseg')

    # Create route segments list
    trkpt_list = list(zip(list(trkseg), list(trkseg)[1:]))

    # Calculate pace
    total_dist = get_total_dist(trkpt_list)
    time_sec = get_time_sec(time_string)
    pace = total_dist / time_sec

    # Create datetime object from start time
    current_time = datetime.fromisoformat(start_time)

    # Add time for first data point
    add_time(trkseg[0], current_time)

    # Calculate and add times for rest of data points
    for prev_trkpt, curr_trkpt in trkpt_list:
        dist = get_dist(prev_trkpt, curr_trkpt)
        current_time += timedelta(seconds=dist/pace)
        add_time(curr_trkpt, current_time)

    # Write output to new file
    date = start_time.split('T')[0]
    new_filename = filename.split('.')[0] + '_' + date + '.gpx'
    tree.write(new_filename, encoding='UTF-8', xml_declaration=True)


if __name__ == '__main__':
    main()
