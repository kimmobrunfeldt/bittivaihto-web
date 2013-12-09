# -*- coding: utf-8 -*-
"""
    audi.assets
    ~~~~~~~~~~~~

    This module contains static asset definitions.
"""

from flask.ext.assets import Bundle, Environment

assets = Environment()


assets.register(
    'all-css',
    Bundle(
        'stylesheets/site.less',
        depends=[
            'stylesheets/**/*.css',
            'stylesheets/**/*.less',
        ],
        filters='less',
        output='stylesheets/less.css'
    ),
    filters='cssmin',
    output='stylesheets/all.css',
)


assets.register(
    'all-js',
    'javascripts/vendor/jquery/jquery.js',
    Bundle(
        'javascripts/site.coffee',
        filters='coffeescript',
        output='javascripts/site-coffee.js'
    ),
    filters='uglifyjs',
    output='javascripts/site.js',
)
