"""
To convert timestamps in Chrome/Webkit format (default) to date
and vice versa.
author: Cat Chenal
"""
import datetime
from datetime import timezone


def chrometime_to_date(datestamp,
                       epoch_yr=1601, epoch_mo=1, epoch_day=1,
                       epoch_tz=timezone.utc,
                       dt_format='%a, %d %B %Y %H:%M:%S %Z'):
    """Chrome/Webkit (microseconds) timestamp -> date;
       Epoch (1601,1,1): preset for Chrome/Webkit timestamp conversion.
       For Unix, epoch_yr = 1970.
       Output: a date-formatted string.
    """
    # Assumption: datestamp is tz_aware.
    if (epoch_tz is None) or not (type(epoch_tz) is timezone):
        raise TypeError('Timezone-aware epoch needed, e.g. `epoch_tz=timezone.utc`.')
        
    epoch = datetime.datetime(epoch_yr, epoch_mo, epoch_day,
                              tzinfo=epoch_tz)
    out = epoch + datetime.timedelta(microseconds=int(datestamp))
    return (out.strftime(dt_format) if len(dt_format) else out)


def date_to_chrometime(tzdate,
                       epoch_yr=1601, epoch_mo=1, epoch_day=1,
                       epoch_tz=timezone.utc):
    """tzdate: a timezone-aware date, e.g.:
         tzdate = datetime.datetime.today().replace(tzinfo=timezone.utc)
       tzdate -> Chrome/Webkit timestamp
       Output: the difference between tzdate and epoch in microseconds (integer).
    """
    # Input check:
    if not (type(tzdate) is datetime.datetime):
        raise TypeError('`tzdate` must be of type `datetime.datetime`.')
        
    if tzdate.tzinfo is None:
        raise TypeError('Timezone-aware date needed.')
        
    if (epoch_tz is None) or not (type(epoch_tz) is timezone):
        msg = 'Timezone-aware epoch needed, e.g. `epoch_tz=timezone.utc`.'
        raise TypeError(msg)

    epoch = datetime.datetime(epoch_yr, epoch_mo, epoch_day,
                              tzinfo=epoch_tz)
    td = tzdate - epoch
        
    daily_secs = 86400 # == 24*60*60 :: 1 day in secs    
    return (td.microseconds + (td.seconds + td.days * daily_secs) * 10**6)


def test_chrome_convert(dtz):
    """ 
    Example: Input: dtz = datetime.datetime.today().replace(tzinfo=timezone.utc)
             Call:  test_chrome_convert(dt)
    """
    print('input date:', dtz)

    atime = date_to_chrometime(dtz)
    print('atime = date_to_chrometime(today):', atime)

    adate = chrometime_to_date(atime, dt_format='')
    print('adate = chrometime_to_date(atime):', adate)
    assert(dtz == adate)
    