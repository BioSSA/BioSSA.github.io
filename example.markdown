---
layout: layout-bootstrap-tmp
title: "Example"
categories: examples
permalink: example.html
tags: mainmenu
---

#  Example of BioSSA application

## Cylindric Shaped 2D-SSA


Let us consider the data for expression of gene activity measured on the embryo of the drosophila (fruit fly).
The form of the embryo is similar to ellipsoid and therefore the cylindrical projection is adequate for
a middle part of the embryo. The technique of SSA analysis of such kind of 2D data by planar non-shaped 2D-SSA
was developed in Golyandina et al (2012) and Holloway et al (2011).
After projection, the initial data given on 3D embryo surfaces are represented in the form `\((x_i, y_i, f_i)\)` where `\((x_i, y_i)\)` are coordinates of nuclei centers in the cylindric projection transformed to a planar rectangle, `\(f_i\)` are the expression values. The aim of the analysis is to decompose the data into a sum of
pattern and noise and then measure the signal/noise ratio. The data are cropped and
then are interpolated to a regular grid; therefore, we obtain a digital image, which
can be processed by 2D-SSA. The values of smoothed expression are interpolated backward onto
nuclei centers.

Here we demonstrate that the developed circular version of 2D-SSA can perform smoothing without
artificial transformation of a cylinder to the rectangle. Thus the result of processing
does not depend on the technique of this transformation and has no extra edge effects. We consider the cylindrical topology.

The data are downloaded from the BDTNP archive,
the file ``v5_s11643-28no06-04.pca'', ``even skipped''.

The data on the surface of embryo are given in 3D coordinates, therefore we calculated cylindric coordinates
by finding the principal axis of the data. The interpolation is performed with the step 0.5% and the
middle part from 20 to 80% of the embryo lengths were processed.

The result of decomposition (the factor vectors from the $12$ leading eigentriples) is depicted in the figure below.

![Factor vectors](circular_factor.png)

![Reconstruction and residuals](circular_reconstructed.png)

The components 1--6 grouped together provide an adequate smoothing; the residual oscillates around zero.
Note that the bottom and top edges are coincide, that is, there is no edge effect.
