---
layout: layout
title: "Brief review of theory"
categories: examples
permalink: theory.html
---

#  Singular Spectrum Analysis
Singular spectrum analysis as a method of time series analysis has
well-elaborated theory and solves various problems: time series decomposition,
trend extraction, periodicity detection and extraction, signal extraction,
denoising, filtering, forecasting, missing data imputation, change point
detection, spectral analysis among them.
Since the method does not need a model given a priori, it is called
nonparametric and is well suited for exploratory analysis of time series.

SSA was originally proposed for time series, but was extended to 2D digital images. 2D-SSA and related subspace based methods find applications in texture analysis, seismology, spatial gene expression data, medical imaging, etc., and are gaining increasing popularity.

The SSA and 2D-SSA methods deal with series and rectangular images and have subseries and rectangles as moving windows.
This can limit applications of the methods; for example, the methods hardly process  circular-shaped images,
images with gaps and so on. Due to this reason, Shaped 2D-SSA
can be proposed, which can deal with images of arbitrary shape and arbitrary window shapes.

General scheme of SSA-like methods is as follows: 

![Scheme of SSA-like methods](scheme.jpg)