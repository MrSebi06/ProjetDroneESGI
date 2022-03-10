t.streamoff() 
t.streamon()    
    
telloVideo = cv2.VideoCapture("udp://@0.0.0.0:11111")
    
ret = False
    
while(True):
ret, frame = telloVideo.read() 
if(ret):                                    
    cv2.imshow('Tello',frame)
            
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("test.jpg",frame)
        print("Capture enregistrée !")
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Quand tout est terminé, on termine et on ferme tout
telloVideo.release()
cv2.destroyAllWindows()
return 0
