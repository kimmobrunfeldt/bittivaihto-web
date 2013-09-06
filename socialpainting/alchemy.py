from flask import current_app
from flask.ext.storage import get_default_storage_class, MockStorage
import sqlalchemy as sa


class FileType(sa.types.TypeDecorator):
    """
    FileType for SQLAlchemy

    When the FileType value is being stored into database the FileType saves
    the filename as unicode in the associated column.

    When the value is fetched from database this type opens the associated
    UniStorage object.
    """
    impl = sa.types.UnicodeText

    def __init__(self, storage=None, upload_to=u'', *args, **kwargs):
        self._storage = storage
        self._upload_to = upload_to
        sa.types.TypeDecorator.__init__(self, *args, **kwargs)

    @property
    def storage(self):
        if self._storage:
            return self._storage
        try:
            return get_default_storage_class(current_app)()
        except RuntimeError:
            # return MockStorage if working outside of application context,
            # e.g. generating migrations
            return MockStorage()

    def process_bind_param(self, value, dialect):
        if value:
            if isinstance(value.name, str):
                return value.name.decode('utf8')
            else:
                return value.name

    def process_result_value(self, value, dialect):
        if not value:
            return self.storage.new_file(prefix=self._upload_to)
        return self.storage.file_class(
            self.storage,
            name=value.encode('utf8')
        )

    def copy(self):
        return FileType(self._storage, self._upload_to)
