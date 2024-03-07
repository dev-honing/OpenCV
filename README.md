# OpenCV

## 작업 의의
### 1. OpenCV를 이용한 이미지 핸들링
회전, 그레이스케일링, 자르기
### 2. 고용량 이미지의 색상 코드 분석
rgb 값을 반복문으로 빈 리스트에 저장
### 3. 이미지의 색상 코드를 JSON 저장
리스트에 저장한 값을 JSON으로 저장
### 4. JSON 색상 코드 기반으로 원본 이미지 복원
저장한 JSON을 불러와 원본 이미지로 복원
### 5. 그레이스케일링 및 평탄화
저장한 JSON 리스트의 길이 및 타입을 체크하고, 2차원->1차원 리스트로 평탄화
### 6. 각 JSON 비교/분석(그래프화)
matplotlib 라이브러리를 사용해 차이점을 그래프화

그레이스케일링의 의의 탐색

![Alt text](image.png)


## 어려움
### 1. GitHub에 Push할 수 없는 문제
#### 1-1. 원인: 대용량(100MB) 이상의 JSON 파일을 Push 시도
```
 OpenCV  git push origin main
Enumerating objects: 73, done.
Counting objects: 100% (73/73), done.
Delta compression using up to 16 threads
Compressing objects: 100% (69/69), done.
error: RPC failed; HTTP 400 curl 92 HTTP/2 stream 7 was not closed cleanly: CANCEL (err 8)
send-pack: unexpected disconnect while reading sideband packet
Writing objects: 100% (71/71), 107.94 MiB | 3.20 MiB/s, done.
Total 71 (delta 30), reused 0 (delta 0), pack-reused 0
fatal: the remote end hung up unexpectedly
```
#### 1-2. 대응: Git LFS를 통해 시도
1-2-1. Git LFS 설치

설치 명령: `git lfs install`

설치 확인: 
```
 OpenCV  git lfs install
Updated Git hooks.
Git LFS initialized.
```

1-2-2. Git LFS가 추적할 파일의 유형 설정

세팅 명령: `git lfs track *.json`

세팅 확인:
```
 OpenCV  git lfs track *.json
Tracking "*.json"
```

1-2-3. Git에 변경 사항을 커밋
새롭게 생성된 .gitattributes 파일을 커밋

커밋 명령: `git commit -m "Setup: Git LFS로 대용량 JSON 파일을 추적`

커밋 확인: 
```
 OpenCV  git commit -m "Setup: Git LFS로 대용량 JSON 파일을 추적"
[main 4986212] Setup: Git LFS로 대용량 JSON 파일을 추적
 4 files changed, 10 insertions(+), 3 deletions(-)
 create mode 100644 .gitattributes
```

1-2-4. main 브랜치에 커밋한 내용을 푸시

푸시 명령: `git push origin main`

푸시 실패: 

```
 OpenCV  git push origin main
Uploading LFS objects: 100% (3/3), 690 MB | 0 B/s, done.
Enumerating objects: 79, done.
Counting objects: 100% (79/79), done.
Delta compression using up to 16 threads
Compressing objects: 100% (74/74), done.
error: RPC failed; HTTP 400 curl 92 HTTP/2 stream 7 was not closed cleanly: CANCEL (err 8)
send-pack: unexpected disconnect while reading sideband packet
Writing objects: 100% (77/77), 107.94 MiB | 3.14 MiB/s, done.
Total 77 (delta 31), reused 0 (delta 0), pack-reused 0
fatal: the remote end hung up unexpectedly
Everything up-to-date
```

### 1-2. 대응: Git Ignore 세팅
JSON 파일의 크기가 매우 크므로, 직접 push하는 것이 권장되지 않는다고 한다.

파일을 분할하거나, 외부의 데이터 저장소(Amazon S3, Google Cloud Storage 등)를 사용해 외부에 저장하는 것이 적절하다고 한다.

