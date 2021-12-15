## 딥러닝을 활용한 위험상황 인지 시스템 개발
- **세부적으로는 공공장소, 가정 등에서 강도상황 발생시 실시간으로 사용자, 경찰서, 소방서 등에 알려주는 것** 
   - 이를 위하여 기본적인 딥러닝 네트워크인 CNN, LSTM을 이해했고, 이것이 더욱더 발전하여 비디오 기반으로 상황을 이해하는 **Video Scene Understanding**, 객체를 인식하는 **Object Detection** 모델을 구축하였다. 이를 통해 사각지대에 빠져 놓칠 수 있는 강도상황을 놓치지 않고 감지할 수 있는 성과를 얻었다.
   - 추가적으로 사용자 편의성을 위하여 **Telegram Chatbot을 제작**하였다. 기존의 Telegram 어플만 있으면 해당 어플의 ip에 파이썬 프로그래밍을 통해 데이터를 전송하여 알림을 주는 성과를 얻었다.  
 
- 대전시의 재난관리과 영상관제팀장님의 말씀을 인용하면 다음과 같다.  

   - **“1인당 약 390대의 CCTV를 관제하고 있습니다. 놓칠 수 있는 그런 사각지대를 해소하는데 많은 도움이 될 거라고 말입니다.”**  
     따라서 우리 SoS팀의 이런 시스템이 개발되어 각 경찰서와 소방서, 공공장소 등에 적용이 된다면   

   **1. CCTV 감시하는 분들의 사각지대 역시 해소**  
   **2. 경찰의 실시간 출동으로 범인을 조기에 검거**   
   **3. 범죄 검거율 상승으로 사회적 범죄 예방 효과**     

   위 세 가지에 큰 기여를 할 수 있을 것이라 본다.  

1. 작품 구상 및 기획

