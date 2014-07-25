"""Raspberry Pi Face Recognition Treasure Box 
Pi Camera OpenCV Capture Device

Copyright 2014 Vaila Ruthvik(ruthvik.nitc@gmail.com)
Copyright 2013 Tony DiCola
Courtesy OpenCv

Pi camera device capture class for OpenCV.  This class allows you to capture a
single image from the pi camera as an OpenCV image.
"""
import io
import time

import cv2
import numpy as np
import picamera

import config


class OpenCVCapture(object):
	def read(self):
		"""Read a single frame from the camera and return the data as an OpenCV
		image (which is a numpy array).
		"""
		# This code is based on the picamera example at:
		# http://picamera.readthedocs.org/en/release-1.0/recipes1.html#capturing-to-an-opencv-object
		# Capture a frame from the camera.
		data = io.BytesIO() # operating with binary data
		with picamera.PiCamera() as camera:
			camera.capture(data, format='jpeg') #capture an image from the camera and storing it in output
		data = np.fromstring(data.getvalue(), dtype=np.uint8) #uint8 is used in graphics (colors have generally non -ve values)
		# Decode the image data and return an OpenCV image.
		image = cv2.imdecode(data, 1)   #imdecode reads an image from buffer and 1 will force the data to be a clolor image. 
		# Save captured image for debugging.
		cv2.imwrite(config.DEBUG_IMAGE, image) #saves an image to a specified file.
		# Return the captured image data.
		return image
