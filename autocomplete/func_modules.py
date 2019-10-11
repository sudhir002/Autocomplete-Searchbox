import operator
import os

word_count = {}
words = []
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'word_search.tsv')
with open(file_path) as datafile:
    for row in datafile:
        word, frequency = row.split('\t')
        word_count[word] = int(frequency.strip())
        words.append(word)
#=========================================================
def searchword(word_letter):
    results = []
    for word in words:
        if word_letter in word:
            results.append(word)
    return results

#=========================================================
def sorting(results, incomplete_word):
    result_distances = [(result, result.find(incomplete_word), word_count[result], len(result)) for result in results]
    result_distances.sort(key=operator.itemgetter(1))
    result_distances.sort(key=operator.itemgetter(3))
    searchResults = [result_distance[0] for result_distance in result_distances][:25]
    return searchResults

#========================================================
def word_filter():
    word_count = {}
    words = []
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'word_search.tsv')
    with open(file_path) as datafile:
        for row in datafile:
            word, frequency = row.split('\t')
            word_count[word] = int(frequency.strip())
            words.append(word)
    return words

#==================================================h======