### 2. Git으로 Commit한 내용을 Push 하지 못하는 문제
#### 2-1. 원인: 대용량 JSON 파일을 이미 Commit
#### 2-2. 대응: 캐시된 인덱스에서 파일을 제거
1. color_codes.json(310MB)을 삭제
    
    삭제 명령 및 확인: 
    ```
     OpenCV  git rm --cached color_codes.json
    rm 'color_codes.json'
    ```

2. color_codes_flat.json(270MB)를 삭제

    삭제 명령 및 확인:
    ```
     OpenCV  git rm --cached color_codes_flat.json
    rm 'color_codes_flat.json'
    ```

3. gray_color_codes.json(90MB)를 삭제
    
    삭제 명령 및 확인:
    ```
     OpenCV  git rm --cached gray_color_codes.json
    rm 'gray_color_codes.json'
    ```

4. 새로운 커밋
    
    커밋 명령 및 확인:
    ```
     OpenCV  git commit -m "Fix: 대용량 JSON 파일들의 캐시된 데이터 삭제"
    [main c3b7006] Fix: 대용량 JSON 파일들 삭제                                                                   in pwsh at 12:20:38
    2 files changed, 6 deletions(-)
    delete mode 100644 color_codes.json
    delete mode 100644 color_codes_flat.json
    ```

    푸쉬 시도 및 실패:
    ```
     OpenCV  git push origin main
    Uploading LFS objects: 100% (3/3), 690 MB | 0 B/s, done.
    Enumerating objects: 86, done.
    Counting objects: 100% (86/86), done.
    Delta compression using up to 16 threads
    Compressing objects: 100% (80/80), done.
    error: RPC failed; HTTP 400 curl 92 HTTP/2 stream 7 was not closed cleanly: CANCEL (err 8)
    send-pack: unexpected disconnect while reading sideband packet
    Writing objects: 100% (84/84), 107.94 MiB | 3.15 MiB/s, done.
    Total 84 (delta 34), reused 0 (delta 0), pack-reused 0
    fatal: the remote end hung up unexpectedly
    Everything up-to-date
    ```

#### 2-2. 대응: JAVA 및 BFG 설치 후 재시도
1. JAVA 설치 및 확인
    ```
     OpenCV  java -version
    java version "1.8.0_401"
    Java(TM) SE Runtime Environment (build 1.8.0_401-b10)
    Java HotSpot(TM) Client VM (build 25.401-b10, mixed mode, sharing)
    ```

2. BFG 설치 및 확인

    https://rtyley.github.io/bfg-repo-cleaner/에서 bfg-1.14.0 설치(Downloads/ 경로에 위치)

3. BFG Repo-Cleaner 실행 및 JSON 삭제
    
    삭제 명령: `java -jar C:\Users\Administrator\Downloads\bfg-1.14.0.jar --delete-files *.json`

    삭제 확인: 
    내용이 길어서 bfg.md를 따로 생성해 저장

4. Git Reflog 만료 및 불필요한 객체 삭제
    
    삭제 명령: `git reflog expire --expire=now --all; git gc --prune=now --aggressive`

    삭제 확인: 
    ```
     OpenCV  git reflog expire --expire=now --all; git gc --prune=now --aggressive
    Enumerating objects: 82, done.
    Counting objects: 100% (82/82), done.
    Delta compression using up to 16 threads
    Compressing objects: 100% (76/76), done.
    Writing objects: 100% (82/82), done.
    Total 82 (delta 35), reused 3 (delta 0), pack-reused 0
    ```

5. 원격 저장소에 강제 푸시
    
    푸시 명령: `git push origin --force --all`

    푸시 확인: 
    ```
     OpenCV  git push origin --force --all
    Enumerating objects: 81, done.
    Counting objects: 100% (81/81), done.
    Delta compression using up to 16 threads
    Compressing objects: 100% (40/40), done.
    Writing objects: 100% (79/79), 70.69 KiB | 70.69 MiB/s, done.
    Total 79 (delta 35), reused 79 (delta 35), pack-reused 0
    remote: Resolving deltas: 100% (35/35), done.
    To https://github.com/dev-honing/OpenCV.git
    426f927..9d0cf4d  main -> main
    ```