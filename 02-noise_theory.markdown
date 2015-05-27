---
layout: layout-bootstrap-tmp
title: "Noise Model"
permalink: 02-noise_theory.html
tags: theory
---

#  Noise model description

The generalized multiplicative noise model is considered:

`\(res_i = σ (trend_i + offset)^α \cdot ξ_i\)`,

where `\(ξ_i\)` has standard normal distribution.

The value of `\(\alpha\)` is estimated as follows:
logarithms of absolute values of residuals and offsetted trend are considered,
then they both are ordered by trend values and the averaging procedure is performed.
There are following averaging methods:

- 'none' means that averaging is not performed,
- 'sliding-window' means averaging by sliding windows (default approach) with window length denoted by the window argument,
- 'equal-break' and 'quantile-break' means splitting all trend values
into bins ('quantile-break' means bins with equal quantity of elements in each bin and
'equal-break' means equal size bins), correspondingly residuals splitting and averaging
log-transformed residuals and trend values in each bin.

Then the linear regression on averaged logarithms is provided. A slope provides the `\(\alpha\)` esimate and a intercept is the estimate of logarithm of the standard deviation of relative noise, i.e. `\(\sigma = \exp(Intercept)\)`.