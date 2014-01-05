import newrelic.agent

from . import Application

app = Application()

@app.route("/google78fada8781858043.html")
def site_verification():
    """Returns site verification content"""
    return 'google-site-verification: google78fada8781858043.html'


app = newrelic.agent.wsgi_application()(app.wsgi_app)
