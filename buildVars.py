# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.


# Since some strings in `addon_info` are translatable,
# we need to include them in the .po files.
# Gettext recognizes only strings given as parameters to the `_` function.
# To avoid initializing translations in this module we simply roll our own "fake" `_` function
# which returns whatever is given to it as an argument.
def _(arg):
	return arg


# Add-on information variables
addon_info = {
	# add-on Name/identifier, internal for NVDA
	"addon_name": "zwxybrl",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on
	# to be shown on installation and add-on information found in Add-ons Manager.
	"addon_summary": _("Chinese XingYi Braille"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description": _("""A set of braille tables and character descriptions enabling users to read/write Chinese by structure and meaning."""),
	# version
	"addon_version": "25.06",
	# Author(s)
	"addon_author": "笑笑鴿 <crazy@mail.batol.net>, Bo-Cheng Jhan <school510587@yahoo.com.tw>, and others",
	# URL for the add-on documentation support
	"addon_url": "https://github.com/school510587/zwxybrl/blob/main/README.md",
	# URL for the add-on repository where the source code can be found
	"addon_sourceURL": "https://github.com/school510587/zwxybrl",
	# Documentation file name
	"addon_docFileName": "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
	"addon_minimumNVDAVersion": "2024.3",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion": "2025.1",
	# Add-on update channel (default is None, denoting stable releases,
	# and for development releases, use "dev".)
	# Do not change unless you know what you are doing!
	"addon_updateChannel": None,
	# Add-on license such as GPL 2
	"addon_license": "GPL 3.0",
	# URL for the license document the ad-on is licensed under
	"addon_licenseURL": "https://github.com/school510587/zwxybrl/blob/main/LICENSE",
}

# Define the python files that are the sources of your add-on.
# You can either list every file (using ""/") as a path separator,
# or use glob expressions.
# For example to include all files with a ".py" extension from the "globalPlugins" dir of your add-on
# the list can be written as follows:
# pythonSources = ["addon/globalPlugins/*.py"]
# For more information on SCons Glob expressions please take a look at:
# https://scons.org/doc/production/HTML/scons-user/apd.html
pythonSources = [
	"addon/*.py",
	"addon/globalPlugins/*/*.py",
]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []

# Base language for the NVDA add-on
# If your add-on is written in a language other than english, modify this variable.
# For example, set baseLanguage to "es" if your add-on is primarily written in spanish.
baseLanguage = "zh_TW"

# Markdown extensions for add-on documentation
# Most add-ons do not require additional Markdown extensions.
# If you need to add support for markup such as tables, fill out the below list.
# Extensions string must be of the form "markdown.extensions.extensionName"
# e.g. "markdown.extensions.tables" to add tables.
markdownExtensions = []

# Custom braille translation tables
# If your add-on includes custom braille tables (most will not), fill out this dictionary.
# Each key is a dictionary named according to braille table file name,
# with keys inside recording the following attributes:
# displayName (name of the table shown to users and translatable),
# contracted (contracted (True) or uncontracted (False) braille code),
# output (shown in output table list),
# input (shown in input table list).
brailleTables = {
	"zzh-tw---ncb_che.ctb": {
		# Translators: Name of the XingYi braille translation table
		"displayName": _("Chinese XingYi Braille"),
		"contracted": False,
		"output": True,
		"input": False,
	},
	"zz-nosp.ctb": {
		# Translators: Name of the XingYi braille (without bopomofo) translation table
		"displayName": _("Chinese XingYi Braille (without bopomofo)"),
		"contracted": False,
		"output": True,
		"input": False,
	},
	"zzh-tw---char.ctb": {
		# Translators: Name of the XingYi braille translation table (helper version for character descriptions)
		"displayName": _("Chinese XingYi Braille (helper version for character descriptions)"),
		"contracted": False,
		"output": True,
		"input": False,
	},
}

# Custom speech symbol dictionaries
# Symbol dictionary files reside in the locale folder, e.g. `locale\en`, and are named `symbols-<name>.dic`.
# If your add-on includes custom speech symbol dictionaries (most will not), fill out this dictionary.
# Each key is the name of the dictionary,
# with keys inside recording the following attributes:
# displayName (name of the speech dictionary  shown to users and translatable),
# mandatory (True when always enabled, False when not.
symbolDictionaries = {}
