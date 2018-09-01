import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import os
import json
import datetime
from save import process,save_txt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
options = {
	'model': 'cfg/yolo-face.cfg',
	'load': 'yolo-face.weights',
	'threshold': 0.244555,
	'gpu': 1.0
}
tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]
writer = None
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 618)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 416)
videowriter = None
while True:
	stime = time.time()
	ret, frame = capture.read()
	if ret:
		results = tfnet.return_predict(frame)
		for color, result in zip(colors, results):
			times = str(datetime.datetime.now())
			times = times[:22]	
			process(color, result,frame, times)
			cv2.imshow('frame', frame)
			save_txt(results, times)
			print('FPS {:.1f}'.format(1 / (time.time() - stime)))
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
cv2.destroyAllWindows()
capture.release()
writer.release()
