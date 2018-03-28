from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG']= True

@app.route('/')
#heady = """<!DOCTYPE html>
#<html>
#	<head>
#		<style>
#			form {
#				background-color: #eee;
#                padding: 20px;
#                margin: 0 auto;
#                width: 540px;
#                font: 16px sans-serif;
#                border-radius: 10px;
#			}
#			textarea {
#				margin: 10px 0;
#                width: 540px;
#                height: 120px;
#			}
#		</style>
#	</head>"""
def index():
	wc_form="""
	<!DOCTYPE html>
	<html>
		<head>
			<style>
				form {
					background-color: #eee;
	                padding: 20px;
	                margin: 0 auto;
	                width: 540px;
	                font: 16px sans-serif;
	                border-radius: 10px;
				}
				textarea {
					margin: 10px 0;
	                width: 540px;
	                height: 120px;
				}
			</style>
		</head>
		<body>
			<form method="POST">
				<label for="rot">Pick a Number</label>
				<input name="rot" type="text" value="0" />
				<textarea type="text" name="text"></textarea>
				<input type="submit">
			</form>
		</body>
	</html>"""
	return wc_form
@app.route('/encrypt', methods=["POST"])
def encrypt():
	mess=str(request.wc_form['text'])
	rott=int(request.wc_form['rot'])
	result=rotate_string(mess,rott)
	return "<h1>"+result+"<h1>"

app.run()
