
from cut import mmcut
from json import load
def searchMovieNameInDic(question):
    cut = mmcut(question)
    with open('new.txt', mode='r', encoding='utf-8-sig') as f:
        a = load(f)
        e = ''
        for key, value in a.items():
            for i in cut:
                if i in value:
                    w = key.lower()
                    u  =str(w)
                    e = e+u
        return e
