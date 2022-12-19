import os
import geoip2.database

from ._version import get_versions
VERSION = get_versions()['version']
del get_versions

DB_PATH = os.getenv('CSIRTG_GEO_SEARCH_PATH')


DB_SEARCH_PATHS = [
    '/usr/share/GeoIP',
    '/usr/local/share/GeoIP',
    '/usr/local/var/GeoIP',
    '/var/lib/GeoIP',
    './',
]

if DB_PATH:
    DB_SEARCH_PATHS.insert(0, DB_PATH)

CITY_DB_PATH = 'GeoLite2-City.mmdb'
ASN_DB_PATH = 'GeoLite2-ASN.mmdb'
CITY_DB = False
ASN_DB = False

for p in DB_SEARCH_PATHS:
    if os.path.isfile(os.path.join(p, CITY_DB_PATH)):
        CITY_DB = geoip2.database.Reader(os.path.join(p, CITY_DB_PATH))

    if os.path.isfile(os.path.join(p, ASN_DB_PATH)):
        ASN_DB = geoip2.database.Reader(os.path.join(p, ASN_DB_PATH))


if not CITY_DB and not ASN_DB:
    raise FileNotFoundError('missing maxmind mmdb files')
