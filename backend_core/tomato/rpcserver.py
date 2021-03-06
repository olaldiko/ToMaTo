#!/usr/bin/python
# -*- coding: utf-8 -*-

# ToMaTo (Topology management software) 
# Copyright (C) 2010 Dennis Schwerdel, University of Kaiserslautern
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys

from . import api
from .lib import util, sslrpc2, logging, exceptionhandling  #@UnresolvedImport
from .lib.error import Error, UserError, InternalError

from lib.settings import settings

import ssl

def logCall(function, args, kwargs):
	logging.log(category="api", method=function.__name__, args=args, kwargs=kwargs)

def handleError(error, function, args, kwargs):
	if not isinstance(error, Error):
		if isinstance(error, TypeError) and function.__name__ in str(error):
			error = UserError.wrap(error, data={"function": function.__name__, "args": args, "kwargs": kwargs})
		else:
			error = InternalError.wrap(error, data={"function": function.__name__, "args": args, "kwargs": kwargs})
	exceptionhandling.writedown_current_exception(exc=error)
	return error

def runServer(server):
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		pass

global server

def start():
	global server
	print >>sys.stderr, "Starting RPC server..."
	def wrapError(error, method, args, kwargs):
		error = handleError(error, method, args, kwargs)
		return sslrpc2.Failure(error.raw)
	for config in settings.get_own_interface_config():
		server = sslrpc2.Server(('0.0.0.0', config['port']), beforeExecute=logCall, onError=wrapError, keyfile=settings.get_ssl_key_filename(),
							certfile=settings.get_ssl_cert_filename(), ca_certs=settings.get_ssl_ca_filename(), cert_reqs=ssl.CERT_REQUIRED)
		server.registerContainer(api)
		util.start_thread(server.serve_forever)
		print >>sys.stderr, "done."

def stop():
	server.shutdown()