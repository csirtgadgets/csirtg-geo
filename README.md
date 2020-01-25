# CSIRTG-GEO

The FASTEST way to get Geo Information.

# Examples
## Shell
```bash
$ csirtg-geo 1.1.1.1

{'asn': 13335,
 'asn_desc': 'Cloudflare, Inc.',
 'cc': 'AU',
 'latitude': -33.494,
 'location': [143.2104, -33.494],
 'longitude': 143.2104,
 'timezone': 'Australia/Sydney'}
```

## Python
```python
from csirtg_geo import get
from pprint import pprint

ts = get('1.1.1.1')
pprint(ts)
```

# Before You Begin
You must:  
  1. install your native OS maxmind tools
  1. visit https://www.maxmind.com/en/home
  1. create an account and an api token
  1. update GeoIP.conf
  1. `pip install csirtg-geo`
  
 MaxMind provides a lot of great data FOR FREE. Consider a paid subscription!
 
 https://www.maxmind.com/en/geoip2-databases