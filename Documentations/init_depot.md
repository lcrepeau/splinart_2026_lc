# CONFIGURATION DU PACKAGE splinart EN PARTANT DES SOURCES FOURNIS

Il s'agit à partir d'un code python fourni de préparer le package à installer.

```bash
# ALLER DANS LE REPERTOIRE DE TRAVAIL
$ cd splinart ; ls
splinart
# CODE FOURNI
splinart $ tree -f
.
├── ./compute.py
├── ./draw.py
├── ./examples
│   ├── ./examples/circle.py
│   ├── ./examples/circles.py
│   ├── ./examples/line.py
│   └── ./examples/lines.py
├── ./__init__.py
├── ./scripts
│   ├── ./scripts/cli_splinart.py
│   └── ./scripts/__init__.py
├── ./shapes
│   ├── ./shapes/base.py
│   └── ./shapes/__init__.py
└── ./spline
    ├── ./spline/__init__.py
    ├── ./spline/spline.py
    └── ./spline/splint.py
```

## DEFINITION DE L'ENVIRONNEMENT DE TRAVAIL

Nous utiliserons la commande `uv` pour le projet.

```bash
$ uv --version
uv 0.9.11
# INITIALISATION DE L'ENVIRONEMENT
$ uv init splinart
Initialized project `splinart` at `/home/lcrepeau/splinart`
$ ls
splinart
$ cd splinart
# PREPARATION D UN pyproject.toml
$ cat > pytproject.toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "splinart"# License: BSD 3 clause

dynamic = ["version"]
description = "spline art generator"
readme = "README.md"apt list --upgradable
requires-python = ">=3.13"
dependencies = [

]

[tool.setuptools.dynamic]
version = { attr = "splinart.version.__version__" }

[tool.setuptools.packages.find]
include = ["splinart*"]

[project.scripts]
splinart = "splinart.scripts.cli_splinart:main"
$
# AJOUT DES LIBRAIRIES DU PROJET ET PREPARATION DU pre-commit
$ uv run pre-commit install
      Built splinart @ file:///hoapt list --upgradableme/lcrepeau/splinart
Uninstalled 1 package in 0.50ms
Installed 1 package in 2ms
pre-commit installed at .git/hooks/pre-commit
# VERIFIER
$ ls -a
.  ..  dist  .git  .gitignore  pyproject.toml  .python-version  README.md
    splinart  splinart.egg-info  tests  uv.lock  .venv
$ uv add ruff
Resolved 13 packages in 892ms
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 2 packages in 257ms
Uninstalled 1 package in 0.40ms
Installed 2 packages in 2ms
 + ruff==0.15.17
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
# CREATION DU FICHIER
$ cat > .pre-commit-config.yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.15.14
  hooks:
    - id: ruff-check
      args: [ --fix ]
      files: ^splinart/ # Only backend folder
      stages: [pre-commit]
    - id: ruff-format
      files: ^splinart/ # Only backend folder
      stages: [pre-commit]

- repo: https://github.com/jackdewinter/pymarkdown
  rev: v0.9.37
  hooks:
    - id: pymarkdown

- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v6.0.0
  hooks:
    - id: check-yaml
    - id: check-toml
    - id: end-of-file-fixer
    - id: trailing-whitespace
# LANCEMENT DU TEST pre-commit
$ uv run pre-commit run  --all-files
ruff check...........................................(no files to check)Skipped
ruff format..........................................(no files to check)Skipped
PyMarkdown...........................................(no files to check)Skipped
check yaml...........................................(no files to check)Skipped
check toml...........................................(no files to check)Skipped
fix end of files.....................................(no files to check)Skipped
trim trailing whitespace.............................(no files to check)Skipped
$ uv add numpy
Resolved 2 packages in 874ms
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 2 packages in 425ms
Installed 2 packages in 16ms
 + numpy==2.4.6
 + splinart==0.1.0 (from file:///home/lcrepeau/splinart)
$ uv add matplotlib
Resolved 12 packages in 892ms
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 8 packages in 418ms
Uninstalled 1 package in 0.56ms
Installed 11 packages in 13ms
 + contourpy==1.3.3
 + cycler==0.12.1
 + fonttools==4.63.0
 + kiwisolver==1.5.0
 + matplotlib==3.11.0
 + packaging==26.2
 + pillow==12.2.0
 + pyparsing==3.3.2
 + python-dateutil==2.9.0.post0
 + six==1.17.0
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
$ uv add argparse
Resolved 14 packages in 816ms
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 2 packages in 232ms
Uninstalled 1 package in 0.42ms
Installed 2 packages in 3ms
 + argparse==1.4.0
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
$ uv pip freeze
argparse==1.4.0
contourpy==1.3.3
cycler==0.12.1
fonttools==4.63.0
kiwisolver==1.5.0
matplotlib==3.11.0
numpy==2.4.6
packaging==26.2
pillow==12.2.0
pyparsing==3.3.2
python-dateutil==2.9.0.post0
ruff==0.15.17
six==1.17.0
-e file:///home/lcrepeau/splinart
$ uv add pre-commit
Resolved 24 packages in 919ms
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 6 packages in 258ms
Uninstalled 1 package in 0.44ms
Installed 11 packages in 6ms
 + cfgv==3.5.0
 + distlib==0.4.3
 + filelock==3.29.4
 + identify==2.6.19
 + nodeenv==1.10.0
 + platformdirs==4.10.0
 + pre-commit==4.6.0
 + python-discovery==1.4.2
 + pyyaml==6.0.3
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
 + virtualenv==21.5.1
# TEST RUFF
$ uv run ruff check */*py
All checks passed!
# AJOUT pylint EQUIVALENT DE ruff
$ uv add pylint
Resolved 31 packages in 889ms
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 7 packages in 258ms
Uninstalled 1 package in 0.46ms
Installed 7 packages in 4ms
 + astroid==4.0.4
 + dill==0.4.1
 + isort==8.0.1
 + mccabe==0.7.0
 + pylint==4.0.6
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
 + tomlkit==0.15.0
$ uv add sphinx
Resolved 53 packages in 1.03s
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 17 packages in 328ms
Uninstalled 1 package in 1ms
Installed 22 packages in 82ms
 + alabaster==1.0.0
 + babel==2.18.0
 + certifi==2026.6.17
 + charset-normalizer==3.4.7
 + docutils==0.22.4
 + idna==3.18
 + imagesize==2.0.0
 + jinja2==3.1.6
 + markupsafe==3.0.3
 + pygments==2.20.0
 + requests==2.34.2
 + roman-numerals==4.1.0
 + snowballstemmer==3.1.1
 + sphinx==9.1.0
 + sphinxcontrib-applehelp==2.0.0
 + sphinxcontrib-devhelp==2.0.0
 + sphinxcontrib-htmlhelp==2.1.0
 + sphinxcontrib-jsmath==1.0.1
 + sphinxcontrib-qthelp==2.0.0
 + sphinxcontrib-serializinghtml==2.0.0
 - splinart==0.1.0 (from file:///home/lcrepeau/splinart)
 + splinart==0.1.0 (from file:///home/lcrepeau/splinart)
 + urllib3==2.7.0
```

## MISE AU POINT DES FICHIERS `__init.py__`

Le code est découpé en petits fichiers dans différents répertoires pour que ce
    soit clair. Il faut que le l'application sache où se trouve quoi. Il faut
    alors remplir des fichiers `__init.py__` qui setrouvent dans chaque
    répertoire. Python sait qu'il faut consulter ces fichiers pour retrouver
    ces petits ainsi que le fichier pyproject.toml à la racine du paquet. La
    mise au point se fait par étape en consultant les messages d'erreur
    générés.

```bash
# LANCEMENT DE L'APPLICATION
$ splinart
Traceback (most recent call last):
  File "/home/lcrepeau/splinart/.venv/bin/splinart", line 10, in <module>
    sys.exit(main())
             ~~~~^^
  File "/home/lcrepeau/splinart/splinart/scripts/cli_splinart.py", line 43, in main
    circle(img)
    ~~~~~~^^^^^
  File "/home/lcrepeau/splinart/splinart/scripts/cli_splinart.py", line 10, in circle
    theta, path = spl.circle([.5, .5], .3, npoints=40)
                  ^^^^^^^^^^
AttributeError: module 'splinart' has no attribute 'circle'
# LE MESSAGE INDIQUE QUE LE MODULE splinart NE TROUVE PAS LA FONCTION circle
# LA FONCTION SE TROUVE DANS LE REPERTOIRE shapes DANS LE FICHIER base.py
# PREPARATION des __init.py__
$ cat > ./splinart/shapes/__init__.py
from .base import line, circle
$ cat > ./plinart/__init__.py
from .shapes import *
# RELANCEMENT DE L'APPLICATION
$ splinart
Traceback (most recent call last):
  File "/home/lcrepeau/splinart/.venv/bin/splinart", line 10, in <module>
    sys.exit(main())
             ~~~~^^
  File "/home/lcrepeau/splinart/splinart/scripts/cli_splinart.py", line 43, in main
    circle(img)
    ~~~~~~^^^^^
  File "/home/lcrepeau/splinart/splinart/scripts/cli_splinart.py", line 11, in circle
    spl.update_img(img, path, xs_func, nrep=4000, x=theta, scale_value=.00005)
    ^^^^^^^^^^^^^^
AttributeError: module 'splinart' has no attribute 'update_img'
# ON VOIT QUE LE MESSAGE A EVOLUE ET N'EST PLUS LE MEME
# IL MANQUE DESORMAIS LA FONCTION update_img
# ELLE SE TROUVE DANS compute.py
$ cat >> ./plinart/__init__.py
from .compute import update_img
# RELANCEMENT DE L'APPLICATION
$ splinart
Traceback (most recent call last):
  File "/home/lcrepeau/splinart/.venv/bin/splinart", line 10, in <module>
    sys.exit(main())
             ~~~~^^
  File "/home/lcrepeau/splinart/splinart/scripts/cli_splinart.py", line 43, in main
    circle(img)
    ~~~~~~^^^^^
  File "/home/lcrepeau/splinart/splinart/scripts/cli_splinart.py", line 11, in circle
    spl.update_img(img, path, xs_func, nrep=4000, x=theta, scale_value=.00005)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/lcrepeau/splinart/splinart/compute.py", line 33, in update_img
    y2 = spline(x, path)
TypeError: 'module' object is not callable
# JE N'AI PAS TROUVE L'ERREUR.
# J'AI RECUPERE LE CODE SUR https://github.com/mfeingesicht/splinart-2026
```

## CONSTRUCTION DU PAQUET

