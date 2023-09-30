#! /usr/bin/env python

from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route('/render')
def render():
    # Handle render request
    # blender -b ~/doc/blender/bathroom/bathroom.blend -x 1 -o //render -a

    """
    Request should look something like this:
    {
        "file": "path/to/blend/file.blend"
    }
    """

    # Get JSON request
    req = request.json
    blendfile = req['file']

    # Command line render the blend file
    blender_proc = subprocess.run(['blender',
                                   '-b', blendfile,
                                   '-x', '1',
                                   '-o', '//render',
                                   '-f', '1'],
                                   capture_output=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)