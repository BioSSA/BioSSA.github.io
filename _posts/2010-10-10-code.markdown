---
layout: layout
title: "Code example"
categories: examples
permalink: code.html
---

#  Some code examples
## C++
{% highlight c++ %}
#include "const.h"
#include "board.h"
#include "game.h"
#include <QPainter>

Game::Game(QPixmap &pixmap, const GameParams &gp) {
    canvas = &pixmap;
    Gp = &gp;
    board = new Board(*canvas, *Gp);
    selected = 0;
    draw_grid();
    score = 0;
    board -> insert_new();
    update_score(0);
}

Game::Game(const Game &game, QPixmap &pixmap) {
    canvas = &pixmap;
    Gp = game.Gp;
    board = new Board(*game.board, *canvas);
    selected = game.selected;
    score = game.score;
    Xsel = game.Xsel; Ysel = game.Ysel;
}

{% endhighlight %}

## R
{% highlight r %}
cadzow.1d.ssa <- function(x, rank,
                          correct = TRUE,
                          eps = 1e-6, numiter = 0,
                          ..., cache = TRUE) {
  # Get the result w/o any correction
  fcall <- match.call(expand.dots = FALSE)
  fcall[[1]] <- cadzow.ssa
  fcall$correct <- NULL
  F <- eval(fcall, parent.frame())

  # Correct the stuff if requested
  if (correct) {
    h1 <- hankel(F, x$window)
    h2 <- hankel(.get(x, "F"), x$window)

    F <- sum(h1 * h2) / sum(h2 * h2) * F
  }

  F
}

cadzow.mssa <- function(x, rank,
                        correct = TRUE,
                        eps = 1e-6, numiter = 0,
                        ..., cache = TRUE) {
  # Get the result w/o any correction
  fcall <- match.call(expand.dots = FALSE)
  fcall[[1]] <- mcadzow
  fcall$correct <- NULL
  F <- eval(fcall, parent.frame())

  # Correct the stuff if requested
  if (correct) {
    h1 <- unlist(.to.series.list(F, na.rm = TRUE))
    h2 <- unlist(.to.series.list(.get(x, "F"), na.rm = TRUE))
    
    F <- sum(h1 * h2 * .hweights(x)) / sum(h2 * h2 * .hweights(x)) * F
  }

  F
}

cadzow <- function(x, ...)
  UseMethod("cadzow")


{% endhighlight %}

