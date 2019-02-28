from flask_project import app , db

# Run Sever
if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)