```bash
$ $ uv build --sdist --wheel
Building source distribution...
running egg_info
writing splinart.egg-info/PKG-INFO
writing dependency_links to splinart.egg-info/dependency_links.txt
writing entry points to splinart.egg-info/entry_points.txt
writing requirements to splinart.egg-info/requires.txt
writing top-level names to splinart.egg-info/top_level.txt
reading manifest file 'splinart.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'splinart.egg-info/SOURCES.txt'
running sdist
running egg_info
writing splinart.egg-info/PKG-INFO
writing dependency_links to splinart.egg-info/dependency_links.txt
writing entry points to splinart.egg-info/entry_points.txt
writing requirements to splinart.egg-info/requires.txt
writing top-level names to splinart.egg-info/top_level.txt
reading manifest file 'splinart.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'splinart.egg-info/SOURCES.txt'
running check
creating splinart-0.1.0
creating splinart-0.1.0/splinart
creating splinart-0.1.0/splinart.egg-info
creating splinart-0.1.0/splinart/scripts
creating splinart-0.1.0/splinart/shapes
creating splinart-0.1.0/splinart/spline
copying files to splinart-0.1.0...
copying LICENSE -> splinart-0.1.0
copying README.md -> splinart-0.1.0
copying pyproject.toml -> splinart-0.1.0
copying splinart/__init__.py -> splinart-0.1.0/splinart
copying splinart/color.py -> splinart-0.1.0/splinart
copying splinart/compute.py -> splinart-0.1.0/splinart
copying splinart/draw.py -> splinart-0.1.0/splinart
copying splinart/version.py -> splinart-0.1.0/splinart
copying splinart.egg-info/PKG-INFO -> splinart-0.1.0/splinart.egg-info
copying splinart.egg-info/SOURCES.txt -> splinart-0.1.0/splinart.egg-info
copying splinart.egg-info/dependency_links.txt -> splinart-0.1.0/splinart.egg-info
copying splinart.egg-info/entry_points.txt -> splinart-0.1.0/splinart.egg-info
copying splinart.egg-info/requires.txt -> splinart-0.1.0/splinart.egg-info
copying splinart.egg-info/top_level.txt -> splinart-0.1.0/splinart.egg-info
copying splinart/scripts/__init__.py -> splinart-0.1.0/splinart/scripts
copying splinart/scripts/cli_splinart.py -> splinart-0.1.0/splinart/scripts
copying splinart/shapes/__init__.py -> splinart-0.1.0/splinart/shapes
copying splinart/shapes/base.py -> splinart-0.1.0/splinart/shapes
copying splinart/spline/__init__.py -> splinart-0.1.0/splinart/spline
copying splinart/spline/spline.py -> splinart-0.1.0/splinart/spline
copying splinart/spline/splint.py -> splinart-0.1.0/splinart/spline
copying splinart.egg-info/SOURCES.txt -> splinart-0.1.0/splinart.egg-info
Writing splinart-0.1.0/setup.cfg
Creating tar archive
removing 'splinart-0.1.0' (and everything under it)
Building wheel...
running egg_info
writing splinart.egg-info/PKG-INFO
writing dependency_links to splinart.egg-info/dependency_links.txt
writing entry points to splinart.egg-info/entry_points.txt
writing requirements to splinart.egg-info/requires.txt
writing top-level names to splinart.egg-info/top_level.txt
reading manifest file 'splinart.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'splinart.egg-info/SOURCES.txt'
running bdist_wheel
running build
running build_py
copying splinart/draw.py -> build/lib/splinart
copying splinart/__init__.py -> build/lib/splinart
copying splinart/color.py -> build/lib/splinart
copying splinart/compute.py -> build/lib/splinart
copying splinart/version.py -> build/lib/splinart
copying splinart/scripts/cli_splinart.py -> build/lib/splinart/scripts
copying splinart/scripts/__init__.py -> build/lib/splinart/scripts
copying splinart/spline/spline.py -> build/lib/splinart/spline
copying splinart/spline/__init__.py -> build/lib/splinart/spline
copying splinart/spline/splint.py -> build/lib/splinart/spline
copying splinart/shapes/base.py -> build/lib/splinart/shapes
copying splinart/shapes/__init__.py -> build/lib/splinart/shapes
running egg_info
writing splinart.egg-info/PKG-INFO
writing dependency_links to splinart.egg-info/dependency_links.txt
writing entry points to splinart.egg-info/entry_points.txt
writing requirements to splinart.egg-info/requires.txt
writing top-level names to splinart.egg-info/top_level.txt
reading manifest file 'splinart.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'splinart.egg-info/SOURCES.txt'
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/splinart
copying build/lib/splinart/draw.py -> build/bdist.linux-x86_64/wheel/./splinart
creating build/bdist.linux-x86_64/wheel/splinart/scripts
copying build/lib/splinart/scripts/cli_splinart.py -> build/bdist.linux-x86_64/wheel/./splinart/scripts
copying build/lib/splinart/scripts/__init__.py -> build/bdist.linux-x86_64/wheel/./splinart/scripts
creating build/bdist.linux-x86_64/wheel/splinart/spline
copying build/lib/splinart/spline/spline.py -> build/bdist.linux-x86_64/wheel/./splinart/spline
copying build/lib/splinart/spline/__init__.py -> build/bdist.linux-x86_64/wheel/./splinart/spline
copying build/lib/splinart/spline/splint.py -> build/bdist.linux-x86_64/wheel/./splinart/spline
copying build/lib/splinart/__init__.py -> build/bdist.linux-x86_64/wheel/./splinart
copying build/lib/splinart/color.py -> build/bdist.linux-x86_64/wheel/./splinart
copying build/lib/splinart/compute.py -> build/bdist.linux-x86_64/wheel/./splinart
copying build/lib/splinart/version.py -> build/bdist.linux-x86_64/wheel/./splinart
creating build/bdist.linux-x86_64/wheel/splinart/shapes
copying build/lib/splinart/shapes/base.py -> build/bdist.linux-x86_64/wheel/./splinart/shapes
copying build/lib/splinart/shapes/__init__.py -> build/bdist.linux-x86_64/wheel/./splinart/shapes
running install_egg_info
Copying splinart.egg-info to build/bdist.linux-x86_64/wheel/./splinart-0.1.0-py3.13.egg-info
running install_scripts
creating build/bdist.linux-x86_64/wheel/splinart-0.1.0.dist-info/WHEEL
creating '/home/lcrepeau/splinart/dist/.tmp-ewl1wniq/splinart-0.1.0-py3-none-any.whl'
    and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'splinart/__init__.py'
adding 'splinart/color.py'
adding 'splinart/compute.py'
adding 'splinart/draw.py'
adding 'splinart/version.py'
adding 'splinart/scripts/__init__.py'
adding 'splinart/scripts/cli_splinart.py'
adding 'splinart/shapes/__init__.py'
adding 'splinart/shapes/base.py'
adding 'splinart/spline/__init__.py'
adding 'splinart/spline/spline.py'
adding 'splinart/spline/splint.py'
adding 'splinart-0.1.0.dist-info/licenses/LICENSE'
adding 'splinart-0.1.0.dist-info/METADATA'
adding 'splinart-0.1.0.dist-info/WHEEL'
adding 'splinart-0.1.0.dist-info/entry_points.txt'
adding 'splinart-0.1.0.dist-info/top_level.txt'
adding 'splinart-0.1.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel
Successfully built dist/splinart-0.1.0.tar.gz
Successfully built dist/splinart-0.1.0-py3-none-any.whl
# VERIFICATION
$ tar tzvf dist/splinart-0.1.0.tar.gz
drwxr-xr-x lcrepeau/lmdpol   0 2026-06-17 15:43 splinart-0.1.0/
-rw-r--r-- lcrepeau/lmdpol 1512 2026-06-17 13:17 splinart-0.1.0/LICENSE
-rw-r--r-- lcrepeau/lmdpol 1716 2026-06-17 15:43 splinart-0.1.0/PKG-INFO
-rw-r--r-- lcrepeau/lmdpol  352 2026-06-17 13:40 splinart-0.1.0/README.md
-rw-r--r-- lcrepeau/lmdpol 1950 2026-06-17 15:42 splinart-0.1.0/pyproject.toml
-rw-r--r-- lcrepeau/lmdpol   38 2026-06-17 15:43 splinart-0.1.0/setup.cfg
drwxr-xr-x lcrepeau/lmdpol    0 2026-06-17 15:43 splinart-0.1.0/splinart/
-rw-r--r-- lcrepeau/lmdpol  275 2026-06-17 15:07 splinart-0.1.0/splinart/__init__.py
-rw-r--r-- lcrepeau/lmdpol  196 2026-06-17 13:17 splinart-0.1.0/splinart/color.py
-rw-r--r-- lcrepeau/lmdpol 3165 2026-06-17 15:10 splinart-0.1.0/splinart/compute.py
-rw-r--r-- lcrepeau/lmdpol 1927 2026-06-17 15:14 splinart-0.1.0/splinart/draw.py
drwxr-xr-x lcrepeau/lmdpol    0 2026-06-17 15:43 splinart-0.1.0/splinart/scripts/
-rw-r--r-- lcrepeau/lmdpol   80 2026-06-17 13:17 splinart-0.1.0/splinart/scripts/__init__.py
-rw-r--r-- lcrepeau/lmdpol 1950 2026-06-17 13:17 splinart-0.1.0/splinart/scripts/cli_splinart.py
drwxr-xr-x lcrepeau/lmdpol    0 2026-06-17 15:43 splinart-0.1.0/splinart/shapes/
-rw-r--r-- lcrepeau/lmdpol  163 2026-06-17 13:17 splinart-0.1.0/splinart/shapes/__init__.py
-rw-r--r-- lcrepeau/lmdpol 1319 2026-06-17 13:17 splinart-0.1.0/splinart/shapes/base.py
drwxr-xr-x lcrepeau/lmdpol    0 2026-06-17 15:43 splinart-0.1.0/splinart/spline/
-rw-r--r-- lcrepeau/lmdpol  189 2026-06-17 13:17 splinart-0.1.0/splinart/spline/__init__.py
-rw-r--r-- lcrepeau/lmdpol 1042 2026-06-17 13:17 splinart-0.1.0/splinart/spline/spline.py
-rw-r--r-- lcrepeau/lmdpol 1057 2026-06-17 13:17 splinart-0.1.0/splinart/spline/splint.py
-rw-r--r-- lcrepeau/lmdpol   47 2026-06-17 15:43 splinart-0.1.0/splinart/version.py
drwxr-xr-x lcrepeau/lmdpol    0 2026-06-17 15:43 splinart-0.1.0/splinart.egg-info/
-rw-r--r-- lcrepeau/lmdpol 1716 2026-06-17 15:43 splinart-0.1.0/splinart.egg-info/PKG-INFO
-rw-r--r-- lcrepeau/lmdpol  516 2026-06-17 15:43 splinart-0.1.0/splinart.egg-info/SOURCES.txt
-rw-r--r-- lcrepeau/lmdpol    1 2026-06-17 15:43 splinart-0.1.0/splinart.egg-info/dependency_links.txt
-rw-r--r-- lcrepeau/lmdpol   64 2026-06-17 15:43 splinart-0.1.0/splinart.egg-info/entry_points.txt
-rw-r--r-- lcrepeau/lmdpol   80 2026-06-17 15:43 splinart-0.1.0/splinart.egg-info/requires.txt
-rw-r--r-- lcrepeau/lmdpol    9 2026-06-17 15:43 splinart-0.1.0/splinart.egg-info/top_level.txt
```

## Analyse de code statique

Installation des paquets `ruff` et `pylint` pour les comparer.

```bash
$ cd splinart
splinart$ ls
color.py  compute.py  draw.py  __init__.py  __pycache__  scripts  shapes
    spline  version.py

splinart$ ruff check color.py --select ALL
All checks passed!
splinart$ ruff format color.py
1 file left unchanged
$ cat color.py
# Author:
#     Loic Gouarin <loic.gouarin@gmail.com>
#
# License: BSD 3 clause
"""Define the default color of the output."""

DEFAULT_COLOR = (0.0, 0.41568627450980394, 0.61960784313725492, 1.0)
```

## Faire la doc de son projet

