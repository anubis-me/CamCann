import cv2
import time
import datetime

def process(color, result, frame):
	tl = (result['topleft']['x'], result['topleft']['y'])
	br = (result['bottomright']['x'], result['bottomright']['y'])
	label = result['label']
	confidence = result['confidence']
	text = '{}: {:.0f}%'.format(label, confidence * 100,2)
	xxx = '{:.0f}'.format(confidence * 100,2)
	xxx = int(xxx)
	frame = cv2.rectangle(frame, tl, br, color, 2)
	frame = cv2.putText(
	frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
	frame = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY )
	if (xxx>20):
		save(frame,tl,br)


def save(frame,tl,br):
	crop_img = frame[(tl[1]):(br[1]),(tl[0]):(br[0])]
	cv2.imwrite("face/"+"face"+str(datetime.datetime.now())+".png", crop_img)


def save_txt(results):
	print(results)
	f = open('data/face.txt', 'a')
	if(results!=[]):
		for jj in results:
			if jj['label']:
				f.write("[")
				f.write('"'+str(datetime.datetime.now())+'"')
				f.write(',"')
				f.write('%s' %jj['confidence'])
				f.write(']')
	f.close()
