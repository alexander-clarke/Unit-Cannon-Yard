import os
import json
import string
from os.path import join

for root, dirnames, filenames in os.walk('.'):
  for f in filenames:
    f = f.lower()
    if f[-5:] == ".json":
      fullpath = join(root, f)
      print("%s" % fullpath)
      fp = open(fullpath)
      data = json.load(fp)
      fp.close()
      fp = open(fullpath, 'w')
      fp.write('{"base_spec":"/pa/units/land/unit_cannon/unit_cannon.json"}')
      fp.close()
