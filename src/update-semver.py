# core
import re
import sys
import tomllib

# community
import semver
import tomli_w

FILE_PYPROJECT = 'pyproject.toml'

with open(FILE_PYPROJECT,'rb') as infile:
  pyproject = tomllib.load(infile)
  version = semver.Version.parse(pyproject["project"]["version"])

print (f'Version before: {version}') 

print (f'cmd: {sys.argv[len(sys.argv)-1]}')
if sys.argv[len(sys.argv)-1] == 'major':
  version = version.bump_major()
elif sys.argv[len(sys.argv)-1] == 'minor':
  version = version.bump_minor()
elif sys.argv[len(sys.argv)-1] == 'patch':
  version = version.bump_patch()
elif re.search('^\d+\.\d+\.\d+$', sys.argv[len(sys.argv)-1]):
  version = version.parse(sys.argv[len(sys.argv)-1])

print (f'Version after: {version}') 
pyproject["project"]["version"] = str(version)
with open(FILE_PYPROJECT, 'wb') as outfile:
  tomli_w.dump(pyproject, outfile)

