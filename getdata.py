import socket
import adsb
import helper
import os
import config

d = config.read_config()
TCP_IP = config.tcp_ip(d)
TCP_PORT = config.tcp_port(d)
#TCP_PORT = 31018
BUFFER_SIZE = config.buffer_size(d)

print TCP_IP, TCP_PORT, BUFFER_SIZE, "\n"
received = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

os.system('cls' if os.name == 'nt' else 'clear')
print '{:15s} {:15s}'.format('MODE-S CODE', 'FLIGHT')
while True:
  raw_data = s.recv(BUFFER_SIZE)
  datahex = raw_data.encode('hex')
  datahex = adsb.remove_preamble(datahex)
  databin = helper.hex2bin(datahex)
  if helper.bin2int(databin[0:5]) == 17 and (1 <= helper.bin2int(databin[32:36]) <= 4):
    print '{:15s} {:15s}'.format(adsb.icao_aircraft_address(databin), adsb.flight_number(databin))

  received += len(raw_data)

s.close()
