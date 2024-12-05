# Configuration file for the Sphinx documentation builder.

import os
import sys
import django  # Required for Django integration

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
# Dynamically set the project root path to locate project modules and packages
# The Sphinx 'conf.py' is in 'docs/source', so we step back 3 directories to the root
project_root = os.path.abspath('../../..')  # Adjusted path to locate the band_site folder
sys.path.insert(0, project_root)

# Add the Django project directory to the Python path
band_site_path = os.path.join(project_root, 'band_site')
sys.path.insert(0, band_site_path)

# Set up Django settings for Sphinx
os.environ['DJANGO_SETTINGS_MODULE'] = 'band_site.settings'  # Ensure the project name matches your project folder
django.setup()

# -- Explanation of `sphinx-apidoc` command -----------------------------------
# Use sphinx-apidoc to find all modules in the parent directory (..), 
# and output (-o) the .rst files to the 'source' subdirectory of this (.) directory:
# sphinx-apidoc .. -o ./source

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

