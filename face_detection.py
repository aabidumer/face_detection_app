import cv2
import matplotlib.pyplot as plt
#importing time library for speed comparisons of both classifiers
import time
import flask
# %matplotlib inline
app = flask.Flask(__name__)
app.config["DEBUG"] = True

cascade_file = cv2.CascadeClassifier('C:/Users/Admin/Downloads/Compressed/haarcascade_frontalface_alt.xml')

def detect_faces(f_cascade, colored_img, scaleFactor = 1.2):
    #just making a copy of image passed, so that passed image is not changed
    test1 = cv2.imread(colored_img)
    # colored_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
    img_copy = test1.copy()
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)       
    #let's detect multiscale (some images may be closer to camera than others) images
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5);   
    #go over list of faces and draw them as rectangles on original colored img
    for (x, y, w, h) in faces:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return img_copy

def convertToRGB(img): 
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



# print(data)

@app.route('/detect', methods=['POST'])
def detect():
    # img = "C:/Users/Admin/Pictures/Camera Roll/WIN_20170729_12_04_57_Pro (2).jpg"
    imagefile = flask.request.get_json('image_path')
    print(imagefile)
    data = detect_faces(cascade_file, imagefile['image_path'])
    # data = convertToRGB(data)
    cv2.imshow("test",data)
    cv2.waitKey(0)
    return "Done"
app.run()