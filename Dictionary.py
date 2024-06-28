from nltk.corpus import wordnet

class Dictionar:
    def Defination(word):
        synsets = wordnet.synsets(word)
        if synsets:
            print(">>>>>Definitions:")
            for synset in synsets:
                print("-", synset.definition())
        else:
            print("!!!!!!No definitions found for the word '{}'".format(word))

    def Synonyms(word):
        synonyms = set()
        for synset in wordnet.synsets(word):
            for lemma in synset.lemmas():
                synonyms.add(lemma.name())
        synonyms.discard(word)
        if synonyms:
            print(">>>>>>>Synonyms:", synonyms)
        else:
            print("!!!!No synonyms found for the word '{}'".format(word))

    def Antonyms(word):
        antonyms = set()
        for synset in wordnet.synsets(word):
            for lemma in synset.lemmas():
                if lemma.antonyms():
                    antonyms.add(lemma.antonyms()[0].name())
        if antonyms:
            print(">>>>>>>>Antonyms:", antonyms)
        else:
            print("!!!!!!!No antonyms found for the word '{}'".format(word))

    def main():
        word = input("Enter a word: ")
        print("Word:", word)
        
    if __name__ == "__main__":
        word = input("Enter a word: ")
        Defination(word)
        Synonyms(word)
        Antonyms(word)
        
ob=Dictionar()