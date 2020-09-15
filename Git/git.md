# git

## Add의 여러 옵션들

- `git add -A` 또는 `git add --all`: stages all changes
- `git add .`: stages new files and modifications, **without deletions**
- `git add -u`: stages modifications and deletions, **without new files**

## git 관련 이슈 해결법

1. WSL 등 리눅스로 실행시 모든 파일들이 modified 로 인지되는 이슈
    `git config --global core.autocrlf true`
