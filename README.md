# ncloud-csr

네이버 클라우드 플랫폼 CSR(Clova Speech Recognition) API 사용을 위한 코드입니다. 음성을 STT로 텍스트로 가져온 후 이를 전처리합니다.

## Getting Started

다음을 설치해야 합니다.

- [ffmpeg](https://www.ffmpeg.org/)

- [libab](https://libav.org/)

- requirements.txt

이후 현재 디렉토리에 `audio.mp3` 파일을 넣고 `python3 main.py` 를 실행하시기 바랍니다.

## env

디렉토리 내에는 다음의 값을 담은 `.env` 파일이 있어야 합니다.

```shell
# .env
CLIENT_ID=<네이버 API client id>
CLIENT_SECRET=<네이버 API client secret>
```

## results

프로그램을 실행 후 결과가 저장되는 디렉토리입니다. STT 처리를 위해 분할된 mp3 파일, STT 결과가 저장된 `result.txt`, kss 를 사용해서 문장별로 나누는 전처리를 수행한 `result_kss.txt` 파일이 생성됩니다.

예시

```shell
# result.txt

2000년도 1월에 이제 팩으로 지수 화 시켜서 얼마만큼 제 차이가 났는지를 본 거예요 같이 동행을 하다가 언제부터 큰차이가 났냐면은 2010년서부터 여기 꼭지가 2015년 말이에요
```

```shell
# result_kss.txt

2000년도 1월에 이제 팩으로 지수 화 시켜서 얼마만큼 제 차이가 났는지를 본 거예요
같이 동행을 하다가 언제부터 큰차이가 났냐면은 2010년서부터 여기 꼭지가 2015년 말이에요
```

## reference

[ncloud guide](https://guide.ncloud-docs.com/docs/ko/naveropenapiv3-speech-recognition-sdk)
