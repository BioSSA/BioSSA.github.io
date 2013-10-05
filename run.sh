#/bin/sh

haml haml/layout.haml -f xhtml _layouts/layout.html
haml haml/layout-tex.haml -f xhtml _layouts/layout-tex.html
jekyll serve