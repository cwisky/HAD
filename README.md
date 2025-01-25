# HAD
* HAD(Human Action Detection)
## Table of Contents(Files)
* 학습용 실제 비디오(mp4) 6개
* 테스트용 실제 비디오(mp4) 150개
* Blender 애니메이션 비디오
* 소스 코드
  + Blender 애니메이션을 mp4 렌더링 : https://github.com/cwisky/HAD/blob/main/scripts/Blender_anim_render_mp4.py
  + Colab에서 Mediapipe를 사용하여 csv 추출 : https://github.com/cwisky/HAD/blob/main/scripts/Colab_Mediapipe_Works.ipynb
  + Anaconda에서 Conditional Sequence 모델 생성 및 Landmark 생성 : https://github.com/cwisky/HAD/blob/main/scripts/Anaconda_Conditional_Sequence.ipynb
  + LSTM 모델 학습 (실제 비디오 Landmark 학습 / 증강된 Landmark 학습) : 위의 링크 참조
  + LSTM 모델을 사용하여 실제 비디오에서 행동 인식  : 위의 링크 참조
* Landmarks
  + 실제 비디오에서 추출한 Landmarks(LSTM Training) : https://github.com/cwisky/HAD/blob/main/csv/csv_real_videos(run)_for_train.zip, https://github.com/cwisky/HAD/blob/main/csv/csv_real_videos(walk)_for_train.zip
  + Blender 애니메이션 파생 비디오에서 추출한 Landmarks(Conditional Sequence 모델 학습용) : https://github.com/cwisky/HAD/blob/main/csv/anim_csv.zip
  + Conditional Sequence 모델을 사용하여 생성한 Landmarks(데이터 증강) : https://github.com/cwisky/HAD/blob/main/csv/generated_csv.zip
* Tensorflow-Keras 모델
  + Conditional Sequence Model(keras) : https://github.com/cwisky/HAD/blob/main/models/best_walk_model.keras, https://github.com/cwisky/HAD/blob/main/models/best_run_model.keras
  + 실제 비디오 데이터를 학습한 모델(Model1.keras) : https://github.com/cwisky/HAD/blob/main/models/seed_R-11_lstm_model.keras
  + 실제 비디오+증강 데이터를 학습한 모델(Model2.keras) : https://github.com/cwisky/HAD/blob/main/models/seed_A-11_lstm_model.keras
* Blender 에서 비디오 다루기(화면캡쳐 이미지)
<ol>
  <li>Blender를 사용하여 mp4 비디오 생성시 크기 및 렌더링 속성 변환하기(Blender Output Properties) : https://github.com/cwisky/HAD/blob/main/images/fbx2mp4_01.png</li>
  <li>Blender를 사용하여 mp4 비디오 생성시 배경색상 지정하기(Blender World Properties) : https://github.com/cwisky/HAD/blob/main/images/fbx2mp4_01_01_background_color.png</li>
  <li>Blender를 사용하여 fbx 애니메이션의 프레임수 조정하기(Blender Graph Editor) : https://github.com/cwisky/HAD/blob/main/images/graph_edit_02.png</li>
  <li>Blender 애니메이션을 mp4 비디오로 변환하기(Blender Output Properties) : https://github.com/cwisky/HAD/blob/main/images/mp4_flip_01.png, https://github.com/cwisky/HAD/blob/main/images/mp4_flip_02.png, https://github.com/cwisky/HAD/blob/main/images/mp4_flip_03.png </li>
  <li>Blender mp4비디오의 해상도, 프레임수, 좌우반전(Blender Output Properties) : https://github.com/cwisky/HAD/blob/main/images/mp4_resolution_fps_adjust.png</li>
  <li>mp4 비디오 파일로 렌더링 : https://github.com/cwisky/HAD/blob/main/images/fbx2mp4_02.png</li>
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

