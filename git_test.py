from flask import Flask

app = Flask(__name__)

@app.route('/')
def top_page():
	return 'Here is root page'

if __name__ == '__main__':
	app.run()
