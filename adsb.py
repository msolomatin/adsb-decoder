import helper

def downlink_format(message):
  return ""

def message_subtype(message):
  return ""

def icao_aircraft_address(binary_message):
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
  number += charset[helper.bin2int(binary_message[40:46])]
  number += charset[helper.bin2int(binary_message[46:52])]
  number += charset[helper.bin2int(binary_message[52:58])]
  number += charset[helper.bin2int(binary_message[58:64])]
  number += charset[helper.bin2int(binary_message[64:70])]
  number += charset[helper.bin2int(binary_message[70:76])]
  number += charset[helper.bin2int(binary_message[76:82])]
  number += charset[helper.bin2int(binary_message[82:88])]
  return number.translate(None, '#')
