import cv2  # OpenCV: 이미지와 비디오 처리를 위한 라이브러리입니다.
import os  # 운영체제 관련 기능을 사용하기 위한 모듈입니다.

# greeting.mp3 파일을 재생하는 함수입니다.
def play_greeting():
    # OS에 따라 다른 명령어를 사용하여 MP3 파일을 재생합니다.
    if os.name == "nt":  # Windows 환경
        os.system("start greeting.mp3")
    else:  # Linux 또는 Mac 환경
        os.system("mpg321 greeting.mp3")

# 얼굴 인식을 위해 OpenCV의 Haar Cascade 분류기를 로드합니다.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 웹캠을 열어 비디오 스트림을 받아옵니다.
cap = cv2.VideoCapture(0)  # 기본 카메라(보통 0번)를 사용하여 비디오 캡처를 시작합니다.

face_detected = False  # 얼굴 감지 여부를 확인하기 위한 변수입니다.

while True:
    ret, frame = cap.read()  # 웹캠으로부터 한 프레임씩 읽어옵니다.
    if not ret:
        break  # 프레임을 제대로 읽지 못하면 반복문을 종료합니다.
    
    # 프레임을 흑백 이미지로 변환합니다.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Haar Cascade를 사용해 얼굴을 감지합니다.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) > 0:
        # 얼굴이 감지된 경우, 처음 감지 시 greeting.mp3 파일을 재생합니다.
        if not face_detected:
            play_greeting()  # greeting.mp3 파일을 재생합니다.
            face_detected = True  # 얼굴 감지 완료 상태로 변경합니다.
        
        # 감지된 얼굴 영역마다 사각형 박스를 그립니다.
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 녹색 박스 표시
        
        # "face detected" 텍스트를 화면에 표시합니다.
        cv2.putText(frame, "face detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)
        #(0, 0, 0)은 검은색, 3은 두께입니다.
        cv2.putText(frame, "face detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 1)

    # 현재 프레임을 화면에 출력합니다.
    cv2.imshow('Face Detection', frame)
    
    # 사용자가 'q' 키를 누르면 반복문을 종료합니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 자원을 해제하고 모든 OpenCV 창을 닫습니다.
cap.release()
cv2.destroyAllWindows()
