# riemapp

[![CI](https://github.com/Saransh-cpp/riemapp/actions/workflows/ci.yml/badge.svg)](https://github.com/Saransh-cpp/riemapp/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/riemapp/badge/?version=latest)](https://riemapp.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Saransh-cpp/riemapp/main.svg)](https://results.pre-commit.ci/latest/github/Saransh-cpp/riemapp/main)
[![codecov](https://codecov.io/gh/Saransh-cpp/riemapp/branch/main/graph/badge.svg?token=L6ObHKhaZ7)](https://codecov.io/gh/Saransh-cpp/riemapp)
[![discussion](https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github)](https://github.com/Saransh-cpp/riemapp/discussions)

[![Python Versions](https://img.shields.io/pypi/pyversions/riemapp)](https://pypi.org/project/riemapp/)
[![Package Version](https://badge.fury.io/py/riemapp.svg)](https://pypi.org/project/riemapp/)
[![PyPI Downloads](https://pepy.tech/badge/riemapp)](https://pepy.tech/project/riemapp)
![License](https://img.shields.io/github/license/Saransh-cpp/riemapp?color=blue)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

riemapp is a fast, easy-to-use, minimal library for Python 3.7+ that aliases
[manim](https://github.com/ManimCommunity/manim) 0.16.0+ functions for
visualising animated and intuitive complex mappings (transformations from the
real plane to the comple plane) for various shapes and real-valued functions in
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

TODO

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

TODO

## Contributing

If you want to contribute to `riemapp` (thanks!), please have a look at our
[Contributing Guide](https://github.com/Saransh-cpp/riemapp/blob/main/CONTRIBUTING.md).
