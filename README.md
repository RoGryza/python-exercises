# Python Exercises

Simple static site builder for some python exercises in brazillian portuguese. Hosted at
https://aulas.rogryza.me.

## Layout

Exercises are under `ex/`, one markdown file per category. Files under `static/` are copied as-is to
the build directory.

The code to compile the src into a static website is in the `build.py` script.

## Building

Use [poetry](https://python-poetry.org/) or [pip](https://pip.pypa.io/en/stable/) to install the
dependencies:

```shellsession
$ poetry install
# or
$ pip install -r requirements.txt
```

Note that it's a good idea to be inside a virtualenv if using pip.

Then you can just run the build script while on the root of the project:

```shellsession
$ python build.py
```

The site is built under the `build/` folder.
