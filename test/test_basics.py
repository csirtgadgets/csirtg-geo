from csirtg_geo import get as get_geo


IPS = (
    '128.205.1.1',
    '1.1.1.1',
    '162.159.44.53'
)


def test_geo():
    for i in IPS:
        d = get_geo(i)
        assert len(d) > 1
