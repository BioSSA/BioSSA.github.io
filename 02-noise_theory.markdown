---
layout: layout-bootstrap-tmp
title: "Noise Model"
permalink: 02-noise_theory.html
tags: theory
---

#  Noise model description

Generalized multiplicative noise model is considered:

`\(res_i = σ (trend_i + offset)^α \cdot ξ_i\)`,

where `\(ξ_i\)` have standard normal distribution.

Value of alpha is estimated as follows: logarithms of absolute values of residuals and ofsetted trend are considered, then they both ordered by the trend values and averaging prcedure performed. There are following averaging methods: 'none' means nothing averaging, 'sliding-window' means sliding window averaging (default approach) with window length denoted by window argument, 'equal-break' and 'quantile-break' mean splitting all trend values into buckets ('quantile-break' means buckets with equal quantity of elements in each bucket and 'equal-break' means equal size buckets), correspondingly residuals splitting and averaging logarithmed residuals and trend values in each bucket.

Then linear regression on averaged logarithms is provided. Slope is alpha esimation and intercept is estimation of logarithm of the standard deviation of relative noise, i.e. `\(\sigma = \exp(Intercept)\)`.