```bash
$ cd splinart
splinart$
# INSTALLER sphinx
splinart$ uv add sphinx
...
# CREER UN REPERTOIRE docs
splinart$ mkdir doc ; cd docs
# AJOUTER LIBRAIRIE
$ uv add numpydoc
warning: `VIRTUAL_ENV=/home/lcrepeau/formations/tests_python/TPs/1.packaging/
   step0/splinart/.venv` does not match the project environment path
   `/home/lcrepeau/splinart/.venv` and will be ignored; use `--active` to target
   the active environment instead
Resolved 82 packages in 1.02s
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 2 packages in Package255ms
Uninstalled 1 package in 0.54ms
Installed 2 packages in 3ms
 + numpydoc==1.10.0
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
# AJOUTER LIBRAIRIE
$ uv add myst_parser
warning: `VIRTUAL_ENV=/home/lcrepeau/formations/tests_python/TPs/1.packaging/
   step0/splinart/.venv` does not match the project environment path
   `/home/lcrepeau/splinart/.venv` and will be ignored; use `--active` to target
   the active environment instead
Resolved 86 packages in 918ms
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 5 packages in 259ms
Uninstalled 1 package in 0.54ms
Installed 5 packages in 6ms
 + markdown-it-py==4.2.0
 + mdit-py-plugins==0.6.1
 + mdurl==0.1.2
 + myst-parser==5.1.0
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
# AJOUTER LIBRAIRIE
$ uv add nbsphinx
warning: `VIRTUAL_ENV=/home/lcrepeau/formations/tests_python/TPs/1.packaging/
   step0/splinart/.venv` does not match the project environment path
   `/home/lcrepeau/splinart/.venv` and will be ignored; use `--active` to target
   the active environment instead
Resolved 80 packages in 1.26s
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 25 packages in 272ms
Uninstalled 1 package in 0.56ms
Installed 26 packages in 16ms
 + attrs==26.1.0
 + beautifulsoup4==4.15.0
 + bleach==6.4.0
 + defusedxml==0.7.1
 + fastjsonschema==2.21.2
 + jsonschema==4.26.0
 + jsonschema-specifications==2025.9.1
 + jupyter-client==8.9.1
 + jupyter-core==5.9.1
 + jupyterlab-pygments==0.3.0
 + mistune==3.2.1
 + nbclient==0.11.0
 + nbconvert==7.17.1
 + nbformat==5.10.4
 + nbsphinx==0.9.8
 + pandocfilters==1.5.1
 + pyzmq==27.1.0
 + referencing==0.37.0
 + rpds-py==2026.5.1
 + soupsieve==2.8.4
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
 + tinycss2==1.5.1
 + tornado==6.5.7
 + traitlets==5.15.1
 + typing-extensions==4.15.0
 + webencodings==0.5.1
 $ uv add nbsphinx-link
Resolved 81 packages in 1.06s
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 2 packages in 240ms
Uninstalled 1 package in 0.51ms
Installed 2 packages in 3ms
 + nbsphinx-linkLoic Gouarin==1.4.1
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
# INITIALISER LE PROJET DOCUMENTATIONS EN REPONDANT AUX QUESTIONS
$ uv run sphinx-quickstart
Bienvenue dans le kit de démarrage rapide de Sphinx 9.1.0.

Veuillez saisir des valeurs pour les paramètres suivants (tapez Entrée pour
 accepter la valeur par défaut, lorsque celle-ci est indiquée entre crochets).

Chemin racine sélectionné : .

Vous avez deux options pour l'emplacement du répertoire de construction de la
    sortie de Sphinx.  Soit vous utilisez un répertoire "_build" dans le chemin
    racine, soit vous séparez les répertoires "source" et "build" dans le
    chemin racine.
> Séparer les répertoires source et de sortie (y/n) [n]: y

Le nom du projet apparaîtra à plusieurs endroits dans la documentation
    construite.
> Nom du projet: Splinart 2026
> Nom(s) de(s) l'auteur(s): Loic Gouarin
> Version du projet []: 0.1.0

Si les documents doivent être rédigés dans une langue autre que l’anglais,
    vous pouvez sélectionner une langue ici grâce à son identifiant. Sphinx
    utilisera ensuite cette langue pour traduire les textes que lui-même génère.

Pour une liste des identifiants supportés, voir
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Langue du projet [en]: fr

Fichier en cours de création /home/lcrepeau/splinart/docs/source/conf.py.
Fichier en cours de création /home/lcrepeau/splinart/docs/source/index.rst.
Fichier en cours de création /home/lcrepeau/splinart/docs/Makefile.
Fichier en cours de création /home/lcrepeau/splinart/docs/make.bat.

Terminé : la structure initiale a été créée.

Vous devez maintenant compléter votre fichier principal
    /home/lcrepeau/splinart/docs/source/index.rst et créer d'autres fichiers
    sources de documentation. Utilisez le Makefile pour construire la
    documentation comme ceci :
    make builder
    où « builder » est l'un des constructeurs disponibles, tel que html,
    latex, ou linkcheck.
$ ls
build  make.bat  Makefile  source
docs$ tree -f
.
├── ./build
├── ./make.bat
├── ./Makefile
└── ./source
    ├── ./source/conf.py
    ├── ./source/index.rst
    ├── ./source/_static
    └── ./source/_templates

5 directories, 4 files
# GENERER LA DOC EN FICHIER rst
cd ..
$ uv run --active sphinx-apidoc -f -o docs/source/api splinart
# VERIFICATIONS
$ tree -f docs/source
.
├── ./api
│   ├── ./api/modules.rst
│   ├── ./api/splinart.rst
│   ├── ./api/splinart.scripts.rst
│   ├── ./api/splinart.shapes.rst
│   └── ./api/splinart.spline.rst
├── ./conf.py
├── ./index.rst
├── ./\_static
└── ./\_templates
# FAIRE LES FICHIERS HTML A PARTIR DES FICHIERS rst CI-DESSUS
$ cd docs
docs $ ls
build  make.bat  Makefile  source
docs $ uv run make html
Sphinx v9.1.0 en cours d'exécution
chargement des traductions [fr]... fait
chargement de l'environnement pickled... La configuration a changé (2 options :
    'nbsphinx_requirejs_options', 'nbsphinx_requirejs_path')
fait
[autosummary] engendrement d’un auto-sommaire pour :
api/modules.rst,
api/splinart.rst,
api/splinart.scripts.rst,
api/splinart.shapes.rst,
api/splinart.spline.rst,
index.rst
myst v5.1.0: MdParserConfig(...)
Écriture du résultat du modèle évalué dans
    /home/lcrepeau/splinart/docs/build/html/_static/nbsphinx-code-cells.css
construction en cours [mo] : cibles périmées pour les fichiers po 0
écriture...
construction [html] : cibles périmées pour les fichiers sources 1
mise à jour de l'environnement : 0 ajouté(s), 1 modifié(s), 0 supprimé(s)
lecture des sources... [100%] index
recherche des fichiers périmés... aucun résultat trouvé
Environnement de sérialisation... fait
vérification de la cohérence... fait
documents en préparation... fait
copie des ressources...
Copie des fichiers statiques...
Écriture du résultat du modèle évalué dans
    /home/lcrepeau/splinart/docs/build/html/_static/documentation_options.js
Écriture du résultat du modèle évalué dans
    /home/lcrepeau/splinart/docs/build/html/_static/language_data.js
Écriture du résultat du modèle évalué dans
    /home/lcrepeau/splinart/docs/build/html/_static/basic.css
Écriture du résultat du modèle évalué dans
    /home/lcrepeau/splinart/docs/build/html/_static/alabaster.css
Copie des fichiers statiques: fait
copie des fichiers complémentaires...
copie des fichiers complémentaires: fait
copie des ressources: fait
écriture... [100%] index
génération des index... genindex py-modindex fait
copying linked files...
copying notebooks ...
Écriture des pages additionnelles... search fait
Export de l'index de recherche en French (code: fr)... fait
Export de l'inventaire des objets... fait
La compilation a réussi.

Les pages HTML sont dans build/html.
# VERIFICATIONS
docs $ cd build
docs/build $ tree -f html
html
├── html/api
│   ├── html/api/modules.html
│   ├── html/api/splinart.html
│   ├── html/api/splinart.scripts.html
│   ├── html/api/splinart.shapes.html
│   └── html/api/splinart.spline.html
├── html/genindex.html
├── html/index.html
├── html/objects.inv
├── html/py-modindex.html
├── html/search.html
├── html/searchindex.js
├── html/\_sources
│   ├── html/\_sources/api
│   │   ├── html/\_sources/api/modules.rst.txt
│   │   ├── html/\_sources/api/splinart.rst.txt
│   │   ├── html/\_sources/api/splinart.scripts.rst.txt
│   │   ├── html/\_sources/api/splinart.shapes.rst.txt
│   │   └── html/\_sources/api/splinart.spline.rst.txt
│   └── html/\_sources/index.rst.txt
└── html/\_static
    ├── html/\_static/alabaster.css
    ├── html/\_static/base-stemmer.js
    ├── html/\_static/basic.css
    ├── html/\_static/custom.css
    ├── html/\_static/doctools.js
    ├── html/\_static/documentation_options.js
    ├── html/\_static/file.png
    ├── html/\_static/french-stemmer.js
    ├── html/\_static/github-banner.svg
    ├── html/\_static/language_data.js
    ├── html/\_static/minus.png
    ├── html/\_static/nbsphinx-broken-thumbnail.svg
    ├── html/\_static/nbsphinx-code-cells.css
    ├── html/\_static/nbsphinx-gallery.css
    ├── html/\_static/nbsphinx-no-thumbnail.svg
    ├── html/\_static/plus.png
    ├── html/\_static/pygments.css
    ├── html/\_static/searchtools.js
    ├── html/\_static/sphinx_highlight.js
    └── html/\_static/translations.js

5 directories, 37 files

docs/build $ cd ../source
# VERIFICATION conf.py
docs/source $ cat conf.py
"""Configuration file for the Sphinx documentation builder."""  # noqa: INP001
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "Splinart 2026"
copyright = "2026, Loic Gouarin"  # noqa: A001
author = "Loic Gouarin"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#

extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "myst_parser",
    "nbsphinx",
    "nbsphinx_link",
]

templates\_path = ["\_templates"]
exclude\_patterns = ["**.ipynb_checkpoints"]

language = "fr"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#

html_theme = "alabaster"
html_static_path = ["_static"]
# VERIFICATION ndex.rst
docs/source $ cat index.rst
.. Splinart 2026 documentation master file, created by
   sphinx-quickstart on Fri Jun 19 16:43:28 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Splinart 2026 documentation
===========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api/modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

### VISUALISATIONS CREEES PAR sphinx

#### HOME

![graph][internal-source1]

[internal-source1]: images/sphinx_splinart_home.png 'Home'

#### INDEX

![graph][internal-source2]

[internal-source2]: images/sphinx_splinart_index.png 'index'

### INDEX DU PACKAGE

![graph][internal-source3]

[internal-source3]: images/sphinx_splinart_index_module.png 'index du package'

### PAGE DE RECHERCHE

![graph][internal-source4]

[internal-source4]: images/sphinx_splinart_recherche.png 'Recherche'

#### PAGE DU CLI

![graph][internal-source5]

[internal-source5]: images/sphinx_splinart_scripts_cli_splinart.png 'Cli'

#### PAGE DU PACKAGE

![graph][internal-source6]

[internal-source6]: images/sphinx_splinart_package.png 'Package'

#### INDEX DES PAGES

![graph][internal-source7]

[internal-source7]: images/sphinx_splinart.png 'Index des pages'

### ESSAI A PARTIR DE FICHIERS markdown AU LIEU DE rst

```bash
# CREATION D'UN REPERTOIRE DEDIE
$ mkdir docs_md ; cd docs_md
# INITIALISER LE DEPOT SPHINX
docs_md $ uv run sphinx-quickstart --suffix md --no-batchfile
Bienvenue dans le kit de démarrage rapide de Sphinx 9.1.0.

Veuillez saisir des valeurs pour les paramètres suivants (tapez Entrée pour
    accepter la valeur par défaut, lorsque celle-ci est indiquée entre crochets
    ).

Chemin racine sélectionné : .

Vous avez deux options pour l'emplacement du répertoire de construction de
    la sortie de Sphinx.
Soit vous utilisez un répertoire "_build" dans le chemin racine, soit vous
    séparez les répertoires "source" et "build" dans le chemin racine.
> Séparer les répertoires source et de sortie (y/n) [n]: y

Le nom du projet apparaîtra à plusieurs endroits dans la documentation
    construite.
> Nom du projet: splinart lc 2026
> Nom(s) de(s) l'auteur(s): Loic Gouarin
> Version du projet []: 0.1.0

Si les documents doivent être rédigés dans une langue autre que l’anglais,
    vous pouvez sélectionner une langue ici grâce à son identifiant. Sphinx
    utilisera ensuite cette langue pour traduire les textes que lui-même génère.

Pour une liste des identifiants supportés, voir
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Langue du projet [en]: fr

Fichier en cours de création /home/lcrepeau/splinart/docs_md/source/conf.py.
Fichier en cours de création /home/lcrepeau/splinart/docs_md/source/index.rst.
Fichier en cours de création /home/lcrepeau/splinart/docs_md/Makefile.

Terminé : la structure initiale a été créée.

Vous devez maintenant compléter votre fichier principal
    /home/lcrepeau/splinart/docs_md/source/index.rst et créer d'autres
    fichiers sources de documentation. Utilisez le Makefile pour construire
    la documentation comme ceci :
    make builder
    où « builder » est l'un des constructeurs disponibles, tel que html,
    latex, ou linkcheck.
