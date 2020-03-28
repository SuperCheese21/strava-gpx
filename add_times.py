import argparse
import time
import xml.etree.ElementTree as ElementTree


filename = 'Alameda_Run.gpx'
namespace = 'http://www.topografix.com/GPX/1/1'
start_time = '2020-03-27T01:00:00Z'
time_string = '28:15'


ElementTree.register_namespace("", namespace)


def get_time_sec(string):
    time_split = string.split(':')
    seconds = 60 * int(time_split[0]) + int(time_split[1])
    return seconds


def main():
    tree = ElementTree.parse(filename)
    root = tree.getroot()
    trk = root.find('{' + namespace + '}trk')
    trkseg = trk.find('{' + namespace + '}trkseg')

    time_sec = get_time_sec(time_string)
    num_points = len(trkseg)
    print('Time (sec): ' + str(time_sec))
    print('Number of data points: ' + str(num_points))

    for trkpt in trkseg:
        time_element = ElementTree.SubElement(trkpt, 'time')
        time_element.text = start_time

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
