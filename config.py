import json

def read_config():
  with open('config.json') as data_file:
    data = json.load(data_file)
  print data
  return data

def tcp_ip(data):
  return data["tcp_ip"]

def tcp_port(data):
  return data["tcp_port"]

def buffer_size(data):
  return data["buffer_size"]
