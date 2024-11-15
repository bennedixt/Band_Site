# Configuration file for the Sphinx documentation builder.

import os
import sys
import django

# -- Project information -----------------------------------------------------
project = 'Band_site'
copyright = '2024, Bennedict Mahlawule'
author = 'Bennedict Mahlawule'
release = '0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',          # Enables automatic documentation generation from docstrings
    'sphinx.ext.napoleon',         # Supports Google-style and NumPy-style docstrings
]

templates_path = ['_templates']
exclude_patterns = []

# -- Django configuration ----------------------------------------------------

sys.path.insert(0, os.path.abspath('/Users/bennedixt/GetStarted/band_site'))


# Set up Django settings for Sphinx
os.environ['DJANGO_SETTINGS_MODULE'] = 'band_site.settings'  # Ensure the project name matches exactly
django.setup()

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
