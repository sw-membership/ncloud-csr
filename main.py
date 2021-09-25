import os

from splitMp3 import split
from sound2text import sound2text
from segmentation import segmentation

result_path = 'results'

if __name__ == '__main__':
    print('오디오 파일 분할중...')
    split()
    print('오디오 파일 분할 완료')

    print('STT 수행중...')
    text = ''
    for file in sorted(os.listdir(result_path)):
        audio_file = os.path.join(result_path, file)
        text += sound2text(audio_file)
    print('STT 완료')
    
    print('결과 저장중...')
    with open(os.path.join(result_path, 'result.txt'), 'w') as f:
        f.write(text)
    print('결과 저장 완료')

    print('띄어쓰기 세그멘테이션 실행중...')
    segmentation()
    print('띄어쓰기 세그멘테이션 완료')
