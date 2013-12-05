import urlparse

from fabric.api import env, local, require, settings

from bittivaihto.settings.development import SQLALCHEMY_DATABASE_URI


def staging():
    """Use staging environment."""
    env.stage = 'staging'


def production():
    """Use production environment."""
    env.stage = 'production'


def _requirements():
    require('stage', provided_by=[staging, deploy])


def push():
    """Push the latest code to the server."""
    _requirements()
    local('git push %(stage)s master' % env)


def syncdb():
    """Synchronize the models with the database."""
    _requirements()
    local('heroku run --remote "%(stage)s" "python manage.py syncdb"' % env)


def deploy():
    """Do a full deploy."""
    _requirements()
    push()
    syncdb()


def shell():
    _requirements()
    local('heroku run --remote %(stage)s "python manage.py shell"' % env)


def copy_postgres(destination=None):
    """Copy PostgreSQL database to staging or local machine."""
    _requirements()
    assert destination in ('staging', 'local')

    local('heroku pgbackups:capture --remote %(stage)s --expire' % env)
    capture_url = local(
        'heroku pgbackups:url --remote %(stage)s' % env, capture=True
    )

    if destination == 'staging':
        local(
            'heroku pgbackups:restore DATABASE "%(capture_url)s" '
            '--remote staging' % dict(
                capture_url=capture_url
            )
        )
    else:
        urlparse.uses_netloc.append('postgres')
        database_uri = urlparse.urlparse(SQLALCHEMY_DATABASE_URI)
        local('curl -o capture.dump "%(capture_url)s"' % dict(
            capture_url=capture_url)
        )
        with settings(warn_only=True):
            arguments = [
                'pg_restore',
                '--verbose',
                '--clean',
                '--no-acl',
                '--no-owner',
                '--host=%s' % database_uri.hostname,
                '--dbname=%s' % database_uri.path[1:],
            ]
            if database_uri.port:
                arguments.append('--port=%s' % database_uri.port)
            if database_uri.username:
                arguments.append('--username=%s' % database_uri.username)
            arguments.append('capture.dump')
            local(' '.join(arguments))
