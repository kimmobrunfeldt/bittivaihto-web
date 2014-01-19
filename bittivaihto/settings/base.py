# -*- coding: utf-8 -*-
"""
    bittivaihto.settings.base
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains global application settings that are common to all
    environments.
"""
import os

#
# Paths
# -----

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)
)
NODE_MODULES_BIN = os.path.join(
    PROJECT_ROOT, os.pardir, 'node_modules', '.bin'
)


#
# Debug Toolbar
# -------------

# Set this to True, if you want Debug Toolbar to intercept redirects.
DEBUG_TB_INTERCEPT_REDIRECTS = False


#
# Webassets
# ---------

# Enable/disable webassets debug mode. Possible values are:
#
# False
#     Production mode. Bundles will be merged and filters applied.
# True
#     Enable debug mode. Bundles will output their individual source
#     files.
# 'merge'
#     Merge the source files, but do not apply filters.
ASSETS_DEBUG = True

# Controls whether bundles should be automatically built, and rebuilt, when
# required (if set to True), or whether they must be built manually be the
# user, for example via a management command.
#
# This is a good setting to have enabled during debugging, and can be very
# convenient for low-traffic sites in production as well. However, there is a
# cost in checking whether the source files have changed, so if you care about
# performance, or if your build process takes very long, then you may want to
# disable this.
#
# By default automatic building is enabled, when debugging is enabled.
ASSETS_AUTO_BUILD = True

# Path to the CoffeeScript binary
COFFEE_BIN = os.path.join(NODE_MODULES_BIN, 'coffee')

# Path to the LessCSS binary
LESS_BIN = os.path.join(NODE_MODULES_BIN, 'lessc')

# Path to the UglifyJS binary
UGLIFYJS_BIN = os.path.join(NODE_MODULES_BIN, 'uglifyjs')

#
# Webassets
# ---------
CSRF_ENABLED = False
