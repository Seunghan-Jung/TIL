# git

## Add의 여러 옵션들

- `git add -A` 또는 `git add --all`: stages all changes
- `git add .`: stages new files and modifications, **without deletions**
- `git add -u`: stages modifications and deletions, **without new files**

## git 관련 이슈 해결법

1. WSL 등 리눅스로 실행시 모든 파일들이 modified 로 인지되는 이슈
    `git config --global core.autocrlf true`

## 추적 중인 파일 이름 변경 또는 디렉토리 변경

추적 중인 파일을 그냥 이름을 바꾸거나 위치를 옮기면, 본래의 파일이 삭제되고 새로운 파일이 생긴 것으로 인식한다.

그렇게 되길 원치 않다면 `git mv` 명령어를 사용한다

- 이름만 바꾼다 : `git mv (파일명) (바꿀 파일명)`

    ex) `git mv test.py model.py`

- 위치만 이동 : `git mv (파일명) (바꿀 위치의 폴더명)`

    ex) `git mv test.py python/`  

- 위치 이동 & 이름 변경 : `git mv (파일명) (바꿀 위치 디렉토리)/(바꿀 파일 명)`

    ex) `git mv test.py python/model.py`

