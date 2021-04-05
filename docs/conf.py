#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# picachooser documentation build configuration file, created by
# sphinx-quickstart on Thu Jun 16 15:27:19 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
from datetime import datetime
from distutils.version import LooseVersion

import sphinx
from m2r import MdInclude

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("sphinxext"))
sys.path.insert(0, os.path.abspath("../picachooser"))

from github_link import make_linkcode_resolve
import picachooser

# -----------------------------------------------------------------------------
# Sphinx settings
# -----------------------------------------------------------------------------
# If your documentation needs a minimal Sphinx version, state it here.
pdf_break_level = 2

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",  # standard
    "sphinx.ext.autosummary",  # standard
    "sphinx.ext.coverage",  # collect doc coverage stats
    "sphinx.ext.doctest",  # runs doctests
    "sphinx.ext.ifconfig",  # includes content based on configuration
    "sphinx.ext.intersphinx",  # links code to other packages
    "sphinx.ext.linkcode",  # links to code from api
    "sphinx.ext.napoleon",  # alternative to numpydoc
    "sphinx.ext.todo",  # support for todo items
    "sphinx_gallery.gen_gallery",  # example gallery
    "sphinxarg.ext",  # argparse
    "recommonmark",  # markdown parser
]

if LooseVersion(sphinx.__version__) < LooseVersion("1.4"):
    extensions.append("sphinx.ext.pngmath")
else:
    extensions.append("sphinx.ext.imgmath")

# General information about the project.
project = "picachooser"
copyright = "2020-" + datetime.today().strftime("%Y") + ", Blaise Frederick"
author = "Blaise Frederick"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "..", "VERSION"), encoding="utf-8") as f:
    version = f.read().replace("v", "")

# The full version, including alpha/beta/rc tags.
release = version

# The master toctree document.
master_doc = "index"

# The suffix(es) of source filenames.
source_suffix = ".rst"

add_module_names = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# -----------------------------------------------------------------------------
# sphinx.ext.autosummary settings
# -----------------------------------------------------------------------------
# generate autosummary even if no references
autosummary_generate = True

# -----------------------------------------------------------------------------
# sphinx.ext.todo settings
# -----------------------------------------------------------------------------
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -----------------------------------------------------------------------------
# sphinx.ext.napoleon settings
# -----------------------------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = False
napoleon_use_keyword = True
napoleon_use_rtype = False

# -----------------------------------------------------------------------------
# LaTeX output
# -----------------------------------------------------------------------------
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "picachooser.tex",
        "picachooser Documentation",
        "Blaise Frederick",
        "manual",
    ),
]

# -----------------------------------------------------------------------------
# Manual page output
# -----------------------------------------------------------------------------
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "picachooser", "picachooser Documentation", [author], 1)]

# -----------------------------------------------------------------------------
# Texinfo output
# -----------------------------------------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "picachooser",
        "picachooser Documentation",
        author,
        "picachooser",
        "One line description of project.",
        "Miscellaneous",
    ),
]
# -----------------------------------------------------------------------------
# HTML output
# -----------------------------------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# installing theme package
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_sidebars = {"**": ["globaltoc.html", "relations.html", "searchbox.html", "indexsidebar.html"]}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -----------------------------------------------------------------------------
# HTMLHelp output
# -----------------------------------------------------------------------------
# Output file base name for HTML help builder.
htmlhelp_basename = "picachooserdoc"

# The following is used by sphinx.ext.linkcode to provide links to github
linkcode_resolve = make_linkcode_resolve(
    "picachooser",
    "https://github.com/bbfrederick/" "picachooser/blob/{revision}/" "{package}/{path}#L{lineno}",
)

# -----------------------------------------------------------------------------
# Intersphinx
# -----------------------------------------------------------------------------
_python_version_str = "{0.major}.{0.minor}".format(sys.version_info)
_python_doc_base = "https://docs.python.org/" + _python_version_str
intersphinx_mapping = {
    "python": (_python_doc_base, None),
    "numpy": (
        "https://docs.scipy.org/doc/numpy",
        (None, "./_intersphinx/numpy-objects.inv"),
    ),
    "scipy": (
        "https://docs.scipy.org/doc/scipy/reference",
        (None, "./_intersphinx/scipy-objects.inv"),
    ),
    "sklearn": (
        "https://scikit-learn.org/stable",
        (None, "./_intersphinx/sklearn-objects.inv"),
    ),
    "matplotlib": (
        "https://matplotlib.org/",
        (None, "https://matplotlib.org/objects.inv"),
    ),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "nibabel": ("https://nipy.org/nibabel/", None),
    "nilearn": ("http://nilearn.github.io/", None),
}

# -----------------------------------------------------------------------------
# Sphinx gallery
# -----------------------------------------------------------------------------
sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": "../examples",
    # path where to save gallery generated examples
    "gallery_dirs": "auto_examples",
    "backreferences_dir": "_build/gen_modules/backreferences",
    # Modules for which function level galleries are created.  In
    # this case sphinx_gallery and numpy in a tuple of strings.
    "doc_module": ("picachooser"),
    "ignore_patterns": ["utils/"],
    "reference_url": {
        # The module you locally document uses None
        "picachooser": None,
    },
}

# Generate the plots for the gallery
plot_gallery = "True"

# -----------------------------------------------------------------------------
# Setup functions
# -----------------------------------------------------------------------------


# https://github.com/rtfd/sphinx_rtd_theme/issues/117
def setup(app):
    app.add_css_file("theme_overrides.css")
    app.connect("autodoc-process-docstring", generate_example_rst)
    # Fix to https://github.com/sphinx-doc/sphinx/issues/7420
    # from https://github.com/life4/deal/commit/7f33cbc595ed31519cefdfaaf6f415dada5acd94
    # from m2r to make `mdinclude` work
    app.add_config_value("no_underscore_emphasis", False, "env")
    app.add_config_value("m2r_parse_relative_links", False, "env")
    app.add_config_value("m2r_anonymous_references", False, "env")
    app.add_config_value("m2r_disable_inline_math", False, "env")
    app.add_directive("mdinclude", MdInclude)


def generate_example_rst(app, what, name, obj, options, lines):
    # generate empty examples files, so that we don't get
    # inclusion errors if there are no examples for a class / module
    folder = os.path.join(app.srcdir, "generated")
    if not os.path.isdir(folder):
        os.makedirs(folder)
    examples_path = os.path.join(app.srcdir, "generated", "%s.examples" % name)
    if not os.path.exists(examples_path):
        # touch file
        open(examples_path, "w").close()
