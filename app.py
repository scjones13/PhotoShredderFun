import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "shredder_secret_key_123"  # For development purposes
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'static/uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/embed')
def embed():
    """Render the embedded version of the shredder"""
    return render_template('embed.html')

@app.route('/get-embed-code')
def get_embed_code():
    """Generate embed code for the shredder"""
    host = request.host_url.rstrip('/')
    embed_code = f'<iframe src="{host}/embed" width="800" height="600" frameborder="0" style="max-width: 100%;"></iframe>'
    return jsonify({'embed_code': embed_code})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
