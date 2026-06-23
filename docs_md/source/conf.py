# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Splinart lc 2026"
copyright = "2026, Loic Gouarin"
author = "Loic Gouarin"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

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
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# INTERPRETATION DES FORMULES MATHEMATIQUES
myst_enable_extensions = ["dollarmath", "amsmath"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
