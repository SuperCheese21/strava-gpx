import argparse
from datetime import datetime, timedelta
from utils import *
import xml.etree.ElementTree as ElementTree


meters_to_miles = 1609.344


filename = 'Ridge_Run.gpx'
namespace = 'http://www.topografix.com/GPX/1/1'
start_time = '2020-03-27T01:00:00'
time_string = '28:15'


ElementTree.register_namespace("", namespace)


def main():
    tree = ElementTree.parse(filename)
    root = tree.getroot()
    trk = root.find('{' + namespace + '}trk')
    trkseg = trk.find('{' + namespace + '}trkseg')

    total_distance = get_total_distance(trkseg)
    print('Total distance: ' + str(total_distance / meters_to_miles) + ' mi')

    time_sec = get_time_sec(time_string)
    num_points = len(trkseg) - 1

    interval_sec = time_sec / num_points
    interval = timedelta(seconds=interval_sec)

    current_time = datetime.fromisoformat(start_time)

    for trkpt in trkseg:
        time_element = ElementTree.SubElement(trkpt, 'time')
        time_element.text = current_time.isoformat() + 'Z'
        current_time = current_time + interval

    new_filename = filename.split('.')[0] + '_timed.gpx'

    tree.write(new_filename, encoding='UTF-8', xml_declaration=True)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Add timing data to GPX file')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                     help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')
    #
    # args = parser.parse_args()
    # print(args.accumulate(args.integers))

    main()
