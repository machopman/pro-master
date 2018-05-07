
import  re
import  requests
from cut import mmcut
from json import load
from googletrans import Translator
import random

from searchMovieNameInDic import searchMovieNameInDic
from namemoviebefore import findmovie

def movie_review(event,question,userid):
    movie_name = re.sub('[กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮฝฦใฬมฒท?ื์ิ.่๋้็เโ,ฯี๊ัํะำไๆ๙๘๗๖๕ึ฿ุู๔๓๒๑+ๅาแ]','',event.message.text).replace(' ', '')
    if movie_name != '':
        movie_name = movie_name.lower()
        URL = "http://mandm.plearnjai.com/API/id_nameMovie.php?key=mandm"
        r = requests.get(url=URL)
        data = r.json()
        found = False
        for movie in data:
            if movie_name == movie['nameEN'].lower().replace(' ', ''):
                found = True
                Movie_URL = 'http://movieapi.plearnjai.com/DEV/API/Summarization.php?idmovie=' + movie['idIMDb']
                r = requests.get(url=Movie_URL)
                response = r.json()
                detail = response['response']['Review_mandm']
                detail = detail.replace('\n','')
                detail = detail.replace('/n','')


                if detail != None or detail != None:
                    translator = Translator()
                    translations = translator.translate(detail, dest='th')
                    return translations.text
                else:
                    return 'ยังไม่ได้รีวิวหนังเรื่องนี้เลยครับ'
        if found == False:
            return 'ยังไม่ได้รีวิวหนังเรื่องนี้เลยครับ'

    elif (movie_name=='')and (searchMovieNameInDic(question)==''):
            mov = findmovie(userid)
            if mov !='A':
                movie_name = mov.lower().replace(' ','')
                URL = "http://mandm.plearnjai.com/API/id_nameMovie.php?key=mandm"
                r = requests.get(url=URL)
                data = r.json()
                found = False
                for movie in data:
                    if movie_name == movie['nameEN'].lower().replace(' ', ''):
                        found = True
                        Movie_URL = 'http://movieapi.plearnjai.com/DEV/API/Summarization.php?idmovie=' + movie['idIMDb']
                        r = requests.get(url=Movie_URL)
                        response = r.json()
                        detail = response['response']['Review_mandm']

                        if detail != None or detail != None:
                            translator = Translator()
                            translations = translator.translate(detail, dest='th')
                            return translations.text
                        else:
                            return 'ยังไม่ได้รีวิวหนังเรื่องนี้เลยครับ'
                if found == False:
                    return 'ยังไม่ได้รีวิวหนังเรื่องนี้เลยครับ'
            elif  mov =='A':
                 return  'กรุณาพิมพ์ ชื่อหนัง + สิ่งที่ต้องการถาม';

    else:
        cut = mmcut(event.message.text)
        with open('new.txt', mode='r', encoding='utf-8-sig') as f:
            a = load(f)
            for key, value in a.items():
                for i in cut:
                    try:
                        if i in value:
                            w = key.lower()
                            movie_name = w.lower()
                            URL = "http://mandm.plearnjai.com/API/id_nameMovie.php?key=mandm"
                            r = requests.get(url=URL)
                            data = r.json()
                            found = False
                            for movie in data:
                                if movie_name == movie['nameEN'].lower().replace(' ', ''):
                                    found = True
                                    Movie_URL = 'http://movieapi.plearnjai.com/DEV/API/Summarization.php?idmovie=' + movie['idIMDb']
                                    r = requests.get(url=Movie_URL)
                                    response = r.json()
                                    detail = response['response']['Review_mandm']
                                    detail = detail.replace('\n', '')
                                    detail = detail.replace('/n', '')

                                    if detail != None or detail != None:
                                        translator = Translator()
                                        translations = translator.translate(detail, dest='th')
                                        return translations.text
                                    else:
                                        return 'ยังไม่ได้รีวิวหนังเรื่องนี้เลย'
                            if found == False:
                                    return 'ยังไม่ได้รีวิวหนังเรื่องนี้เลย'
                    except :
                        return 'ยังไม่ข้อมูลรีวิวเลย'

#print(movie_review('ขอรีวิวwonderwomanหน่อย'))
#print(movie_review('ขอรีวิววันเดอวูแมนหน่อย'))