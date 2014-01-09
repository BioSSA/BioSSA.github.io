---
layout: layout
title: "Example"
categories: examples
permalink: example.html
---

#  Example of BioSSA application

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