![image](https://user-images.githubusercontent.com/76835313/145256882-4589eae3-07fe-477b-917c-6768319ccf96.png)
2. 데이터 수집 및 전처리 과정 수행

![image](https://user-images.githubusercontent.com/76835313/145256959-7663b1dd-2e28-4c35-8226-104df3836bd0.png)
- 데이터 수집 및 전처리 과정입니다. 이후 소개드릴 Video Understanding과 Object Detection에 필요한 데이터들을 수집하였습니다. 비디오 데이터 포함 약 2000여개의 데이터를 수집하였습니다. Object Detection에서는 라벨링 작업을 [makesense.ai](https://www.makesense.ai/) 사이트에서 직접 수행해 주었습니다. 이 때 좀더 수월한 데이터 수집을 위하여 직접 Frame Extractor를 제작하였습니다. 
 
2-1. Frame Extractor GUI exe 파일 생성 프로그램 제작  

![image](https://user-images.githubusercontent.com/76835313/145257066-2376f51b-bc59-4754-83b4-7accdbb1c377.png)
- 파이썬을 활용하여 직접 Frame Extractor를 제작하였고 exe파일로 생성하여 다른 사용자에게도 사용할 수 있도록 배포할 수 있습니다. 이를 통해 동영상을 넣어 쉽게 frame을 추출합니다.
3. Video Scene Understanding, Object Detection 논문 분석 및 스터디

![image](https://user-images.githubusercontent.com/76835313/145257139-f293da29-b1dc-4038-a01f-a6af73f27d51.png)
![image](https://user-images.githubusercontent.com/76835313/145257162-89090682-0288-486b-b562-798d02f53ce5.png)
- 이번 프로젝트에서는 위와같은 논문을 기반으로 아이디어를 얻고 프로그래밍으로 구현하였습니다. 대부분 오픈소스로 코드가 공개되어있습니다. 여기에 좀더 프로그래밍을 더해 저희의 목적에 맞도록 개선하였습니다.

   * [Action_Recognition_in_Video_Sequences_using_Deep_Bi-Directional_LSTM_With_CNN_Features](https://github.com/engineerjkk/CapstoneDesign/blob/main/05.Reference/Action_Recognition_in_Video_Sequences_using_Deep_Bi-Directional_LSTM_With_CNN_Features.pdf)
   * [DB-LSTM Densely-connected Bi-directional LSTM for human action recognition](https://github.com/engineerjkk/CapstoneDesign/blob/main/05.Reference/DB-LSTM%20Densely-connected%20Bi-directional%20LSTM%20for%20human%20action%20recognition.pdf)
   * [YOLOv1](https://github.com/engineerjkk/CapstoneDesign/blob/main/05.Reference/YOLOv1.pdf)
   * [YOLOv4](https://github.com/engineerjkk/CapstoneDesign/blob/main/05.Reference/YOLOv4.pdf)
4. Video Scene Understanding 코드 분석 및 개선 프로그래밍

![image](https://user-images.githubusercontent.com/76835313/145257241-bbf1b38f-3545-4ed5-9426-3db6fb6003e1.png)
5. Object Detection 코드 분석 및 개선 프로그래밍
6. 
 ![Capture](https://user-images.githubusercontent.com/57138931/145999774-8861cb18-bf4e-428b-b885-b90f8656e4b3.JPG)

- Video Scene Understandig과 Object Detection 코드 분석 및 개선 프로그래밍에 사용된 코드 중 일부내용입니다. 코랩 환경에서도 학습과 실행이 가능하며 주피터 노트북 및 파이참과 같은 개발환경에서도 가능합니다. 저희팀의 경우 코랩의 환경에서 실행하였습니다. 

   * [Video Scene Understanding train python file](https://github.com/engineerjkk/CapstoneDesign/blob/main/01.Video_Scene_Understanding/train.py)
   * [Video Scene Understanding Execution file](https://github.com/engineerjkk/CapstoneDesign/blob/main/01.Video_Scene_Understanding/predict_video.py)
   * [Object Detection train python file](https://github.com/engineerjkk/CapstoneDesign/blob/main/02.Object_Detection/train.py)
   * [Object Detection Execution file](https://github.com/engineerjkk/CapstoneDesign/blob/main/02.Object_Detection/detect.py)
  
6. Video Scene Understanding, Object Detection 학습 결과

![image](https://user-images.githubusercontent.com/76835313/145257355-4612fb62-32f6-4de4-b7a9-32e7d9d8f253.png)
- Video Scene Understanding과 Object Detection의 학습결과입니다. 두 학습 모두 매우 높은 정확도를 보이고있습니다. 이는 질적으로 굉장히 우수한 데이터셋을 구축하는데 노력을 많이 기울였고 전처리과정 중 하나인 라벨링에서 역시 매우 꼼꼼히 했기에 높은 성능이 나올 수 있었습니다.
7. Video Scene Understanding, Object Detection 실행결과

![image](https://user-images.githubusercontent.com/76835313/145257430-cf85f4fa-f0d6-4d5d-92bc-7911998a5175.png)
- 첫 번 째 단계에서 우선적으로 Video Scene Understanding을 실행합니다. 기존의 트레이닝 데이터셋을 활용하여 학습한 모델로 현재 테스트 데이터셋에서 실행한 결과 좌측 상단의 강도를 뜻하는 Robbery가 생성됨을 보실 수 있습니다. 확률은 93.7%로 신뢰성이 있는 정확도입니다. 
- 두 번째는 이전에 받은 프레임에서 추가적인 객체인식을 해줍니다. 학습된 클래스는 사람(person)과 총(gun)으로 총 두 개입니다. 이를 통해 현재 CCTV속 포착된 공간에 몇몇의 사람이 있는지와 강도는 총을 들고있는지의 유무를 알 수 있습니다. 
8. Application 개발 (Telegram chatbot)

![image](https://user-images.githubusercontent.com/76835313/145257505-fdb6b416-3668-4a2f-b3ff-3f414d7c89f8.png)
- 이전단계에서 실행한 Video Scene Understanding과 Object Detection을 통하여 실제 강도가 들어온 상황이라면 CCTV속 몇 명의 사람이 있고 총을 들었는지 유무를 전송해줍니다.
- 텔레그램 어플을 설치한 뒤 ip를 확인합니다. 파이썬 프로그래밍을 통해서 해당하는 ip에 데이터를 보내줄 수 있습니다. 

   * [Telegram Chatbot python file](https://github.com/engineerjkk/CapstoneDesign/blob/main/04.Application/README.md)

- 마무리
- 
![image](https://user-images.githubusercontent.com/76835313/146137294-9f1fb10b-91b9-44f3-96a7-eaffcf1e5114.png)
- 마지막으로 
대전시의 재난관리과 영상관제팀장님께서는 이렇게 말씀하십니다.  
**"1인당 약 390대의 CCTV를 관제하고 있습니다. 놓칠 수 있는 그런 사각지대를 해소하는데 많은 도움이 될 것"** 이라고 말입니다.  
따라서 저희의 이런 시스템이 개발되어 각 경찰서와 소방서, 공공장소 등에 적용이 된다면 CCTV 감시하는 분들의 사각지대 역시 해소하고
경찰의 실시간 출동으로 범인을 조기에 잡거나 범죄 예방에 큰 기여를 할 수 있을 것이라 봅니다.

## 감사합니다.

