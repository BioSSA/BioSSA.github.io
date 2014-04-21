---
layout: layout-bootstrap-tmp
title: "Example of application"
categories: examples
permalink: example_application.html
tags: mainmenu
---

#  Example of BioSSA application

## Decomposition of cylindrical data

Let us consider data for expression of gene activity measured on the embryo of the drosophila (fruit fly).
The form of the embryo is similar to ellipsoid and therefore the cylindrical projection is adequate for
a middle part of the embryo. The technique of SSA analysis of such kind of 2D data by planar non-shaped 2D-SSA
was developed in Golyandina et al (2012) and Holloway et al (2011).
After projection, the initial data given on 3D embryo surfaces are represented in the form `\((x_i, y_i, f_i)\)` where `\((x_i, y_i)\)` are coordinates of nuclei centers in the cylindric projection transformed to a planar rectangle, `\(f_i\)` are the expression values. The aim of the analysis is to decompose data into a sum of
pattern and noise and then measure the signal/noise ratio. Data are cropped and
then are interpolated to a regular grid; therefore, we obtain a digital image, which
can be processed by 2D-SSA. Values of smoothed expression are interpolated backward onto
nuclei centers.

Here we demonstrate that the developed circular version of 2D-SSA can perform smoothing without
artificial transformation of a cylinder to the rectangle. Thus the result of processing
does not depend on the technique of this transformation and has no extra edge effects. We consider the cylindrical topology.

Data were downloaded from the BDTNP archive, the file "v5_s11643-28no06-04.pca".

Data on the surface of embryo are given in 3D coordinates, therefore we calculated cylindric coordinates
by finding the principal axis of the data. The interpolation is performed with the step 0.5% and the
middle part from 20 to 80% of the embryo lengths were processed.

The result of decomposition (the factor vectors from the `\(12\)` leading eigentriples) is depicted in the figure below.

![Factor vectors](circular_factor.png) 

![Reconstruction and residuals](circular_reconstructed.png)

The components 1-6 grouped together provide an adequate smoothing; the residual oscillates around zero.
Note that the bottom and top edges are coincide, that is, there is no edge effect.

## Construction of noise model

To begin with, we choose parameters for SSA based on 2D-SSA theory and size of embryo. Then we check that the result of reconstruction is adequate. Then `\(\alpha\)` needs to be estimated, and we decide what noise model was used depending on `\(\alpha\)`. It's multiplicative noise model the following example:

{% highlight r %}

xlim <- c(22, 88)
ylim <- c(32, 68)
L <- c(15, 15)

file <- system.file("extdata/data", "ab16.txt", package = "BioSSA")
df <- read.emb.data(file)

bs <- BioSSA(cad ~ AP + DV, data = df, ylim = ylim, xlim = xlim, L = L)
nm <- noise.model(bs, 1:3, averaging.type = "none")
plot(plot(nm))
summary(nm)

{% endhighlight %}

{% highlight r %}

Noise model:
  Multiplicity: 1.236 
  sigma: 0.009559 
  Noise sd: 0.0207 
{% endhighlight %}

![Noise model](03_noisemodel.png)
