import re


tr_stops = ['a', 'acaba', 'alti', 'altmis', 'ama', 'ancak', 'arada', 'artik', 'aslinda', 'aslinda', 'ayrica', 'az', 'bana', 'bazen', 'bazi', 'bazilari', 'belki', 'ben', 'benden', 'beni',
        'benim', 'beri', 'bes', 'bile', 'bilhassa', 'bin', 'bir', 'biraz', 'bircogu', 'bircok', 'biri', 'birisi', 'birkac', 'birsey', 'biz', 'bizden', 'bize', 'bizi', 'bizim', 'boyle', 
        'boylece', 'bu', 'buna', 'bunda', 'bundan', 'bunlar', 'bunlari', 'bunlarin', 'bunu', 'bunun', 'burada', 'butun', 'cogu', 'cogunu', 'cok', 'cunku', 'da', 'daha', 'dahi', 'dan',
        'de', 'defa', 'diger', 'digeri', 'digerleri', 'diye', 'doksan', 'dokuz', 'dolayi', 'dolayisiyla', 'dort', 'e', 'eden', 'ederek', 'eger', 'elbette', 'elli', 'en', 'etmesi', 
        'ettigi', 'ettigini', 'fakat', 'falan', 'filan', 'gene', 'geregi', 'gerek', 'gibi', 'gore', 'hala', 'halde', 'halen', 'hangi', 'hangisi', 'hani', 'hatta', 'hem', 'henuz', 'hep', 'hepsi',
        'her', 'herhangi', 'herkes', 'herkese', 'herkesi', 'herkesin', 'hic', 'hicbir', 'hicbiri', 'i', 'i', 'icin', 'icinde', 'iki', 'ile', 'ilgili', 'ise', 'iste', 'itibaren', 'itibariyle',
        'kac', 'kadar', 'karsin', 'kendi', 'kendilerine', 'kendine', 'kendini', 'kendisi', 'kendisine', 'kendisini', 'kez', 'ki', 'kim', 'kime', 'kimi', 'kimin', 'kimisi', 'kimse', 'kirk', 
        'madem', 'mi', 'mi', 'milyar', 'milyon', 'mu', 'mu', 'nasil', 'ne', 'neden', 'nedenle', 'nerde', 'nerede', 'nereye', 'neyse', 'nicin', 'nin', 'nin', 'niye', 'nun', 'nun', 'o', 'obur', 'olan', 
        'olarak', 'oldugunu', 'olduklarini', 'olmak', 'olup', 'on', 'ona', 'once', 'ondan', 'onlar', 'onlara', 'onlardan', 'onlari', 
        'onlarin', 'onu', 'onun', 'orada', 'ote', 'oturu', 'otuz', 'oyle', 'oysa', 'pek', 'ragmen', 'sana', 'sanki', 'sanki', 'sayet', 'sekilde', 'sekiz', 'seksen', 'sen', 'senden', 'seni', 'senin',
        'sey', 'seyden', 'seye', 'seyi', 'seyler', 'simdi', 'siz', 'siz', 'sizden', 'sizden', 'size', 'sizi', 'sizi', 'sizin', 'sizin', 'sonra', 'soyle', 'su', 'suna', 'sunlari', 'sunu', 'ta', 'tabii',
        'tam', 'tamam', 'tamamen', 'tarafindan', 'trilyon', 'tum', 'tumu', 'u', 'u', 'uc', 'un', 'un', 'uzere', 'var', 'vardi', 've', 'veya', 'ya', 'yani', 'yapmak',
        'ye', 'yedi', 'yerine', 'yetmis', 'yi', 'yi', 'yine', 'yirmi', 'yoksa', 'yu', 'yuz', 'zaten', 'zira', 'film ', 'filmi ', 'filmin', 'filme', 'filmde', 'gibi', 'bu', 'ben', 'olan', 'diye', 'sadece',
        'sonra', 'her', 'olarak', 'orada', 'orda', 'surda','burda','surada', 'burada', 'hizmet', 'urun', 'etiket', 'film', 'bilgilendirme']
