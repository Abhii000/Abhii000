import cv2
import mediapipe as mp

def main():
    mp_objectron = mp.solutions.objectron
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)  # Open the default camera (0)

    with mp_objectron.Objectron(
        static_image_mode=False,
        max_num_objects=5,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as objectron:

        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                print("Camera not accessible.")
                break

            # Flip the frame horizontally for a later selfie-view display
            frame = cv2.flip(frame, 1)
            # Convert the BGR image to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = objectron.process(rgb_frame)

            if results.detected_objects:
                for detected_object in results.detected_objects:
                    mp_drawing.draw_landmarks(
                        frame, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)

            cv2.imshow('Object Detection', frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
