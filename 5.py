from flask import Flask
import random
app = Flask(__name__)

facts_list = ["Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
            "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor.",
            "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
            "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir."]

@app.route("/")
def index():
        return f'<h1>MERHABA! Bu sayfada, teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz!<a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a>'

@app.route("/rastgele_gercek")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/yazi-tura")
def yazi_tura():
    sonuc = random.choice(["Yazı", "Tura"])
    sonuc2 = random.choice(["Yazı", "Tura"])
    sonuc3 = random.choice(["Yazı", "Tura"])
    return f"Yazı–Tura sonucunları: {sonuc} {sonuc2} {sonuc3}"


app.run(debug=True)
