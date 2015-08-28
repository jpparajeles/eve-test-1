# -*- coding: utf-8 -*-

"""
    Eve Demo
    ~~~~~~~~

    A demostration of a simple API powered by Eve REST API.

    The live demo is available at eve-demo.herokuapp.com. Please keep in mind
    that the it is running on Heroku's free tier using a free MongoHQ
    sandbox, which means that the first request to the service will probably
    be slow. The database gets a reset every now and then.

    :copyright: (c) 2015 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os
import bcrypt
from eve import Eve
from eve.auth import BasicAuth
from flask_sslify import SSLify
import custom

class RolesAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['anvandaren']
        lookup = {'anvandarnamn': username}
        if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['roll'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        return account and bcrypt.hashpw(password, account['losenord']) == account['losenord']




# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'

app = Eve(auth=RolesAuth)
if 'DYNO' in os.environ: # only trigger SSLify if the app is running on Heroku
    sslify = SSLify(app,permanent=True, subdomains=True)

# app.on_pre_POST_anvandaren += custom.pre_anvandaren_post_callback
app.on_insert_anvandaren += custom.ch_pass
app.on_insert_log += custom.log_log

if __name__ == '__main__':
    app.run(host=host, port=port)