pos_words = ['tesekkur','tebrik','mukemmel','muthis','ilgili','kusursuz','dost','iyi','muthis','harika','idare eder','guzel','akli','aktif','alakadar','alakali','alisilmis','analitik','animsatici','antrenmanli','atak','aydinlatici','ayrintici','bagdastirici','bagimsiz','berk','betimleyici','bilindik','bilinen','bilissel','birinci','bitirim','ciddi',
        'curetkar','cabuk','cocuk ruhlu','cogulcu','cok yonlu','cozumlemeci','dayanakli','denetimli','dengeci','denk','destekci','detayli','diplomali','disiplinli','dogal','dominant','duyarli','dusunceli','eriskin','gercekci','gururlu',
        'haberli','hareketli','hassas','hatirlatici','hesapci','heyecanli','idareci','iddiali','ilgili','itaatkar','itaatli','kararli','kendi halinde','kuralli','mantiksal','metotlu','net','normal','organize','otoriteli','otoriter','olculu','mutevazi','caliskan',
        'oncelikli','parlak','pozitif','sakin','sistematik','sistemli','standartli','tarafsiz','toleransli','uyanik','yardimci','yatistirici','yatkin','dengeli','duygusal','etkili','gonullu','is birlikci','verimli','nazik','komik','bilge','akilli',
        'narin','planli','programli','sabirli','teskilatli','tutkulu','uzlasmaci','aciklayici','becerikli','bilgili','bilincli','cesaretli','dayanikli','degerli','deneyimli','dikkatli','dinamik','disiplinli','duyarli','durust','duzenli','duzeyli',
        'egitimli','gayretli','hazirlikli','sorunsuz','idealist','ileri goruslu','istekli','ise uygun','iyi','kidemli','mantikli','nezaketli','nitelikli','prezantabl','profesyonel','sagduyulu','tedbirli','temkinli','uzman','vasifli','yaratici','adaletli','adil',
        'akilli','caliskan','dakik','enerjik','hakli','kaliteli','optimist','olumlu','rasyonel','tutarli','uyumlu','uretken','verimli','yararli','yardimsever','yenilikci','yetenekli']
neg_words = ['gereksiz','dusman','killik','kusurlu','kusur','nefret','arizali','bozuk','kirik','suratsiz','mahvetti','mahvolmus','kotu','sorun','problem','fena','abartili','acgozlu','adaletsiz','agresif','agzi bozuk','ahlak disi','ahlaksiz','ahmak','ahmakca','akillara zarar','akillanmaz','alayci','aptal','aptalca','ara bozucu','arsiz','art niyetli','asagilik',
        'barbar','bombok','bozgun','bozuk','cani','cildirtici','cozumsuz','daginik','diktator','duzenbaz','duzensiz','eksik','eski','gecersiz','gulunc','gurultu','guvensiz','hadsiz','hain','hevessiz','iki yuzlu','istikrarsiz','islevsiz',
        'kalitesiz','kansiz','karaktersiz','kirilgan','kiskanc','kisiliksiz','kof','korkutucu','korkunc','kullanissiz','limoni','madara','medeniyetsiz','olumsuz','plansiz','problem','ruhsuz','sapik','sarsak','sonucsuz','seytan',
        'tecrubesiz','tekinsiz','tembel','temelsiz','terbiyesiz','ters ters','tertipsiz','tiksindirici','tutarsiz','ukala','utandirici','utanmaz','uyusuk','uyumsuz','uygunsuz','uyduruk','ustunkoru','usengec','uzucu','vahim','verimsiz',
        'yalaka','yalanci','yanlis','yapmacik','yaltak','yaramaz','yararsiz','yilisik','yuz kizartici','asik yuzlu','yuzsuz','zararli','zevksiz','zevzek','zirdeli','zorba',
        'acemi','agir aksak','agzi gevsek','anlayissiz','antipatik','asabi','asalak','asik suratli','asagilayici','avanak','azimsiz','bakimsiz','basiretsiz','basarisiz','beceriksiz','bencil','berbat','bilincsiz','bilmis bilmis',
        'bilgisiz','boktan','bosbogaz','budala','burnu havada','cadaloz','bunaltici','can sikici','ciddiyetsiz','cenesi dusuk','cenesiz','cirkef','cirkin','cokbilmis','dalgaci','dalkavuk','dangalak','dar kafali','darmadaginik',
        'dayaklik','deli','deneyimsiz','demode','degersiz','dedikoducu','despot','disiplinsiz','dikkatsiz','duyarsiz','dusman','duzensiz','eften puften','egitimsiz','embesil','engelli','eski kafali','ezik','felaket','gaddar','gammaz',
        'gayretsiz','gorgusuz','gucsuz','hatali','hilebaz','hosgorusuz','hosnutsuz','huysuz','igrenc','ilkel','incitici','iradesiz','issiz','kaba','kafasiz','kalpsiz','kanunsuz','kirli','korkak','kustah','kusurlu','kompleksli']
