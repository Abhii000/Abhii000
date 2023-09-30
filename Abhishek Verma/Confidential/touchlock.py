import ctypes,os,time
import cv2
import win32api
import win32con
import mediapipe as mp
MOUSEEVENTF_MOVE = 0x0001
MOUSE_EVENT_LEFTDOWN = 0x0002
MOUSE_EVENT_LEFTUP = 0x0004
print('To Activate Show the vicctory Sign')

x_1=0
y_1=0
lock=0

def click():
    global x_1,y_1
    # Set the cursor position
    #ctypes.windll.user32.SetCursorPos(x, y)
    if x_1==0:
        if lock==1:


        

            
        # Simulate the left mouse button down and up events
            # Sleep briefly to simulate a human-like click action
            if y_1==0:
                win32api.mouse_event(MOUSE_EVENT_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.05)
                win32api.mouse_event(MOUSE_EVENT_LEFTUP, 0, 0, 0, 0)
                y_1=1
            else:

                win32api.mouse_event(MOUSE_EVENT_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.05)  # Sleep briefly to simulate a human-like click action

            x_1=1

def main():
    global x_1,y_1,lock
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)
        #id=3(thumb point),id=4(thumb Tip)
        
        #id=5(Point finger bottom),id=6(Point finger 2nd bottom),id=7(Point finger 2nd top)


        if results.multi_hand_landmarks:
            for abhi in results.multi_hand_landmarks:
                
                for id, lm in enumerate(abhi.landmark):
                    h, w, _ = frame.shape
                    
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    m=int(640-cx)*3-260
                    n=int(cy)*2

                    if id ==4 :  # Thumb Tip Landmark
                        a=cx
                        b=cy

                        cv2.circle(frame, (cx, cy), 8, (255, 0, 0), -1)
                        
                        print(m,' x ',n)

                    elif id ==8 :  # Index finger tip landmark
                        cv2.circle(frame, (cx, cy), 8, (255, 255, 0), -1)
                        a1=cx
                        b1=cy
                        #print(a-a1)
                        if (b-b1)<=14 and (a-a1)<=14 :
                            if x_1==0:
                                if lock==1:

                                    click()
                                    os.system('color 04')
                        
                        else:
                            x_1=0
                        
                            win32api.mouse_event(MOUSE_EVENT_LEFTUP, 0, 0, 0, 0)
                            os.system('color 03')

                    elif id==20:
                        cv2.circle(frame, (cx, cy), 8, (255, 0, 0), -1)
                        if lock==1:

                            ctypes.windll.user32.SetCursorPos(m,n)
                    elif id==16:
                        a2=cx
                        b2=cy
                        cv2.circle(frame, (cx, cy), 8, (255, 0, 0), -1)
                        if (b-b2)<=14 and (a-a2)<=14:
                            lock=1

                    cv2.imshow('Finger Tracking', frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
                    
                    

                            
                                
                            
                                
                            
                            
                    




