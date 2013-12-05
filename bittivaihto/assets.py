# -*- coding: utf-8 -*-
"""
    bittivaihto.assets
    ~~~~~~~~~~~~~~~~~~~~~

    This module contains static asset definitions.
"""

from flask.ext.assets import Bundle, Environment

assets = Environment()

less = Bundle(
    'stylesheets/site.less',
    debug=False,
    depends=[
        'stylesheets/**/*.css',
        'stylesheets/**/*.less',
    ],
    filters='less',
    output='stylesheets/less.css'
)

assets.register(
    'all-css',
    less,
    filters='cssmin',
    output='stylesheets/all.css',
)

coffeescripts = Bundle(
    'javascripts/site.coffee',
    debug=False,
    filters='coffeescript',
    output='javascripts/coffee.js'
)

assets.register(
    'all-js',
    'javascripts/vendor/jquery/jquery.js',
    coffeescripts,
    filters='uglifyjs',
    output='javascripts/all.js',
)
