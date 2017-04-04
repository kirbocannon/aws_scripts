import nltk

from archive.TextToSpeech import voiceInputToAlexis
from aws import callServerStatus

#tags
NNP = 'NNP'
WP = 'WP'
WRB = 'WRB'
VBZ = 'VBZ'
NN = 'NN'



def questionInput(sentence):
    pb = 0
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    print(tokens)
    print(tagged)
    for i in tokens:
        if i == 'server':
            pb +=1
        if i == 'status':
            pb +=1
    if pb == 2:
        result = callServerStatus()
    if result == 1:
        voiceInputToAlexis('All Servers are Operational')
    else:
        voiceInputToAlexis('There appears to be an issue ')
















"""
class Questions:

    def questionsSentenceInput(self, sentence):
        '''This is where the question is asked. My voice is converted into text and ingested here'''
        self.tokens = nltk.word_tokenize(sentence)

        for i in self.tokens: #Always strip the calling of my dear friend Alexis, maybe later make into function
            if 'Alexis' in i:
                self.tokens.remove(i)

        print(self.tokens)

        tagged = nltk.pos_tag(self.tokens)
        print(tagged)

        #self.questionsWhat(tagged)

    def questionsWhat(self, input_tags):
        '''This function checks the probability of you asking who someone is'''
        tags = input_tags
        total_index_cnt = len(self.tokens)
        condition = 0
        cnt = 0
        pronouns = []
        nouns = []

        while cnt < total_index_cnt:
            if WP in tags[cnt]:
                pronouns.append(tags[cnt][0])
                if 'who' in pronouns:
                    condition += 2
            if NNP in tags[cnt]:
                nouns.append(tags[cnt][0])
                condition += 1

            cnt += 1

        if condition > 2:
            print("You would like to know who %s is." %(self.printList(nouns)))
            voiceInputToAlexis("You would like to know who %s is." %(self.printList(nouns)))

    def printList(self, list):
        self.l = list
        self.l = ",".join(list).replace(',' ,' ')
        return self.l

    def search(self, voice):
        voiceInputToAlexis(voice)


#q = Questions()
#q.sentenceInput("Who is Tom Cruise?")

"""



