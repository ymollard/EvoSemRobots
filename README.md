# EvoSemRobots
Project developed during technical atelier [Evolutionary Semantics On Real Robots](http://ai.vub.ac.be/como-atelier-2016/) during [Creativity And Evolution Summerschool (CAES)](http://caes.lakecomoschool.org/) which took place in Como, 5 – 9 September 2016.

Repository consists of two folders which represents two different topics discussed during this atelier:
- lisp - excercises on naming games and guessing games,
- python - language games that uses comuter vision and NAO V5 robot.

## lisp 

Three excercises on color categories lexicon learning.

#### Prerequisites
- [Babel2](http://emergent-languages.org/Babel2/) - use installation [script](http://emergent-languages.org/Babel2/script.html) to install all other necessery software (Lisp, emacs, slime, Gnuplot, ...)

## python 

This folder contains files connected to the experiments with NAO V5 robot. It uses OpenCV for computer vision and PyNaoqi to connect with NAO robot.

#### Prerequisites
- [Python 2.7](http://emergent-languages.org/Babel2/) with pip, numpy, etc.
- OpenCV - you can use this [guide](http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/) to install it on Ubuntu
- [NAOqi for Python](http://doc.aldebaran.com/1-14/dev/python/install_guide.html)

#### Usage

Just run file experiments.py which contains two sections:
- learner : NAO is learning names for colors of objects that it recognizes
- teacher : NAO is teaching a user three basic colors (blue, red, green) and directions (left, right, centre) in italian

