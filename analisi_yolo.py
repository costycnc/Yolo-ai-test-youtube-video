import cv2
import os
from ultralytics import YOLO


# Percorso assoluto verso il file sul tuo PC
peso_path = r"c:\test\robot_project\yolov8n.pt"

if not os.path.exists(peso_path):
    print(f"Errore: il file {peso_path} non esiste!")
    exit()

try:
    modello = YOLO(peso_path)
    print("Modello caricato con successo!")
except Exception as e:
    print(f"Errore nel caricamento di YOLO: {e}")
    exit()

classi_nomi = modello.names

# Il tuo video
video_locale = r"c:\test\youtube\video.mp4"



# Apriamo il file locale appena scaricato
cap = cv2.VideoCapture(video_locale)
print("Test visivo avviato. Premi 'q' sulla finestra del video per chiudere.")

# Inizializziamo il contatore dei frame
contatore_frame = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    contatore_frame += 1
    altezza, larghezza, _ = frame.shape
    
    # Eseguiamo l'inferenza
    risultati = modello(frame, conf=0.4, verbose=False)
    oggetti_rilevati = {}

    for r in risultati:
        if r.boxes is not None and len(r.boxes) > 0:
            for box in r.boxes:
                cls_id = int(box.cls.item())
                nome_classe = classi_nomi.get(cls_id, f"ID {cls_id}")
                oggetti_rilevati[nome_classe] = oggetti_rilevati.get(nome_classe, 0) + 1

                # Estrazione coordinate
                coordinate = box.xyxy[0].tolist()
                x1, y1, x2, y2 = map(int, coordinate)
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, nome_classe, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Costruzione della stringa di riepilogo
    if oggetti_rilevati:
        elementi = [f"{v} {k}" for k, v in oggetti_rilevati.items()]
        testo_oggetti = ", ".join(elementi)
    else:
        testo_oggetti = "Nessun oggetto"

    # NUOVA FUNZIONALITÀ: Stampa in tempo reale nella finestra di DOS (Terminale)
    print(f"Frame #{contatore_frame}: Rilevati -> {testo_oggetti}")

    # Barra nera inferiore sulla finestra video
    testo_riassunto = f"Rilevati: {testo_oggetti}"
    cv2.rectangle(frame, (0, altezza - 40), (larghezza, altezza), (0, 0, 0), -1)
    cv2.putText(frame, testo_riassunto, (10, altezza - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Rilevamento YOLO - Video Locale", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


