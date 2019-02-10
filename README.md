----
# Chrome/Webkit/Unix timestamp to date conversion and vice versa
----
# Usage example:

### Import the two conversion functions from the conversion module (`convert_dt_ts.py`):

```python
from convert_dt_ts import (chrometime_to_date,
                           date_to_chrometime
                          )
```

### Get the Chrome/Webkit timestamp for a timezone-aware date:
```python
dtz = datetime.datetime(2019, 1, 1, 12, 45, 30, 15*10000, tzinfo=timezone.utc)
print('Timezone-aware date to use (created): {}'.format(dtz))

dtz_ts = date_to_chrometime(dtz)
print('Date ({}) in "chrome timestamp": {}'.format(dtz, dtz_ts))
```
Printout:
```
Timezone-aware date to use (created): 2019-01-01 12:45:30.150000+00:00
Date (2019-01-01 12:45:30.150000+00:00) in "chrome timestamp": 13190820330150000
```

### To get a Unix timestamp, change the epoch year to 1970:
```python
dtz_ts_nix = date_to_chrometime(dtz, epoch_yr=1970)
print('Date ({}) in Unix timestamp: {}'.format(dtz, dtz_ts_nix))
```
Printout:
```
Date (2019-01-01 12:45:30.150000+00:00) in Unix timestamp: 1546346730150000
```

### Use this same timestamp to get back the date with the default date format:
```python
dtz_again = chrometime_to_date(dtz_ts)
print('Date from timestamp, default date format:\n{}'.format(dtz_again))
```
Printout:
```
Date from timestamp, default date format:
Tue, 01 January 2019 12:45:30 UTC
```

### Use this same timestamp to get back the date with a new date format:
```python
fmat = '%Y-%m-%d %H:%M:%S'
dtz_again = chrometime_to_date(dtz_ts, dt_format=fmat)
print('Date from timestamp, new date format ({}):\n{}'.format(fmat, dtz_again))
```
Printout:
```
Date from timestamp, new date format (%Y-%m-%d %H:%M:%S):
2019-01-01 12:45:30
```

### Note that `chrometime_to_date` return a string; to get back a date object, use `.strptime` with the same date format
```python
dt_dtz_again = datetime.datetime.strptime(dtz_again, fmat)
print(dt_dtz_again)
type(dt_dtz_again)
```
Printout:
```
2019-01-01 12:45:30
datetime.datetime
```