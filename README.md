# SoMA-Hackathon


## 팀 소개 

> 팀명 
- SWM 12기 해카톤 21팀 `부캐 파티`

> 멘토
- [`이민경`] 
> 팀원
- [`이정우`]
- [`오승찬`]
- [`정용훈`]
- [`정재헌`]
- [`최수환`]


## 기획 의도

저희는 팬데믹으로 인해 여러모로 교육, 관광 등 일상생활에 어려움이 있기에, 동물과 문화사에 대한 교육적 3D 공공 데이터를 수집 및 재구성하여 집에서 쉽게 이용 가능한 `AR 실감 체험 웹` "내 손안의 ***** 라이브러리" 프로토타입을 개발하였습니다.

## 콘텐츠 및 기능 

프로토타입의 시범 콘텐츠는 동물, 우리나라의 문화재, 해외의 문화재 등 카테고리로 구성하였습니다.  
각 항목에서 세부 콘텐츠를 선택하여 3D와 AR로 볼 수 있습니다. 

스크린샷 3장 나란히
<p align="left"><img src="https://user-images.githubusercontent.com/42955392/118197773-91d3de80-b48a-11eb-8333-fcee19e6c38b.PNG" width="30%">
<img src="https://user-images.githubusercontent.com/42955392/118203859-f3e71080-b497-11eb-9fa1-8341841c87fb.jpeg" width="30%"><img src="https://user-images.githubusercontent.com/42955392/118203952-1842ed00-b498-11eb-9b64-a724cf5aff34.jpeg" width="30%"></p>



## 서버 실행 방법 

구름 컨테이너 생성
Github 연동 통해  SoMA_Hackathon 불러오기
Django 선택

가장 위쪽 web_study를 경로로 놓고
`python manage.py migrate` 실행

이후 web_study 경로에서 항상 `python manage.py runserver 0.0.0.0:포트번호`으로 서버 실행
`web_study/settings.py`에서 ALLOWED_HOSTS에 자기 서버 주소 넣어야 외부 접속 가능
