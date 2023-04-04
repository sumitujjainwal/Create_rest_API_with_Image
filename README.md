# Create_rest_API_with_Image
Now firstly upload the image then import the libraries like numpy as np
from glob import globmage
import cv2
from PIL import image as img.
then my_image = glob('shishldin.jpg') that is the image name.
then my_image = cv2.imread(my_image[0]).
now print (my_image[0]).
print(my_image.size) here, you can see the image and image size also and you can see your image shape also.
print(my_image.shape[1]).



LEARNING OBJECTIVES...
Create this api with using a flask. and pycharm also.
Import the flask libraries.

FLASK.....
Flask is a popular Python web framework that allows developers to build web applications quickly and efficiently. 
It is classified as a micro-framework, which means it provides minimal tools for building web applications and leaves many design decisions up to the developer.
Flask is lightweight and easy to learn, making it a great choice for small to medium-sized web projects. Some of its key features include support for handling HTTP requests, URL routing, session management, and integration with various database systems.
Flask also has a large and active community, which means developers can easily find support and resources online.


RESULT........
import flask library and jsonify.
from flask import flask .
import cv2.
app = flask(__name__).
using the one of the main library of flask @app.route('/',methods=['get'])

Here is the image details.
[ "Hight = 580, width = 860",
"R = 106, G =123, B = 151",
"B=151"
]
