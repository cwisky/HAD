# HAD
* HAD(Human Action Detection)
## Table of Contents
* 학습용 실제 비디오(mp4) 6개
* 테스트용 실제 비디오(mp4) 150개
* Blender 애니메이션 비디오 
* 소스 코드
  + Blender 애니메이션을 mp4 렌더링
  + csv 추출
  + Conditional Sequence 모델 생성 및 Landmark 생성
  + LSTM 모델 학습 (실제 비디오 Landmark 학습 / 증강된 Landmark 학습)
  + LSTM 모델을 사용하여 실제 비디오에서 행동 인식
* Landmarks
  + 실제 비디오에서 추출한 Landmarks
  + Conditional Sequence 모델을 사용하여 생성한 Landmarks(데이터 증강)
* Blender 에서 비디오 다루기(화면 캡쳐)
* Tensorflow-Keras 모델
  + Conditional Sequence Model(keras)
  + 실제 비디오 데이터를 학습한 모델(keras)
  + 실제 비디오+증강 데이터를 학습한 모델(keras)
* Blender 에서 비디오 다루기(화면캡쳐 이미지)
<ol>
  <li>Github에 저장된 소스코드와 데이터, 이미지 링크 </li>
  <li>미디어파이프를 사용하여 mp4 비디오로부터 관절정보 추출하기(Python)</li>
  <li>추출된 관절 정보(CSV) </li>
  
  <li>Blender를 사용하여 mp4 비디오 생성시 크기 및 렌더링 속성 변환하기(Blender Output Properties) </li>
  <li>Blender를 사용하여 mp4 비디오 생성시 배경색상 지정하기(Blender World Properties) </li>
  <li>Blender를 사용하여 fbx 애니메이션의 프레임수 조정하기(Blender Graph Editor) </li>
  <li>Blender에서 애니메이션의 키프레임에 접근하여 관절의 회전량 조작하기(Python) </li>
  <li>Blender 애니메이션을 mp4 비디오로 변환하기(Blender Output Properties) </li>
  <li>Blender를 이용한 mp4 비디오의 좌우반전(Flipping, Blender Video Editing) </li>
  <li>Blender mp4비디오의 해상도, 프레임수, 좌우반전(Blender Output Properties) </li>
  <li>Google colab에서 mp4 비디오 데이터 학습(Model 1, Python) </li>
  <li>Google colab에서 mp4 비디오 데이터 학습(Model 2, Model 3, Python) </li>
  <li>모델검증 측정지표(Python) </li>
  <li>모델 검증에 사용된 150개 비디오 압축파일(real_vids_01.zip, real_vids_02.zip, real_vids_03.zip) </li>
  <li>LSTM 모델 시계열 데이터 전처리(Window Sliding) 이미지 및 코드 </li>
  <li>Mediapipe 관절정보 추출 대상 주요 관절이름(그래픽, 텍스트) </li>
  <li>원본 비디오 학습용으로 사용된 비디오(mp4):걷기, 달리기, 반전된 비디오 2개(총 4개) </li>
  <li>학습된 LSTM 모델 3개(Model 1, Model 2, Model 3)</li>
</ol>
