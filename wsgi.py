from src.flask_project import application , db
import logging 
# Run Sever
if __name__ == '__main__':
	db.create_all()
	logging.warning("created db models")
	application.run(debug=True)
	logging.warning("running application")
