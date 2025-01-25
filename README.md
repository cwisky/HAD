# HAD
* HAD(Human Action Detection)
## Table of Contents(Files)
* 학습용 실제 비디오(mp4) 6개
* 테스트용 실제 비디오(mp4) 150개
* Blender 애니메이션 비디오
* 소스 코드
  + Blender 애니메이션을 mp4 렌더링
  + Colab에서 Mediapipe를 사용하여 csv 추출
  + Anaconda에서 Conditional Sequence 모델 생성 및 Landmark 생성
  + LSTM 모델 학습 (실제 비디오 Landmark 학습 / 증강된 Landmark 학습)
  + LSTM 모델을 사용하여 실제 비디오에서 행동 인식
* Landmarks
  + 실제 비디오에서 추출한 Landmarks(LSTM Training)
  + Blender 애니메이션 파생 비디오에서 추출한 Landmarks(Conditional Sequence 모델 학습용)
  + Conditional Sequence 모델을 사용하여 생성한 Landmarks(데이터 증강)
* Tensorflow-Keras 모델
  + Conditional Sequence Model(keras)
  + 실제 비디오 데이터를 학습한 모델(Model1.keras)
  + 실제 비디오+증강 데이터를 학습한 모델(Model2.keras)
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

## 작업 순서
1. mixamo.com 에서 애니메이션(walk.fbx, run.fbx) 다운로드
2. Blender에서 fbx import
3. 애니메이션을 mp4 비디오로 렌더링하기 위한 설정(카메라, 조명, Armature 회전, 출력을 위한 포맷/인코딩/크기/배경/조명/밝기 등)
4. Blender에서 Python 코드를 실행하여 mp4 비디오 생성(Armature 회전량을 증가하면서 매 지정 각도마다 mp4 렌더링 실행)
   + Armature의 회전각도를 mp4 파일명에 포함(Anim_run_angel_5.mp4 형식)
5. 위에서 생성된 mp4 비디오로부터 Google Mediapipe를 사용하여 Landmarks 추출하고 csv 파일에  저장
6. 위의 csv 파일을 사용하여Conditional Sequence 모델 학습/파일에 저장(.keras)
7. 학습된 Conditinal Sequence 모델을 사용하여 Landmark 생성 및 csv 파일에 저장(데이터 증강)
8. 실제 비디오 6개 Landmark를 학습한 LSTM 모델(Model 1) 생성/학습/저장
9. Model 1을 사용하여 실제 비디오 150개 인식율 확인
10. 실제 비디오 6개 Landmark + 증강 데이터를 학습한 LSTM 모델(Model 2) 생성/학습/저장
    + 실제 사용된 증강 데이터, 각도별 (0, -1, 15, -20, 35,  –50, 50, -60, 60, -75, -80, -85)
11. Model 2를 사용하여 실제 비디오 150개 인식율 확인

## 작업 순서에 따라 생성되거나 사용되는 산출물(파일)
1. walk.fbx, run.fbx
2. x
3. x
4. Blender_anim_render_mp4.py, *.mp4 (anim_walk_angle_n_.mp4,  anim_run_angle_n형식)
5. *.csv (anim_walk__angle_n_.csv 형식) : blender_anim_render_mp4.py,  anim_csv.zip
6. Anaconda_Conditional_Sequence.ipynb, *.keras ( conditional_run_LSTM_model.keras, conditional_walk_LSTM_model.keras )
7. *.csv
8. Colab_Meediapipe_work.ipynb, Model 1.keras, 학습용 실제 비디오(mp4) 6개,
9. Colab_Mediapipe_work.ipynb, 테스트용 실제 비디오(mp4) 150개
10.Colab_Mediapipe_work.ipynb, Model 2.keras, Blender_rendered_videos(walk).zip,  Blender_rendered_videos(run).zip
11.Model 2.keras, 테스트용 비디오 150개
