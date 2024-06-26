# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings


# Log anonymous actions?
ACTIVITYLOG_MAIN_IP_KEY_VALUE = getattr(settings, 'ACTIVITYLOG_MAIN_IP_KEY_VALUE', "MAIN_IP")
ANONIMOUS = getattr(settings, 'ACTIVITYLOG_ANONIMOUS', False)
# Ensure misspelling from previous versions is handled
if ANONIMOUS:
    ANONYMOUS = True
else:
    ANONYMOUS = getattr(settings, 'ACTIVITYLOG_ANONYMOUS', True)

# Update last activity datetime in user profile
LAST_ACTIVITY = getattr(settings, 'ACTIVITYLOG_LAST_ACTIVITY', True)

# Only this methods will be logged
METHODS = getattr(settings, 'ACTIVITYLOG_METHODS',
                  ('GET', 'POST', 'PUT', 'PATCH', 'DELETE'))

# List of response statuses, which logged. By default - all logged.
# Don't use with ACTIVITYLOG_EXCLUDE_STATUSES
STATUSES = getattr(settings, 'ACTIVITYLOG_STATUSES', None)

# List of response statuses, which ignores. Don't use with ACTIVITYLOG_STATUSES
EXCLUDE_STATUSES = getattr(settings, 'ACTIVITYLOG_EXCLUDE_STATUSES', None)

# URL substrings, which ignores
EXCLUDE_URLS = getattr(settings, 'ACTIVITYLOG_EXCLUDE_URLS', ())

# IPs substrings, which ignores
EXCLUDE_IP_LIST = getattr(settings, 'EXCLUDE_IP_LIST', [])
# Create DB automatically (for postgres, and may be mysql)
AUTOCREATE_DB = getattr(settings, 'ACTIVITYLOG_AUTOCREATE_DB', False)

# Customization for ip_address field.
# List of HTTP headers where we will search user IP
IP_ADDRESS_HEADERS = (ACTIVITYLOG_MAIN_IP_KEY_VALUE,'HTTP_X_FORWARDED_FOR','HTTP_X_REAL_IP', 'HTTP_CLIENT_IP',
                       'REMOTE_ADDR')

# Customization for extra_data field.
# Function get request and response objects, returns str
GET_EXTRA_DATA = getattr(settings, 'ACTIVITYLOG_GET_EXTRA_DATA', None)

# Log DB key in DATABASES (for internal usage only, don't modify)
LOG_DB_KEY = getattr(settings, 'DATABASE_APPS_MAPPING', {}).get('activity_log')

if LOG_DB_KEY and not settings.DATABASES.get(LOG_DB_KEY):
    db = settings.DATABASES['default'].copy()
    db['NAME'] = '{}_{}'.format(db['NAME'], LOG_DB_KEY)
    settings.DATABASES[LOG_DB_KEY] = db

ACTIVITYLOG_MAXIMUM_RECORD_SIZE = getattr(settings, 'ACTIVITYLOG_MAXIMUM_RECORD_SIZE', None)
