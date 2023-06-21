# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys



sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../Project"))

project = 'Game Of Life'
copyright = '2023, Kuba Malewicz, Mikolaj Kowaszewicz'
author = 'Kuba Malewicz, Mikolaj Kowaszewicz'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc", "rinoh.frontend.sphinx" , "sphinx.ext.napoleon" ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'PL'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

rinoh_documents = [
    dict(doc='index', target='manual', toctree_only=False,
         template='manual.rtt', logo='logo.pdf'),
    dict(doc='ref', target='reference', title='Reference Manual',
         template='reference.rtt', stamp='DRAFT'),
]



html_theme = 'press'
html_static_path = ['_static']