# PREPARER LES FICHIERS DU CODE
$ uv run --active sphinx-apidoc -f -o docs_md/source/api -s md splinart
# VERFICATIONS DE CE QUI A ETE CREE
docs_md $ tree -f
.
├── ./build
├── ./Makefile
└── ./source
    ├── ./source/api
    │   ├── ./source/api/modules.md
    │   ├── ./source/api/splinart.md
    │   ├── ./source/api/splinart.scripts.md
    │   ├── ./source/api/splinart.shapes.md
    │   └── ./source/api/splinart.spline.md
    ├── ./source/conf.py
    ├── ./source/index.rst
    ├── ./source/_static
    └── ./source/_templates

6 directories, 8 files
# GENERE LE HTML A PARTIR DES FICHIERS CI-DESSUS
cd docs_md
# AJOUT DE DES LIBRAIRIES PYTHON
$ uv add Pygments
Resolved 90 packages in 1.00s
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 1 package in 260ms
Uninstalled 1 package in 0.60ms
Installed 1 package in 2ms
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
# AJOUT DE l'OUTIL sphinx-autobuild POUR VISUALISER LES MISES A JOUR EN DIRECT
$  uv add sphinx-autobuild
Resolved 98 packages in 1.01s
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 9 packages in 323ms
Uninstalled 1 package in 0.68ms
Installed 10 packages in 11ms
 + anyio==4.14.0
 + click==8.4.1
 + colorama==0.4.6
 + h11==0.16.0
 + sphinx-autobuild==2025.8.25
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
 + starlette==1.3.1
 + uvicorn==0.49.0
 + watchfiles==1.2.0
 + websockets==16.0
 # EXTENSION POUR LIRE LES FORMULES MATHEMATIQUES
 $ uv add sphinx-math-dollar
Resolved 103 packages in 1.10s
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 2 packages in 236ms
Uninstalled 1 package in 0.55ms
Installed 2 packages in 3ms
 + sphinx-math-dollar==1.3
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)

```

#### LANCEMENT DE L'AUTOBUILD

Un serveur web est lancé et on peut suivre les mises à jour de la conf ou des
    pages en direct sur une adresse locale en http::127.0.1:8000. Un `^C` dans
    la fenêtre permet d'arrêter le serveur web.

```bash
cd docs_md
docs_md$ ls
build  Makefile  source
docs_md$ uv run sphinx-autobuild source build/html
[sphinx-autobuild] Starting initial build
[sphinx-autobuild] > python -m sphinx build source build/html
Sphinx v9.1.0 en cours d'exécution
chargement des traductions [fr]... fait
Conversion de  `source_suffix = '.md'` en `source_suffix = {'.md': 'restructuredtext'}`.
myst v5.1.0: MdParserConfig(...)
[autosummary] engendrement d’un auto-sommaire pour :
api/modules.md,
api/splinart.md,
api/splinart.scripts.md,
api/splinart.shapes.md,
api/splinart.spline.md,
index.md
Écriture du résultat du modèle évalué dans
    docs_md/build/html/_static/nbsphinx-code-cells.css
construction en cours [mo] : cibles périmées pour les fichiers po 0
écriture...
construction [html] : cibles périmées pour les fichiers sources 6
mise à jour de l'environnement : [nouvelle configuration] 6 ajouté(s),
    0 modifié(s), 0 supprimé(s)
lecture des sources... [100%] index
<unknown>:1: WARNING: description dupliquée de l'objet splinart.spline.splint,
    autre instance dans api/splinart.spline, utiliser :no-index: pour l'un d'eux
recherche des fichiers périmés... aucun résultat trouvé
Environnement de sérialisation... fait
vérification de la cohérence... docs_md/source/api/splinart.md: document
    référencé dans plusieurs arborescences : ['api/modules', 'index'],
    sélectionnant : index <- api/splinart
docs_md/source/api/splinart.scripts.md: document référencé dans plusieurs
    arborescences : ['api/splinart', 'index'], sélectionnant : index <-
    api/splinart.scripts
docs_md/source/api/splinart.shapes.md: document référencé dans plusieurs
    arborescences : ['api/splinart', 'index'], sélectionnant : index <-
    api/splinart.shapes
docs_md/source/api/splinart.spline.md: document référencé dans plusieurs
    arborescences : ['api/splinart', 'index'], sélectionnant : index <-
    api/splinart.spline
fait
documents en préparation... fait
copie des ressources...
Copie des fichiers statiques...
Écriture du résultat du modèle évalué dans
    docs_md/build/html/_static/documentation_options.js
Écriture du résultat du modèle évalué dans
    docs_md/build/html/_static/language_data.js
Écriture du résultat du modèle évalué dans
    docs_md/build/html/_static/basic.css
Écriture du résultat du modèle évalué dans
    docs_md/build/html/_static/alabaster.css
Copie des fichiers statiques: fait
copie des fichiers complémentaires...
copie des fichiers complémentaires: fait
copie des ressources: fait
écriture... [100%] index
génération des index... genindex py-modindex fait
copying linked files...
copying notebooks ...
Écriture des pages additionnelles... search fait
Export de l'index de recherche en French (code: fr)... fait
Export de l'inventaire des objets... fait
La compilation a réussi, 1 avertissement.

Les pages HTML sont dans build/html.
[sphinx-autobuild] Serving on http://127.0.0.1:8000
[sphinx-autobuild] Waiting to detect changes...
^C
docs_md $
```

#### MODIFICATIONS DES FICHIERS MD

Les fichiers ci-dessous contennaient des consignes shpinx qui étaient
    affichées directement genre "..automodule" dans la page générée. Il a
    fallu englober toutes les consignes par des balises pour qu'elles soient
    interprétées.

```bash
docs_md $ tree -f
.
├── ./build
├── ./Makefile
└── ./source
    ├── ./source/api
    │   ├── ./source/api/modules.md
    │   ├── ./source/api/splinart.md
    │   ├── ./source/api/splinart.scripts.md
    │   ├── ./source/api/splinart.shapes.md
    │   └── ./source/api/splinart.spline.md
    ├── ./source/conf.py
    ├── ./source/index.rst
    ├── ./source/_static
    └── ./source/_templates

6 directories, 8 files
```

#### EXEMPLE

Dans la page source/api/modules.md nous avions :

``````bash
splinart
========

.. toctree::
   :maxdepth: 4

   splinart
# APRES MODIFICATION
splinart
========

```{eval-rst}
.. toctree::
   :maxdepth: 4

   splinart
```
``````

C'est à faire pour toutes les consignes sphinx dans tous les fichiers :

* source/index.md
* source/api/splinart.spline.md
* source/api/modules.md
* source/api/splinart.shapes.md
* source/api/splinart.md
* source/api/splinart.scripts.md

#### ENSUITE ON RELANCE LA GENERATION DES PAGES HTML

```bash
docs_md$ uv run make html
Sphinx v9.1.0 en cours d'exécution
chargement des traductions [fr]... fait
Conversion de  `source_suffix = '.md'` en `source_suffix = {'.md':
    'restructuredtext'}`.
chargement de l'environnement pickled... La configuration a changé (2 options :
    'nbsphinx_requirejs_options', 'nbsphinx_requirejs_path')
fait
myst v5.1.0: MdParserConfig(...)
[autosummary] engendrement d’un auto-sommaire pour :
api/modules.md,
 api/splinart.md,
 api/splinart.scripts.md,
 api/splinart.shapes.md,
 api/splinart.spline.md, index.md
Écriture du résultat du modèle évalué dans
    docs_md/build/html/_static/nbsphinx-code-cells.css
construction en cours [mo] : cibles périmées pour les fichiers po 0
écriture...
construction [html] : cibles périmées pour les fichiers sources 0
mise à jour de l'environnement : 0 ajouté(s), 0 modifié(s), 0 supprimé(s)
lecture des sources...
recherche des fichiers périmés... aucun résultat trouvé
aucune cible n'est périmée.
documents en préparation... fait
copie des ressources...
Copie des fichiers statiques...
Écriture du résultat du modèle évalué dans
    docs_md/build/html/_static/documentation_options.js
Écriture du résultat du modèle évalué dans
    docs_md/build/html/_static/language_data.js
Écriture du résultat du modèle évalué dans
    docs_md/build/html/_static/basic.css
Écriture du résultat du modèle évalué dans
    docs_md/build/html/_static/alabaster.css
Copie des fichiers statiques: fait
copie des fichiers complémentaires...
copie des fichiers complémentaires: fait
copie des ressources: fait
génération des index... genindex py-modindex fait
copying linked files...
copying notebooks ...
Écriture des pages additionnelles... search fait
Export de l'index de recherche en French (code: fr)... fait
Export de l'inventaire des objets... fait
La compilation a réussi.

Les pages HTML sont dans build/html
# ON VERIFIE AVEC LE NAVIGATEUR
```

### FICHIERS DE CONF

``````bash
# FICHIER conf.py
docs_md $ cat source/conf.py
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#

project = "Splinart lc 2026"
copyright = "2026, Loic Gouarin"
author = "Loic Gouarin"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#

extensions = ["myst_parser",
    "sphinx.ext.autodoc",
    "numpydoc",
    "nbsphinx",
    "nbsphinx_link",
        ]

templates_path = ["_templates"]
exclude_patterns = ["**.ipynb_checkpoints"]

source_suffix = ".md"
language = "fr"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#

html_theme = "alabaster"
html_static_path = ["_static"]
# INTERPRETATION DES FORMULES MATHEMATIQUES
myst_enable_extensions = ["dollarmath", "amsmath"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
# FICHIER index.md
docs_md $ cat source/index.md
# Splinart lc 2026 documentation

## User manual

```{toctree}
:maxdepth: 2

spline
```

## Index

```{eval-rst}
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```
## Tutorial

```{toctree}
:maxdepth: 2

notebooks/circle
```

## Reference manual


```{toctree}
   :maxdepth: 2
   :caption: Contents:

api/modules.md
api/splinart.md
api/splinart.scripts.md
api/splinart.shapes.md
api/splinart.spline.md
```

``````

### VISUALISATIONS CREEES PAR sphinx A PARTIR DES md

#### HOME md

![graph][internal-sourcemd1]

[internal-sourcemd1]: images/sphinx_splinart_home_md.png 'Home'

#### INDEX md

![graph][internal-sourcemd2]

[internal-sourcemd2]: images/sphinx_splinart_index_md.png 'index'

### INDEX DU PACKAGE md

![graph][internal-sourcemd3]

[internal-sourcemd3]: images/sphinx_splinart_index_module_md.png 'package'

### PAGE DE RECHERCHE md

![graph][internal-sourcemd4]

[internal-sourcemd4]: images/sphinx_splinart_recherche_md.png 'Recherche'

#### PAGE DU CLI md

![graph][internal-sourcemd5]

[internal-sourcemd5]: images/sphinx_splinart_scripts_cli_splinart_md.png 'Cli'

#### PAGE DU PACKAGE md

![graph][internal-sourcemd6]

[internal-sourcemd6]: images/sphinx_splinart_package_md.png 'Package'

#### INDEX DES PAGES md

![graph][internal-sourcemd7]

[internal-sourcemd7]: images/sphinx_splinart_md.png 'Index des pages'

#### PAGE THEORIE md

![graph][internal-sourcemd8]

[internal-sourcemd8]: images/sphinx_splinart_cubic_spline_md.png 'Théorie'

#### NOTEBOOK md

![graph][internal-sourcemd9]

[internal-sourcemd9]: images/sphinx_splinart_notebook_md.png 'Notebooks'

## TESTER l'APPLICATION splinart

### INSTALLATION DES LIBRAIRIES

L'extension pytest pytest-cov sert pour calculer la couverture des tests.
    L'extension pytest pytest-mpl sert à comparer des images matplotlib.

```bash
# AJOUT
$ uv add pytest-cov pytest-mpl
```

### FAIRE LES TESTS

```bash
# PROGRAMMES DE TESTS UNITAIRES
$ tree -f tests
tests
├── tests/baseline
│   └── tests/baseline/test_circle_case.png
├── tests/test_all.py
├── tests/test_shape.py
└── tests/test_spline.py
# LANCEMENT DU PREMIER TEST
$ uv run pytest -v tests/test_all.py
==================================== test session starts =======================
platform linux -- Python 3.13.5, pytest-9.1.1, pluggy-1.6.0 --
   /home/lcrepeau/.venv/bin/python3
