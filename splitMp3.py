import os
import math
import shutil

from pydub import AudioSegment


def split(audio_file='./audio.mp3', sec=1, result_path='./results', format='mp3'):
    segment = AudioSegment.from_mp3(audio_file)
    duration = duration_end(segment.duration_seconds)

    song_list = get_song_list(segment, duration, sec)

    readyFolder('results')
    download(song_list, result_path, format)


def duration_end(duration):
    return math.ceil(duration * 1000)


def millisecond(sec):
    return sec * 60 * 1000


def get_song_list(segment, duration, sec):
    song_list = []
    for i in range(0, duration, millisecond(sec)):
        song_list.append(segment[i:i+millisecond(sec)])
    return song_list


def readyFolder(directory):
    try:
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def download(song_list, result_path, format):
    index = 0
    for song in song_list:
        file_name = os.path.join(result_path, f'{index}.{format}')
        song.export(file_name, format=format)
        index += 1
