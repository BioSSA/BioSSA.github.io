install.packages(c("latticeExtra", "rgl", "stringr", "akima", "pracma", "geometry", "tripack"))

temp.file.name <- tempfile()
temp.dir.name <- tempdir()

sysname <- as.character(Sys.info()["sysname"])
if (identical(sysname, "Linux")) {
  download.file("https://github.com/BioSSA/BioSSA/archive/master.zip", destfile = temp.file.name, method = "wget")
} else if (identical(sysname, "Windows")){
  # utils::setInternet2(TRUE)
  download.file("https://github.com/BioSSA/BioSSA/archive/master.zip", destfile = temp.file.name)
} else {
  stop(sprintf("Unsupported OS: %s", sysname))
}

unzip(temp.file.name, exdir = temp.dir.name)

pkg.dir.name <- paste(temp.dir.name, "BioSSA-master", sep = "/")
install.packages(pkg.dir.name, repos = NULL, type = "source")

unlink(pkg.dir.name, recursive = TRUE)
unlink(temp.file.name)

