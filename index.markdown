---
layout: layout-bootstrap-tmp
title: "About Package"
categories: examples
permalink: index.html
tags: mainpage
---
# Aim of the project


Aim of the project is to create the package, which is designed for analysis of 2D data or 3D surface irregular data in cylindrical projection. Interface of the package should be convenient for 
processing of data of gene expression of drosophila fly.

**Input data**: points `\((x_i, y_i, f_i)\)` given on a planar surface.

**Output**:  decomposition of data on trend (pattern) and noise, construction of the noise model.

# Possibilities of the package

1.	Loading the data from files given in the following formats
(x,y, gene expression).
2.	Decomposition of data
	-	 Transformation of data to the scale 0-100% by AP and DV coordinates
	-	Choice of rectangular area for analysis
	-	Regularization of data (interpolation to regular grid), the step of the grid can be set.
	-	Decomposition of regularized data by the 2D-SSA method
	-	Interpolation of data to initial coordinates.
3.	Checking the decomposition quality
	- Profiles of patterns along AP or DV axis
	- Profiles of noise along AP or DV axis
4.	Analysis of residuals, model of residuals
	-	Graphs of dependence of noise on patters, 
	-	Estimation of noise model: additive, multiplicative or Poissonian model.
5.	Pictures with the results of decomposition in 2D or 3D forms.

# Implementation

The package is implemented as an R-package [BioSSA](BioSSA_0.0.1.zip)

It essentially uses the  [Rssa]( http://cran.r-project.org/web/packages/Rssa/ "Cсылка на Rssa") package.  

# Method

Decomposition of the image into a sum of pattern and noise is fulfilled  by 2D Singular Spectrum Analysis. 

#Support

This work is supported by the NG13-083 grant of Dynasty Foundation.
