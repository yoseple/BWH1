from flask import Flask, request, render_template, send_file, url_for, jsonify, redirect
import nibabel as nib
import os
from threading import Thread
from totalsegmentator.python_api import totalsegmentator

app = Flask(__name__)
output_dir = 'processed_files'
os.makedirs(output_dir, exist_ok=True)

processing_status = {"is_processing": False, "result_file_name": None}

def process_image(input_file_path):
    global processing_status
    processing_status["is_processing"] = True
    try:                    
        result_nifti_image = totalsegmentator(input=input_file_path, output=output_dir, task="vertebrae_body")
        result_file_name = "result_segmentation.nii.gz"
        result_file_path = os.path.join(output_dir, result_file_name)
        nib.save(result_nifti_image, result_file_path)
        processing_status["result_file_name"] = result_file_name
    except Exception as e:
        processing_status["result_file_name"] = f"Error: {e}"
    finally:
        processing_status["is_processing"] = False
        

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/loading')
def loading():
    return render_template("loading.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file:
            input_file_path = os.path.join(output_dir, uploaded_file.filename)
            uploaded_file.save(input_file_path)
            Thread(target=process_image, args=(input_file_path,)).start()
            return redirect(url_for('loading'))

    return "No file uploaded"

@app.route('/check_status')
def check_status():
    return jsonify(processing_status)

@app.route('/final_page/<result_file_name>')
def final_page(result_file_name):
    return render_template("nii2mesh.html", download_link=url_for('download_file', file_name=result_file_name))

@app.route('/download/<file_name>')
def download_file(file_name):
    file_path = os.path.join(output_dir, file_name)
    if os.path.exists(file_path):
        app.logger.info(f"Sending file: {file_path}")
        return send_file(file_path, as_attachment=True, download_name=file_name)
    else:
        app.logger.error(f"File not found: {file_path}")
        return "File not found", 404


if __name__ == '__main__':
    app.run(debug=True)
