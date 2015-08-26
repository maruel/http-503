# Copyright (c) 2010 Marc-Antoine Ruel. All rights reserved.
# Use of this source code is governed by Apache 2.0 license that can be
# found at http://www.apache.org/licenses/LICENSE-2.0.html

"""Returns a HTTP code on all requests."""

import webapp2


class Error(webapp2.RequestHandler):
  # http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
  error_code = 503

  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Get lost.')
    self.response.set_status(self.error_code)

  def post(self):
    self.response.set_status(self.error_code)


class Redirect(webapp2.RequestHandler):
  # Put the new host there.
  new_host = 'my.new.host.com'

  def redirect_all(self):
    dest_url = '%s://%s%s' % (
        self.request.scheme, self.new_host, self.request.path_qs)
    self.redirect(dest_url, permanent=True)

  def get(self):
    self.redirect_all()

  def post(self):
    self.redirect_all()


app = webapp2.WSGIApplication([('.*', Error)], debug=False)
#app = webapp2.WSGIApplication([('.*', Redirect)], debug=False)
