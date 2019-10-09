"""Orange and Rockland Utility Smart Energy Meter"""
import requests
import logging as _LOGGER


class Meter(object):
    """A smart energy meter of Orange and Rockland Utility.

    Attributes:
        meter_id: A string representing the meter's id
    """

    def __init__(self, meter_id):
        """Return a meter object whose meter id is *meter_id*"""
        self.meter_id = meter_id
        self.unit_of_measurement = 'WH'

    def last_read(self):
        """Return the last meter read in WH"""
        url = 'https://oru.opower.com/ei/edge/apis/cws-real-time-ami-v1/cws' \
            '/oru/meters/' + self.meter_id + '/usage'
        _LOGGER.debug("url = %s", url)

        response = requests.get(url)
        _LOGGER.debug("response = %s", response)

        jsonResponse = response.json()
        _LOGGER.debug("jsonResponse = %s", jsonResponse)

        if 'error' in jsonResponse:
            print('Error = %s', jsonResponse['error'])
            raise RuntimeError()

        # parse the return reads and extract the most recent one (i.e. last not None)
        lastRead = None
        for read in jsonResponse['reads']:
            if read['value'] is None:
                break
            lastRead = read
        _LOGGER.info("lastRead = %s", lastRead)

        val = lastRead['value']
        _LOGGER.debug("val = %s", val, )

        val *= 1000  # transform from KWH in WH
        val = int(round(val))
        _LOGGER.info("val = %s %s", val, self.unit_of_measurement)

        self.last_read_wh = val

        return self.last_read_wh