cachedir: .pytest_cache
Matplotlib: 3.11.0
Freetype: 2.14.3
rootdir: /home/lcrepeau/splinart
configfile: pyproject.toml
plugins: mpl-0.19.0, cov-7.1.0, anyio-4.14.0
collected 1 item

tests/test_all.py::test_circle_case PASSED                                [100%]

==================================== 1 passed in 3.64s =========================
# LANCEMENT DU DEUXIEME TEST
$ uv run pytest -v tests/test_shape.py
==================================== test session starts =======================
platform linux -- Python 3.13.5, pytest-9.1.1, pluggy-1.6.0 --
    /home/lcrepeau/.venv/bin/python3
cachedir: .pytest_cache
Matplotlib: 3.11.0
Freetype: 2.14.3
rootdir: /home/lcrepeau/splinart
configfile: pyproject.toml
plugins: mpl-0.19.0, cov-7.1.0, anyio-4.14.0
collected 8 items

tests/test_shape.py::test_circle_1 PASSED                                 [ 12%]
tests/test_shape.py::test_circle_2 PASSED                                 [ 25%]
tests/test_shape.py::test_line_1 PASSED                                   [ 37%]
tests/test_shape.py::test_line_2 PASSED                                   [ 50%]
tests/test_shape.py::test_circle[2-expected0] PASSED                      [ 62%]
tests/test_shape.py::test_circle[5-expected1] PASSED                      [ 75%]
tests/test_shape.py::test_line[2-expected0] PASSED                        [ 87%]
tests/test_shape.py::test_line[3-expected1] PASSED                        [100%]

==================================== 8 passed in 0.46s =========================
# LANCEMENT DU TROISIEME TEST
$ uv run pytest -v tests/test_spline.py
==================================== test session starts =======================
platform linux -- Python 3.13.5, pytest-9.1.1, pluggy-1.6.0 --
    /home/lcrepeau/.venv/bin/python3
cachedir: .pytest_cache
Matplotlib: 3.11.0
Freetype: 2.14.3
rootdir: /home/lcrepeau/splinart
configfile: pyproject.toml
plugins: mpl-0.19.0, cov-7.1.0, anyio-4.14.0
collected 18 items

tests/test_spline.py::test_spline[10-0-1] PASSED                          [  5%]
tests/test_spline.py::test_spline[10--2--1] PASSED                        [ 11%]
tests/test_spline.py::test_spline[10--20-10] PASSED                       [ 16%]
tests/test_spline.py::test_spline[20-0-1] PASSED                          [ 22%]
tests/test_spline.py::test_spline[20--2--1] PASSED                        [ 27%]
tests/test_spline.py::test_spline[20--20-10] PASSED                       [ 33%]
tests/test_spline.py::test_spline[30-0-1] PASSED                          [ 38%]
tests/test_spline.py::test_spline[30--2--1] PASSED                        [ 44%]
tests/test_spline.py::test_spline[30--20-10] PASSED                       [ 50%]
tests/test_spline.py::test_spline_circle[10-center0-1] PASSED             [ 55%]
tests/test_spline.py::test_spline_circle[10-center1-0.1] PASSED           [ 61%]
tests/test_spline.py::test_spline_circle[10-center2-0.3] PASSED           [ 66%]
tests/test_spline.py::test_spline_circle[20-center0-1] PASSED             [ 72%]
tests/test_spline.py::test_spline_circle[20-center1-0.1] PASSED           [ 77%]
tests/test_spline.py::test_spline_circle[20-center2-0.3] PASSED           [ 83%]
tests/test_spline.py::test_spline_circle[30-center0-1] PASSED             [ 88%]
tests/test_spline.py::test_spline_circle[30-center1-0.1] PASSED           [ 94%]
tests/test_spline.py::test_spline_circle[30-center2-0.3] PASSED           [100%]

==================================== 18 passed in 0.50s ========================
# LANCEMENT DE COUVERTURE DE L'APPLI splinart DES TESTS
$ uv run pytest --cov=splinart tests/
==================================== test session starts =======================
platform linux -- Python 3.13.5, pytest-9.1.1, pluggy-1.6.0
Matplotlib: 3.11.0
Freetype: 2.14.3
rootdir: /home/lcrepeau/splinart
configfile: pyproject.toml
plugins: mpl-0.19.0, cov-7.1.0, anyio-4.14.0
collected 27 items

tests/test_all.py .                                                       [  3%]
tests/test_shape.py ........                                              [ 33%]
tests/test_spline.py ..................                                   [100%]

==================================== tests coverage ============================
________________________ coverage: platform linux, python 3.13.5-final-0 _______

Name                                   Stmts   Miss  Cover
----------------------------------------------------------
src/splinart/__init__.py                   4      0   100%
src/splinart/color.py                      1      0   100%
src/splinart/compute.py                   30      4    87%
src/splinart/draw.py                      27      9    67%
src/splinart/scripts/__init__.py           0      0   100%
src/splinart/scripts/cli_splinart.py      31     31     0%
src/splinart/shapes/__init__.py            2      0   100%
src/splinart/shapes/base.py                9      0   100%
src/splinart/spline/__init__.py            3      0   100%
src/splinart/spline/spline.py             18      0   100%
src/splinart/spline/splint.py             13      0   100%
src/splinart/version.py                    1      1     0%
----------------------------------------------------------
TOTAL                                    139     45    68%
==================================== 27 passed in 4.51s ========================
```

## FAIRE UN PAQUET

Faire le test que la création du paquet splinart fonctionne toujours suite aux
    différentes étapes.

```bash
$ uv build --sdist --wheel
Building source distribution...
running egg_info
writing src/splinart.egg-info/PKG-INFO
writing dependency_links to src/splinart.egg-info/dependency_links.txt
writing entry points to src/splinart.egg-info/entry_points.txt
writing requirements to src/splinart.egg-info/requires.txt
writing top-level names to src/splinart.egg-info/top_level.txt
reading manifest file 'src/splinart.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'src/splinart.egg-info/SOURCES.txt'
running sdist
running egg_info
writing src/splinart.egg-info/PKG-INFO
writing dependency_links to src/splinart.egg-info/dependency_links.txt
writing entry points to src/splinart.egg-info/entry_points.txt
writing requirements to src/splinart.egg-info/requires.txt
writing top-level namesDocumentations/init_depot.md to src/splinart.egg-info/top_level.txt
reading manifest file 'src/splinart.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'src/splinart.egg-info/SOURCES.txt'
running check
creating splinart-0.1.0
creating splinart-0.1.0/src/splinart
creating splinart-0.1.0/src/splinart.egg-info
creating splinart-0.1.0/tests
copying files to splinart-0.1.0...
copying LICENSE -> splinart-0.1.0
copying README.md -> splinart-0.1.0
copying pyproject.toml -> splinart-0.1.0
copying src/splinart/__init__.py -> splinart-0.1.0/src/splinart
copying src/splinart/color.py -> splinart-0.1.0/src/splinart
copying src/splinart/compute.py -> splinart-0.1.0/src/splinart
copying src/splinart/draw.py -> splinart-0.1.0/src/splinart
copying src/splinart/version.py -> splinart-0.1.0/src/splinart
copying src/splinart.egg-info/PKG-INFO -> splinart-0.1.0/src/splinart.egg-info
copying src/splinart.egg-info/SOURCES.txt -> splinart-0.1.0/src/splinart.egg-info
copying src/splinart.egg-info/dependency_links.txt -> splinart-0.1.0/src/splinart.egg-info
copying src/splinart.egg-info/entry_points.txt -> splinart-0.1.0/src/splinart.egg-info
copying src/splinart.egg-info/requires.txt -> splinart-0.1.0/src/splinart.egg-info
copying src/splinart.egg-info/top_level.txt -> splinart-0.1.0/src/splinart.egg-info
copying tests/test_all.py -> splinart-0.1.0/tests
copying tests/test_shape.py -> splinart-0.1.0/tests
copying tests/test_spline.py -> splinart-0.1.0/tests
copying src/splinart.egg-info/SOURCES.txt -> splinart-0.1.0/src/splinart.egg-info
Writing splinart-0.1.0/setup.cfg
Creating tar archive
removing 'splinart-0.1.0' (and everything under it)
Building wheel...
running egg_info
writing src/splinart.egg-info/PKG-INFO
writing dependency_links to src/splinart.egg-info/dependency_links.txt
writing entry points to src/splinart.egg-info/entry_points.txt
writing requirements to src/splinart.egg-info/requires.txt
writing top-level names to src/splinart.egg-info/top_level.txt
reading manifest file 'src/splinart.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'src/splinart.egg-info/SOURCES.txt'
running bdist_wheel
running build
running build_py
copying src/splinart/draw.py -> build/lib/splinart
copying src/splinart/__init__.py -> build/lib/splinart
copying src/splinart/color.py -> build/lib/splinart
copying src/splinart/compute.py -> build/lib/splinart
copying src/splinart/version.py -> build/lib/splinart
running egg_info
writing src/splinart.egg-info/PKG-INFO
writing dependency_links to src/splinart.egg-info/dependency_links.txt
writing entry points to src/splinart.egg-info/entry_points.txt
writing requirements to src/splinart.egg-info/requires.txt
writing top-level names to src/splinart.egg-info/top_level.txt
reading manifest file 'src/splinart.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'src/splinart.egg-info/SOURCES.txt'
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/splinart
copying build/lib/splinart/draw.py -> build/bdist.linux-x86_64/wheel/./splinart
creating build/bdist.linux-x86_64/wheel/splinart/scripts
copying build/lib/splinart/scripts/cli_splinart.py -> build/bdist.linux-x86_64/wheel/./splinart/scripts
copying build/lib/splinart/scripts/__init__.py -> build/bdist.linux-x86_64/wheel/./splinart/scripts
creating build/bdist.linux-x86_64/wheel/splinart/spline
copying build/lib/splinart/spline/spline.py -> build/bdist.linux-x86_64/wheel/./splinart/spline
copying build/lib/splinart/spline/__init__.py -> build/bdist.linux-x86_64/wheel/./splinart/spline
copying build/lib/splinart/spline/splint.py -> build/bdist.linux-x86_64/wheel/./splinart/spline
copying build/lib/splinart/__init__.py -> build/bdist.linux-x86_64/wheel/./splinart
copying build/lib/splinart/color.py -> build/bdist.linux-x86_64/wheel/./splinart
copying build/lib/splinart/compute.py -> build/bdist.linux-x86_64/wheel/./splinart
copying build/lib/splinart/version.py -> build/bdist.linux-x86_64/wheel/./splinart
creating build/bdist.linux-x86_64/wheel/splinart/shapes
copying build/lib/splinart/shapes/base.py -> build/bdist.linux-x86_64/wheel/./splinart/shapes
copying build/lib/splinart/shapes/__init__.py -> build/bdist.linux-x86_64/wheel/./splinart/shapes
running install_egg_info
Copying src/splinart.egg-info to build/bdist.linux-x86_64/wheel/./splinart-0.1.0-py3.13.egg-info
running install_scripts
creating build/bdist.linux-x86_64/wheel/splinart-0.1.0.dist-info/WHEEL
creating '/home/lcrepeau/splinart/dist/.tmp-saigts_9/splinart-0.1.0-py3-none-any.whl'
    and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'splinart/__init__.py'
