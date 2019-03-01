import logging
from routes import db
from routes import application
# Run Sever
if __name__ == '__main__':
	db.create_all()
	logging.debug("created db models")
	application.run(debug=True)
	logging.debug("running application")
