import cv2
import mediapipe as mp
import numpy as np

#----------------------------------------------- 

def Etiqueta(idx, mano, results):
    aux = None#si no encuentra manos no se ejecuta
    for _, clase in enumerate(results.multi_handedness):
      if clase.classification[0].index == idx:
        label = clase.classification[0].label
        texto = '{}'.format(label)
        #indica que mano estas usando para detectar
        #usa lar cordenadas de los dedos indices para indicar que mano detecta


#-----------------------------------------------------

mp_drawing = mp.solutions.drawing_utils #puntos de referencia
mp_drawing_styles = mp.solutions.drawing_styles #variable que da estilo
mp_hands = mp.solutions.hands
change = True
change2 = False


#parametros para la variable de manos
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=1, #modelo regular de complejidad
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=2) as hands: #numero de manos que se usaran
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      continue


#------------------------------------------------------
    #la imagen se convierte a BGR
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
#


    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#------------------------------------------------------



    image_height, image_width, _ = image.shape
    if results.multi_hand_landmarks:
        if len(results.multi_hand_landmarks): 
            #recorrera las manos que se han encontrado
            for num, hand_landmarks in enumerate(results.multi_hand_landmarks):
                
                mp_drawing.draw_landmarks( #recopila la imagen, coloca los puntos de referencia y conecciones en la imagen tomada
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                
                #---------------------------------------------------------------------
                
                #se definen los puntos de los dedos
                index_finger_tip = (int(hand_landmarks.landmark[8].x * image_width),
                                int(hand_landmarks.landmark[8].y * image_height))
                index_finger_pip = (int(hand_landmarks.landmark[6].x * image_width),
                                int(hand_landmarks.landmark[6].y * image_height))
                
                thumb_tip = (int(hand_landmarks.landmark[4].x * image_width),
                                int(hand_landmarks.landmark[4].y * image_height))
                thumb_pip = (int(hand_landmarks.landmark[2].x * image_width),
                                int(hand_landmarks.landmark[2].y * image_height))
                
                middle_finger_tip = (int(hand_landmarks.landmark[12].x * image_width),
                                int(hand_landmarks.landmark[12].y * image_height))
                
                middle_finger_pip = (int(hand_landmarks.landmark[10].x * image_width),
                                int(hand_landmarks.landmark[10].y * image_height))
                
                ring_finger_tip = (int(hand_landmarks.landmark[16].x * image_width),
                                int(hand_landmarks.landmark[16].y * image_height))
                ring_finger_pip = (int(hand_landmarks.landmark[14].x * image_width),
                                int(hand_landmarks.landmark[14].y * image_height))
                
                pinky_tip = (int(hand_landmarks.landmark[20].x * image_width),
                                int(hand_landmarks.landmark[20].y * image_height))
                pinky_pip = (int(hand_landmarks.landmark[18].x * image_width),
                                int(hand_landmarks.landmark[18].y * image_height))
                
                wrist = (int(hand_landmarks.landmark[0].x * image_width),
                                int(hand_landmarks.landmark[0].y * image_height))
                #----------------------------------------------------------------------------
                
                #condiciones para detectar la mano
                #las condiciones indican que el dedo pulgar es mayor que los demas dedos
                if thumb_pip[1] - thumb_tip[1] > 0 and thumb_pip[1] - index_finger_tip[1] < 0 \
                    and thumb_pip[1] - middle_finger_tip[1] < 0 and thumb_pip[1] - ring_finger_tip[1]<0 \
                    and thumb_pip[1] - pinky_tip[1] < 0:
                    cv2.putText(image, 'Bien', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                
                
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
cv2.destroyAllWindows()