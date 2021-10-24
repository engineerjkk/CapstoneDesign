_____________________________________
# 실험 방법
# 1.'UCF50/WalkingWithDog' 위치에 학습할 프레임을 넣을것.
ex) Fighting 프레임들을 넣을 것
![image](https://user-images.githubusercontent.com/76835313/138607935-d03a3514-4ced-4a2a-af58-8b8b5f615e0a.png)

# 2. 클래스 설정할 것 -> Fight
![image](https://user-images.githubusercontent.com/76835313/138607972-1e76d658-5260-4b01-8264-7ad948d83553.png)

# 3. 미리 유투브로 테스트 동영상을 업로드 해 놓을것
![image](https://user-images.githubusercontent.com/76835313/138608009-39c2ebaf-a8f0-47c9-b463-afe8a2532754.png)

# 4. 데이터 수집은 약 8초간의 동영상(30프레임이므로 총 240프레임정도)를 25개정도는 있어야한다. 
![image](https://user-images.githubusercontent.com/76835313/138608639-11bef76b-7900-4578-91f8-64e1b1f059da.png)

# 차별성
1. 위 4번의 데이터수집을 실제가 아닌 메타버스 환경의 동영상 데이터셋을 만들기
________________________________________

# [Tutorial Link!](https://github.com/spmallick/learnopencv/tree/master/video-classification-and-human-activity-recognition)
# [Go to Colab](https://colab.research.google.com/drive/1Yxsyc7qTr7KjTyz8qa6mJqb3TagthWK-?usp=sharing#scrollTo=RiAMJx7tr5-I)
[Introduction to Video Classification and Human Activity Recognition](https://learnopencv.com/introduction-to-video-classification-and-human-activity-recognition/)
# [OpenCV Github](https://github.com/spmallick/learnopencv)
# 1. Understanding Human Activity Recognition
- in Human Activity Recognition, you actually need a series of data points to predict the action being performed correctly
1. Video Classification의 경우 여러개의 데이터를 가지고 어떠한 행동을 하는지 예측하는 행위이다. 
2. 비디오 프레임 중 한개의 프레임만으로는 예측할 수 없어 기존의 객체인식과는 다른 좀더 복잡한 알고리즘이 필요하다. 
- So **Human Activity Recognition** is a type of time series classification problem where you need data from a series of timesteps to correctly classify the action being performed
3. 이전의 사람의 행동인식은 카메라 기반이아닌 센서였습니다. 스마트폰에 부착된 센서를 통해 포착한 X,Y,Z로 방향과 각도, 속도를 계산할 수 있었습니다. 보통 센서는 스마트폰에 내장된 가속도 센서와 자이로 센서를 활용합니다.
* 하지만 저희는 두가지 이유로 센서를 사용하지 않습니다.
1. In most practical scenarios you won't have access to sensor data. For example, if you want to detect illegal activity at a place then you may have to rely on just video feeds from CCTV cameras
2. I am mostly interested in solving this problem using Computer Vision, so we will be using Video Classification methods to acheive activity recogntion
# 2. Video Classification and Human Activity Recognition
- 이게 필요한 이유는 다음과 같습니다.
an aimage classifier의 경우 정확한 결과를 도출해내지 못합니다.  
![image](https://user-images.githubusercontent.com/76835313/138604493-05bcfb38-144c-4d63-b420-8ef1a19994aa.png)
하지만 Multiple Images의 경우 데이터를 이해하고 결과를 출력할 수 있습니다.  
![image](https://user-images.githubusercontent.com/76835313/138604516-c8195ebf-56f6-4a72-af65-96221c654d50.png)
![image](https://user-images.githubusercontent.com/76835313/138604525-4fd8d831-1e48-410e-89e8-e9c3f6512e25.png)

* This is because the model is not looking at the entire video sequence but just classifying each frame independently.
* Consider the action of **Standing Up from a Chair** and **Sitting Down on a Chair.** In both actions, the frames are almost the same. The main differentiator is the order of the frame sequence. So you need temporal information to correctly predict these actions.  
![Person-standing-up-and-sitting-down-on-a-chair](https://user-images.githubusercontent.com/76835313/138604679-aaa8a56e-6dd8-400b-8aec-42159db2fb52.gif)


# 3. Video Classification Methods
1. Method 1
* ![image](https://user-images.githubusercontent.com/76835313/138604875-50be711d-92a3-4347-9eea-e8598aad4a1e.png)  
* [ “Action Recognition in Video Sequences using Deep Bi-Directional LSTM With CNN Features”, by Amin Ullah (IEEE 2017)](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8121994)
2. Method 2
* Pose를 Detect해서 생긴 여러 프레임을 LSTM Network에 넣어 Output을 냄
* ![image](https://user-images.githubusercontent.com/76835313/138604921-a63d85c3-b09b-4000-b2bc-efc41d93ea5a.png)
3. Method 3
* Single Frame들을 받아 각각의 Optical Flow를 생성해 낸다.
* ![image](https://user-images.githubusercontent.com/76835313/138604987-35b78eb7-6d9f-4884-a112-9d995243f9cc.png)
* [“A Comprehensive Review on Handcrafted and Learning-Based Action Representation Approaches for Human Activity Recognition”](https://www.mdpi.com/2076-3417/7/1/110)
# 4. Types of Video Classification problems
# 5. Making a Video Classifier Using Keras.


