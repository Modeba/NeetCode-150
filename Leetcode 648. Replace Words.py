sentence = "the cattle was rattled by the battery"
dictionary = ["cat","bat","rat"]

def replaceWords(dictionary, sentence):
    sentence = sentence.split()

    for i in range(len(sentence)):
        for root in dictionary:
            if sentence[i].startswith(root):
                sentence[i] = root
    
    sentence = ' '.join(sentence)
    return sentence

print(replaceWords(dictionary, sentence))