# CapstoneDesign

CCTV or MetaVerse 상에서 사람들을 추척관찰하며 특정 이상한 행동을 하면 알려준다.

1. person counting (굳이 할필요없다.)
* https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/
1. Labeling 필요 
2. person tracking (10초 녹화)
3. 그 사람의 반경내로 이상한 행동하면 알려주기.
4. 행동 recognition -> 시위, 방화, 절도  (SVM or Rndom Forest)


5. 그루핑해서 뭐하고있는지?
6. 10 frame 들을 통해서 activity recognition (ex. 공을 인식하는게 아니라 공을 준다.)
7. 10초의 프레임을 이어서 동작을 알아낸다. 


1. perosn counting 필요 X
2. 그룹 디텍팅(DBSCAN), 판단
3. 뭐하는지 (activity)

* 이걸 하고나서 그냥 다른 데이터로 학습시키면 될 거다. 

* 10초정도의 동영상을 학습시킬 것.

* SIFT

## 어플로 만들어 하나의 실행파일로 만드는 것은 어떤지?
-> 단순히 코드만으로는 완성도가 적어보임. 이 기회에 컴퓨터비전 기술을 모바일 기기에 이식하는 기술도 습득하는게 좋을 것 같은데?

1.CCTV의 목적 중 하나는 범죄자를 잡는것이다.
하지만 보통 범죄가 이미 일어난 후 범인을 잡기 위해 CCTV를 돌려본다.
하지만 이미 범죄자는 떠났다
따라서 이를 방지하기 위해 CCTV에 실시간으로 범죄현장을 인식하여 경찰에게 알림을 주는 연구를 하였다.
- https://www.facebook.com/wlkynews/videos/1068177840588006/


When gun is detected in scene, It send notification to the owner of camera or to police in case it is public owned camera.
Currently, we created Telegram Chatbot for that purpose( Notify in case of danger).

Contents: Number of guns available and number of People around.

3. Notification on Screen

![3](https://user-images.githubusercontent.com/57138931/143757808-7acd602d-9493-4412-9740-23d6064e6e9c.jpg)

4.Contents of Notification

![4](https://user-images.githubusercontent.com/57138931/143758492-ab051bae-db11-49e4-96fe-2ee90acac699.jpg)

1. Notification on Screen

![1](https://user-images.githubusercontent.com/57138931/143758797-5a66813d-bd5c-49af-a392-7ac031a95869.jpg)

2. Contents of Notification

![2](https://user-images.githubusercontent.com/57138931/143759188-b0775065-bb36-490f-a412-8cc0c3eca393.jpg)
