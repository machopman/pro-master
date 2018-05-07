import re

import requests
from namemoviebefore import findmovie
def checkfunction(event,userid):
    movie_name = re.sub('[กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮฝฦใฬมฒท?ื์ิ.่๋้็เโ,ฯี๊ัํะำไๆ๙๘๗๖๕ึ฿ุู๔๓๒๑+ๅาแ]','', event.message.text).replace(' ', '')
    if movie_name != '':
        movie_name = movie_name.lower()
        URL = "http://mandm.plearnjai.com/API/id_nameMovie.php?key=mandm"
        r = requests.get(url=URL)
        data = r.json()
        found = False
        for movie in data:
            print(movie['nameEN'])
            if movie_name == movie['nameEN'].lower().replace(' ', ''):
                found = True
                Movie_URL = 'http://mandm.plearnjai.com/API/detailMovie.php?idmovie=' + movie['idIMDb']
                r = requests.get(url=Movie_URL)
                movie_detail = r.json()
                gen = movie_detail['response'][0]['detailMovie'][0]['Genre']
                date = movie_detail['response'][0]['detailMovie'][0]['Date']
                poster = movie_detail['response'][0]['detailMovie'][0]['Poster']
                direct = movie_detail['response'][0]['detailMovie'][0]['Direct']
                actor = movie_detail['response'][0]['detailMovie'][0]['Actor']
                story = movie_detail['response'][0]['detailMovie'][0]['Synopsis']
                url = 'http://movieapi.plearnjai.com/DEV/API/Summarization.php?idmovie=' + movie['idIMDb']
                r = requests.get(url=url)
                response = r.json()
                review = response['response']['Review_mandm']
                spoil = response['response']['spoilers']
                sum = []
                if actor !='':
                    sum.append('ชื่อนักแสดง ')
                if direct !='':
                    sum.append('ชื่อผู้กำกับ ')
                if poster!='':
                    sum.append('แสดงรูปภาพ ')
                if story!='':
                    sum.append('เรื่องย่อ ')
                if story!='':
                    sum.append('เรื่องย่อ ')
                if date !='':
                    sum.append('ประเภทเรื่อง ')
                if review!='':
                    sum.append('รีวิวหนัง ')
                if spoil!='':
                    sum.append('สปอย ')
                return  sum

    if movie_name == '':
        mov = findmovie(userid)
        movie_name = mov.lower().replace(' ', '')
        URL = "http://mandm.plearnjai.com/API/id_nameMovie.php?key=mandm"
        r = requests.get(url=URL)
        data = r.json()
        found = False
        for movie in data:
            print(movie['nameEN'])
            if movie_name == movie['nameEN'].lower().replace(' ', ''):
                found = True
                Movie_URL = 'http://mandm.plearnjai.com/API/detailMovie.php?idmovie=' + movie['idIMDb']
                r = requests.get(url=Movie_URL)
                movie_detail = r.json()
                gen = movie_detail['response'][0]['detailMovie'][0]['Genre']
                date = movie_detail['response'][0]['detailMovie'][0]['Date']
                poster = movie_detail['response'][0]['detailMovie'][0]['Poster']
                direct = movie_detail['response'][0]['detailMovie'][0]['Direct']
                actor = movie_detail['response'][0]['detailMovie'][0]['Actor']
                story = movie_detail['response'][0]['detailMovie'][0]['Synopsis']
                url = 'http://movieapi.plearnjai.com/DEV/API/Summarization.php?idmovie=' + movie['idIMDb']
                r = requests.get(url=url)
                response = r.json()
                review = response['response']['Review_mandm']
                spoil = response['response']['spoilers']
                sum = []
                if actor !='':
                    sum.append('ชื่อนักแสดง ')
                if direct !='':
                    sum.append('ชื่อผู้กำกับ ')
                if poster!='':
                    sum.append('แสดงรูปภาพ ')
                if story!='':
                    sum.append('เรื่องย่อ ')
                if story!='':
                    sum.append('เรื่องย่อ')
                if date !='':
                    sum.append('ประเภทเรื่อง ')
                if review!='':
                    sum.append('รีวิวหนัง ')
                if spoil!='':
                    sum.append('สปอย ')
                return  sum

