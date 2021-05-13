# SoMA-Hackathon


구름 컨테이너 생성
Github 연동 통해  SoMA_Hackathon 불러오기
Django 선택

가장 위쪽 web_study를 경로로 놓고
`python manage.py migrate` 실행

이후 web_study 경로에서 항상 `python manage.py runserver 0.0.0.0:포트번호`으로 서버 실행
`web_study/settings.py`에서 ALLOWED_HOSTS에 자기 서버 주소 넣어야 외부 접속 가능
자기 서버 주소로 폰이든 컴이든 접속