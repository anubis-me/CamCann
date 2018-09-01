import cv2
import time
import datetime

def process(color, result, frame,times):
	tl = (result['topleft']['x'], result['topleft']['y'])
	br = (result['bottomright']['x'], result['bottomright']['y'])
	label = result['label']
	confidence = result['confidence']
	text = '{}: {:.0f}%'.format(label, confidence * 100,2)
	xxx = '{:.0f}'.format(confidence * 100,2)
	xxx = int(xxx)
	#frame = cv2.rectangle(frame, tl, br, color, 2)
	#frame = cv2.putText(
	#frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
	if (xxx>44):
		y1=tl[1]
		y2=br[1]
		x1=tl[0]
		x2=br[0]	
		save(frame,tl,br,times, x1, x2, y1, y2,label)
		

def save(frame,tl,br,times, x1, x2, y1, y2,label):
	crop_img = frame[y1:y2,x1:x2]
	cv2.imwrite("images/"+label+times+".png", crop_img)
	

def save_txt(results, times):
	print(results)
	f = open('data/face.txt', 'a')
	if(results!=[]):
		for jj in results:
			if jj['label']:
				f.write("[")
				f.write('"'+times+'"')
				f.write(', "')
				f.write('%s' %jj['confidence'])
				f.write('" ,')
				f.write(' "camera1" ')
				f.write(',')
				f.write(' "url" ')
				f.write(',"')
				f.write('%s' %jj['label'])
				f.write('",')
				f.write('%s' %jj['topleft'])
				f.write(',')
				f.write('%s' %jj['bottomright'])
				f.write(']')
	f.close()
