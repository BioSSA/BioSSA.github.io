#!/usr/bin/env python
# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2

import re
import glob
import os
import sys
import fileinput
os.chdir(".")

subs = set()
for file in glob.glob("*.html"):
  for line in open(file):
    matches = re.findall("href=\\\"(\.\.\/\.\.[^\\\"]*)\\\"", line)
    if (len(matches)):
      for match in matches:
        subs.add(match)

print subs

subrules = {}
for sub in subs:
  pkg = re.findall("\.\.\/\.\./([^\/]*).*", sub)[0]
  if (pkg in ["lattice", "stats", "base", "grDevices"]):
    subrules[sub] = sub.replace("../../", "http://stat.ethz.ch/R-manual/R-devel/library/")
    subrules[sub] = subrules[sub].replace("lattice%2dpackage", "Lattice").replace("colorRampPalette", "colorRamp")
  else:
    subrules[sub] = "http://cran.r-project.org/web/packages/%s/%s.pdf" % (pkg, pkg)


subrules["\"../DESCRIPTION\""] = "\"DESCRIPTION\""
subrules["\"embryo3d.html\""] = "\"embryo.html\""
subrules["\"embryo2d.html\""] = "\"embryo.html\""

print subrules

for file in glob.glob("*.html"):
  for line in fileinput.input(file, inplace = True):
    for what, to in subrules.iteritems():
      line = line.replace(what, to)
    sys.stdout.write(line)
