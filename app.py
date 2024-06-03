from flask import Flask, request, render_template, send_file
from steganography import encode_text, decode_text
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    image_file = request.files['image']
    text = request.form['text']
    
    image = Image.open(image_file)
    encoded_image = encode_text(image, text)
    
    byte_io = io.BytesIO()
    encoded_image.save(byte_io, 'PNG')
    byte_io.seek(0)
    
    return send_file(byte_io, mimetype='image/png', as_attachment=True, download_name='encoded_image.png')

@app.route('/decode', methods=['POST'])
def decode():
    image_file = request.files['image']
    image = Image.open(image_file)
    
    decoded_text = decode_text(image)
    
    return decoded_text

if __name__ == '__main__':
    app.run(debug=True)
