# Contributing guide

If you are planning to develop `riemapp`, or want to use the latest commit of
`riemapp` on your local machine, you might want to install it from the source.
This installation is not recommended for users who want to use the stable
version of `riemapp`. The steps below describe the installation process of
`riemapp`'s latest commit. It also describes how to test `riemapp`'s codebase
and build `riemapp`'s documentation.

**Note**: `riemapp` uses
[Scikit-HEP's developer information](https://scikit-hep.org/developer) as a
reference for all the development work. The guide is a general and much more
explained collection of documentation available for developing `Scikit-HEP`
packages. `riemapp` is not a `Scikit-HEP` package, but it still loosely follows
this developer guide as the guide is absolutely amazing!

## Installing

We recommend using a virtual environment to install `riemapp`. This would
isolate the library from your global `Python` environment, which would be
beneficial for reproducing bugs, and the overall development of `riemapp`. The
first step would be to clone `riemapp` -

```bash
git clone https://github.com/Scikit-hep/riemapp.git
```

and then we can change the current working directory and enter `riemapp` -

```bash
cd riemapp
```

### Creating a virtual environment

A virtual environment can be set up and activated using `venv` in both `UNIX`
and `Windows` systems.

**UNIX**:

```bash
python3 -m venv .env
. .env/bin/activate
```

**Windows**:

```bash
python -m venv .env
.env\bin\activate
```

### Installing dependencies

**FFmpeg**

- Install FFmpeg through their [download page](https://ffmpeg.org/download.html)
  or your system's package manager (`apt, `brew`, ...) or clone
  [Saransh-cpp/FFmpeg](https://github.com/Saransh-cpp/FFmpeg).
- Add the `bin` folder to system path.

**pangocairo** (Linux systems)

Install `libpango1.0-dev` if you are on a Linux system -

```bash
sudo apt-get update
sudo apt install libpango1.0-dev
```

### Installing riemapp

`riemapp` uses modern `Python` packaging and can be installed using `pip` -

```bash
python -m pip install riemapp
```

The developer installation of `riemapp` comes with a lot of options -

- `test`: the test dependencies
- `docs`: extra dependencies to build and develop `riemapp`'s documentation
- `dev`: installs the `test` and `docs` dependencies

These options can be used with `pip` with the editable (`-e`) mode of
installation in the following ways -

```bash
pip install -e .[dev,test]
```

For example, if you want to install the `docs` dependencies along with the
dependencies included above, use -

```bash
pip install -e .[dev,test,docs]
```

### Adding riemapp for notebooks

`riemapp` can be added to the notebooks using the following commands -

```bash
python -m ipykernel install --user --name riemapp
```

## Activating pre-commit

`riemapp` uses a set of `pre-commit` hooks and the `pre-commit` bot to format,
type-check, and prettify the codebase. The hooks can be installed locally
using -

```bash
pre-commit install
```

This would run the checks every time a commit is created locally. The checks
will only run on the files modified by that commit, but the checks can be
triggered for all the files using -

```bash
pre-commit run --all-files
```

If you would like to skip the failing checks and push the code for further
discussion, use the `--no-verify` option with `git commit`.

## Testing riemapp

`riemapp` is tested with `pytest` and `xdoctest`. `pytest` is responsible for
testing the code, whose configuration is available in
[pyproject.toml](https://github.com/Saransh-cpp/riemapp/blob/main/pyproject.toml),
and on the other hand, `xdoctest` is responsible for testing the examples
available in every docstring, which prevents them from going stale.
Additionally, `riemapp` also uses `pytest-cov` to calculate the coverage of
these unit tests.

### Running tests locally

The tests can be executed using the `test` dependencies of `riemapp` in the
following way -

```bash
python -m pytest
```

### Running tests with coverage locally

The coverage value can be obtained while running the tests using `pytest-cov` in
the following way -

```bash
python -m pytest --cov=riemapp tests/
```

A much more detailed guide on testing with `pytest` is available
[here](https://scikit-hep.org/developer/pytest).

## Documenting riemapp

`riemapp`'s documentation is mainly written in the form of
[docstrings](https://peps.python.org/pep-0257/) and
[Markdown](https://en.wikipedia.org/wiki/Markdown). The docstrings include the
description, arguments, examples, return values, and attributes of a class or a
function, and the `.md` files enable us to render this documentation on
`riemapp`'s documentation website.

`riemapp` primarily uses [MkDocs](https://www.mkdocs.org/) and
[mkdocstrings](https://mkdocstrings.github.io/) for rendering documentation on
its website. The configuration file (`mkdocs.yml`) for `MkDocs` can be found
[here](https://github.com/Saransh-cpp/riemapp/blob/main/mkdocs.yml). The
documentation is deployed on <https://readthedocs.io>
[here](https://riemapp.readthedocs.io/en/latest/).

Ideally, with the addition of every new feature to `riemapp`, documentation
should be added using comments, docstrings, and `.md` files.

### Building documentation locally

The documentation is located in the `docs` folder of the main repository. This
documentation can be generated using the `docs` dependencies of `riemapp` in the
following way -

```bash
mkdocs serve
```

The commands executed above will clean any existing documentation build, create
a new build (in `./site/`), and serve it on your `localhost`. To just build the
documentation, use -

```bash
mkdocs build
```

## Nox

`riemapp` supports running various critical commands using
[nox](https://github.com/wntrblm/nox) to make them less intimidating for new
developers. All of these commands (or sessions in the language of `nox`) -
`lint`, `tests`, `docs`, and `build` - are defined in
[noxfile.py](https://github.com/Saransh-cpp/riemapp/blob/main/noxfile.py).

`nox` can be installed via `pip` using -

```bash
pip install nox
```

The default sessions (`lint`, `tests`) can be executed using -

```bash
nox
```

### Running pre-commit with nox

The `pre-commit` hooks can be run with `nox` in the following way -

```bash
nox -s lint
```

### Running tests with nox

Tests can be run with `nox` in the following way -

```bash
nox -s tests
```

### Building documentation with nox

Docs can be built with `nox` in the following way -

```bash
nox -s docs
```

Use the following command if you want to deploy the docs on `localhost` -

```bash
nox -s docs -- serve
```
