from flask import Flask, jsonify
import cv2


app = Flask(__name__)

@app.route('/', methods=['get'])
def main():
        image = cv2.imread('shishaldin.jpg')

        h, w = image.shape[:2]

        h_w = ("Height = {},  Width = {}".format(h, w))

        (B, G, R) = image[100, 100]

        B_G_R = ("R = {}, G = {}, B = {}".format(R, G, B))

        B = image[100, 100, 0]
        x = ("B = {}".format(B))
        return jsonify(h_w, B_G_R, x)
    # return jsonify(main())

if __name__ == '__main__':
    app.run(debug=True)
