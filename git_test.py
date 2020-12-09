from flask import Flask,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello():
	if request.method =="GET":
		return """
		整数入れて
		<form action="/" method="POST">
		<input name="num"></input>
		</form>"""
	else:
		try
			return """
			{}は{}です
			<form action="/" method="POST">
			<input name="num"></input>
			</form>""".format(str(request.form["num"]),["偶数","奇数"][int(request.form["num"])%2])
		except:
			return"""
			NG
			<form action="/" method="POST">
			<input name="num"></input>
			</form>"""
	
if __name__ == "__main__":
	app.run()
