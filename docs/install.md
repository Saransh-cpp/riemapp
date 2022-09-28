# Installation

Follow the steps below to install `riemapp` locally.

## Create a virtual environment

Create and activate a virtual environment

```bash
python -m venv env

. env/bin/activate
```

## Install dependencies

**FFmpeg**

- Install FFmpeg through their [download page](https://ffmpeg.org/download.html)
  or your system's package manager (`apt, `brew`, ...) or clone
  [Saransh-cpp/FFmpeg](https://github.com/Saransh-cpp/FFmpeg).
- Add the `bin` folder to system path.

**pangocairo** (Linux systems)

Install `libpango1.0-dev` if you are on a Linux system -

```
sudo apt-get update
sudo apt install libpango1.0-dev
```

## Install riemapp

`riemapp` uses modern `Python` packaging and can be installed using `pip` -

```
python -m pip install riemapp
```

## Build riemapp from source

If you want to develop `riemapp`, or use its latest commit (!can be unstable!),
you might want to install it from the source -

- Install Tesseract for your OS and add it to PATH

The installation guide is available
[here](https://tesseract-ocr.github.io/tessdoc/Installation.html)

- Clone this repository

```bash
git clone https://github.com/Saransh-cpp/riemapp
```

- Change directory

```bash
cd riemapp
```

- Install the package in editable mode with the "dev" dependencies

```bash
python -m pip install -e ".[dev]"
```

Feel free to read our
[Contributing Guide](https://github.com/Saransh-cpp/riemapp/blob/main/CONTRIBUTING.md)
for more information on developing `riemapp`.
