import cv2
import mediapipe as mp

def track_hands():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the image to RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow(image_rgb)
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break
       
    
        # Process the frame to detect hands
        results = hands.process(image_rgb)
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for landmark in hand_landmarks.landmark:
                    # Get the coordinates of the hand landmarks
                    x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                    cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_hands()
