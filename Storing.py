from tkinter import Frame
import cv2

cap=cv2.VideoCapture(0)

#returns bool value
opened=cap.isOpened()

height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
 
fps=cap.get(cv2.CAP_PROP_FPS)
print("Frames are {}".format(fps))

fourcc=cv2.VideoWriter_fourcc(*"MJPG")

##video writer for storing

out=cv2.VideoWriter('trial.avi',fourcc,fps,(int(width),int(height)))



if(opened):
    
    while(cap.isOpened()):
        ret,frame=cap.read()
        
        if(ret==True):  
            cv2.imshow('video frame',frame)
            
            #for storing video instances
            out.write(frame)
            
            if(cv2.waitKey(2)==27):
                break

# now release all the variables
out.release()
cap.release()
cv2.destroyAllWindows()

