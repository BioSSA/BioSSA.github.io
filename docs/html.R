#!/usr/bin/Rscript

library(knitr)
knit_rd("BioSSA")


file.copy("../DESCRIPTION", ".")
system("python2.7 links.py")

