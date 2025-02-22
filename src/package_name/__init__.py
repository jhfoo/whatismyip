import os

def cli():
  print (f'File: {__file__}')
  print (f'Script folder: {os.path.realpath(__file__)}')
  print ('Run from module:cli()')
