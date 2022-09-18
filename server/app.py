import os

import colorgram
import numpy
import scipy.cluster
import sklearn.cluster
from flask import Flask, jsonify, render_template, request
from PIL import Image
from webcolors import rgb_to_hex

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./upload/"


@app.route("/")
def index():
    return render_template("index.html")


def getDominantColorsFromImage(path):
    image = Image.open(path)
    image = image.resize((150, 150))      # optional, to reduce time
    ar = numpy.asarray(image)
    shape = ar.shape
    ar = ar.reshape(numpy.product(shape[:2]), shape[2]).astype(float)

    kmeans = sklearn.cluster.MiniBatchKMeans(
        n_clusters=10,
        init="k-means++",
        max_iter=20,
        random_state=1000
    ).fit(ar)
    codes = kmeans.cluster_centers_

    vecs, _dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, _bins = numpy.histogram(vecs, len(codes))    # count occurrences

    colors = []
    for index in numpy.argsort(counts)[::-1]:
        colors.append(tuple([int(code) for code in codes[index]]))
    finalRGBVals = []
    for color in colors[:3]:
        finalRGBVals.append(rgb_to_hex(color))
    return finalRGBVals


def getColorsFromImage(path):
    # Extract colors from an image.
    path = ".\\"+path
    print(path)
    colors = colorgram.extract(path, 4)
    finalRGBVals = []
    for color in colors:
        print(color.rgb)
        finalRGBVals.append(rgb_to_hex(color.rgb))
    return finalRGBVals


@app.route("/api/v1/get", methods=['POST'])
def getPalette():
    print(request.files)
    file1 = request.files['image']
    path1 = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
    file1.save(path1)
    finalRGBVals = getColorsFromImage(path1)
    return jsonify({
        'colors': finalRGBVals,
    })


if __name__ == "__main__":
    app.run(debug=True)
