"""Raspberry Pi Face Recognition Treasure Box
Treasure Box Class
Copyright 2013 Tony DiCola
Copyright 2014 Vaila Ruthvik(ruthvik.nitc@gmail.com)
This code can be sujected to any kind of editions and distributions provided the names of
previous writers are provided as above.
"""
import time

import cv2
import RPIO
from RPIO import PWM

import picam
import config
import face


class GPIO(object):
	"""Class to represent the state and encapsulate access to the hardware of 
	the treasure box."""
	def __init__(self):
		# Initialize button.
		RPIO.setup(config.BUTTON_PIN, RPIO.IN)
		# Set initial button state.
		self.button_state = RPIO.input(config.BUTTON_PIN)
		self.is_locked = None

	def is_button_up(self):
		"""Return True when the box button has transitioned from down to up (i.e.
		the button was pressed)."""
		old_state = self.button_state
		self.button_state = RPIO.input(config.BUTTON_PIN)
		# Check if transition from down to up
		if old_state == config.BUTTON_DOWN and self.button_state == config.BUTTON_UP:
			# Wait 20 milliseconds and measure again to debounce switch.
			time.sleep(20.0/1000.0)
			self.button_state = RPIO.input(config.BUTTON_PIN)
			if self.button_state == config.BUTTON_UP:
				return True
		return False
