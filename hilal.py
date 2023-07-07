from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href="/gerçekler_sayfasi">Rastgele bir gerçeği görüntüle!</a>'


@app.route("/hilal")
def hilal():
    return '<h1>merhaba ben hilalim!</h1>'


@app.route("/gerçekler_sayfasi")
def gercekler():
    facts_lists = ['Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.',
                   'Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.',
                   '2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin 50den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.',
                   'Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.']
   
    return f'<h1>{random.choice(facts_lists)}</h1>'

@app.route("/şifre_oluşturucu")
def sifre_olusturucu():
    sifre = ["+-/*!&$#?=@<>","+-/*,.:2`4&","90+-*1½$#£","7'^+%98½$#","½#$56/&"]

    return f'<h1>{random.choice(sifre)}</h1>'


app.run(debug=True)