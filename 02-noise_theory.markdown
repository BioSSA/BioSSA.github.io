---
layout: layout-bootstrap-tmp
title: "Noise Model"
permalink: 02-noise_theory.html
tags: theory
---

# Model application
<div class="alert alert-success">
    The suggested model is introduced and applied in the following papers supported by NG13-083 Grant of Dynasty Foundation, US NIH Grant R01-GM072022, and The Russian Foundation for Basic Research Grant 13-04-02137
    <ul>
    <li> A. Shlemov, N. Golyandina, D. Holloway, A. Spirov. <a href = "https://www.hindawi.com/journals/bmri/2015/689745/" class="alert-link">
    Shaped Singular Spectrum Analysis for quantifying gene expression, with application to the early <i>Drosophila</i> embryo.</a> <i>BioMed Research International,</i> vol. 2015, Article ID 689745, 14 pages, 2015</li>
    <li> A. Shlemov, N. Golyandina, D. Holloway, A. Spirov.<a href = "https://www.hindawi.com/journals/bmri/2015/986436/" class="alert-link">Shaped 3D Singular Spectrum Analysis for Quantifying Gene Expression, with Application to the Early <i>Zebrafish</i> Embryo.</a> <i>BioMed Research International,</i> vol. 2015, Article ID 986436, 18 pages, 2015</li>
    </ul>
</div>
#  Noise model description

Generalized multiplicative noise model is considered:

`\(res_i = σ (trend_i + offset)^α \cdot ξ_i\)`,

where `\(ξ_i\)` have standard normal distribution.

The value of `\(\alpha\)` is estimated as follows:
logarithms of absolute values of residuals and offsetted trend are considered,
then they both are ordered by the trend values and the averaging procedure is performed.
There are following averaging methods:

- 'none' means nothing averaging,
- 'sliding-window' means averaging by sliding windows (default approach) with window length denoted by window argument,
- 'equal-break' and 'quantile-break' means splitting all trend values
into bins ('quantile-break' means bins with equal quantity of elements in each bin and
'equal-break' means equal size bins), correspondingly residuals splitting and averaging
log-transformed residuals and trend values in each bin.

Then linear regression on averaged logarithms is provided. Slope provides an
`\(\alpha\)` esimate and correted (on the non-zero expectation of logarithmed absolute value of standard normal variate) intercept is an estimate of logarithm of the standard
deviation of relative noise, i.e. `\(\hat{\sigma} = \exp(Intercept - \mathop{\mathbb{E}}(\xi))\)`.
