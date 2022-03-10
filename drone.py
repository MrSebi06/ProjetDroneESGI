import cv2
from djitellopy import Tello

class Drone:
    def __init__(self):
        self.t = Tello()
        self.t.connect()
        
    def video(self):
        self.telloVideo = cv2.VideoCapture("udp://@0.0.0.0:11111")   # On ouvre le fichier vidéo envoyé par la caméra IP du drone
        self.ret = False  
        
        while (True):
            self.ret, self.frame = self.telloVideo.read()
            
            if (self.frameret):
                cv2.imshow('Tello', self.frame)
                
            if cv2.waitkey(1) & 0xFF == ord('q'):
                break
            
        self.telloVideo.release()
        cv2.destroyAllWindows()
        
        return 0
    