mistakes = {'bn':'ben', 'bne':'ben', 'bnm':'benim', 'tsk':'tesekkur', 'deyil':'degil', 'malesef':'maalesef', 'orjinal':'orijinal', 'saol':'sag ol', 'sagol':'sag ol', 'farket':'fark et', 'yanliz':'yalniz', 'yalnis':'yanlis', 'sey':' sey'}

def convertTRLetters(entry):
    tr_char = {'ı':'i','ş':'s','ğ':'g','ö':'o','ç':'c','ü':'u'}
    for key, value in tr_char.items():
        entry = entry.replace(key, value)
    return entry


def removeSpecialChar(entry):
    entry = re.sub(r"[^a-zA-Z ]+", '', entry)
    string_length = len(entry)+1
    entry_revised = entry.ljust(string_length)
    return entry_revised


def fixCommonMistakes(entry):
    entry = entry.split()
    fixed_entry = []
    for word in entry:
        for key, value in mistakes.items():
            if key in word:
                word = word.replace(key,value)
        fixed_entry.append(word)
    entry = ' '.join(fixed_entry)
    string_length = len(entry)+1
    return entry.ljust(string_length)


def removeStopWords(entry):
    entry = ' '.join([word for word in entry.split() if word not in tr_stops])
    string_length = len(entry)+1
    return entry.ljust(string_length)


def removeSuffix(entry):
    entry = entry.split()
    suffixes = ['leri', 'lari',
                'lere', 'lara',
                'ler', 'lar',
                'dim', 'din',
                'tim', 'tin',
                'sin', 'sun',
                'in', 'im', 'u', 'um',
                'iyor', 'uyor', 'yor',
                'imiz', 'umuz',
                'si', 'su',
                'ydir', 'ydur',
                'ydik', 'yduk',
                'ydi', 'ydu',
                'dik' , 'duk',
                'dir', 'dur',
                'di', 'du',
                'tir', 'tur',
                'ti', 'tu',
                'ymis', 'ymus',
                'mis', 'mus',
                'acak', 'ecek',
                'ler', 'lar']
    for suffix in suffixes:
        entry = [word[:-(len(suffix))] if word.endswith(suffix) else word for word in entry]
    return ' '.join(entry)

def extractCommonAdj(entry):
    splitted = entry.split()
    positive = [word for word in splitted if any(pos in word for pos in pos_words)]
    negative = [word for word in splitted if any(neg in word for neg in neg_words)]
    entry = re.sub("|".join(pos_words), " ", entry)
    entry = re.sub("|".join(neg_words), " ", entry)
    string_length = len(entry)+1
    entry = entry.ljust(string_length)
    score = len(positive)-len(negative)
    return positive, negative, entry, score

def preprocess(entry, extract = False):
    entry = entry.lower()
    entry = convertTRLetters(entry)
    entry = removeSpecialChar(entry)
    entry = fixCommonMistakes(entry)
    entry = removeStopWords(entry)
    entry = removeSuffix(entry)
    if extract:
        pos, neg, rest, score = extractCommonAdj(entry)
        return entry, pos, neg, rest, score
    else:
        return entry

from keras import backend as K

def recall_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def precision_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision
def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))
