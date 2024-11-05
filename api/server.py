from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET'])
def landingPage():  
    return render_template("main.html")

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'response': 'Failed, file not found!'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'response': 'Failed, no file selected!'}), 400
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    return jsonify({'response': 'Success, file saved.'}), 200

if __name__ == "__main__":
    app.run(debug=True)
