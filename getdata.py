"""ADS-B Decode demo."""

import sys
sys.path.append("src")
import socket
import os
import time

import adsb
import config

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

def find_pair_in_list(display, k):
    found = -1
    for key, value in display:
        if key == k:
            found += 1
            return found
        found += 1
    return -1

def updateData(display, index, aircraft_data):
    mode, lst = display[found]
    flight_number = aircraft_data.get('flight_number')
    latitude = aircraft_data.get('latitude')
    longitude = aircraft_data.get('longitude')
    altitude = aircraft_data.get('altitude')
    velocity = aircraft_data.get('velocity')
    direction = aircraft_data.get('direction')

    if flight_number != None and flight_number != lst[0]:
        lst[0] = flight_number
    if latitude != None and latitude != lst[1]:
        lst[1] = latitude
    if longitude != None and longitude != lst[2]:
        lst[2] = longitude
    if altitude != None and altitude != lst[3]:
        lst[3] = altitude
    if velocity != None and velocity != lst[4]:
        lst[4] = velocity
    if direction != None and direction != lst[5]:
        lst[5] = direction
    display[found] = (mode, lst)
    #print display[found]

def redraw(display):
    os.system('cls' if os.name == 'nt' else 'clear')
    print '{:10s} {:10s} {:10s} {:10s} {:10s} {:10s} {:10s}'.format('MODE-S', 'FLIGHT', 'LAT', 'LON', 'ALT', 'SPEED', 'TRACK')
    print '-----------------------------------------------------------------------'
    for mode, aircraft in display:
        #print aircraft
        print '{:10s} {:10s} {:10s} {:10s} {:10s} {:10s} {:10s}'.format(
            mode,
            str(aircraft[0]),
            str(aircraft[1]),
            str(aircraft[2]),
            str(aircraft[3]),
            str(aircraft[4]),
            str(aircraft[5])
            )


d = config.read_config()
TCP_IP = config.tcp_ip(d)
TCP_PORT = config.tcp_port(d)
BUFFER_SIZE = config.buffer_size(d)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
display = []
os.system('cls' if os.name == 'nt' else 'clear')
print '{:10s} {:10s} {:10s} {:10s} {:10s} {:10s} {:10s}'.format('MODE-S', 'FLIGHT', 'LAT', 'LON', 'ALT', 'SPEED', 'TRACK')
print '-----------------------------------------------------------------------'
while True:
    raw_data = s.recv(BUFFER_SIZE)
    aircraft_data = adsb.aircraft_data(raw_data)
    if bool(aircraft_data):

        found = find_pair_in_list(display, aircraft_data['mode-s'])

        if found == -1 :

            flight_number = aircraft_data.get('flight_number')
            latitude = aircraft_data.get('latitude')
            longitude = aircraft_data.get('longitude')
            altitude = aircraft_data.get('altitude')
            velocity = aircraft_data.get('velocity')
            direction = aircraft_data.get('direction')

            display.append((aircraft_data.get('mode-s'),
                [
                    '' if flight_number == None else flight_number,
                    '' if latitude == None else latitude,
                    '' if longitude == None else longitude,
                    '' if altitude == None else altitude,
                    '' if velocity == None else velocity,
                    '' if direction == None else direction
                ])
            )
        else:
            updateData(display, found, aircraft_data)

        redraw(display)

s.close()
