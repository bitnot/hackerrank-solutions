#!/bin/python3

import os
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    letter_heights = [h[ord(c)-ord('a')] for c in word]
    return max(letter_heights)*len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    fptr.write(str(result) + '\n')
    fptr.close()