bittivaihto
===========

Requirements
------------

- Python 2.7
- PostgreSQL
- `Node.js <http://nodejs.org/>`_

Optional:

- `virtualenvwrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_
- autoenv


Development
-----------

Follow the instructions below to set up the development environment.

1. Create a virtualenv::

    $ mkvirtualenv bittivaihto

2. Make the virtualenv activate automagically when traversing inside the
   project directory:

    $ echo -e "workon bittivaihto\n" > .env

3. Install Python dependencies::

    $ pip install -r requirements-dev.txt

4. Install Node.js dependencies::

    $ npm install

5. Create database for development and testing::

    $ createdb bittivaihto
    $ createdb bittivaihto_test

6. Create database tables::

    $ python manage.py syncdb

7. Finally, start the development server::

    $ python manage.py runserver


Copying the production database to the development environment
--------------------------------------------------------------

1. Re-create the development database::

    $ dropdb pelsu
    $ createdb pelsu

2. Copy the production database to the development database::

    $ fab production copy_postgres:local


Testing
-------

You can run the tests with `py.test <http://pytest.org>`_::

    $ py.test


Setting up the Heroku application
---------------------------------

If someone has already created the Heroku applications for this project, you
only need to add the following Git remotes to your local Git clone::

  $ git remote add production git@heroku.com:pelastussuunnitelma.git
  $ git remote add staging git@heroku.com:pelastussuunnitelma-staging.git

Otherwise, follow the steps below to create the Heroku applications for this
project.

1. Create a new Heroku application.::

    $ heroku apps:create bittivaihto \
        --buildpack https://github.com/fastmonkeys/heroku-buildpack-flask.git \
        --remote production

   Change the project name and remote argument, if you are creating a staging
   application. The above command assumes you are creating a production
   application.

2. Enable environmental variables during the slug compilation phase::

    $ heroku labs:enable user_env_compile --remote production

3. Set the application to use production environment::

    $ heroku config:add FLASK_ENV=production --remote production

4. Generate a secret key for the application::

    $ heroku config:add SECRET_KEY=`python manage.py generate_secret_key` \
        --remote production

5. Add Heroku PostgreSQL addon to the application for relational database
   support::

    $ heroku addons:add heroku-postgresql:dev --remote production
    $ heroku pg:promote HEROKU_POSTGRESQL_COLOR --remote production

6. (Optional) Add New Relic addon to the application, if you want to monitor
   application's performance::

    $ heroku addons:add newrelic --remote production


Deploying to Heroku
-------------------

Deploying the application to Heroku is really easy.

If you are deploying to production::

    $ fab production deploy

If you are deploying to staging::

    $ fab staging deploy

This simple command will take care of

- pushing new code to Heroku
- migrating the database to the latest revision.
