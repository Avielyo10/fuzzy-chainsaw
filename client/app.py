#!/usr/bin/python3

import shutil
import os
import time
from flask import Flask, send_file, Response

app = Flask(__name__)


@app.route('/api/v1/get_zip', methods=['GET'])
def get_zip():
    if len(os.listdir('/home/avielyosef/Desktop/to-zip')) == 0:
        try:
            os.remove("to-zip.zip")
        except FileNotFoundError:
            pass
        return Response(status=404)
    else:
        shutil.make_archive(
            'to-zip', 'zip', '/home/avielyosef/Desktop', 'to-zip')
        send_file("to-zip.zip", mimetype='zip',
                  attachment_filename='my-zip.zip', as_attachment=True)
        return Response(status=200)


if __name__ == '__main__':
    app.run(debug=True)
