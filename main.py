from flask import Flask, request
from caesar import rotate_string, alphabet_position

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
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
            h2 {{
				margin: 0 auto;
				text-align: center;
			}}
        </style>
    </head>
    <body>
      <form method='POST'>
		<label>{1}: 
		<input name="rot" type="text" value="0" />
		</label>
		<textarea name="text">{0}</textarea>
		<input type="submit" value="Encrypt" />
		<input type="reset" value="Clear Text" />
      </form>
      <br>
      <h2>{2}? <a href="{4}">click here</a> for {3} Cipher instead.</h2>
    </body>
</html>
'''

@app.route('/')
def index():
	return form.format('','Rotate by','Caesar not secure enough','Vigenere','./vigenere')
	
@app.route('/', methods=['POST'])
def encrypt():
	rot = request.form['rot']
	text = request.form['text']
	message = rotate_string(text, rot)
	return form.format(message,'Rotate by','Caesar not secure enough','Vigenere','.vigenere')

@app.route('/vigenere', methods=['GET'])
def blank_vig():
	return form.format('','Key','Vigenere too secure','Caesar','..')

@app.route('/vigenere', methods=['POST'])
def vigenere():
	key = request.form['rot']
	text = request.form['text']
	return text
	
app.run()
