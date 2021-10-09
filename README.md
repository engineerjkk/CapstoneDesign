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
