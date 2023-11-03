import cv2
vidcap = cv2.VideoCapture('C:\\Users\\user\\Music\\pylance\\slicer\\video\\cam.avi')
success,image = vidcap.read()

count = 1
success = True

while success:
  success,image = vidcap.read()
  cv2.imwrite("C:\\Users\\user\\Music\\pylance\\slicer\\img\\%d.jpg" % count, image)
  print("이미지 저장됨 %d.jpg" % count)
  
  if cv2.waitKey(10) == 27:                    
      break
  count += 1