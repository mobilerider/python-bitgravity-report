python-bitgravity-report
========================

A library to pull reports from Bitgravity CDN dashboard

    >>> from bitgravity import Dashboard
    >>> dashboard = Dashboard(your_username, your_password)
    >>> dashboard.traffic_report()  # Return CSV data
    >>> dashboard.subdirectory_report()  # Return CSV data


bitgravity.Dashboard
====================
- `__init__()` (constructor):
 - `username`: Account user name.
 - `password`: Account password.
 - `eager_login`: If `True`, inmediately perform a login using the specified credentials. Default is `False`.

- `login()`: Perform the login into the Bitgravity dashboard.
 - `username`: (optional) Use an alternative username when login.
 - `password`: (optional) Use an alternative password when login.

- `traffic_report()`: Return CSV report data for traffic usage, optionally filtered by domain.
 - `start`: range from (`datetime`). If not specified, `datetime.now()` is used.
 - `end`: range to (`datetime`). If not specified, the `start` value plus 10 days is used.
 - `host` (optional): Filter traffic data by host.
 - `result_type (optional): Output type. Current only `'csv'` is supported. Default is `'csv'.`
 - `title` (optional): Report title. Currently has no effect since is not included into the output.
 - `filename_filter` (optional): GLOB pattern to filter traffic by file name.

- `subdirectory_report()`: Return CSV report data for subdirectory usage, optionally filtered by domain.
 - `start`: range from (`datetime`). If not specified, `datetime.now()` is used.
 - `end`: range to (`datetime`). If not specified, the `start` value plus 10 days is used.
 - `host` (optional): Filter traffic data by host.
 - `result_type (optional): Output type. Current only `'csv'` is supported. Default is `'csv'.`
 - `title` (optional): Report title. Currently has no effect since is not included into the output.
 - `directory_filter` (optional): GLOB pattern to filter usage by directory.
