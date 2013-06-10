from datetime import datetime, timedelta

from requests import Session


class DashboardError(Exception):
    pass


class DashboardLoginError(DashboardError):
    pass


class Dashboard(object):
    DASHBOARD_BASE_URL = 'https://dashboard.bitgravity.com/index.php'

    @staticmethod
    def login_test(response):
        return '/index.php?cmd=logout' in unicode(response.content)

    def __init__(self, username, password, eager_login=False):
        self.username = username
        self.password = password
        self.session = None

        if eager_login:
            self.login()

    def login(self, username=None, password=None):
        if username and password:
            self.username = username
            self.password = password

        if self.session:
            self.session.get(self.DASHBOARD_BASE_URL, params={'cmd': 'logout', })

        self.session = Session()

        response = self.session.post(self.DASHBOARD_BASE_URL, data={
            'acct': self.username,
            'pass': self.password,
            'action': 'loginForm',
            'cmd': 'login',
        })

        if not self.login_test(response):
            raise DashboardLoginError('Wrong credentials for "{username}"'.format(
                username=self.username,
            ))

    def report(self, report_type='traffic_usage', start=None, end=None, result_type='csv', title=None):
        if not self.session:
            self.login()

        if not report_type in ('traffic_usage', ):
            raise ValueError('Wrong `report_type`: {report_type}'.format(
                report_type=report_type
            ))

        if not result_type in ('csv', ):
            raise ValueError('Wrong `result_type`: {result_type}'.format(
                result_type=result_type
            ))

        if not start:
            start = datetime.now()

        if not end:
            end = start + timedelta(days=10)

        if not title:
            title = {
                'traffic_usage': 'Traffic usage from {start} to {end}',
            }[report_type].format(
                start=start.strftime('%m/%d/%Y %H:%M'),
                end=end.strftime('%m/%d/%Y %H:%M'),
            )

        params = {
            'cmd': 'reports',

            'action': report_type,
            'handler': result_type,

            'startMonth': start.strftime('%m'),
            'startDay': start.strftime('%d'),
            'startYear': start.strftime('%Y'),
            'startTime': start.strftime('%H:%M'),

            'endMonth': end.strftime('%m'),
            'endDay': end.strftime('%d'),
            'endYear': end.strftime('%Y'),
            'endTime': end.strftime('%H:%M'),

            'reportTitle': title,
        }

        response = self.session.post(self.DASHBOARD_BASE_URL, data=params)

        return response.content
