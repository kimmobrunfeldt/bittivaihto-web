from flask import template_rendered

from socialpainting import Application
from socialpainting.extensions import db


class ContextVariableDoesNotExist(Exception):
    pass


class TestCase(object):
    def create_app(self):
        """
        Create your Flask app here, with any configuration you need.
        """
        return Application('test')

    def setup_method(self, method):
        self.app = self.create_app()

        self.client = self.app.test_client()

        self._ctx = self.app.test_request_context()
        self._ctx.push()

        db.create_all()

        self.templates = []
        template_rendered.connect(self._add_template)

    def _add_template(self, app, template, context):
        self.templates.append((template, context))

    def teardown_method(self, method):
        del self.client

        db.drop_all()
        db.session.remove()

        self._ctx.pop()

        template_rendered.disconnect(self._add_template)

    def assert_template_used(self, name):
        """
        Checks if a given template is used in the request.

        :param name: template name
        """
        for template, context in self.templates:
            if template.name == name:
                return True
        raise AssertionError("template %s not used" % name)

    def get_context_variable(self, name):
        """
        Returns a variable from the context passed to the template.

        Raises a ContextVariableDoesNotExist exception if does
        not exist in context.

        :param name: name of variable
        """
        for template, context in self.templates:
            if name in context:
                return context[name]
        raise ContextVariableDoesNotExist

    def assert_context(self, name, value):
        """
        Checks if given name exists in the template context and equals the
        given value.

        :param name: name of context variable
        :param value: value to check against
        """

        try:
            assert self.get_context_variable(name) == value
        except ContextVariableDoesNotExist:
            self.fail("Context variable does not exist: %s" % name)

    def assert_redirects(self, response, location):
        """
        Checks if response is an HTTP redirect to the given location.

        :param response: Flask response
        :param location: relative URL (i.e. without **http://localhost**)
        """
        assert response.status_code in (301, 302)
        assert response.location == "http://localhost" + location

    def assert_status(self, response, status_code):
        """
        Helper method to check matching response status.

        :param response: Flask response
        :param status_code: response status code (e.g. 200)
        """
        assert response.status_code == status_code

    def assert200(self, response):
        """
        Checks if response status code is 200

        :param response: Flask response
        """

        self.assert_status(response, 200)

    def assert400(self, response):
        """
        Checks if response status code is 400

        :param response: Flask response
        """

        self.assert_status(response, 400)

    def assert401(self, response):
        """
        Checks if response status code is 401

        :param response: Flask response
        """

        self.assert_status(response, 401)

    def assert403(self, response):
        """
        Checks if response status code is 403

        :param response: Flask response
        """

        self.assert_status(response, 403)

    def assert404(self, response):
        """
        Checks if response status code is 404

        :param response: Flask response
        """

        self.assert_status(response, 404)

    def assert405(self, response):
        """
        Checks if response status code is 405

        :param response: Flask response
        """

        self.assert_status(response, 405)