adding 'splinart/color.py'
adding 'splinart/compute.py'
adding 'splinart/draw.py'
adding 'splinart/version.py'
adding 'splinart/scripts/__init__.py'
adding 'splinart/scripts/cli_splinart.py'
adding 'splinart/shapes/__init__.py'
adding 'splinart/shapes/base.py'
adding 'splinart/spline/__init__.py'
adding 'splinart/spline/spline.py'
adding 'splinart/spline/splint.py'
adding 'splinart-0.1.0.dist-info/licenses/LICENSE'
adding 'splinart-0.1.0.dist-info/METADATA'
adding 'splinart-0.1.0.dist-info/WHEEL'
adding 'splinart-0.1.0.dist-info/entry_points.txt'
adding 'splinart-0.1.0.dist-info/top_level.txt'
adding 'splinart-0.1.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel
Successfully built dist/splinart-0.1.0.tar.gz
Successfully built dist/splinart-0.1.0-py3-none-any.whl
# VERIFICATION
$ ls -gG dist/\*
-rw-r--r-- 1 9816 juin  23 15:23 dist/splinart-0.1.0-py3-none-any.whl
-rw-r--r-- 1 6249 juin  23 15:23 dist/splinart-0.1.0.tar.gz
$ tar ztvf dist/splinart-0.1.0.tar.gz
drwxr-xr-x lcrepeau/lmdpol   0 2026-06-23 15:23 splinart-0.1.0/
-rw-r--r-- lcrepeau/lmdpol 1512 2026-06-17 13:17 splinart-0.1.0/LICENSE
-rw-r--r-- lcrepeau/lmdpol 2067 2026-06-23 15:23 splinart-0.1.0/PKG-INFO
-rw-r--r-- lcrepeau/lmdpol  374 2026-06-19 10:51 splinart-0.1.0/README.md
-rw-r--r-- lcrepeau/lmdpol 2311 2026-06-23 15:06 splinart-0.1.0/pyproject.toml
-rw-r--r-- lcrepeau/lmdpol   38 2026-06-23 15:23 splinart-0.1.0/setup.cfg
drwxr-xr-x lcrepeau/lmdpol    0 2026-06-23 15:23 splinart-0.1.0/src/
drwxr-xr-x lcrepeau/lmdpol    0 2026-06-23 15:23 splinart-0.1.0/src/splinart/
-rw-r--r-- lcrepeau/lmdpol  275 2026-06-23 08:50 splinart-0.1.0/src/splinart/__init__.py
-rw-r--r-- lcrepeau/lmdpol  196 2026-06-23 08:50 splinart-0.1.0/src/splinart/color.py
-rw-r--r-- lcrepeau/lmdpol 3380 2026-06-23 15:09 splinart-0.1.0/src/splinart/compute.py
-rw-r--r-- lcrepeau/lmdpol 2112 2026-06-23 08:50 splinart-0.1.0/src/splinart/draw.py
-rw-r--r-- lcrepeau/lmdpol   47 2026-06-23 08:50 splinart-0.1.0/src/splinart/version.py
drwxr-xr-x lcrepeau/lmdpol    0 2026-06-23 15:23 splinart-0.1.0/src/splinart.egg-info/
-rw-r--r-- lcrepeau/lmdpol 2067 2026-06-23 15:23 splinart-0.1.0/src/splinart.egg-info/PKG-INFO
-rw-r--r-- lcrepeau/lmdpol  425 2026-06-23 15:23 splinart-0.1.0/src/splinart.egg-info/SOURCES.txt
-rw-r--r-- lcrepeau/lmdpol    1 2026-06-23 15:23 splinart-0.1.0/src/splinart.egg-info/dependency_links.txt
-rw-r--r-- lcrepeau/lmdpol   64 2026-06-23 15:23 splinart-0.1.0/src/splinart.egg-info/entry_points.txt
-rw-r--r-- lcrepeau/lmdpol  259 2026-06-23 15:23 splinart-0.1.0/src/splinart.egg-info/requires.txt
-rw-r--r-- lcrepeau/lmdpol    9 2026-06-23 15:23 splinart-0.1.0/src/splinart.egg-info/top_level.txt
drwxr-xr-x lcrepeau/lmdpol    0 2026-06-23 15:23 splinart-0.1.0/tests/
-rw-rw-r-- lcrepeau/lmdpol  735 2026-06-23 11:32 splinart-0.1.0/tests/test_all.py
-rw-rw-r-- lcrepeau/lmdpol 1246 2026-06-08 10:13 splinart-0.1.0/tests/test_shape.py
-rw-rw-r-- lcrepeau/lmdpol  866 2026-06-23 15:05 splinart-0.1.0/tests/test_spline.py
```

## INSTALLER UNE INTEGRATION CONTINUE github SUR splinart

```bash
# CREER UNE NOUVELLE BRANCHE
$ git checkout -b cicd
# CREER LES REPERTOIRES POUR LA CI github
$ mkdir -p .github/workflows
```

On crée le premier fichier ci où cette action sera lancé sur une pull request
    vers la branche `main`. Ici on clone le dépôt courant et on installe une
    version de python 3.13 :

```bash
# CREER LE PREMIER FICHIER CI
$ cat > .github/workflows/ci.yml
name: ci

on:
  pull_request:
    branches: [main]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python 3.13
      uses: actions/setup-python@v3
      with:
        python-version: "3.13"
# VERSIONNEMENT DU FICHIER
$ git add .github/workflows/ci.yml
$ git commit -m'Premier essai ci dans .github/workflows/ci.yml.'
# CONFIGURATION DU POUSSAGE VERS github
$ git push --set-upstream origin cicd
X11 forwarding request failed on channel 0
Énumération des objets: 32, fait.
Décompte des objets: 100% (32/32), fait.
Compression par delta en utilisant jusqu'à 4 fils d'exécution
Compression des objets: 100% (25/25), fait.
Écriture des objets: 100% (28/28), 3.96 Kio | 270.00 Kio/s, fait.
Total 28 (delta 12), réutilisés 0 (delta 0), réutilisés du pack 0
remote: Resolving deltas: 100% (12/12), completed with 3 local objects.
remote:
remote: Create a pull request for 'cicd' on GitHub by visiting:
remote:      https://github.com/lcrepeau/splinart_2026_lc/pull/new/cicd
remote:
To github.com:lcrepeau/splinart_2026_lc.git
 * [new branch]      cicd -> cicd
La branche 'cicd' est paramétrée pour suivre la branche distante 'cicd' depuis
    'origin'.
```

### SUIVI SUR github

Figures des actions sur github pour l'intégration continue :

#### Onglet `Pull request` sur github

![graph][internal-github1]

[internal-github1]: images/github_post_pull_request1.png 'Pull request'

#### Branche disponible

![graph][internal-github2]

[internal-github2]: images/github_post_pull_request2.png

### Clic sur Cicd

![graph][internal-github3]

[internal-github3]: images/github_post_pull_request3.png 'Merge demandé'

### Onglet `Actions`

![graph][internal-github4]

[internal-github4]: images/github_actions1.png 'Onglet Actions'

#### Clic sur Cicd dans `Actions`

![graph][internal-github5]

[internal-github5]: images/github_actions2.png 'Clic sur build'

#### Panneau de retour de la ci

![graph][internal-github6]

[internal-github6]: images/github_actions3.png 'Ci build'

#### Onglet `Set up job` déployé

![graph][internal-github7]

[internal-github7]: images/github_actions4.png 'Set up job'

#### Onglet `Run actions/checkout@v3` déployé

![graph][internal-github8]

[internal-github8]: images/github_actions5.png 'actions/checkout@v3'

#### Onglet `Set up Python 3.13` déployé

![graph][internal-github9]

[internal-github9]: images/github_actions6.png 'Set up Python 3.13'

#### Onglet `Post Set up job` déployé

![graph][internal-github10]

[internal-github10]: images/github_actions7.png 'Post Set up job'

#### Onglet `Post Run actions/checkout@v3` déployé

![graph][internal-github11]

[internal-github11]: images/github_actions8.png 'Post Run actions/checkout@v3'

#### Onglet `Complete job` déployé

![graph][internal-github12]

[internal-github12]: images/github_actions9.png 'Complete job'

#### Coût ci

![graph][internal-github13]

[internal-github13]: images/github_actions_cout_ci.png 'Coût ci'

#### Fichier ci qui a tourné

![graph][internal-github14]

[internal-github14]: images/github_actions_fichier_ci.png 'Fichier ci connu'

### REMARQUES SUR LES GITHUB ACTIONS

Le [Marketplace GitHub Actions](https://github.com/marketplace?type=actions 'la')
    est une place de marché qui regroupe des milliers d'actions réutilisables
    créées par GitHub, des éditeurs, et la communauté. C'est un gain de temps
    énorme. Mais c'est aussi un risque de sécurité majeur si vous ne savez
    pas évaluer ce que vous allez utiliser (Stéphane Robert).

[Remarques]["lien"]

[lien] <https://blog.stephane-robert.info/docs/pipeline-cicd/github/fondations/marketplace/>

Vérifier régulièrement les versions des github actions que vous utilisez,
    les développements sont rapides.

**Attention aux fautes de frappes. C'est très dangereux !**

#### VERIFICATION FICHIER ci.yml

##### actions/checkout@v3

Dans le fichier le clône du dépôt est la version v3 : actions/checkout@v3. Sur
    [Marketplace GitHub Actions](https://github.com/marketplace?type=actions 'la'),
    on cherche la version la plus récente en sélectionnant `Verified creators`.
    Au 20260623 c'est la version v7 qui est la plus récente.

```bash
# RECHERCHE du sha DE CETTE VERSION
$ curl -s https://api.github.com/repos/actions/checkout/commits/v7 | jq -r .sha
9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0
# MODIFICATION DU FICHIER ci.yml
uses: actions/checkout@v3 ->
    uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7
```

##### actions/setup-python@v3

Sur [Marketplace GitHub Actions](https://github.com/marketplace?type=actions 'la'),
    on cherche la version la plus récente en sélectionnant `Verified creators`.
    Au 20260623 c'est la version v6 qui est la plus récente.

```bash
# RECHERCHE du sha DE CETTE VERSION
$ curl -s https://api.github.com/repos/actions/setup-python/commits/v6 | jq -r .sha
a309ff8b426b58ec0e2a45f0f869d46889d02405
# MODIFICATION DU FICHIER ci.yml
uses: actions/setup-python@v3 ->
    uses: actions/setup-python@a309ff8b426b58ec0e2a45f0f869d46889d02405 # v6
```

#### EXEMPLE DE LANCEMENT D'UN PROGRAMME PYTHON

```yaml
# action.yml
steps:
- uses: actions/checkout@v6
- uses: actions/setup-python@v6
  with:
    python-version: '3.13'
- run: python my_script.py
```

### INSTALLER LE GITHUB RUNNER EN LOCAL

Au 20260623 voir le [lien](https://lindevs.com/install-act-on-ubuntu/).

```bash
$ wget -qO act.tar.gz https://github.com/nektos/act/releases/latest/download/act_Linux_x86_64.tar.gz
# Extract act executable file to /usr/local/bin directory:
sudo tar xf act.tar.gz -C /usr/local/bin act
# Now the act command can be used for all users as a system-wide command.
# We can check act version as follows:
$ act --version
act version 0.2.89
# Remove tar.gz file:
$ rm -rf act.tar.gz
# Testing act Clone the sample repository for testing:
$ git clone https://github.com/cplee/github-actions-demo.git
# Run the act command and specify working directory with -C option to run
# GitHub Actions locally:
$ act -C github-actions-demo
# LANCER LE TEST essai UNIQUEMENT
$ act -C github-actions-demo -j essai
# For the first time, you will be asked to choose the image to be used as default.
# You can select Medium size image. It can be changed later in ~/.actrc
# configuration file.
# The act run jobs defined in YAML file which stored in github/workflows directory:

[CI/test] Start image=ghcr.io/catthehacker/ubuntu:act-latest
......
[CI/test] *  Run actions/checkout@v2
[CI/test]   Success - actions/checkout@v2
[CI/test] *  Run actions/setup-node@v1
......
[CI/test]   Success - actions/setup-node@v1
[CI/test] *  Run npm install
......
[CI/test]   Success - npm install
[CI/test] *  Run npm test
......
|   GET /
|     ✓ should respond with hello world
|
|
|   1 passing (28ms)
|
[CI/test]   Success - npm test

# Uninstall act If act is no longer needed, remove the executable file:
$ sudo rm -rf /usr/local/bin/act
# You can also remove configuration file and cache:
$ rm -rf ~/.actrc ~/.cache/act
#
# OPTIONS DE act
#
$ act --help
Run GitHub actions locally by specifying the event name (e.g. `push`) or an
    action name directly.

Usage:
  act [event name to run] [flags]

If no event name passed, will default to "on: push"
If actions handles only one event it will be used as default instead of
    "on: push"

