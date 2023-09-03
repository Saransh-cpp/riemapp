# riemapp

[![CI](https://github.com/Saransh-cpp/riemapp/actions/workflows/ci.yml/badge.svg)](https://github.com/Saransh-cpp/riemapp/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/riemapp/badge/?version=latest)](https://riemapp.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Saransh-cpp/riemapp/main.svg)](https://results.pre-commit.ci/latest/github/Saransh-cpp/riemapp/main)
[![codecov](https://codecov.io/gh/Saransh-cpp/riemapp/branch/main/graph/badge.svg?token=L6ObHKhaZ7)](https://codecov.io/gh/Saransh-cpp/riemapp)
[![discussion](https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github)](https://github.com/Saransh-cpp/riemapp/discussions)

[![Python Versions](https://img.shields.io/pypi/pyversions/riemapp)](https://pypi.org/project/riemapp/)
[![Package Version](https://badge.fury.io/py/riemapp.svg)](https://pypi.org/project/riemapp/)
[![Downloads](https://static.pepy.tech/badge/riemapp)](https://pepy.tech/project/riemapp)
![License](https://img.shields.io/github/license/Saransh-cpp/riemapp?color=blue)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

riemapp is a fast, easy-to-use, minimal library for Python 3.7+ that aliases
[manim](https://github.com/ManimCommunity/manim) 0.16.0+ functions for
visualising animated and intuitive complex mappings (transformations from the
real plane to the complex plane) for various shapes and real-valued functions in
two dimensions. It uses a minimum number of dependencies through
[FFmpeg](https://github.com/FFmpeg/FFmpeg) and
[pangocairo](https://gitlab.gnome.org/GNOME/pango) on Linux.

Users and learners may use riemapp to:

1. Plot (user-defined)
   - Points
   - Lines
   - Triangles
   - Squares
   - Rectangles
   - Other regular polygons
   - Circles
   - Irregular polygons
   - …and so on
2. Create smooth, precise animations for plotted figures and map them on the
   Argand plane according to user-defined complex functions.
3. Save these animations and play them in the default video player available

## Structure

- Right now, `riemapp` aliases the geometries provided by `manim` under
  `riemapp.geometry`. Users can either use these alias classes or directly use
  the `MObject`s provided by `manim`.
- `riemapp` programmatically generates `manim` animations, and the code for this
  is available under `riemapp.core`. All of the information added by a user is
  passed into a placeholder class which inherits `manim.Scene`. This class'
  object is then used to render the animation.

## Installation

### Install dependencies

**FFmpeg**

- Install FFmpeg through their [download page](https://ffmpeg.org/download.html)
  or your system's package manager (`apt`, `brew`, ...) or clone
  [Saransh-cpp/FFmpeg](https://github.com/Saransh-cpp/FFmpeg).
- Add the `bin` folder to system path.

**pangocairo** (Linux systems)

Install `libpango1.0-dev` if you are on a Linux system -

```
sudo apt-get update
sudo apt install libpango1.0-dev
```

### Install riemapp

`riemapp` uses modern `Python` packaging and can be installed using `pip` -

```
python -m pip install riemapp
```

## Usage example

```py
In [1]: import riemapp as rp
Manim Community v0.16.0.post0

In [2]: import numpy as np

In [3]: square = rp.geometry.Square(2.)

In [4]: square
Out[4]: Square(side_length=2.0) (alias for manim.Square)

In [5]: cm = rp.ComplexMap(square, lambda z: np.e ** z)

In [6]: cm
Out[6]: ComplexMap(f=Square(side_length=2.0) (alias for manim.Square), transformation=<lambda>)

In [7]: cm.generate_animation(run_time=2.)
Out[7]: Animate(f=Square(side_length=2.0) (alias for manim.Square), transformation=<lambda>)

In [8]: cm.render(preview=False)
```

https://user-images.githubusercontent.com/74055102/193077326-2c21cb9e-eb24-473e-b69c-3376f7664ecd.mp4

## Contributing

If you want to contribute to `riemapp` (thanks!), please have a look at our
[Contributing Guide](https://github.com/Saransh-cpp/riemapp/blob/main/CONTRIBUTING.md).
