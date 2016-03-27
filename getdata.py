"""ADS-B Decode demo."""

import socket
import os
import adsb
import config

d = config.read_config()
TCP_IP = config.tcp_ip(d)
TCP_PORT = config.tcp_port(d)
BUFFER_SIZE = config.buffer_size(d)

print TCP_IP, TCP_PORT, BUFFER_SIZE, "\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

os.system('cls' if os.name == 'nt' else 'clear')
#print '{:15s} {:15s} {:15s} {:15s} {:15s}'.format('MODE-S CODE', 'FLIGHT', 'LAT', 'LON', 'ALT')
while True:
    raw_data = s.recv(BUFFER_SIZE)
    aircraft_data = adsb.aircraft_data(raw_data)

    if bool(aircraft_data):
        print aircraft_data

s.close()
