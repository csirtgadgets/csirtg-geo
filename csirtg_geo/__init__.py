
import re
from pprint import pprint
import sys
from geoip2.errors import AddressNotFoundError
from csirtg_geo.constants import CITY_DB, ASN_DB


def _get_asn(i):
    try:
        g = ASN_DB.asn(i)

    except AddressNotFoundError as e:
        return

    if not g:
        return

    rv = {}

    if g.autonomous_system_number:
        rv['asn'] = g.autonomous_system_number

    if g.autonomous_system_organization:
        rv['asn_desc'] = g.autonomous_system_organization

    return rv


def _get_city(i):

    rv = {}

    try:
        g = CITY_DB.city(i)

    except AddressNotFoundError as e:
        return

    if g.country.iso_code:
        rv['cc'] = g.country.iso_code

    if g.city.name:
        rv['city'] = g.city.name

    if g.location.longitude:
        rv['longitude'] = g.location.longitude

    if g.location.latitude:
        rv['latitude'] = g.location.latitude

    if g.location.latitude and g.location.longitude:
        rv['location'] = [g.location.longitude, g.location.latitude]

    if g.location.time_zone:
        rv['timezone'] = g.location.time_zone

    try:
        rv['region'] = g.subdivisions[0].names['en']

    except IndexError as e:
        pass

    return rv


def get(ip):
    """Take an IP and get it's Geo Information

Examples:

    from csirtg_geo import get as get_geo
    geo = get('1.1.1.1')

Arguments:

    :param ip: ip string
    :return: dict
    """

    match = re.search(r'^(\S+)\\/\d+$', ip)
    if match:
        ip = match.group(1)

    try:
        city = _get_city(ip)

    except ValueError as e:
        return

    try:
        asn = _get_asn(ip)

    except ValueError as e:
        return city

    asn.update(city)
    return asn


def main():
    i = sys.argv[1]

    i = get(i)

    pprint(i)


if __name__ == "__main__":
    main()

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
