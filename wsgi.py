import logging
from src.flask_project import application,db
# Run Sever
if __name__ == '__main__':
	db.create_all()
	logging.debug("created db models")
	application.run(debug=True)
	logging.debug("running application")
