'''
Given array of sentences, return the set of words that are in one sentence but not all.

For example:

"My dog eats food"
"She eats food too"
"My dog food is good good"

Would return ['She', 'too', 'is', 'good']
*/
'''

def listOne(sentences):
    uniqueWords = {}
    for sentence in sentences:
        words = set(sentence.split(" "))
        for word in words:
            if word not in uniqueWords:
                uniqueWords[word] = 1
            else:
                uniqueWords[word] += 1

    ans = []
    for word, occurence in uniqueWords.items():
        if occurence == 1:
            ans.append(word)
    return ans


print(listOne(["My dog eats food","She eats food too","My dog food is good good"]))