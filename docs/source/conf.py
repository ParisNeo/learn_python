# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Learn python'  # <--- SET THIS!
copyright = '2025, ParisNeo'
author = 'ParisNeo'

# The short X.Y version
version = '0.1'
# The full version, including alpha/beta/rc tags
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',    # If you have Python code to document
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages', # If deploying to GitHub Pages
    'myst_parser',           # For Markdown support
    'sphinx_intl',           # For i18n
    # Add theme extension if needed, e.g. 'sphinx_rtd_theme'
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
html_theme = 'sphinx_rtd_theme' # Or 'furo', 'alabaster', etc.

# Language settings
language = 'en'
locale_dirs = ['locale/']   # Directory to store translation files (.po)
gettext_compact = False     # Or True
# For sphinx-intl, usually you don't need to set gettext_uuid = True