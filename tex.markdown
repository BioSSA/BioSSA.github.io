---
layout: layout-tex
title: "TeX example"
categories: examples
permalink: tex.html
---

#  Some math text

<div>
 Пусть у нас имеется распределение с плотностью \(p(x) = c_1 e^{-x^2/2}\), сосредоточенное на промежутке \((a; +\infty)\), где \(c_1\) --- нормирующий множитель, который выражается следующим образом:
\begin{equation*}
c_1 = \frac{1}{\int\limits_a^{+\infty}e^{-x^2 / 2} dx}.
\end{equation*}
Для моделирования использовать метод отбора, а в качестве вспомогательного распределения возьмем распределение, сосредоточенное на том же промежутке \((a; +\infty)\), и имеющее плотность \(g(x) = c_2 x e^{-x^2/2}\), где:
\begin{equation*}
c_2 = \frac{1}{\int\limits_a^{+\infty} x e^{-x^2/2} dx} = \frac{1}{-e^{-x^2/2}\bigg|_a^{+\infty}} = \frac{1}{e^{-a^2/2}} = e^{a^2/2}.
\end{equation*}
</div>

#  Equation

<div>
$$\begin{matrix}
\dot{x} & = & \sigma(y-x) \\
\dot{y} & = & \rho x - y - xz \\
\dot{z} & = & -\beta z + xy
\end{matrix} $$
 </div>

#  More info

1. One rabbit
2. Two rabbits
3. **A lot of rabbits**