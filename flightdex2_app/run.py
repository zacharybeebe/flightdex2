from flightdex2_app import app, REDO_DATABASE


if __name__ == '__main__':
	no_debug = False
	debug = True
	if REDO_DATABASE or no_debug:
		debug = False
		host = '0.0.0.0'

	else:
		host = 'localhost'

	app.run(host=host, port=5000, debug=debug)
