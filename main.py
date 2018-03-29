from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG']= True
wc_form="""
<!DOCTYPE html>
<html>
	<head>
		<style>
			form {{
				background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
			}}
			textarea {{
				margin: 10px 0;
                width: 540px;
                height: 120px;
			}}
		</style>
	</head>
	<body>
		<form action="/encrypt" method="POST">
			<label for="rot">Pick a Number</label>
			<input id="rotation" name="rot" type="text" value="0" />
			<br>
			<textarea type="text" name="message">{0}</textarea>
			<br>
			<input type="submit" />
		</form>
	</body>
</html>"""
@app.route('/')
def index():
	inny=wc_form.format("")
	return inny

@app.route('/encrypt', methods=["POST"])
def encrypt():
	mess=str(request.form['message'])
	rott=int(request.form['rot'])
	result=rotate_string(mess,rott)
	outty=wc_form.format(result)
	return outty

app.run()
