---
layout: layout-bootstrap-tmp
title: "Code fragments"
categories: examples
permalink: codefrag.html
tags: mainmenu
---

#  Code fragments

## The most important function is BioSSA.

- data is the collection of data as a data frame 
- biossa.formula help to choose ; e.g., biossa.formula = mean ~ X + Y 
- L is the window length
- step is the step of interpolation
- xlim and ylim are ???
- xperc and yperc are ???

{% highlight r %}

  bss <- BioSSA(biossa.formula, data = emb.raw,
                L = L,
                step = 0.5,
                xlim = xlim,
                ylim = ylim,
                xperc = xperc,
                yperc = yperc)

#***w-correlations for identification
  plot(plot(bss, type = "wcor", groups=as.list(1:30)))

#***Reconstruction of elementary components
  rec.elem <- reconstruct(bss, groups=as.list(1:6))
  plot(plot(rec.elem))


{% endhighlight %}

## Checking of decomposition quality

{% highlight r %}
#***Sections for testing the reconstruction quality
  rec.cum <- reconstruct(bss, list(1, 1:2, 1:3, 1:4, 1:5, 1:6, 1:7, 1:8, 1:9, 1:10))
  p.ny <- plot(attr(rec.cum, "series"), "nuclei-section", at = aty, coord = "y", tol = toly)
  p.fy1 <- plot(rec.cum[[bad]], "field-section", at = aty, coord = "y")
  p.fy2 <- plot(rec.cum[[good]], "field-section", at = aty, coord = "y")
  p.nx <- plot(attr(rec.cum, "series"), "nuclei-section", at = atx, coord = "x", tol = tolx)
  p.fx1 <- plot(rec.cum[[bad]], "field-section", at = atx, coord = "x")
  p.fx2 <- plot(rec.cum[[good]], "field-section", at = atx, coord = "x")
  pls <- list()

#y-sections, good and bad
  pls[[1]] <- p.ny + p.fy1
  pls[[2]] <- plot(residuals(bss, 1:bad), "nuclei-section", at = aty, coord = "y", tol = toly,
                   ref = TRUE, col = "blue")
  pls[[3]] <- p.ny + p.fy2
  pls[[4]] <- plot(residuals(bss, 1:good), "nuclei-section", at = aty, coord = "y", tol = toly,
                   ref = TRUE, col = "blue")

  print(pls[[1]], split = c(1, 1, 2, 2), more = TRUE)
  print(pls[[2]], split = c(2, 1, 2, 2), more = TRUE)
  print(pls[[3]], split = c(1, 2, 2, 2), more = TRUE)
  print(pls[[4]], split = c(2, 2, 2, 2))

#x-sections, good and bad
  pls[[1]] <- p.nx + p.fx1
  pls[[2]] <- plot(residuals(bss, 1:bad), "nuclei-section", at = atx, coord = "x", tol = tolx,
                   ref = TRUE, col = "blue")
  pls[[3]] <- p.nx + p.fx2
  pls[[4]] <- plot(residuals(bss, 1:good), "nuclei-section", at = atx, coord = "x", tol = tolx,
                   ref = TRUE, col = "blue")

  print(pls[[1]], split = c(1, 1, 2, 2), more = TRUE)
  print(pls[[2]], split = c(2, 1, 2, 2), more = TRUE)
  print(pls[[3]], split = c(1, 2, 2, 2), more = TRUE)
  print(pls[[4]], split = c(2, 2, 2, 2))

{% endhighlight %}
