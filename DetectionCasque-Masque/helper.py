from ultralytics import YOLO
import streamlit as st
import cv2
import settings

def load_model(model_path):
    model = YOLO(model_path)
    return model

def _display_detected_frames_guidelines(conf, model, st_frame, image, is_display_tracking=None):
    classNames =["Hardhat", "Mask", "NO-Hardhat", "NO-Mask", "NO-Safety Vest", "Person", "Safety Cone", "Safety Vest", "machinery", "vehicle"]
    image = cv2.resize(image, (720, int(720*(3/4))))

    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True)
    else:
        res = model.predict(image, conf=conf)

    #Test pour trouver si il n'ya pas de casque ou pas de gilet ou de personne 
    safety_violation_detected = False
    person_detected = False
    for r in res:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            if classNames[cls] in ['NO-Hardhat', 'NO-Safety Vest']:
                safety_violation_detected = True
            if classNames[cls] == 'Person':
                person_detected = True

    # Camera
    org = (50, 50)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    if safety_violation_detected and person_detected:
        color = (0, 0, 255)
        text = 'Safety Guidelines not respected'
    elif not safety_violation_detected and not person_detected:
        color = (255,255,255)
        text = 'No person detected'
    else :
        color = (0, 255, 0)
        text = 'Safety Guidelines respected'
    thickness = 2
    image = cv2.flip(image, 1)
    cv2.putText(image, text, org, font, fontScale, color, thickness)
    
    st_frame.image(image,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )

def _display_detected_frames_labels(conf, model, st_frame, image, is_display_tracking=None):

    image = cv2.resize(image, (720, int(720*(3/4))))
    image = cv2.flip(image, 1)

    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True)
    else:
        res = model.predict(image, conf=conf)

    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )


def play_webcam(conf, model, type):
    source_webcam = settings.WEBCAM_PATH
    if st.sidebar.button('Lancer la détection'):
        try:
            vid_cap = cv2.VideoCapture(source_webcam, cv2.CAP_DSHOW)
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success and type == 1:
                    _display_detected_frames_guidelines(conf,
                                             model,
                                             st_frame,
                                             image)
                elif success and type == 2:
                    _display_detected_frames_labels(conf,
                                             model,
                                             st_frame,
                                             image)
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Erreur de chargement de la webcam: " + str(e))