import cv2
import numpy as np

count = 0
dead_tot = 0

def processar_imagem(image, img: bool):
    global count
    global dead_tot

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    low_color = np.array([10, 50, 50])
    up_color = np.array([30, 255, 255])

    mask = cv2.inRange(hsv_image, low_color, up_color)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    total_area = image.shape[0] * image.shape[1]
    area_afetada = sum(cv2.contourArea(contour) for contour in contours)
    dead_porcent = round((area_afetada / total_area) * 100, 2)
    dead_tot += dead_porcent

    if count % 20 == 1:
        avg_dead_porcent = dead_tot / count

        if avg_dead_porcent < 10:
            print("A porcentagem de folha morta é baixa:", avg_dead_porcent, "%")
            print("Nenhuma ação imediata é necessária.")
        elif avg_dead_porcent < 50:
            print("A porcentagem de folha morta é moderada:", avg_dead_porcent, "%")
            print("Recomenda-se realizar ações de controle e tratamento adequados.")
        else:
            print("A porcentagem de folha morta é alta:", avg_dead_porcent, "%")
            print("Ações de controle e tratamento devem ser tomadas urgentemente.")
    elif img:
        if dead_porcent < 10:
            print("A porcentagem de folha morta é baixa:", dead_porcent, "%")
            print("Nenhuma ação imediata é necessária.")
        elif dead_porcent < 50:
            print("A porcentagem de folha morta é moderada:", dead_porcent, "%")
            print("Recomenda-se realizar ações de controle e tratamento adequados.")
        else:
            print("A porcentagem de folha morta é alta:", dead_porcent, "%")
            print("Ações de controle e tratamento devem ser tomadas urgentemente.")

    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Análise da Planta', image)
    count += 1

modo = input("Digite 'webcam' para usar a webcam, 'imagem' para usar uma imagem estática ou 'video' para usar um vídeo MP4: ")

if modo.lower() == 'webcam':
    cap = cv2.VideoCapture(0)  
    while True:
        _, frame = cap.read()  
        processar_imagem(frame, False)  

        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break

    cap.release()  
    cv2.destroyAllWindows()

elif modo.lower() == 'imagem':
    imagem = cv2.imread('planta.jpg')

    processar_imagem(imagem, True)  

    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif modo.lower() == 'video':
    video_path = input("Digite o caminho para o vídeo MP4: ")
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        processar_imagem(frame, False)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

else:
    print("Opção inválida.")
