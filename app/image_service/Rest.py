from flask import Flask, request, send_from_directory, jsonify
from PIL import Image
from io import BytesIO
import os
import time
import base64
import random
import string

app = Flask(__name__)


def generate_random_name(length):
    """В Image.save() необходим обязательный аргумент с сохраняемым именем файла, если его указать прямо,
    то больше одной картинки сохранить невозможно. Для решения этой проблемы написана функция, генерирующая рандомные
    имена."""
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


@app.route('/')
def hello():
    return jsonify('Hello!'), 200


@app.route('/image', methods=['GET'])
def get_images_info():
    """Выводит список изображений в JSON формате который содержит имя файла, размер, время последнего изменения."""
    res = {}
    for i in os.listdir('images'):
        res[i] = [time.ctime(os.path.getmtime(os.path.abspath(os.path.join('images', i)))),
                  str(os.stat(os.path.abspath(os.path.join('images', i))).st_size / 1024) + ' kilobytes']
    return jsonify(res), 200


@app.route('/image', methods=['POST'])
def base64_upload():
    """Создает новое изображение из переданной base64 строки.
    example:
    endpoint: http://<hostname>:<port>/image
    POST JSON {"file": "your_base64_string"}"""
    try:
        file = request.get_json()
        data = file.get('file')
        im = Image.open(BytesIO(base64.b64decode(data))).convert('RGB')
        filename = generate_random_name(3) + '.jpg'
        im.save(os.path.join('images', filename), 'JPEG')
        return jsonify(f"file {filename} added to 'images' folder"), 201
    except Exception:
        return jsonify('Incorrect JSON or base64 string.'), 400


@app.route('/image', methods=['DELETE'])
def delete_image():
    """Удаляет изображение по его имени.
    example:
    http://<hostname>:<port>/image?filename=<filename>.jpg"""
    try:
        filename = request.args.get('filename')
        os.remove(os.path.join('images', filename))
        return jsonify(f" file {filename} has been deleted"), 200
    except Exception:
        return jsonify('Incorrect filename in args.'), 404


@app.route('/images/<filename>', methods=['GET'])
def image_preview(filename):
    """Отдает изображения из images по эндпоинту.
     example:
     http://<hostname>:<port>/images/<filename>.jpg"""
    try:
        return send_from_directory('images', filename), 200
    except Exception:
        return jsonify('Incorrect filename.'), 404


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
