import argparse
import time
import xml.etree.ElementTree as ElementTree


filename = 'Alameda_Run.gpx'
namespace = 'http://www.topografix.com/GPX/1/1'
start_time = '2020-03-27T01:00:00Z'
time_string = '28:15'


def get_time_sec(string):
    time_split = string.split(':')
    seconds = 60 * int(time_split[0]) + int(time_split[1])
    return seconds


def main():
    tree = ElementTree.parse(filename)
    root = tree.getroot()
    trk = root.find('{' + namespace + '}trk')
    trkseg = trk.find('{' + namespace + '}trkseg')
    num_points = len(trkseg)

    time_sec = get_time_sec(time_string)
    print('Time (sec): ' + str(time_sec))

    print('Number of data points: ' + str(num_points))


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
