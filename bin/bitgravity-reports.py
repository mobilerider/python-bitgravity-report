# import argparse

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument(
#     'integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
# parser.add_argument(
#     '--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

from datetime import datetime, timedelta

from dateutil.parser import parse as parse_date

from bitgravity import Dashboard


def parse_cmdline():
    import argparse
    parser = argparse.ArgumentParser(description='Simple command-line frontend for the bitgravity.Dashboard class')
    parser.add_argument('report', metavar='REPORT', type=str, nargs=1, choices=['traffic_report', 'subdirectory_report', ], help='Report type')

    parser.add_argument('-u', '--username', dest='username', required=True, metavar='USERNAME', action='store', help='User name to login')
    parser.add_argument('-p', '--password', dest='password', required=False, metavar='PASSWORD', action='store', help='Password to login')

    parser.add_argument('--start-datetime', dest='start_datetime', metavar='DATE', action='store', help='Start date for report data')
    parser.add_argument('--end-datetime', dest='end_datetime', metavar='DATE', action='store', help='End date for report data')

    parser.add_argument('-s', '--host-filter', dest='host_filter', metavar='GLOB', action='store', help='Hostname filter')
    parser.add_argument('-d', '--directory-filter', dest='directory_filter', metavar='GLOB', action='store', help='Directory name filter')
    parser.add_argument('-f', '--filename-filter', dest='filename_filter', metavar='GLOB', action='store', help='File name filter')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_cmdline()

    dashboard = Dashboard(args.username, args.password, eager_login=True)

    args.report = args.report[0]
    args.start_datetime = parse_date(args.start_datetime) if args.start_datetime else datetime.now()
    args.end_datetime = parse_date(args.end_datetime) if args.end_datetime else args.start_datetime + timedelta(days=10)

    if args.report in ('traffic_report', 'subdirectory_report', ):
        method = getattr(dashboard, args.report)
        params = {
            'start': args.start_datetime,
            'end': args.end_datetime,
        }
        if args.host_filter:
            params['host'] = args.host_filter
        if args.directory_filter:
            params['directory_filter'] = args.directory_filter
        if args.filename_filter:
            params['filename_filter'] = args.filename_filter

        print method(**params)
