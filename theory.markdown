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
detection, spectral analysis among them (see examples and references in
\citet{Vautard.Ghil1989,Golyandina.etal2001,Ghil.etal2002,Golyandina.Zhigljavsky2012}).
Since the method does not need a model given a priori, it is called
nonparametric and is well suited for exploratory analysis of time series.

Additionally, SSA allows the construction of the model during or after
exploratory analysis.  The underlying parametric model of the signal is the sum
of products of polynomial, exponential and sine-wave functions.  This is a
linear model in the following sense: such series constitute the class of
solutions of linear differential equations. In the case of discrete time, such
time series satisfy linear recurrent relations (LRRs).  There is a class of so
called subspace-based methods \citep{VanDerVeen.etal1993}, which are related to
estimation of parameters in the mentioned parametric model, in particular, to
estimation of frequencies.

Although some problems like frequency estimation do need the model, some
problems like smoothing do not need a model at all.  For forecasting in SSA, the
time series may satisfy the model approximately and locally, since the
forecasting is based on estimation of the signal subspace and not on estimation
of the parameters of the model.  Depending on the quality of approximation of the series by
the model, long or short horizon forecasts can be constructed.

![Scheme of SSA-like methods](scheme.ipg)