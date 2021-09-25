from kss import split_sentences

def segmentation(source='results/result.txt', target='results/result_kss.txt'):
    text = ''
    with open(source, 'r') as f:
        text = f.readline()

    with open(target, 'w') as f:
        for sentence in split_sentences(text):
            f.write(sentence + '\n')
