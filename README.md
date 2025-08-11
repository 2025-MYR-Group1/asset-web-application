# asset-web-application
2025 UCSI Malaysia Intership Back-end 레포지토리입니다.


## 가상환경 생성
> 작업시 가상환경을 생성해주세요.
```
python -m venv venv
```

## 가상환경 활성화
> 프로젝트 루트에서 실행해주세요.
```
source venv/bin/activate
```
> windows에서는 아래의 명령어를 입력하여 주시기 바랍니다.
```
source venv/Scripts/activate
```

## 의존성 패키지 설치
> 작업시 의존성 패키지를 설치해주세요.
```
pip install -r requirements.txt
```

## 의존성 패키지 업데이트
```
pip freeze > requirements.txt
```

## Commit Message Convetion Type 
> 커밋 메세지 앞에 접두사(prefix)를 붙입니다.

|**type**|**description**|
|--|--|
| `Feat` | 새로운 화면, 기능, 이미지 등 **추가 작업** |
| `Fix` | 버그, 기능 등 **오류 수정** |
| `Style` | 여백(padding), 색상(Color) 등 **UI 디테일 변경** |
| `Chore` | 설정, 파일정리, 리소스 관리(이미지 삭제, 파일 이름 변경 등) **기능 외 작업** |
| `Docs` | 문서(README) 작성 및 주석 추가/삭제/수정 |
| `Refactor` | 내부 코드 구조 개선(변수명 정리, 코드 분리, 모듈화 등) |
| `Perf` | 성능 최적화(루프 최적화, 중복제거, 연산량 감소 등) |
