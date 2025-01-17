# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys

sys.path.insert(0, os.path.abspath(".."))  # Source code dir relative to this file


# -- Project information -----------------------------------------------------

project = "bento-tools"
copyright = " Carter Lab & Yeo Lab. 2023"
author = "Clarence Mah"
html_favicon = "favicon.ico"

# The full version, including alpha/beta/rc tags
release = "2.0.0a0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "myst_nb",
    "sphinx_design",
]

myst_enable_extensions = ["colon_fence", "html_image", "dollarmath"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

html_theme_options = {
    "repository_url": "https://github.com/ckmah/bento-tools",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs",
    "logo": {
        "alt_text": "Bento Logo",
    },
}

html_context = {"default_mode": "auto"}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = ["custom.css"]

# -- Options for Autosummary, Autodoc, Napolean docstring format -------------------------------------------------

autosummary_generate = True
autodoc_docstring_signature = True
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_rtype = False
numpydoc_show_class_members = False

html_title = "bento-tools"
html_logo = "_static/bento-name.png"

# -- Options for extensions -------------------------------------------------------------------------------

nb_execution_mode = "off"
