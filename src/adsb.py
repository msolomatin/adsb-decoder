import helper
from math import sqrt
from math import atan2
from math import pi
'''
{
  mode-s,
  flight_number,
  latitude,
  longitude,
  altitude,
  velocity,
  binary
}
'''
def aircraft_data(raw_message):
    databin = _raw_message_to_binary_string(raw_message)
    downlink_format = _downlink_format(databin)

    data = {}

    if downlink_format == 17:
        data = _relevant_data(databin)

    return data

def _relevant_data(binary_message):
    data = {}
    type_code = _type_code(binary_message)
    if 1 <= type_code <= 4:
        data = _aircraft_identification(binary_message)
    if 9 <= type_code <= 18:
        data = _airbone_details(binary_message)
    if type_code == 19:
        data = _velocity(binary_message)
    return data

def _velocity(binary_message):
    subtype = helper.bin2int(binary_message[37:40])
    velocity = "N/A"
    direction = "N/A"
    if subtype == 1:
        east_west_velocity = helper.bin2int(binary_message[46:56])
        east_west_velocity_sign = helper.bin2int(binary_message[45])
        north_south_velocity = helper.bin2int(binary_message[57:67])
        north_south_velocity_sign = helper.bin2int(binary_message[56])
        velocity_east_west = -1 * (east_west_velocity - 1) if east_west_velocity_sign == 1 else east_west_velocity - 1
        velocity_north_south = -1 * (north_south_velocity - 1) if north_south_velocity_sign == 1 else north_south_velocity - 1
        velocity = sqrt(velocity_east_west * velocity_east_west + velocity_north_south * velocity_north_south)
        direction = atan2(velocity_east_west, velocity_north_south) * 1.0 * 180 / pi
        if direction < 0:
            direction += 360

    return {
        "mode-s": _icao_aircraft_address(binary_message),
        "velocity": velocity,
        "direction": direction
    }

def _aircraft_identification(binary_message):
    return {
        "mode-s": _icao_aircraft_address(binary_message),
        "flight_number": flight_number(binary_message)
        }

def _airbone_details(binary_message):
    return {
        "mode-s": _icao_aircraft_address(binary_message),
        "altitude": _altitude(binary_message)
    }

def _raw_message_to_binary_string(raw_data):
    datahex = raw_data.encode('hex')
    datahex = remove_preamble(datahex)
    databin = helper.hex2bin(datahex)
    return databin

def _type_code(binary_message):
    return helper.bin2int(binary_message[32:37])

def _downlink_format(binary_message):
    return helper.bin2int(binary_message[0:5])

def message_subtype(message):
    return ""

def _icao_aircraft_address(binary_message):
    return helper.bin2hex(binary_message[8:32])

def data_frame(message):
    return ""

def parity_check(message):
    return ""

def preamble(message):
    return ""

def remove_preamble(raw_message):
    return raw_message[18:]

def flight_number(binary_message):
    charset = '#ABCDEFGHIJKLMNOPQRSTUVWXYZ#####################0123456789######'
    number = ''
    start = 40
    offset = 6
    while start <= 82:
        number += charset[helper.bin2int(binary_message[start:(start + offset)])]
        start += offset
    return number.translate(None, '#')
'''
def position(binary_message):
  bit = binary_message[53]
  latitude_even = 0.0
  longitude_even = 0.0
  # Bit is even
  if bit == '0':
    latitude_even = bin2int(binary_message[54:71]) / 131072
    longitude_even = bin2int(binary_message[71:88]) / 131072
  latitude_odd = 0.0
  longitude_odd = 0.0
  if bit == '1':
    latitude_odd = bin2int(binary_message[54:71]) / 131072
    longitude_odd = bin2int(binary_message[71:88]) / 131072


def latitude(binary_message):
  bit = binary_message[53]
  latitude_even = 0.0
  latitude_odd = 0.0
  # Bit is even
  if bit == '0':
    latitude_even = bin2int(binary_message[54:71]) / 131072

  return [latitude, longitude]

def longitude(binary_message):
  return binary_message[71:88]
'''

def _altitude(binary_message):
    q_bit = binary_message[47:48]
    multiplier = 25 if q_bit == '1' else 100

    string_without_q_bit = binary_message[:47] + binary_message[48:]
    N = helper.bin2int(string_without_q_bit[40:51])

    return str(N * multiplier - 1000)
