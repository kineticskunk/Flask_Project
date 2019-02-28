from flask_project import application , db

# Run Sever
if __name__ == '__main__':
	db.create_all()
	application.run(debug=True)
