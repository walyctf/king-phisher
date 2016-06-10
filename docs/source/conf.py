# -*- coding: utf-8 -*-
#
# King Phisher documentation build configuration file, created by
# sphinx-quickstart on Fri Jun 13 09:54:27 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

GITHUB_BRANCH = 'dev'
GITHUB_REPO = 'securestate/king-phisher'

import os
import ssl
import sys

ssl.HAS_SNI = False  # patch this to work around an issue with RTDs

_prj_root = os.path.dirname(__file__)
_prj_root = os.path.relpath(os.path.join('..', '..'), _prj_root)
_prj_root = os.path.abspath(_prj_root)
sys.path.insert(1, _prj_root)

_pkg = os.path.join(_prj_root, 'king_phisher', 'third_party')
sys.path.insert(2, _pkg)

del _prj_root, _pkg

import king_phisher.client
import king_phisher.its
import king_phisher.version
import king_phisher.utilities

# -- General configuration ------------------------------------------------
needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'king_phisher.rpc_docs',
	'sphinx.ext.autodoc',
	'sphinx.ext.extlinks',
	'sphinx.ext.intersphinx',
	'sphinx.ext.linkcode',
	'sphinxcontrib.httpdomain'
]

tab_width = 4

extlinks = {
	'release': ("https://github.com/{0}/releases/tag/v%s".format(GITHUB_REPO), 'v')
}

def linkcode_resolve(domain, info):
	if domain != 'py':
		return None
	if not info['module']:
		return None
	file_name = info['module'].replace('.', '/') + '.py'
	return "https://github.com/{0}/blob/{1}/{2}".format(GITHUB_REPO, GITHUB_BRANCH, file_name)

intersphinx_mapping = {
	'glib': ('http://lazka.github.io/pgi-docs/GLib-2.0/', None),
	'gobject': ('http://lazka.github.io/pgi-docs/GObject-2.0/', None),
	'gtksource': ('https://lazka.github.io/pgi-docs/GtkSource-3.0/', None),
	'gtk': ('http://lazka.github.io/pgi-docs/Gtk-3.0/', None),
	'paramiko': ('http://docs.paramiko.org/en/latest/', None),
	'smokezephyr': ('https://smoke-zephyr.readthedocs.io/en/latest/', None),
	'webkit2': ('http://lazka.github.io/pgi-docs/WebKit2-4.0/', None)
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'King Phisher'
copyright = '2013-2016, SecureState LLC'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = king_phisher.version.version.split('-')[0]
# The full version, including alpha/beta/rc tags.
release = king_phisher.version.distutils_version

language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# HTTP domain specifc settings http://pythonhosted.org/sphinxcontrib-httpdomain/#additional-configuration
http_index_shortname = 'rest-api'
http_index_localname = "{0} REST API".format(project)

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
if not king_phisher.its.on_rtd:
	html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'king_phisher_doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
	('index', 'KingPhisher.tex', u'King Phisher Documentation', u'Spencer McIntyre', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
	('index', 'kingphisher', u'King Phisher Documentation', [u'Spencer McIntyre'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
	('index', 'KingPhisher', u'King Phisher Documentation', u'Spencer McIntyre', 'KingPhisher', 'One line description of project.', 'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# mock specific external packages
MOCK_MODULES = [
	'gi',
	'gi.repository',
	'matplotlib',
	'matplotlib.backends',
	'matplotlib.backends.backend_gtk3',
	'matplotlib.backends.backend_gtk3agg',
	'matplotlib.figure'
]
sys.modules.update((mod_name, king_phisher.utilities.Mock()) for mod_name in MOCK_MODULES)
