from flask.ext.security import UserMixin, RoleMixin

from bittivaihto.extensions import db


roles_users = db.Table(
    'user_role',
    db.Column(
        'user_id',
        db.Integer(),
        db.ForeignKey('user.id', ondelete='CASCADE'),
        primary_key=True
    ),
    db.Column(
        'role_id',
        db.Integer(),
        db.ForeignKey('role.id', ondelete='CASCADE'),
        primary_key=True
    )
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship(
        'Role',
        secondary=roles_users,
        backref=db.backref('users', lazy='dynamic')
    )
