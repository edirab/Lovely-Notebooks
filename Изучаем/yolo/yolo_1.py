"""
https://www.youtube.com/watch?v=xK4li3jinSw&list=PLMoSUbG1Q_r8nz4C5Yvd17KaXy8p0ufPH&index=3

https://pjreddie.com/darknet/yolo/


"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

WIDH_HEIGHT_TARGET = 320

WIDTH_TARGET = 640
HEIGHT_TARGET  = 480

confTresh = 0.5
nmsTreshold = 0.3

#classesFile = 'classes_coco.txt'
classesFile = 'v3/classes_yolov3.txt'
#modelCfg = 'yolov4.cfg'
modelCfg = 'v3/yolov3-320.cfg'
#modelWeights = 'yolov4.weights'
modelWeights = 'v3/yolov3-320.weights'

classNames = []

with open(classesFile) as f:
    classNames = f.read().rstrip('\n').split('\n')

#print(len(classNames) , classNames)

net = cv2.dnn.readNetFromDarknet(modelCfg, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

layerNames = net.getLayerNames()
#print(layerNames)

def findObjects(outputs, img):
    height, width, channels = img.shape
    bbox = []
    classIds = []
    confs = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]

            if confidence > confTresh:
                w, h = int(det[2] * width), int(det[3] * height)
                x, y = int( det[0] * width - width/2 ), int( det[1]*height - height/2 )
                bbox.append([x, y, width, height])
                classIds.append(classId)
                confs.append(float(confidence))
    #print(len(bbox))
    indices = cv2.dnn.NMSBoxes(bbox, confs, confTresh, nmsTreshold)
    #print(indices)

    for i in indices:
        i = i[0]
        box = bbox[i]
        x,y,w,h = box[0], box[1], box[2], box[3]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2 )
        cv2.putText(frame, f'{classNames[classIds[i]].upper() } {int(confs[i] * 100)}%',
        (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255, 2))

        print(classNames[classIds[i]].upper(), int(confs[i] * 100), ' ', end = '')

    if len(indices):
        print('\n')


while True:
    _, frame = cap.read()

    blob = cv2.dnn.blobFromImage(frame, 1/255,
                                 (WIDH_HEIGHT_TARGET, WIDH_HEIGHT_TARGET),
                                 #(WIDTH_TARGET, HEIGHT_TARGET),
                                 [0,0,0], 1, crop = False)

    net.setInput(blob)

    layerNames = net.getLayerNames()

    outputNames = [layerNames[i[0] - 1]  for i in net.getUnconnectedOutLayers() ]
    #print(outputNames)
    #print(net.getUnconnectedOutLayers())

    outputs = net.forward(outputNames)
    # print(len(outputs), type(outputs), type(outputs[0]), outputs[0].shape)

    #print(outputs[0].shape)
    #print(outputs[1].shape)
    #print(outputs[2].shape)

    #print(outputs[0][0])

    findObjects(outputs, frame)

    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