Flags:
      --action-cache-path string                          Defines the path where
    the actions get cached and host workspaces created. (default
    "/home/lcrepeau/.cache/act")
      --action-offline-mode                               If action contents
    exists, it will not be fetch and pull again. If turn on this, will turn off
    force pull
  -a, --actor string                                      user that triggered
    the event (default "nektos/act")
      --artifact-server-addr string                       Defines the address
    to which the artifact server binds. (default "129.104.56.198")
      --artifact-server-path string                       Defines the path where
    the artifact server stores uploads and retrieves downloads from. If not
    specified the artifact server will not start.
      --artifact-server-port string                       Defines the port
    where the artifact server listens. (default "34567")
  -b, --bind                                              bind working directory
    to container, rather than copy
      --bug-report                                        Display system
    information for bug report
      --cache-server-addr string                          Defines the address to
    which the cache server binds. (default "129.104.56.198")
      --cache-server-external-url string                  Defines the external
    URL for if the cache server is behind a proxy. e.g.:
    https://act-cache-server.example.com. Be careful that there is no trailing slash.
      --cache-server-path string                          Defines the path where
    the cache server stores caches. (default "/home/lcrepeau/.cache/actcache")
      --cache-server-port uint16                          Defines the port where
    the artifact server listens. 0 means a randomly available port.
      --concurrent-jobs int                               Maximum number of
    concurrent jobs to run. Default is the number of CPUs available.
      --container-architecture string                     Architecture which
    should be used to run containers, e.g.: linux/amd64. If not specified, will
    use host default architecture. Requires Docker server API Version 1.41+.
    Ignored on earlier Docker server platforms.
      --container-cap-add stringArray                     kernel capabilities to
    add to the workflow containers (e.g. --container-cap-add SYS_PTRACE)
      --container-cap-drop stringArray                    kernel capabilities to
    remove from the workflow containers (e.g. --container-cap-drop SYS_PTRACE)
      --container-daemon-socket string                    URI to Docker Engine
    socket (e.g.: unix://~/.docker/run/docker.sock or - to disable bind mounting
    the socket)
      --container-options string                          Custom docker
    container options for the job container without an options property in thei
    job definition
      --defaultbranch string                              the name of the main
    branch
      --detect-event                                      Use first event type
    from workflow as event that triggered the workflow
  -C, --directory string                                  working directory
    (default ".")
  -n, --dryrun                                            disable container
    creation, validates only workflow correctness
      --env stringArray                                   env to make available
    to actions with optional value (e.g. --env myenv=foo or --env myenv)
      --env-file string                                   environment file to
    read and use as env in the containers (default ".env")
  -e, --eventpath string                                  path to event JSON
    file
      --github-instance string                            GitHub instance toi
    use. Only use this when using GitHub Enterprise Server. (default "github.com")
  -g, --graph                                             draw workflows
  -h, --help                                              help for act
      --input stringArray                                 action input to make
    available to actions (e.g. --input myinput=foo)
      --input-file string                                 input file to read
    and use as action input (default ".input")
      --insecure-secrets                                  NOT RECOMMENDED!
    Doesn't hide secrets while printing logs.
  -j, --job string                                        run a specific job ID
      --json                                              Output logs in json
    format
  -l, --list                                              list workflows
      --list-options                                      Print a json structure
    of compatible options
      --local-repository stringArray                      Replaces the specified
    repository and ref with a local folder (e.g. https://github.com/test/test@v0
    =/home/act/test or test/test@v0=/home/act/test, the latter matches any hosts
    or protocols)
      --log-prefix-job-id                                 Output the job id
    within non-json logs instead of the entire name
      --man-page                                          Print a generated
    manual page to stdout
      --matrix stringArray                                specify which matrix
    configuration to include (e.g. --matrix java:13
      --network string                                    Sets a docker network
    name. Defaults to host. (default "host")
      --no-cache-server                                   Disable cache server
      --no-recurse                                        Flag to disable
    running workflows from subdirectories of specified path '--workflows'/'-W'
    flag
      --no-skip-checkout                                  Use actions/checkout
    instead of copying local files into container
  -P, --platform stringArray                              custom image to use
     per platform (e.g. -P ubuntu-18.04=nektos/act-environments-ubuntu:18.04)
      --privileged                                        use privileged mode
  -p, --pull                                              pull docker image(s)
     even if already present (default true)
  -q, --quiet                                             disable logging of
     output from steps
      --rebuild                                           rebuild local action
     docker image(s) even if already present (default true)
      --remote-name string                                git remote name that
     will be used to retrieve url of git repo (default "origin")
      --replace-ghe-action-token-with-github-com string   If you are using
    replace-ghe-action-with-github-com and you want to use private actions oni
    GitHub, you have to set personal access token
      --replace-ghe-action-with-github-com stringArray    If you are using
    GitHub Enterprise Server and allow specified actions from GitHub
    (github.com), you can set actions on this.
    (e.g. --replace-ghe-action-with-github-com =github/super-linter)
  -r, --reuse                                             don't remove
    container(s) on successfully completed workflow(s) to maintain state between
    runs
      --rm                                                automatically remove
    container(s)/volume(s) after a workflow(s) failure
  -s, --secret stringArray                                secret to make
    available to actions with optional value (e.g. -s mysecret=foo or
    -s mysecret)
      --secret-file string                                file with list of
    secrets to read from (e.g. --secret-file .secrets) (default ".secrets")
      --strict                                            use strict workflow
    schema
      --use-gitignore                                     Controls whether paths
    specified in .gitignore should be copied into container (default true)
      --use-new-action-cache                              Enable using the new
    Action Cache for storing Actions locally
      --userns string                                     user namespace to use
      --validate                                          validate workflows
      --var stringArray                                   variable to make
    available to actions with optional value (e.g. --var myvar=foo or
    --var myvar)
      --var-file string                                   file with list of
    vars to read from (e.g. --var-file .vars) (default ".vars")
  -v, --verbose                                           verbose output
      --version                                           version for act
  -w, --watch                                             watch the contents of
    the local repo and run when files change
  -W, --workflows string                                  path to workflow
    file(s) (default "./.github/workflows/")
# AFFICHER LA LISTE DES ETIQUETTES CONNUES
splinart$ act -l
INFO[0000] Using docker host 'unix:///var/run/docker.sock', and daemon socket 'unix:///var/run/docker.sock'
Stage  Job ID           Job name             Workflow name     Workflow file  Events
0      build            build                ci                ci.yml         pull_request
0      pre-commit       python               ci_splinart_2026  ci1.yml        pull_request
0      build            build                ci                ci_test.yml    pull_request
0      make_sdist       Make SDist and weel  publish           publish.yml    release
0      release-please   release-please       release-please    realease.yml   workflow_dispatch
1      tests            python               ci_splinart_2026  ci1.yml        pull_request
1      upload_on_conda  upload_on_conda      publish           publish.yml    release
1      upload_on_pypi   upload_on_pypi       publish           publish.yml    release
# LANCER QU'UN FICHIER yml S'IL Y EN A PLUSIEURS (VOIR CI-DESSUS)
$ act -W .github/workflows/<file_name>.yml
# LANCER UN FICHIER yml S'IL Y EN A PLUSIEURS (VOIR CI-DESSUS) ET UNE ETIQUETTE
# -r POUR GARDER LE RUNNER A L'ISSUE DE LA CI POUR POUVOIR LA REUTILISER
$ act -W .github/workflows/<file_name>.yml -j test -r
# 4. Verify the Deployment
#   After pushing changes to your main branch, check the Actions tab in your repository
#   to ensure the workflow runs successfully.
#   Access your documentation at https://<username>.github.io/<repository>.
```

### ERREUR en cours

```bash
$ act -W .github/workflows/ci_publish_sphinx.yml -j build -r \
    --artifact-server-path /tmp/artifacts
INFO[0000] Using docker host 'unix:///var/run/docker.sock', and daemon socket
INFO[0000] Start server on http://129.104.56.198:34567
[ci_splinart_2026/python] ⭐ Run Set up job
[ci_splinart_2026/python] 🚀  Start image=catthehacker/ubuntu:act-latest
[ci_splinart_2026/python]   🐳  docker pull image=catthehacker/ubuntu:act-latest
[ci_splinart_2026/python]   🐳  docker create image=catthehacker/ubuntu:act-latest
[ci_splinart_2026/python]   🐳  docker run image=catthehacker/ubuntu:act-latest
[ci_splinart_2026/python]   🐳  docker exec cmd=[node --no-warnings \
    -e console.log(process.execPath)] user= workdir=
[ci_splinart_2026/python]   ✅  Success - Set up job
[ci_splinart_2026/python]   ☁  git clone 'https://github.com/astral-sh/setup-uv'\
     # ref=08807647e7069bb48b6ef5acd8ec9567f424441b
[ci_splinart_2026/python]   ☁  git clone 'https://github.com/actions/upload-pages-artifact'\
     # ref=fc324d3547104276b827a68afc52ff2a11cc49c9
[ci_splinart_2026/python] ⭐ Run Pre Upload artifact
[ci_splinart_2026/python]   ☁  git clone 'https://github.com/actions/upload-artifact'\
     # ref=bbbca2ddaa5d8feaa63e36b76fdaad77386f024f
[ci_splinart_2026/python]   ✅  Success - Pre Upload artifact [1.11947227s]
[ci_splinart_2026/python] ⭐ Run Main Cloner le depot
[ci_splinart_2026/python]   🐳  docker cp src=/home/lcrepeau/splinart/. \
    dst=/home/lcrepeau/splinart
[ci_splinart_2026/python]   ✅  Success - Main Cloner le depot [760.878735ms]
[ci_splinart_2026/python] ⭐ Run Main Install uv
| Trying to find version for uv in: /home/lcrepeau/splinart/uv.toml
| Could not find file: /home/lcrepeau/splinart/uv.toml
| Trying to find version for uv in: /home/lcrepeau/splinart/pyproject.toml
| Could not determine uv version from uv.toml or pyproject.toml. Falling back
| Fetching manifest data from \
    https://raw.githubusercontent.com/astral-sh/versions/main/v1/uv.ndjson ...
| Found uv in tool-cache for 0.11.24
| Added /root/.local/bin to the path
| Added /opt/hostedtoolcache/uv/0.11.24/x86_64 to the path
| Set UV_PYTHON_INSTALL_DIR to /root/.local/share/uv/python
| Added /root/.local/share/uv/python to the path
[ci_splinart_2026/python]   ❓ add-matcher
| Successfully installed uv version 0.11.24
[ci_splinart_2026/python]   ✅  Success - Main Install uv [1.221664759s]
[ci_splinart_2026/python]   ⚙  ::set-env:: UV_PYTHON_INSTALL_DIR=/root/.local/share/uv/python
[ci_splinart_2026/python]   ⚙  ::set-output:: uv-path=/opt/hostedtoolcache/uv/0.11.24/x86_64/uv
[ci_splinart_2026/python]   ⚙  ::set-output:: uvx-path=/opt/hostedtoolcache/uv/0.11.24/x86_64/uvx
[ci_splinart_2026/python]   ⚙  ::set-output:: uv-version=0.11.24
[ci_splinart_2026/python]   ⚙  ::set-output:: python-version=3.13.14
[ci_splinart_2026/python]   ⚙  ::add-path:: /root/.local/bin
[ci_splinart_2026/python]   ⚙  ::add-path:: /opt/hostedtoolcache/uv/0.11.24/x86_64
[ci_splinart_2026/python]   ⚙  ::add-path:: /root/.local/share/uv/python
[ci_splinart_2026/python] ⭐ Run Main Install the project
[ci_splinart_2026/python]   🐳  docker exec cmd=[bash -e /var/run/act/workflow/2]
| Resolved 102 packages in 36ms
    Built splinart @ file:///home/lcrepeau/formations/tests_python/TPs/3.linter
Prepared 1 package in 1.14s
| Uninstalled 1 package in 1ms
|[0/1] Installing wheels...
Installed 1 package in 3ms
|  ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
[ci_splinart_2026/python]   ✅  Success - Main Install the project [1.519652919s]
[ci_splinart_2026/python] ⭐ Run Main Install Pandoc
[ci_splinart_2026/python]   🐳  docker exec cmd=[bash -e /var/run/act/workflow/3]
Hit:1 https://packages.microsoft.com/ubuntu/24.04/prod noble InRelease
Hit:2 http://archive.ubuntu.com/ubuntu noble InRelease
Get:3 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]
Hit:4 https://ppa.launchpadcontent.net/git-core/ppa/ubuntu noble InRelease
Get:5 http://archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
Hit:6 http://archive.ubuntu.com/ubuntu noble-backports InRelease
Get:7 http://security.ubuntu.com/ubuntu noble-security/main Packages [976 kB]
Get:8 http://security.ubuntu.com/ubuntu noble-security/universe ges [1487 kB]
Get:9 http://security.ubuntu.com/ubuntu noble-security/restricted [1339 kB]
Get:10 http://archive.ubuntu.com/ubuntu noble-updates/restricted [1412 kB]
Get:11 http://archive.ubuntu.com/ubuntu noble-updates/universe  [2108 kB]
Get:12 http://archive.ubuntu.com/ubuntu noble-updates/main Packages [1296 kB]
Hit:13 https://packagecloud.io/github/git-lfs/ubuntu noble InRelease
Fetched 8869 kB in 2s (5492 kB/s)
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
| pandoc is already the newest version (3.1.3+ds-2).
| 0 upgraded, 0 newly installed, 0 to remove and 19 not upgraded.
| pandoc 3.1.3
| Features: -server +lua
| Scripting engine: Lua 5.4
| User data directory: /root/.local/share/pandoc
| Copyright (C) 2006-2023 John MacFarlane. Web: https://pandoc.org
| This is free software; see the source for copying conditions. There is no
| warranty, not even for merchantability or fitness for a particular purpose.
| /usr/bin/pandoc
[ci_splinart_2026/python]   ✅  Success - Main Install Pandoc [4.594071253s]
[ci_splinart_2026/python] ⭐ Run Main Run sphinx api doc
[ci_splinart_2026/python]   🐳  docker exec cmd=[bash -e /var/run/act/workflow/4]
| Running Sphinx v9.1.0
| loading translations [fr]... done
| WARNING: html_static_path entry '_static' does not exist
| Converting `source_suffix = '.rst'` to `source_suffix = {'.rst': 'restructuredtext'}`.
| loading pickled environment... The configuration has changed
    (3 options: 'nbsphinx_custom_formats', 'nbsphinx_requirejs_options',
    'nbsphinx_requirejs_path')
