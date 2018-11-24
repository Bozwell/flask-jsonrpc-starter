# flask-jsonrpc-starter
flask를 이용해서 api서버를 만들때 구조화되어 있고 좀더 쉽게 개발을 시작할 목적으로 시작한 템플릿프로젝트 입니다.

## 본 템플릿 프로젝트는 아래와 같운 기술들로 구성되어 있습니다.
* Flask-JSONRPC를 이용해서 jsonrpc 형식의 api를 제공합니다.
* 데이타 저장소는 Postgresql DB를 사용하며 SQLAlehemy를 이용해서 핸들링합니다.
* 스케쥴 작업은 Flask-APScheduler를 이용합니다.



[2018-11-24] @scheduler.task decordater를 사용하기위해 Flask-APScheduler를 pip를 통해 설치하지 않고 소스코드를 다운받아 설치해야한다.
