# Formation Python pour la communauté 20260608->202611

* [lien transparents formation](https://gouarin.github.io/python-packaging-2023/)
* [lien github](https://github.com/gouarin/python-packaging-2023)
* [lien aplide support](https://github.com/gouarin/splinart)
* mail formateur : <loic.gouarin@polytechnique.edu>

Utilisation de `pixi` comme gestionnaire d'environnement python, sur-couche d'`uv`.

## Jour 1 - Packaging

Commandes faites

```bash
$ git clone https://github.com/gouarin/python-packaging-2023.git
$ cp -r python-packaging-2023/practical_session/TPs/1.packaging/step0 packaging
$ pixi workspace environment add publish --feature pypi-release
$ pixi run -e publish python -m build --sdist
#
$ pixi task add build-sdist "python -m build --sdist" -f pypi-release
$ pixi run build-sdist
#
$ pixi task add build-wheel "python -m build --wheel" -f pypi-release
$ pixi run build-wheel
#
$ pixi add -f pypi-release twine
$ pixi run -e publish twine upload \
    --repository-url https://test.pypi.org/legacy/ dist/*
#
$ pip install -i https://test.pypi.org/simple/ splinart-2026-JS
$ pip install -i https://test.pypi.org/simple/ splinart-2026-MF
$ pip install -i https://test.pypi.org/project/splinart-mag/0.1.0/
$ pip install -i https://test.pypi.org/simple/ splinart-iryna==0.1.0
#
mise exec -- uv pip install -i https://test.pypi.org/simple/ respline
```

Ressources :

* Semantic versioning: <https://semver.org/>
    (cf. <https://en.wikipedia.org/wiki/Semantic_versioning#Semantic_versioning>)
* Spécification de pyproject.toml:
    <https://packaging.python.org/en/latest/specifications/pyproject-toml/>
* Livre (en.)  Publishing Python Packages (Manning, 2022) de Dane Hillard:
    <https://www.manning.com/books/publishing-python-packages>

### pyproject.toml créé

```yaml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "splinart-2026"
version = "0.1.1"
dependencies = ["numpy>=2", "matplotlib>=3.5"]

[tool.setuptools.packages.find]
include = ["splinart*"]

[project.scripts]
splinart = "splinart.scripts.cli_splinart:main"

[tool.pixi.workspace]
channels = ["conda-forge"]
platforms = ["osx-arm64"]

[tool.pixi.tasks]

[tool.pixi.environments]
default = ["dev"]
publish = ["pypi-release", "conda-publish"]
test = ["test"]
test-conda = ["test-conda"]

[tool.pixi.feature.pypi-release.tasks]
build-sdist = "python -m build --sdist"
build-wheel = "python -m build --wheel"
build = { depends-on = ["build-sdist", "build-wheel"] }

[tool.pixi.feature.pypi-release.dependencies]
twine = ">=6.2.0,<7"

[tool.pixi.feature.pypi-release.pypi-dependencies]
build = ">=1.5.0,<2"

[tool.pixi.feature.dev.pypi-dependencies]
splinart-2026 = { path = ".", editable = true }

[tool.pixi.feature.conda-publish.tasks]
build = "conda-build recipes/ --output-folder ./dist/conda"

[tool.pixi.feature.conda-publish.dependencies]
conda-build = "*"
anaconda-client = "*"

[tool.pixi.feature.test.tasks]
install = "pip install --extra-index-url https://test.pypi.org/simple/ splinart-2026"

[tool.pixi.feature.test.dependencies]
pip = "*"

[tool.pixi.feature.test-conda.tasks]
install = "conda create -y -p /tmp/test-splinart-conda \
    -c ./dist/conda -c conda-forge splinart_2026"
test = "conda run -p /tmp/test-splinart-conda \
    python -c \"import splinart; print('✅ OK')\""
clean = "rm -rf /tmp/test-splinart-conda"

[tool.pixi.feature.test-conda.dependencies]
conda-libmamba-solver = "*"
conda = "*"
```

## Jour 2 - linters, tests, doc

Commandes pour configurer les linters ruff pylint

```bash
$ pixi add -f linter ruff pylint
$ pixi workspace environment add linter --feature linter
#
$ pixi run -e linter pylint splinart/compute.py
$ pixi run -e linter ruff check splinart/compute.py
```

### Documentation automatique

Utilisation de sphinx.

Utilisation de Myst :

Add your content using Markdown syntax. See the
[MyST Markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html)
documentation for details.

#### Modification de docs/source/index.md

``````text
# Splinart documentation

```{toctree}
:maxdepth: 2
:caption: Contents:
```
``````

### Pour les tests

* Tester les lignes

```python
path = spl.line(beg, end, npoints=nbpoints)
y2s = spl.spline.spline(path[:, 0], path[:, 1])
```

* Vérifier que les valeurs de y2s sont proches de 0

* Tester le comportement du calcul de la spline

```python
    theta, path = spl.circle(center, radius, npoints=nbpoints)
    y2s = spl.spline.spline(theta, path)
    y_new = np.zeros_like(path)
    spl.spline.splint(theta, path, y2s, theta, y_new)
```

Vérifier que le path est proche de y_new

#### Ressources Jour 2

* livre (en.) Python Testing with pytest (Pragmatic Bookshelf, 2022,
    Second Edition) de Brian Okken:
    <https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/>
* mailing-liste Python ESR: <python@services.cnrs.fr>
    (<https://listes.services.cnrs.fr/wws/info/python>)

## Jour 3 - pre-commit & GitHub actions

Etapes pour l'automatisation

* faire cette partie en vous appuyant sur le final_step de 5.pytest
* lire la partie automatisation et commencer à la mettre en oeuvre
* créer un fichier .gitignore avec le contenu suivant

```bash
# CREER UN .gitignore
$ cat > .gitignore
*.egg-info
__pycache__
_build
dist
*.egg
*.pyc
^D
# INITIALISER LE DEPOT git
$ git init
$ git add .
$ git commit -m "initial commit"
```

### Suite initialisation

* se créer une clé ssh si ce n'est déjà fait avec la commande ssh-keygen
* copier la clé public (.pub) dans les clés ssh du compte github

* A changer dans le pyptroject.toml

```yaml
dependencies = ["numpy>=2.0.0,<2.1", "matplotlib>=3.8.4,<3.9"]
```

### Dépot de référence

Dépôt d'un formaté qui a réussi les exercices :

[Dépôt Maxime Feingesicht](https://github.com/mfeingesicht/splinart-2026#)

### Gestion automatique des releases de code

Utilisation de release-please

```json
# FICHIER DE CONFIGURATION release-please-config.json
{
    "$schema": "https://raw.githubusercontent.com/googleapis/release-please/main/schemas/config.json",
    "release-type": "python",
    "include-component-in-tag": false,
    "packages": {
        ".": {
            "package-name": "splinart-2026",
            "changelog-path": "CHANGELOG.md",
            "extra-files": [
                {
                    "type": "generic",
                    "path": "splinart/version.py",
                    "pattern": "__version__ = \"([^\"]+)\""
                }
            ]
        }
    }
}
```

#### Integration continue github

Utilisation du fichier .github/workflow/release.yml

```yaml
name: release-please

on: workflow_dispatch

permissions:
    contents: write
    pull-requests: write

jobs:
    release-please:
        runs-on: ubuntu-latest
        steps:
            - uses: googleapis/release-please-action@v4
              with:
                  # Token personnel spécialement créé, plutôt que GITHUB_TOKEN
                  token: ${{ secrets.RELEASE_PLEASE_TOKEN }}
                  release-type: python
                  target-branch: main
```

### Ressources

* Alternative à pre-commit: prek
    (GitHub: <https://github.com/j178/prek>, doc: <https://prek.j178.dev/>)
* Runner de tâche de projet, "équivalent" à GNU make: just
    (<https://just.systems/>, GitHub: <https://github.com/casey/just>)
* Extensions sphinx pour faire du pdf:
  * <https://sphinx-simplepdf.readthedocs.io/en/latest/>
  * rinohtype: <https://pypi.org/project/rinohtype/>
        (GitHub: <https://github.com/brechtm/rinohtype/issues>,
        doc: <https://www.mos6581.org/rinohtype/master/>)
* Normalisation des commits <https://www.conventionalcommits.org/en/v1.0.0/>
* Formation github action de 202612 <https://gouarin.github.io/dev_env_and_automatisation/>
