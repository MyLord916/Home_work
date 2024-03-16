import random

cities = [
    'абакан', 'азов', 'александров', 'алексин', 'альметьевск', 'анапа', 'ангарск', 'анжеро-судженск', 'апатиты',
    'арзамас', 'армавир', 'арсеньев', 'артем', 'архангельск', 'асбест', 'астрахань', 'ачинск', 'балаково',
    'балахна', 'балашиха', 'балашов', 'барнаул', 'батайск', 'белгород', 'белебей', 'белово', 'белогорск',
    'белорецк', 'белореченск', 'бердск', 'березники', 'березовский', 'бийск', 'биробиджан', 'благовещенск',
    'бор', 'борисоглебск', 'боровичи', 'братск', 'брянск', 'бугульма', 'буденновск', 'бузулук', 'буйнакск',
    'великие', 'луки', 'великий новгород', 'верхняя пышма', 'видное', 'владивосток', 'владикавказ',
    'владимир', 'волгоград', 'волгодонск', 'волжск', 'волжский', 'вологда', 'вольск', 'воркута', 'воронеж',
    'воскресенск', 'воткинск', 'всеволожск', 'выборг', 'выкса', 'вязьма', 'гатчина', 'геленджик', 'георгиевск',
    'глазов', 'горно-алтайск', 'грозный', 'губкин', 'гудермес', 'гуково', 'гусь-хрустальный', 'дербент',
    'дзержинск', 'димитровград', 'дмитров', 'долгопрудный', 'домодедово', 'донской', 'дубна', 'евпатория',
    'егорьевск', 'ейск', 'екатеринбург', 'елабуга', 'елец', 'ессентуки', 'железногорск', 'железногорск',
    'жигулевск', 'жуковский', 'заречный', 'зеленогорск', 'зеленодольск', 'златоуст', 'иваново', 'ивантеевка',
    'ижевск', 'избербаш', 'иркутск', 'искитим', 'ишим', 'ишимбай', 'йошкар-ола', 'казань', 'калининград',
    'калуга', 'каменск-уральский', 'каменск-шахтинский', 'камышин', 'канск', 'каспийск', 'кемерово', 'керчь',
    'кинешма', 'кириши', 'киров', 'кирово-чепецк', 'киселевск', 'кисловодск', 'клин', 'клинцы', 'ковров',
    'когалым', 'коломна', 'комсомольск-на-амуре', 'копейск', 'королев', 'кострома', 'котлас', 'красногорск',
    'краснодар', 'краснокаменск', 'краснокамск', 'краснотурьинск', 'красноярск', 'кропоткин', 'крымск',
    'кстово', 'кузнецк', 'кумертау', 'кунгур', 'курган', 'курск', 'кызыл', 'лабинск', 'лениногорск',
    'ленинск-кузнецкий', 'лесосибирск', 'липецк', 'лиски', 'лобня', 'лысьва', 'лыткарино', 'люберцы',
    'магадан', 'магнитогорск', 'майкоп', 'махачкала', 'междуреченск', 'мелеуз', 'миасс', 'минеральные воды', 'минусинск', 'михайловка', 'михайловск', 'мичуринск', 'москва', 'мурманск', 'муром', 'мытищи',
    'набережные', 'челны', 'назарово', 'назрань', 'нальчик', 'наро-фоминск', 'находка', 'невинномысск',
    'нерюнгри', 'нефтекамск', 'нефтеюганск', 'нижневартовск', 'нижнекамск', 'нижний', 'новгород', 'нижний',
    'тагил', 'новоалтайск', 'новокузнецк', 'новокуйбышевск', 'новомосковск', 'новороссийск', 'новосибирск',
    'новотроицк', 'новоуральск', 'новочебоксарск', 'новочеркасск', 'новошахтинск', 'новый', 'уренгой',
    'ногинск', 'норильск', 'ноябрьск', 'нягань', 'обнинск', 'одинцово', 'озерск', 'октябрьский', 'омск',
    'орел', 'оренбург', 'орехово-зуево', 'орск', 'павлово', 'павловский', 'посад', 'пенза', 'первоуральск',
    'пермь', 'петрозаводск', 'петропавловск-камчатский', 'подольск', 'полевской', 'прокопьевск', 'прохладный',
    'псков', 'пушкино', 'пятигорск', 'раменское', 'ревда', 'реутов', 'ржев', 'рославль', 'россошь',
    'ростов-на-дону', 'рубцовск', 'рыбинск', 'рязань', 'салават', 'сальск', 'самара', 'санкт-петербург',
    'саранск', 'сарапул', 'саратов', 'саров', 'свободный', 'севастополь', 'северодвинск', 'северск',
    'сергиев', 'посад', 'серов', 'серпухов', 'сертолово', 'сибай', 'симферополь', 'славянск-на-кубани',
    'смоленск', 'соликамск', 'солнечногорск', 'сосновый', 'бор', 'сочи', 'ставрополь', 'старый', 'оскол',
    'стерлитамак', 'ступино', 'сургут', 'сызрань', 'сыктывкар', 'таганрог', 'тамбов', 'тверь', 'тимашевск',
    'тихвин', 'тихорецк', 'тобольск', 'тольятти', 'томск', 'троицк', 'туапсе', 'туймазы', 'тула', 'тюмень',
    'узловая', 'улан-удэ', 'ульяновск', 'урус-мартан', 'усолье-сибирское', 'уссурийск', 'усть-илимск', 'уфа',
    'ухта', 'феодосия', 'фрязино', 'хабаровск', 'ханты-мансийск', 'хасавюрт', 'химки', 'чайковский',
    'чапаевск', 'чебоксары', 'челябинск', 'черемхово', 'череповец', 'черкесск', 'черногорск', 'чехов',
    'чистополь', 'чита', 'шадринск', 'шали', 'шахты', 'шуя', 'щекино', 'щелково', 'электросталь', 'элиста',
    'энгельс', 'южно-сахалинск', 'юрга', 'якутск', 'ялта', 'ярославль'
]

alpha_valid = 'абвгдежзийклмнопрстуфхчшщэюя'
alpha_invalid = 'цъыь'

cities_out = []


def corr_last_letter(word):
    for let in word[::-1]:
        if let not in alpha_invalid:
            break
        else:
            continue
    return let

def corr_name_city(word):
	anspaceword = word.replace(' ', '').lower()
	if anspaceword.isalpha():
		if word in cities:
			return 'valid_name'
		elif word in cities_out:
			return 'invalid_name'
		else:
			return 'word'
	elif anspaceword.isdigit() or word.isalnum():
		return 'digit'
	elif not anspaceword:
		return 'none'
	else:
		return 'error'

while cities:
    input_city = input()
    if corr_name_city(input_city) =='valid_name':
        end = corr_last_letter(input_city)
        first_letter = []
        for city in cities:
            if city.lower().startswith(end):
                first_letter.append(city)
        rand_corr_city = random.choice(first_letter)
        print(f'{rand_corr_city.title()}, тебе на "{corr_last_letter(rand_corr_city).upper()}"')
        cities_out.append(cities.pop(cities.index(rand_corr_city)))
        cities_out.append(cities.pop(cities.index(input_city)))
    else:
        print('error')
