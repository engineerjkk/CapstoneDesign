# 딥러닝을 활용한 위험상황 인지 시스템 개발 🚨

> 학부 캡스톤디자인(졸업작품) 최우수상 수상작 (2021) | [📺 발표 영상](https://youtu.be/MaQp2NTFgFk?si=Vg0pdIEPHqfypPNe)

## 📌 프로젝트 개요
공공장소 및 가정에서 발생하는 강도 상황을 실시간으로 감지하여 사용자, 경찰서, 소방서 등에 즉각 알림을 제공하는 시스템

### 🎯 핵심 목표
1. CCTV 관제 요원의 사각지대 해소
2. 경찰의 실시간 출동을 통한 조기 검거 지원
3. 범죄 검거율 향상을 통한 사회적 범죄 예방

## 🛠 기술 스택
- **딥러닝 모델**: CNN, LSTM
- **주요 기능**: 
  - Video Scene Understanding
  - Object Detection
- **알림 시스템**: Telegram Chatbot

## 💡 시스템 구성

### 1. 작품 구상 및 기획
![시스템 구성도](https://user-images.githubusercontent.com/76835313/145256882-4589eae3-07fe-477b-917c-6768319ccf96.png)

### 2. 데이터 구축
![데이터 처리 과정](https://user-images.githubusercontent.com/76835313/145256959-7663b1dd-2e28-4c35-8226-104df3836bd0.png)
- **데이터셋 규모**: 약 2,000개의 이미지 및 비디오
- **라벨링 도구**: [makesense.ai](https://www.makesense.ai/)
- **자체 개발 도구**: Frame Extractor GUI 프로그램

#### Frame Extractor GUI 프로그램
![Frame Extractor](https://user-images.githubusercontent.com/76835313/145257066-2376f51b-bc59-4754-83b4-7accdbb1c377.png)
- Python 기반 GUI 애플리케이션
- 동영상에서 프레임 추출 자동화
- 실행 파일(.exe) 형태로 배포 가능

### 3. 연구 기반 논문
![논문 분석](https://user-images.githubusercontent.com/76835313/145257139-f293da29-b1dc-4038-a01f-a6af73f27d51.png)
- Action Recognition using Deep Bi-Directional LSTM
- DB-LSTM for Human Action Recognition
- YOLOv1 & YOLOv4

### 4. 구현 및 성능
#### Video Scene Understanding & Object Detection
![구현 결과](https://user-images.githubusercontent.com/76835313/145257355-4612fb62-32f6-4de4-b7a9-32e7d9d8f253.png)

#### 실행 결과
![실행 화면](https://user-images.githubusercontent.com/76835313/145257430-cf85f4fa-f0d6-4d5d-92bc-7911998a5175.png)
- Scene Understanding: 강도 상황 감지 (정확도 93.7%)
- Object Detection: 사람 및 무기 인식

### 5. 알림 시스템 (Telegram Chatbot)
![텔레그램 봇](https://user-images.githubusercontent.com/76835313/145257505-fdb6b416-3668-4a2f-b3ff-3f414d7c89f8.png)
- 실시간 위험 상황 알림
- 현장 상황 정보 제공 (인원수, 무기 소지 여부)

## 📊 기대효과
> "1인당 약 390대의 CCTV를 관제하고 있습니다. 놓칠 수 있는 그런 사각지대를 해소하는데 많은 도움이 될 것" - 대전시 재난관리과 영상관제팀장

1. CCTV 관제 효율성 향상
2. 실시간 대응 체계 구축
3. 범죄 예방 효과 증대

## 🔗 관련 링크
### 소스코드
- [Video Scene Understanding - 학습](https://github.com/engineerjkk/CapstoneDesign/blob/main/01.Video_Scene_Understanding/train.py)
- [Video Scene Understanding - 실행](https://github.com/engineerjkk/CapstoneDesign/blob/main/01.Video_Scene_Understanding/predict_video.py)
- [Object Detection - 학습](https://github.com/engineerjkk/CapstoneDesign/blob/main/02.Object_Detection/train.py)
- [Object Detection - 실행](https://github.com/engineerjkk/CapstoneDesign/blob/main/02.Object_Detection/detect.py)
- [Telegram Chatbot](https://github.com/engineerjkk/CapstoneDesign/blob/main/04.Application/README.md)

### 참고 논문
- [Action Recognition using Deep Bi-Directional LSTM](https://github.com/engineerjkk/CapstoneDesign/blob/main/05.Reference/Action_Recognition_in_Video_Sequences_using_Deep_Bi-Directional_LSTM_With_CNN_Features.pdf)
- [DB-LSTM](https://github.com/engineerjkk/CapstoneDesign/blob/main/05.Reference/DB-LSTM%20Densely-connected%20Bi-directional%20LSTM%20for%20human%20action%20recognition.pdf)
- [YOLOv1](https://github.com/engineerjkk/CapstoneDesign/blob/main/05.Reference/YOLOv1.pdf)
- [YOLOv4](https://github.com/engineerjkk/CapstoneDesign/blob/main/05.Reference/YOLOv4.pdf)
