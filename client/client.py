from flask import Flask, render_template, request, redirect, flash, send_file, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from split_util import split_into_files  
from join_util import join_files
from connection import send_grpc
import os
import requests

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SPLIT_FOLDER'] = 'file_chunks/'
app.config['JOINED_FOLDER'] = 'joined_files/'
app.secret_key = 'development_key'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html', datos={})

@app.route('/do_login', methods=['POST'])
def do_login():
    body = {
        "username": request.form['username'],
        "password": request.form['password']
    }

    response = requests.post('http://localhost:5000/login', json=body)
    print(response.json()['status'])
    if (response.json()['status'] == True):
        return redirect('/')
    else:
        return render_template('login.html', datos=response.json())


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['input_file']
    if file and file.filename != '':
        filename = secure_filename(file.filename)
        input_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_file_path)
        print(f"Archivo subido a: {input_file_path}")

        split_response = split_into_files(input_file_path, os.path.join(app.config['SPLIT_FOLDER'], filename), 1024)

        response = requests.post('http://localhost:5000/add-files', json=split_response)
        if response.json()["status"]:
            file_info = response.json()["data_file"]
            nodes_info = response.json()["data_node"]
            send_grpc(file_info, nodes_info)
        print(response.content)

        flash('File successfully uploaded and split!')
        return redirect(url_for('index'))

    else:
        flash('No file selected or file type not allowed.')
        return redirect(request.url)


@app.route('/download/<file_name>')
def download_file(file_name):
    try:
        joined_folder = app.config['JOINED_FOLDER']
        joined_file_path = join_files(file_name, joined_folder)
        return send_file(joined_file_path, as_attachment=True)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/search_files', methods=['POST'])
def search_files_route():
    file_name = request.form.get('file_name', '')
    response = requests.post('http://localhost:5000/search_files', json={"file_name": file_name})
    if response.status_code == 200:
        files = response.json().get("files", [])
        print(f"Archivos encontrados: {files}")
    else:
        files = []
    return render_template('index.html', files=files)


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5001)
