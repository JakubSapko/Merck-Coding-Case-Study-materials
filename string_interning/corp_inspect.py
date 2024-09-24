import guppy
import nltk
import sys

heap = guppy.hpy()
heap.setrelheap()

nltk.download("genesis")

gen = nltk.corpus.genesis.words()
print(heap.heap())

del gen

gen = [sys.intern(word) for word in nltk.corpus.genesis.words()]
print(heap.heap())