| done
| [autosummary] generating autosummary for: api/modules.md, api/splinart.md,
     api/splinart.scripts.md, api/splinart.shapes.md, api/splinart.spline.md,
     index.md, notebooks/circle.nblink, spline.md
| myst v5.1.0:
| Writing evaluated template result to docs_md/build/html/_static/nbsphinx-code-cells.css
| building [mo]: targets for 0 po files that are out of date
| writing output...
| building [html]: targets for 0 source files that are out of date
| updating environment: [config changed ('nbsphinx_custom_formats')]\
    8 added, 0 changed, 0 removed
reading sources... [100%] spline
| WARNING: multiple files found for the document "index": index.md, index.rst
| Use _StrPath('/home/lcrepeau/splinart/docs_md/source/index.md') for the build.
| WARNING: multiple files found for the document "spline": spline.rst, spline.md
| Use _StrPath('/home/lcrepeau/splinart/docs_md/source/spline.md') for the build.
| looking for now-outdated files... none found
| pickling environment... done
| checking consistency... done
| preparing documents... done
| copying assets...
| copying static files...
| Writing evaluated template result to docs_md/build/html/_static/documentation_options.js
| Writing evaluated template result to docs_md/build/html/_static/language_data.js
| Writing evaluated template result to docs_md/build/html/_static/basic.css
| Writing evaluated template result to docs_md/build/html/_static/alabaster.css
| copying static files: done
| copying extra files...
| copying extra files: done
| copying assets: done
writing output... [100%] spline
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| /home/lcrepeau/splinart/docs_md/source/notebooks/circle.nblink:: WARNING:
| generating indices... genindex done
| copying linked files...
  copying notebooks ... [100%] notebooks/circle.ipynb
| writing additional pages... search done
copying images... [100%] ../build/doctrees/nbsphinx/notebooks_circle_22_0.png
| dumping search index in French (code: fr)... done
| dumping object inventory... done
| build succeeded, 22 warnings.
|
| The HTML pages are in build/html.
[ci_splinart_2026/python]   ✅  Success - Main Run sphinx api doc [4.170595222s]
[ci_splinart_2026/python] ⭐ Run Main Upload artifact
[ci_splinart_2026/python] ⭐ Run Main Archive artifact
[ci_splinart_2026/python]   🐳  docker exec \
   cmd=[sh -e /var/run/act/workflow/5-composite-0.sh] user= workdir=
[ci_splinart_2026/python]   ❓  ::group::Archive artifact
| ./
| ./_sources/
| ./_sources/notebooks/
| ./_sources/notebooks/circle.nblink.txt
| ./_sources/index.md.txt
| ./_sources/api/
| ./_sources/api/modules.md.txt
| ./_sources/api/splinart.spline.md.txt
| ./_sources/api/splinart.md.txt
| ./_sources/api/splinart.scripts.md.txt
| ./_sources/api/splinart.shapes.md.txt
| ./_sources/spline.md.txt
| ./objects.inv
| ./notebooks/
| ./notebooks/circle.ipynb
| ./notebooks/circle.html
| ./_static/
| ./_static/documentation_options.js
| ./_static/github-banner.svg
| ./_static/base-stemmer.js
| ./_static/nbsphinx-no-thumbnail.svg
| ./_static/nbsphinx-code-cells.css
| ./_static/language_data.js
| ./_static/french-stemmer.js
| ./_static/alabaster.css
| ./_static/plus.png
| ./_static/custom.css
| ./_static/pygments.css
| ./_static/file.png
| ./_static/nbsphinx-broken-thumbnail.svg
| ./_static/searchtools.js
| ./_static/basic.css
| ./_static/sphinx_highlight.js
| ./_static/translations.js
| ./_static/doctools.js
| ./_static/minus.png
| ./_static/nbsphinx-gallery.css
| ./api/
| ./api/splinart.html
| ./api/modules.html
| ./api/splinart.spline.html
| ./api/splinart.scripts.html
| ./api/splinart.shapes.html
| ./search.html
| ./index.html
| ./genindex.html
| ./_images/
| ./_images/notebooks_circle_19_1.png
| ./_images/notebooks_circle_22_0.png
| ./_images/notebooks_circle_16_1.png
| ./_images/notebooks_circle_13_1.png
| ./_images/notebooks_circle_4_1.png
| ./searchindex.js
| ./spline.html
[ci_splinart_2026/python]   ❓  ::endgroup::
[ci_splinart_2026/python]   ✅  Success - Main Archive artifact [84.140873ms]
[ci_splinart_2026/python] ⭐ Run Main Upload artifact
[ci_splinart_2026/python]   🐳  docker cp src=/home/lcrepeau/.cache/act/actions-upload-artifact
[ci_splinart_2026/python]   🐳  docker exec cmd=[/opt/acttoolcache/node/24.17.0/x64/bin/node
| With the provided path, there will be 1 file uploaded
| Artifact name is valid!
| Root directory input is valid!
ERRO[0019] Error decode request body: proto: (line 1:140): unknown field "mime_type"
| Attempt 1 of 5 failed error: Unexpected end of JSON. Retrying in 3000 ms...
ERRO[0022] Error decode request body: proto: (line 1:140): unknown field "mime_type"
| Attempt 2 of 5 failed error: Unexpected end of JSON. Retrying in 4510 ms...
ERRO[0026] Error decode request body: proto: (line 1:140): unknown field "mime_type"
| Attempt 3 of 5 failed error: Unexpected end of JSON. Retrying in 8354 ms...
ERRO[0035] Error decode request body: proto: (line 1:140): unknown field "mime_type"
| Attempt 4 of 5 failed error: Unexpected end of JSON. Retrying in 15078 ms...
ERRO[0050] Error decode request body: proto: (line 1:140): unknown field "mime_type"
[ci_splinart_2026/python]   ❗  ::error::Failed to CreateArtifact: Failed to
    make request after 5 attempts: Unexpected end of JSON input
[ci_splinart_2026/python]   ❌  Failure - Main Upload artifact [31.52579249s]
[ci_splinart_2026/python] exitcode '1': failure
[ci_splinart_2026/python]   ⚙  ::set-output:: artifact_id=
[ci_splinart_2026/python]   ❌  Failure - Main Upload artifact [31.812797758s]
[ci_splinart_2026/python] exitcode '1': failure
[ci_splinart_2026/python] ⭐ Run Post Upload artifact
[ci_splinart_2026/python]   🐳  docker cp src=/home/lcrepeau/.cache/act/actions-upload-pages-artifact
[ci_splinart_2026/python]   ✅  Success - Post Upload artifact [47.596225ms]
[ci_splinart_2026/python] ⭐ Run Complete job
[ci_splinart_2026/python]   ✅  Success - Complete job
[ci_splinart_2026/python] 🏁  Job failed
Error: Job 'python' failed
```

### INSTALLATION DE myst

```bash
$ uv add mystmd
Resolved 102 packages in 1.52s
      Built splinart @ file:///home/lcrepeau/splinart
Prepared 4 packages in 239ms
Uninstalled 4 packages in 23ms
Installed 5 packages in 4ms
 + mystmd==1.10.1
 - nodeenv==1.10.0
 + nodeenv==1.9.1
 - platformdirs==4.10.0
 + platformdirs==4.2.2
 ~ splinart==0.1.0 (from file:///home/lcrepeau/splinart)
 - virtualenv==21.5.1
 + virtualenv==20.39.1
 uv run myst init
❗ Node.js (node) is required to run MyST, but could not be found`.
❔ Install Node.js in '/home/lcrepeau/.local/share/myst/20.0.0'? (y/N): y
⚙️  Attempting to install Node.js in /home/lcrepeau/.local/share/myst/20.0.0 ...
ℹ️  Successfully installed Node.js 20.0.0
building myst-cli session with API URL: https://api.mystmd.org
🍡 Execution parallelism set to: 3

Welcome to the MyST CLI! 🎉 🚀

myst init walks you through creating a myst.yml file.

You can use MyST to:

 - create interactive websites from markdown and Jupyter Notebooks 📈
 - build & export professional PDFs and Word documents 📄

Learn more about this CLI and MyST Markdown at: https://mystmd.org


💾 Updating .gitignore
💾 Writing new project and site config file: myst.yml
...

```

```bash
$ uv run myst init --gh-pages
building myst-cli session with API URL: https://api.mystmd.org
🍡 Execution parallelism set to: 3
📝 Creating a GitHub Action to deploy your MyST Site

? What branch would you like to deploy from? main
? What would you like to call the action? deploy.yml

🎉 GitHub Action is configured:

.github/workflows/deploy.yml

✅ Next Steps

1. Navigate to your GitHub Pages settings

    https://github.com/lcrepeau/splinart_2026_lc/settings/pages

2. Enable GitHub Pages
3. Use GitHub Actions as the source
4. Push these changes (and/or merge to main)
5. Look for a new action to start

    https://github.com/lcrepeau/splinart_2026_lc/actions

6. Once the action completes, your site should be deployed at:

    https://lcrepeau.github.io/splinart_2026_lc

7. 🎉 Celebrate and tell us about your site on BlueSky or Mastodon! 🐦 🐘

```

```bash
$ cat .github/workflows/deploy.yml
# This file was created automatically with `myst init --gh-pages` 🪄 💚
# Ensure your GitHub Pages settings for this repository are set to deploy with
# **GitHub Actions**.

name: MyST GitHub Pages Deploy
on:
  push:
    # Runs on pushes targeting the default branch
    branches: [main]
env:
  # `BASE_URL` determines, relative to the root of the domain, the URL that
  # your site is served from.
  # E.g., if your site lives at `https://mydomain.org/myproject`,
  # set `BASE_URL=/myproject`.
  # If, instead, your site lives at the root of the domain, at
  # `https://mydomain.org`, set `BASE_URL=''`.
  BASE_URL: /${{ github.event.repository.name }}

# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write
# Allow only one concurrent deployment, skipping runs queued between the run
# in-progress and latest queued.
# However, do NOT cancel in-progress runs as we want to allow these production
#  deployments to complete.
concurrency:
  group: 'pages'
  cancel-in-progress: false
jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Pages
        uses: actions/configure-pages@v3
      - uses: actions/setup-node@v4
        with:
          node-version: 18.x
      - name: Install MyST
        run: npm install -g mystmd
      - name: Build HTML Assets
        run: myst build --html
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './_build/html'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```
