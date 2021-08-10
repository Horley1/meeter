import overpy
import math 

places=[
        
        {
            "title": "#Milk&Beans", 
            "url": "https://coffeemap.ru/milk-beans/", 
            "time": "ПН-ВС: 8:00-22:00", 
            "note": "", 
            "address": "Мичуринский проспект, 5", 
            "lat": 55.7035059, 
            "lng": 37.51115170000003, 
            "id": 1
        }, 
        {
            "title": "#Milk&Beans", 
            "url": "https://coffeemap.ru/milk-beans/", 
            "time": "ПН-ВС: 8:00-22:00", 
            "note": "", 
            "address": "Мичуринский пр-т, Олимпийская деревня, 1 корпус 4, БЦ «Чемпион парк»", 
            "lat": 55.6793904, 
            "lng": 37.468272100000036, 
            "id": 2
        }, 
        {
            "title": "#Milk&Beans", 
            "url": "https://coffeemap.ru/milk-beans/", 
            "time": "ПН-ВС: 8:00-20:00", 
            "note": "https://www.instagram.com/milk_and_beans/", 
            "address": "Шмитовский проезд 39к1, ЖК Хедлайнер", 
            "lat": 55.7544413, 
            "lng": 37.5239749, 
            "id": 3
        }, 
        {
            "title": "1554", 
            "url": "https://coffeemap.ru/1554-2/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 9:00-22:00", 
            "note": "https://www.instagram.com/1554cafe/", 
            "address": "ул. Новослободская, 50/1", 
            "lat": 55.78673999999999, 
            "lng": 37.59540399999992, 
            "id": 6
        }, 
        {
            "title": "2046", 
            "url": "https://coffeemap.ru/2046-2/", 
            "time": "ПН: 10:00-21:00, ВТ-ПТ: 8:00-21:00, СБ-ВС: 10:00-21:00", 
            "note": "https://www.instagram.com/2046.moscow/", 
            "address": "1-й Неопалимовский переулок, 1/9", 
            "lat": 55.740789354662084, 
            "lng": 37.58404733802871, 
            "id": 7
        }, 
        {
            "title": "42 Coffee Shop", 
            "url": "https://coffeemap.ru/42-coffee-shop/", 
            "time": "ПН-ПТ: 9:00–23:00, СБ: 10:00–23:00, ВС: 10:00–22:00", 
            "note": "https://www.instagram.com/42_coffeeshop/", 
            "address": "Ул. Малая Бронная, 28", 
            "lat": 55.7636364, 
            "lng": 37.59418789999995, 
            "id": 8
        }, 
        {
            "title": "6 am bread kitchen", 
            "url": "https://coffeemap.ru/6-am-bread-kitchen/", 
            "time": "ПН-ПТ: 9:00-20:00, СБ-ВС: 10:00-18:00", 
            "note": "https://www.instagram.com/6ambreadkitchen/", 
            "address": "Ул. Садовническая, 80", 
            "lat": 55.737803646092715, 
            "lng": 37.64161078227843, 
            "id": 10
        }, 
        {
            "title": "8/25 кофейня", 
            "url": "https://coffeemap.ru/8-25/", 
            "time": "ПН–ПТ: 8:00–20:00, СБ–ВС: 10:00–20:00", 
            "note": "", 
            "address": "Ул. Большая Новодмитровская, 36 строение 1", 
            "lat": 55.8045378, 
            "lng": 37.5846674, 
            "id": 11
        }, 
        {
            "title": "8/25 кофейня", 
            "url": "https://coffeemap.ru/8-25/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/8.25coffee.sav.city", 
            "address": "Ул. Новодмитровская, д. 2, корп. 7", 
            "lat": 55.80303805229215, 
            "lng": 37.591647361885876, 
            "id": 12
        }, 
        {
            "title": "93 Градуса", 
            "url": "https://coffeemap.ru/93-gradusa/", 
            "time": "ПН-ПТ: 08:00-20:00, СБ-ВС: 10:00-20:00", 
            "note": "https://www.instagram.com/93gradusa", 
            "address": "Ул. Соколово-Мещерская, 25", 
            "lat": 55.90216509383837, 
            "lng": 37.38489478826523, 
            "id": 14
        }, 
        {
            "title": "9CUPS", 
            "url": "https://coffeemap.ru/9cups/", 
            "time": "ПН-ПТ: 7:30-21:30, СБ-ВС: 9:30-21:30", 
            "note": "https://www.instagram.com/9cups_coffee/", 
            "address": "Ул. Новотушинская, 2, ЖК Новое Тушино", 
            "lat": 55.8680805, 
            "lng": 37.3973128, 
            "id": 15
        }, 
        {
            "title": "ABC Coffee Roasters", 
            "url": "https://coffeemap.ru/abc-coffee-roasters/", 
            "time": "ПН-ПТ: 9:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Покровка, 7", 
            "lat": 55.7590799561868, 
            "lng": 37.64222575611939, 
            "id": 16
        }, 
        {
            "title": "ABC Coffee Roasters", 
            "url": "https://coffeemap.ru/abc-coffee-roasters/", 
            "time": "ПН-ПТ: 9:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Большая Никитская, 19/16", 
            "lat": 55.75712201239555, 
            "lng": 37.600762525131245, 
            "id": 17
        }, 
        {
            "title": "ABC Coffee Roasters", 
            "url": "https://coffeemap.ru/abc-coffee-roasters/", 
            "time": "ПН-ПТ: 9:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ордынский тупик, 4", 
            "lat": 55.741089290094806, 
            "lng": 37.62321885581969, 
            "id": 18
        }, 
        {
            "title": "ABC Coffee Roasters", 
            "url": "https://coffeemap.ru/abc-coffee-roasters/", 
            "time": "ПН-ЧТ: 8:00-00:00, ПТ-СБ: 8:00-02:00, ВС: 8:00-00:00", 
            "note": "", 
            "address": "Рождественский бульвар, 1, Центральный рынок", 
            "lat": 55.7668997068815, 
            "lng": 37.623882734254494, 
            "id": 19
        }, 
        {
            "title": "ABC Coffee Roasters", 
            "url": "https://coffeemap.ru/abc-coffee-roasters/", 
            "time": "ПН-ПТ: 9:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Милютинский переулок, 3", 
            "lat": 55.76147940117019, 
            "lng": 37.63165781719658, 
            "id": 20
        }, 
        {
            "title": "ABC Coffee Roasters", 
            "url": "https://coffeemap.ru/abc-coffee-roasters/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/abc.roasters/", 
            "address": "Пресненская набережная, 6с2", 
            "lat": 55.7474907, 
            "lng": 37.5412388, 
            "id": 21
        }, 
        {
            "title": "All Day", 
            "url": "https://coffeemap.ru/all-day/", 
            "time": "ПН-ПТ: 08:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/all.day_restaurant/", 
            "address": "Пресненская наб., 12", 
            "lat": 55.74991554698954, 
            "lng": 37.53800363198998, 
            "id": 24
        }, 
        {
            "title": "Alternative", 
            "url": "https://coffeemap.ru/alternative-coffee-shop/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ: 10:00-18:00, ВС: закрыто", 
            "note": "https://www.instagram.com/alternative_coffee/", 
            "address": "Романов переулок, 4", 
            "lat": 55.7546378, 
            "lng": 37.6090164, 
            "id": 25
        }, 
        {
            "title": "ANDY Coffee", 
            "url": "https://coffeemap.ru/andy-coffee/", 
            "time": "ПН-ПТ: 8:00-18:00, СБ-ВС: выходной", 
            "note": "https://www.instagram.com/andymsk/", 
            "address": "Ул. Новорязанская 18с2", 
            "lat": 55.77224731321863, 
            "lng": 37.6621045079346, 
            "id": 27
        }, 
        {
            "title": "Angel Cakes", 
            "url": "https://coffeemap.ru/angel-cakes/", 
            "time": "ПН-ВС: 8:30 - 22:30", 
            "note": "https://www.instagram.com/angelcakes.patriki", 
            "address": "Большой Козихинский переулок, 15", 
            "lat": 55.763768, 
            "lng": 37.5957249, 
            "id": 28
        }, 
        {
            "title": "Atelier De Tartelettes", 
            "url": "https://coffeemap.ru/atelier-de-tartelettes/", 
            "time": "ПН-ПТ: 9:00-22:00, СБ-ВС: 9:00-23:00", 
            "note": "https://www.instagram.com/atelier_de_tartelettes/", 
            "address": "Спиридоньевский пер., 10А", 
            "lat": 55.76275075484399, 
            "lng": 37.59571232501162, 
            "id": 29
        }, 
        {
            "title": "Basic.", 
            "url": "https://coffeemap.ru/basic/", 
            "time": "ПН-ПТ: 11:00-20:00", 
            "note": "https://www.instagram.com/basic.msk/", 
            "address": "Садовническая улица, 76/71с1", 
            "lat": 55.738514011572406, 
            "lng": 37.64139982110977, 
            "id": 33
        }, 
        {
            "title": "Beloque", 
            "url": "https://coffeemap.ru/beloque/", 
            "time": "ПН-ВС: 10:00 – 23:00", 
            "note": "https://www.instagram.com/beloque_msk/", 
            "address": "ул. Рочдельская 15с26", 
            "lat": 55.75521257398075, 
            "lng": 37.56122158106956, 
            "id": 34
        }, 
        {
            "title": "Bitter Drop", 
            "url": "https://coffeemap.ru/bitter-drop/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-21:00", 
            "note": "https://www.instagram.com/bitterdrop.c/", 
            "address": "Ул. Нижняя Сыромятническая, 10 стр 4", 
            "lat": 55.752189270212874, 
            "lng": 37.67030065020094, 
            "id": 35
        }, 
        {
            "title": "Black Cups", 
            "url": "https://coffeemap.ru/black-cups/", 
            "time": "ПН-ПТ: 8:00 - 20:00, СБ-ВС: 10:00 - 18:00", 
            "note": "https://www.instagram.com/blackcups_moscow/", 
            "address": "Пресненская набережная, 12", 
            "lat": 55.74954248031153, 
            "lng": 37.53805173754267, 
            "id": 37
        }, 
        {
            "title": "Blau", 
            "url": "https://coffeemap.ru/blau/", 
            "time": "ПН-ВС: 10:00 - 23:00", 
            "note": "https://www.instagram.com/blau.moscow/", 
            "address": "Садовническая набережная, 7", 
            "lat": 55.747022442010056, 
            "lng": 37.62789436480407, 
            "id": 39
        }, 
        {
            "title": "Bloom-n-Bre//w", 
            "url": "https://coffeemap.ru/bloom-n-bre-w/", 
            "time": "ПН-ПТ: 8:30-21:00, СБ-ВС: 9:30-21:30", 
            "note": "", 
            "address": "Ул. Нижняя Красносельская, 35с50", 
            "lat": 55.77472896508671, 
            "lng": 37.67314648472518, 
            "id": 40
        }, 
        {
            "title": "Bloom-n-Bre//w", 
            "url": "https://coffeemap.ru/bloom-n-bre-w/", 
            "time": "ПН-ПТ: 8:30-21:00, СБ-ВС: 9:30-21:30", 
            "note": "https://www.instagram.com/bloomnbrew/", 
            "address": "Ул. Вятская, 27с2, БЦ Factoria", 
            "lat": 55.79683327748002, 
            "lng": 37.58193789999998, 
            "id": 41
        }, 
        {
            "title": "Bolshoi Lozowski", 
            "url": "https://coffeemap.ru/bolshoi-lozowski/", 
            "time": "ПН-ПТ: 9:00-20:00, СБ: 10:00-18:00, ВС: выходной", 
            "note": "https://www.instagram.com/bolshoilozowski/", 
            "address": "Ул. Ольховская, 45с1", 
            "lat": 55.777841660729635, 
            "lng": 37.672636069311466, 
            "id": 43
        }, 
        {
            "title": "Breakfast boy", 
            "url": "https://coffeemap.ru/breakfast-boy/", 
            "time": "ПН-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/breakfastboy_cafe/", 
            "address": "Ул. Солянка, 1/2с2", 
            "lat": 55.75373911801608, 
            "lng": 37.63825983663178, 
            "id": 45
        }, 
        {
            "title": "BREW Coffee", 
            "url": "https://coffeemap.ru/brew-coffee/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/brew.coffeebar/", 
            "address": "Мичуринский проспект, 27", 
            "lat": 55.69743870000001, 
            "lng": 37.50025040000001, 
            "id": 46
        }, 
        {
            "title": "Bro.We", 
            "url": "https://coffeemap.ru/espressovarnya-bro-we/", 
            "time": "ПН–ЧТ: 8:00–21:00, ПТ: 8:00–22:00, СБ-ВС: 9:00-22:00", 
            "note": "https://www.instagram.com/bro.we.coffee/", 
            "address": "Ул. Татарская, 5, стр. 1", 
            "lat": 55.7347389, 
            "lng": 37.637937400000055, 
            "id": 47
        }, 
        {
            "title": "Broker Coffee", 
            "url": "https://coffeemap.ru/broker-coffee/", 
            "time": "ПН-ПТ: 8:00 - 21:00, СБ-ВС: 9:00 - 21:00", 
            "note": "", 
            "address": "Б-р Маршала Рокоссовского, 6к1Б", 
            "lat": 55.81050699999999, 
            "lng": 37.726292599999965, 
            "id": 48
        }, 
        {
            "title": "Broker Coffee", 
            "url": "https://coffeemap.ru/broker-coffee/", 
            "time": "ПН-ПТ: 7:00 - 21:00, СБ-ВС: 9:00 - 21:00", 
            "note": "https://www.instagram.com/brokercoffee/", 
            "address": "Открытое шоссе, 5к11", 
            "lat": 55.8145443, 
            "lng": 37.733097600000065, 
            "id": 49
        }, 
        {
            "title": "BRRREW!", 
            "url": "https://coffeemap.ru/brrrew/", 
            "time": "ПН-ВС: 08:00-21:00", 
            "note": "https://www.instagram.com/brrrew.coffee/", 
            "address": "Ул. Бакунинская, д. 8", 
            "lat": 55.7734132, 
            "lng": 37.68065780000006, 
            "id": 50
        }, 
        {
            "title": "C-CUPS", 
            "url": "https://coffeemap.ru/c-cups/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/ccupscoffee/", 
            "address": "Ул. Большая Серпуховская, 32 строение 1", 
            "lat": 55.72526800000001, 
            "lng": 37.62562200000002, 
            "id": 53
        }, 
        {
            "title": "Cafe by Smoothie&Coffee", 
            "url": "https://coffeemap.ru/cafe-by-smoothie-coffee/", 
            "time": "ПН–ВС: 8:00–23:00", 
            "note": "https://www.instagram.com/smoothie_coffee/", 
            "address": "Ул. Мантулинская, 18, парк «Красная Пресня»", 
            "lat": 55.7552306, 
            "lng": 37.551828099999966, 
            "id": 54
        }, 
        {
            "title": "Caffeine | crew", 
            "url": "https://coffeemap.ru/caffeine-crew/", 
            "time": "ПН-ВС: 7:00-20:00", 
            "note": "https://www.instagram.com/caffeine.crew/", 
            "address": "Старопетровский проезд, д.1/1", 
            "lat": 55.823196, 
            "lng": 37.50087789999998, 
            "id": 55
        }, 
        {
            "title": "Cake for Break", 
            "url": "https://coffeemap.ru/cake-for-break/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ: 9:00-17:00, ВС: выходной", 
            "note": "https://instagram.com/cakeforbreakcafe", 
            "address": "Ул. Поклонная, 3к2", 
            "lat": 55.7364605, 
            "lng": 37.5332138, 
            "id": 56
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН–ПТ: 8:00–20:00, СБ: 10:00–18:00, ВС: закрыто", 
            "note": "", 
            "address": "Ул. Дубининская, 68с3, кофейня «Желтая стрела»", 
            "lat": 55.7225476, 
            "lng": 37.635817299999985, 
            "id": 59
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН–ПТ: 09:00–22:00, СБ–ВС: 11:00–22:00", 
            "note": "", 
            "address": "Столешников пер., 9с3, салон Chop-Chop", 
            "lat": 55.7633225, 
            "lng": 37.61443329999997, 
            "id": 60
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ВС: 8:00–22:00", 
            "note": "", 
            "address": "Ул. Вавилова, 64, Черемушкинский рынок", 
            "lat": 55.683952, 
            "lng": 37.55058280000003, 
            "id": 61
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ВС: 10:00–23:00", 
            "note": "", 
            "address": "Рождественский бульвар, 1, Центральный рынок", 
            "lat": 55.766771929790735, 
            "lng": 37.62407832009899, 
            "id": 62
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН–ВС: 09:00–22:00", 
            "note": "", 
            "address": "Проспект Мира, д. 26, стр. 2, фудкорт «Садовый буфет», цокольный этаж", 
            "lat": 55.77727822273693, 
            "lng": 37.63652299870296, 
            "id": 63
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ПТ: 09:00-23:00, СБ-ВС: 10:00-00:00", 
            "note": "", 
            "address": "Ул. Маросейка 4", 
            "lat": 55.75738078468937, 
            "lng": 37.633152859385746, 
            "id": 64
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ЧТ: 07:30-20:00, ПТ: 07:30-19:00, СБ-ВС: выходной", 
            "note": "", 
            "address": "Проспект Андропова, 18к1", 
            "lat": 55.694996, 
            "lng": 37.662802899999974, 
            "id": 65
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ВС: 10:00–22:00", 
            "note": "", 
            "address": "Чонгарский бульвар, 7, ТЦ Ангара", 
            "lat": 55.6513595, 
            "lng": 37.61237630000005, 
            "id": 66
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ПТ: 08:00-22:00, СБ-ВС: 11:00-20:00", 
            "note": "", 
            "address": "Ул. Новослободская 16, коворкинг Tablica", 
            "lat": 55.7815035, 
            "lng": 37.59940809999999, 
            "id": 67
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ВС: 8:00-22:00", 
            "note": "", 
            "address": "Шлюзовая набережная, 2/1с1, фуд-корт Комбинат", 
            "lat": 55.732384, 
            "lng": 37.642337, 
            "id": 68
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Тишинская площадь, 1с1,  фудмаркет Тишинка гастро холл", 
            "lat": 55.76913242150392, 
            "lng": 37.583594797005176, 
            "id": 69
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ПТ: 08:00-20:00, СБ-ВС: закрыто", 
            "note": "", 
            "address": "Ул. Бутырский Вал, 10", 
            "lat": 55.77861233963988, 
            "lng": 37.5859712748688, 
            "id": 70
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ВС: 09:00 – 22:00", 
            "note": "", 
            "address": "1-й Тверской-Ямской пер., 11", 
            "lat": 55.7731064, 
            "lng": 37.597362, 
            "id": 71
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ: 10:00-17:00, ВС: выходной", 
            "note": "", 
            "address": "Большой бульвар, 42, строение 1", 
            "lat": 55.69016523428713, 
            "lng": 37.34673500061035, 
            "id": 72
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ПТ: 9:00-23:00, СБ-ВС: 11:00-23:00", 
            "note": "", 
            "address": "Ул. Никольская, 10, гастромаркет Вокруг Света", 
            "lat": 55.7580556, 
            "lng": 37.62416669999999, 
            "id": 73
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Лескова, 14, ТРК Будапешт", 
            "lat": 55.897347, 
            "lng": 37.60451499999999, 
            "id": 74
        }, 
        {
            "title": "Camera Obscura", 
            "url": "https://coffeemap.ru/camera-obscura/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/cameraobscuracoffee/", 
            "address": "Ул. Тимура Фрунзе, 11с13", 
            "lat": 55.7351316, 
            "lng": 37.5878315, 
            "id": 75
        }, 
        {
            "title": "Cannibal Coffee", 
            "url": "https://coffeemap.ru/1861-2/", 
            "time": "ПН-ПТ: 08:00-21:00, СБ-ВС: 10:00-21:00", 
            "note": "https://www.instagram.com/cannibal.coffee", 
            "address": "Ул. Большая Якиманка, 25", 
            "lat": 55.736298815333015, 
            "lng": 37.61441348458959, 
            "id": 76
        }, 
        {
            "title": "Cappuccino Kids", 
            "url": "https://coffeemap.ru/cappuccino-kids/", 
            "time": "ПН-ВС: 9:00-22:00", 
            "note": "", 
            "address": "Ул. Земляной Вал, 18/22, кинотеатр Звезда", 
            "lat": 55.7599041, 
            "lng": 37.65707969999994, 
            "id": 77
        }, 
        {
            "title": "Cappuccino Kids", 
            "url": "https://coffeemap.ru/cappuccino-kids/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Кедрова, 14к3, кинотеатр Салют", 
            "lat": 55.682826, 
            "lng": 37.571229, 
            "id": 78
        }, 
        {
            "title": "Cappuccino Kids", 
            "url": "https://coffeemap.ru/cappuccino-kids/", 
            "time": "ПН-ЧТ: 10:00-22:00, ПТ: 10:00-23:00, СБ-ВС: 11:00-23:00", 
            "note": "", 
            "address": " ул. Ленинская Слобода, 26, фудмаркет Streat", 
            "lat": 55.7089224, 
            "lng": 37.6525151, 
            "id": 79
        }, 
        {
            "title": "Cappuccino Kids", 
            "url": "https://coffeemap.ru/cappuccino-kids/", 
            "time": "ПН-ПТ: 9:00-18:00, СБ-ВС: выходной", 
            "note": "", 
            "address": "Ул. Валовая, 35 (вход с улицы Зацепа)", 
            "lat": 55.7290796570375, 
            "lng": 37.62659937143326, 
            "id": 80
        }, 
        {
            "title": "Cappuccino Kids", 
            "url": "https://coffeemap.ru/cappuccino-kids/", 
            "time": "ПН-ПТ: 8:30-18:00, СБ-ВС: выходной", 
            "note": "", 
            "address": "Проектируемый проезд №4062, дом 6с2, БЦ Portplaza", 
            "lat": 55.693291, 
            "lng": 37.6605803, 
            "id": 81
        }, 
        {
            "title": "Cappuccino Kids", 
            "url": "https://coffeemap.ru/cappuccino-kids/", 
            "time": "ПН-ПТ: 8:30-18:30, СБ-ВС: выходной", 
            "note": "", 
            "address": "Ул. Отрадная, 2Б с1", 
            "lat": 55.8579077, 
            "lng": 37.6023903, 
            "id": 82
        }, 
        {
            "title": "Cappuccino Kids", 
            "url": "https://coffeemap.ru/cappuccino-kids/", 
            "time": "ПН-ВС: 8:30-18:00", 
            "note": "https://www.instagram.com/capp.kids/", 
            "address": "Ул. Тимура Фрунзе, 11к2, БЦ Мамонтов", 
            "lat": 55.7337444, 
            "lng": 37.5894276, 
            "id": 83
        }, 
        {
            "title": "Cezve", 
            "url": "https://coffeemap.ru/cezve/", 
            "time": "ПН-ВС: 10:00–22:00", 
            "note": "https://www.instagram.com/cezve_coffee/", 
            "address": "Ул. Крымский Вал, 10/14", 
            "lat": 55.734148020406906, 
            "lng": 37.60561364694365, 
            "id": 84
        }, 
        {
            "title": "Cheer Up", 
            "url": "https://coffeemap.ru/cheer-up/", 
            "time": "ПН-ВС: 8:00-20:00", 
            "note": "https://www.instagram.com/cheerup.airport/", 
            "address": "Ул. Часовая, 11/3, Ленинградский рынок", 
            "lat": 55.8079554, 
            "lng": 37.5291284, 
            "id": 85
        }, 
        {
            "title": "Coffee&Milk", 
            "url": "https://coffeemap.ru/coffee-milk/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 9:00–21:00", 
            "note": "", 
            "address": "Грохольский пер., 1, сад «Аптекарский огород»", 
            "lat": 55.77754148419957, 
            "lng": 37.633291482925415, 
            "id": 89
        }, 
        {
            "title": "Coffee&Milk", 
            "url": "https://coffeemap.ru/coffee-milk/", 
            "time": "ПН–ПТ: 7:00–22:00, СБ–ВС: 9:00–21:00", 
            "note": "https://www.instagram.com/co_and_mi/", 
            "address": "Ул. Бауманская, 32с2, ТЦ «Елоховский пассаж»", 
            "lat": 55.77240029999999, 
            "lng": 37.67846439999994, 
            "id": 90
        }, 
        {
            "title": "Coffee Crew", 
            "url": "https://coffeemap.ru/coffee-crew/", 
            "time": "ПН–ПТ: 8:00–21:00, СБ–ВС: 10:00–21:00", 
            "note": "https://www.instagram.com/coffee.crew/", 
            "address": "Мичуринский пр-т, 34", 
            "lat": 55.6985888, 
            "lng": 37.49860949999993, 
            "id": 92
        }, 
        {
            "title": "coffee first®", 
            "url": "https://coffeemap.ru/coffee-first/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 9:00-22:00", 
            "note": "https://www.instagram.com/coffeefirst_moscow/", 
            "address": "Крымский Вал, 8", 
            "lat": 55.7312522, 
            "lng": 37.6091097, 
            "id": 94
        }, 
        {
            "title": "Coffee Mill", 
            "url": "https://coffeemap.ru/piligrimy/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://instagram.com/_coffee_mill_", 
            "address": "Бульвар Адмирала Ушакова, 11", 
            "lat": 55.5462585, 
            "lng": 37.5493504, 
            "id": 95
        }, 
        {
            "title": "Coffee WOO", 
            "url": "https://coffeemap.ru/coffee-woo/", 
            "time": "ПН-ПТ: 7:30-23:00, СБ: 10:00-23:00, ВС: 8:30-23:00", 
            "note": "https://www.instagram.com/woo_coffee_co/", 
            "address": "Боровское шоссе, 2к5", 
            "lat": 55.66160722785216, 
            "lng": 37.420011633343506, 
            "id": 99
        }, 
        {
            "title": "Coffeegram", 
            "url": "https://coffeemap.ru/coffeegram/", 
            "time": "ПН-ВС: 09:00-20:00", 
            "note": "https://instagram.com/coffeegram_group", 
            "address": "Ул.Красная 7/5, Гатчина", 
            "lat": 59.5656444, 
            "lng": 30.122138, 
            "id": 102
        }, 
        {
            "title": "Coffeelavka", 
            "url": "https://coffeemap.ru/coffeelavka/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Большая Семеновская, 16, ТЦ Серебрянный  дом", 
            "lat": 55.78202489999999, 
            "lng": 37.70421550000003, 
            "id": 103
        }, 
        {
            "title": "Coffeelavka", 
            "url": "https://coffeemap.ru/coffeelavka/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Щелковское шоссе, 100, ТЦ Щелково", 
            "lat": 55.8105321, 
            "lng": 37.83075550000001, 
            "id": 104
        }, 
        {
            "title": "Coffeelavka", 
            "url": "https://coffeemap.ru/coffeelavka/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/coffeelavka_ru/", 
            "address": "Большой Овчинниковский переулок, 16", 
            "lat": 55.7442137152389, 
            "lng": 37.63056092586601, 
            "id": 106
        }, 
        {
            "title": "CoffeeNAT", 
            "url": "https://coffeemap.ru/coffeenat/", 
            "time": "ПН–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Ул. Адмирала Лазарева, 24", 
            "lat": 55.54691, 
            "lng": 37.53246999999999, 
            "id": 107
        }, 
        {
            "title": "CoffeeNAT", 
            "url": "https://coffeemap.ru/coffeenat/", 
            "time": "ПН-СБ: 9:00-21:00, ВС: 9:00-19:00", 
            "note": "", 
            "address": "Ул. Гурьянова 31с2", 
            "lat": 55.685108, 
            "lng": 37.71792000000005, 
            "id": 108
        }, 
        {
            "title": "CoffeeNAT", 
            "url": "https://coffeemap.ru/coffeenat/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 10:00-18:00", 
            "note": "", 
            "address": "Киевское ш., 1с2, БЦ Румянцево", 
            "lat": 55.63440385493674, 
            "lng": 37.43769407272339, 
            "id": 109
        }, 
        {
            "title": "CoffeeNAT", 
            "url": "https://coffeemap.ru/coffeenat/", 
            "time": "ПН-ВС: 10:00-21:00", 
            "note": "https://www.instagram.com/coffee.nat/", 
            "address": "Ул. Борисовские пруды, 26, ТРК Ключевой", 
            "lat": 55.6401252, 
            "lng": 37.7585106, 
            "id": 110
        }, 
        {
            "title": "Coffeeshots Lesnaya", 
            "url": "https://coffeemap.ru/coffeeshots-lesnaya/", 
            "time": "ПН-ПТ: 9:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/coffeeshots.lesnaya/", 
            "address": "Ул. Лесная, д. 10-16", 
            "lat": 55.77852005816003, 
            "lng": 37.58906709073789, 
            "id": 111
        }, 
        {
            "title": "Coffeesphere", 
            "url": "https://coffeemap.ru/coffeesphere/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 9:00–22:00", 
            "note": "", 
            "address": "1-й Нагатинский пр-д, 11к2", 
            "lat": 55.6766985, 
            "lng": 37.6340273, 
            "id": 112
        }, 
        {
            "title": "Coffeesphere", 
            "url": "https://coffeemap.ru/coffeesphere/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 9:00–22:00", 
            "note": "", 
            "address": "Корабельная ул, 17к2", 
            "lat": 55.6832761, 
            "lng": 37.69424500000002, 
            "id": 113
        }, 
        {
            "title": "Coffeesphere", 
            "url": "https://coffeemap.ru/coffeesphere/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 9:00–22:00", 
            "note": "", 
            "address": "Ул. Архитектора Щусева, 2 корпус 2", 
            "lat": 55.69923199999999, 
            "lng": 37.6349227, 
            "id": 114
        }, 
        {
            "title": "Coffeesphere", 
            "url": "https://coffeemap.ru/coffeesphere/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 9:00-22:00", 
            "note": "", 
            "address": "Проезд Невельского, 3/2", 
            "lat": 55.75182591760754, 
            "lng": 37.69810215211489, 
            "id": 115
        }, 
        {
            "title": "Coffeesphere", 
            "url": "https://coffeemap.ru/coffeesphere/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 9:00-22:00", 
            "note": "", 
            "address": "Ул. 3-я Хорошевская, 25к2", 
            "lat": 55.785804509168145, 
            "lng": 37.495787623358325, 
            "id": 116
        }, 
        {
            "title": "Coffeesphere", 
            "url": "https://coffeemap.ru/coffeesphere/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 9:00-22:00", 
            "note": "", 
            "address": "Шелепихинская набережная, 34к3", 
            "lat": 55.76284675234997, 
            "lng": 37.51519815489182, 
            "id": 117
        }, 
        {
            "title": "Coffeesphere", 
            "url": "https://coffeemap.ru/coffeesphere/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 9:00-22:00", 
            "note": "https://www.instagram.com/coffeesphere.ru/", 
            "address": "Ул. Профсоюзная, 68 стр.1", 
            "lat": 55.6644744, 
            "lng": 37.5460456, 
            "id": 118
        }, 
        {
            "title": "Coffeewood", 
            "url": "https://coffeemap.ru/coffeewood/", 
            "time": "ПН-ЧТ: 9:00 - 22:00, ПТ: 9:00 - 23:00, СБ-ВС: 10:00 - 23:00", 
            "note": "https://www.instagram.com/coffeewood.tg/", 
            "address": "Ул. Таганская, д. 1/2 стр. 2", 
            "lat": 55.74146709248643, 
            "lng": 37.65686797486879, 
            "id": 119
        }, 
        {
            "title": "COMETODEEMA", 
            "url": "https://coffeemap.ru/cometodeema/", 
            "time": "ПН-ПТ: 9:00-21:00, СБ-ВС: 10:00-21:00", 
            "note": "https://www.instagram.com/cometodeema/", 
            "address": "Ул. Татарская, 14", 
            "lat": 55.733654859704835, 
            "lng": 37.637841157077794, 
            "id": 120
        }, 
        {
            "title": "Cooks Cafe", 
            "url": "https://coffeemap.ru/cooks-cafe/", 
            "time": "ПН-ВС: 8:00-20:00", 
            "note": "https://www.instagram.com/cooks.cafe/", 
            "address": "Чонгарский бульвар, 8к1", 
            "lat": 55.65369, 
            "lng": 37.61583780000001, 
            "id": 122
        }, 
        {
            "title": "Corner Coffee", 
            "url": "https://coffeemap.ru/corner-coffee-roasters/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "", 
            "address": "Покровский бульвар, 14/6", 
            "lat": 55.755121614737774, 
            "lng": 37.647867051555295, 
            "id": 123
        }, 
        {
            "title": "Corner Coffee", 
            "url": "https://coffeemap.ru/corner-coffee-roasters/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/corner_coffee_roasters/", 
            "address": "Ул. Новокузнецкая, 3", 
            "lat": 55.740151544181536, 
            "lng": 37.6299987790985, 
            "id": 124
        }, 
        {
            "title": "Cosmic latte", 
            "url": "https://coffeemap.ru/cosmic-latte/", 
            "time": "ПН-ВС: 9:00-21:00", 
            "note": "", 
            "address": "Ул. Большая Дорогомиловская, 14", 
            "lat": 55.746643, 
            "lng": 37.55945710000003, 
            "id": 125
        }, 
        {
            "title": "Cosmic latte", 
            "url": "https://coffeemap.ru/cosmic-latte/", 
            "time": "ПН-ВС: 7:30-21:00", 
            "note": "", 
            "address": "Ленинградский пр-т., 60к1", 
            "lat": 55.79987897709115, 
            "lng": 37.534993846557654, 
            "id": 126
        }, 
        {
            "title": "Cosmic latte", 
            "url": "https://coffeemap.ru/cosmic-latte/", 
            "time": "ПН-ПТ: 8:00-19:00, СБ-ВС: выходной", 
            "note": "", 
            "address": "МКАД 69 километр (внешн.), БП Green Wood, корпус 17", 
            "lat": 55.86780262862161, 
            "lng": 37.40318419870755, 
            "id": 127
        }, 
        {
            "title": "Cosmic latte", 
            "url": "https://coffeemap.ru/cosmic-latte/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 10:00-21:00", 
            "note": "", 
            "address": "Ул. Валовая, 30", 
            "lat": 55.7302677, 
            "lng": 37.62651759999994, 
            "id": 128
        }, 
        {
            "title": "Cosmic latte", 
            "url": "https://coffeemap.ru/cosmic-latte/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Новый Арбат, 21, Huinday MotorStudio", 
            "lat": 55.7519974, 
            "lng": 37.58548689999998, 
            "id": 129
        }, 
        {
            "title": "Cosmic latte", 
            "url": "https://coffeemap.ru/cosmic-latte/", 
            "time": "ПН-ВС: 8:00-21:00", 
            "note": "https://www.instagram.com/cosmiclatte.coffee/", 
            "address": "Ул. Ходынская, 2", 
            "lat": 55.770066, 
            "lng": 37.56492590000001, 
            "id": 130
        }, 
        {
            "title": "Creative Diaspora", 
            "url": "https://coffeemap.ru/creative-diaspora/", 
            "time": "ПН-ВС: 9:00 - 21:00", 
            "note": "https://www.instagram.com/creative.diaspora/", 
            "address": "Ул. Мясницкая, 24/7 строение 3", 
            "lat": 55.76291715045551, 
            "lng": 37.63678002561622, 
            "id": 131
        }, 
        {
            "title": "Crema", 
            "url": "https://coffeemap.ru/crema/", 
            "time": "ПН-ВС: 10:00 - 23:00", 
            "note": "https://www.instagram.com/crema_eclair/", 
            "address": "Ул. Лесная, 20, фудмолл Депо", 
            "lat": 55.77982307453386, 
            "lng": 37.59286646270448, 
            "id": 132
        }, 
        {
            "title": "Crop.", 
            "url": "https://coffeemap.ru/crop/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Складочная, 1c1", 
            "lat": 55.800827, 
            "lng": 37.59457889999999, 
            "id": 133
        }, 
        {
            "title": "Crop.", 
            "url": "https://coffeemap.ru/crop/", 
            "time": "ПН-ПТ: 8:00-19:30, СБ-ВС: выходной", 
            "note": "", 
            "address": "Даниловская мануфактура", 
            "lat": 55.7000919, 
            "lng": 37.62546939999993, 
            "id": 134
        }, 
        {
            "title": "Crop.", 
            "url": "https://coffeemap.ru/crop/", 
            "time": "ПН-ПТ: 9:00-21:00, СБ-ВС: 10:00-21:00", 
            "note": "", 
            "address": "Проспект Вернадского, 39", 
            "lat": 55.6756442, 
            "lng": 37.505991199999926, 
            "id": 135
        }, 
        {
            "title": "Crop.", 
            "url": "https://coffeemap.ru/crop/", 
            "time": "ПН-ПТ: 8:30-20:00, СБ-ВС: выходной", 
            "note": "https://instagram.com/crop_cof", 
            "address": "Ул. Тимура Фрунзе 11с1, БЦ Демидов", 
            "lat": 55.7344509, 
            "lng": 37.58894179999993, 
            "id": 136
        }, 
        {
            "title": "Crosby Coffee Company", 
            "url": "https://coffeemap.ru/roast-crosby/", 
            "time": "ПН–ПТ: 8:00–19:00, СБ–ВС: закрыто", 
            "note": "", 
            "address": "Страстной б-р, 9", 
            "lat": 55.767585, 
            "lng": 37.60858699999994, 
            "id": 137
        }, 
        {
            "title": "Crosby Coffee Company", 
            "url": "https://coffeemap.ru/roast-crosby/", 
            "time": "ПН–ПТ: 8:00–18:00, СБ–ВС: закрыто", 
            "note": "", 
            "address": "Ольховская улица 4 корпус 1", 
            "lat": 55.773452, 
            "lng": 37.665406899999994, 
            "id": 138
        }, 
        {
            "title": "Crosby Coffee Company", 
            "url": "https://coffeemap.ru/roast-crosby/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 9:00-20:00", 
            "note": "", 
            "address": "Шоссе Энтузиастов, 50А строение 6", 
            "lat": 55.75862919999999, 
            "lng": 37.75798869999994, 
            "id": 139
        }, 
        {
            "title": "Crosby Coffee Company", 
            "url": "https://coffeemap.ru/roast-crosby/", 
            "time": "ПН–ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/crosbycoffee_moscow/", 
            "address": "Ул. Мантулинская 5с4, парк Красная Пресня", 
            "lat": 55.754829538493404, 
            "lng": 37.54874171147003, 
            "id": 140
        }, 
        {
            "title": "Crow Coffee Bar", 
            "url": "https://coffeemap.ru/crow-coffee-bar/", 
            "time": "ПН-ПТ: 08:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "https://www.instagram.com/crow.coffee.bar/", 
            "address": "Мичуринский проспект, 21", 
            "lat": 55.699955222444984, 
            "lng": 37.504726561844336, 
            "id": 141
        }, 
        {
            "title": "CUP&CUP", 
            "url": "https://coffeemap.ru/cupncup/", 
            "time": "ПН-ПТ: 8:00-18:00, СБ-ВС: закрыто", 
            "note": "", 
            "address": "Ул. Ленинградский проспект, 7с3, БЦ «Авион»", 
            "lat": 55.77966610000001, 
            "lng": 37.57594770000003, 
            "id": 142
        }, 
        {
            "title": "CUP&CUP", 
            "url": "https://coffeemap.ru/cupncup/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: закрыто", 
            "note": "", 
            "address": "г.Химки, ул.Юннатов, 1а", 
            "lat": 55.899029, 
            "lng": 37.46434499999998, 
            "id": 143
        }, 
        {
            "title": "CUP&CUP", 
            "url": "https://coffeemap.ru/cupncup/", 
            "time": "ПН-ПТ: 8:00-18:00, СБ-ВС: закрыто", 
            "note": "", 
            "address": "Минская, 2,Ж Бизнес центр Victory Park", 
            "lat": 55.72686939999999, 
            "lng": 37.4956076, 
            "id": 144
        }, 
        {
            "title": "CUP&CUP", 
            "url": "https://coffeemap.ru/cupncup/", 
            "time": "ПН-ПТ: 8:00-18:00, СБ-ВС: закрыто", 
            "note": "https://www.instagram.com/cupncup.msk/", 
            "address": "Ул. Кировоградская, 23а, БЦ Art Gallery", 
            "lat": 55.60049840000001, 
            "lng": 37.60036900000001, 
            "id": 145
        }, 
        {
            "title": "Daily Green", 
            "url": "https://coffeemap.ru/daily-green/", 
            "time": "ПН-ПТ: 9:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/cafe_daily_green/", 
            "address": "Руновский переулок, 5с1", 
            "lat": 55.74269414921647, 
            "lng": 37.63477278339766, 
            "id": 146
        }, 
        {
            "title": "David B. Cafe", 
            "url": "https://coffeemap.ru/david-b-cafe/", 
            "time": "ПН–ПТ: 8:00–21:00, СБ–ВС: 10:00–21:00", 
            "note": "https://www.instagram.com/davidbcafe/", 
            "address": "Большой Палашевский пер., 8", 
            "lat": 55.764027, 
            "lng": 37.59851600000002, 
            "id": 147
        }, 
        {
            "title": "Dobryakova Bakery", 
            "url": "https://coffeemap.ru/dobryakova-bakery/", 
            "time": "ПН-ВС: 10:00 - 21:00", 
            "note": "https://www.instagram.com/dobryakova_bakery/", 
            "address": "Малый Кисловский переулок, 9с1", 
            "lat": 55.75619943904743, 
            "lng": 37.60243219199601, 
            "id": 148
        }, 
        {
            "title": "Dolphin coffee", 
            "url": "https://coffeemap.ru/dolphin-coffee/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/dolphin_cdkino", 
            "address": "Зубовский бульвар, 2 строение 7", 
            "lat": 55.7359273, 
            "lng": 37.5940527, 
            "id": 149
        }, 
        {
            "title": "Doubleshot Moscow", 
            "url": "https://coffeemap.ru/doubleshot-moscow/", 
            "time": "ПН-ВС: 8:00-20:00", 
            "note": "https://www.instagram.com/doubleshotmoscow/", 
            "address": "Ул. Новослободская, 35", 
            "lat": 55.78235859999999, 
            "lng": 37.59810270000003, 
            "id": 152
        }, 
        {
            "title": "Drink IT", 
            "url": "https://coffeemap.ru/drinkit/", 
            "time": "ПН–ВС: 9:00–20:00", 
            "note": "", 
            "address": "Ул. Шарикоподшипниковская, 6/14", 
            "lat": 55.71986311974311, 
            "lng": 37.671871824606335, 
            "id": 156
        }, 
        {
            "title": "Drink IT", 
            "url": "https://coffeemap.ru/drinkit/", 
            "time": "ПН–ВС: 9:00–20:00", 
            "note": "https://www.instagram.com/its_drinkit", 
            "address": "4-я Гражданская улица, 36", 
            "lat": 55.807216, 
            "lng": 37.7192786, 
            "id": 157
        }, 
        {
            "title": "Eggsellent", 
            "url": "https://coffeemap.ru/eggsellent/", 
            "time": "ПН-ВС: 8:00-18:00", 
            "note": "", 
            "address": "Ул. Большая Садовая, 5к1", 
            "lat": 55.7682301, 
            "lng": 37.5926298, 
            "id": 158
        }, 
        {
            "title": "Eggsellent", 
            "url": "https://coffeemap.ru/eggsellent/", 
            "time": "ПН-ВС: 8:00-18:00", 
            "note": "https://www.instagram.com/eggsellent.ru/", 
            "address": "Тверской бульвар, 26/2", 
            "lat": 55.76250109404038, 
            "lng": 37.60382740944566, 
            "id": 159
        }, 
        {
            "title": "ELEVEN COFFEE", 
            "url": "https://coffeemap.ru/eleven-coffee/", 
            "time": "ПН-ВС: 08:00-23:00", 
            "note": "https://www.instagram.com/eleven___coffee/", 
            "address": "Арбатская пл., 14", 
            "lat": 55.7524691, 
            "lng": 37.60162079999999, 
            "id": 160
        }, 
        {
            "title": "Espressium", 
            "url": "https://coffeemap.ru/espressium/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "https://www.instagram.com/espressium.msk/", 
            "address": "Большая Сухаревская пл., 14/7", 
            "lat": 55.77183927521481, 
            "lng": 37.63667076997528, 
            "id": 161
        }, 
        {
            "title": "EVA", 
            "url": "https://coffeemap.ru/eva/", 
            "time": "ПН-ВС: 09:00-23:00", 
            "note": "https://www.instagram.com/eva__restaurant/", 
            "address": "Ул. Большая Грузинская, 69 ", 
            "lat": 55.7739062, 
            "lng": 37.5863421, 
            "id": 164
        }, 
        {
            "title": "Finch", 
            "url": "https://coffeemap.ru/finch/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-21:00", 
            "note": "", 
            "address": "Ул. Большая Серпуховская, 5", 
            "lat": 55.72888340383417, 
            "lng": 37.625888571163934, 
            "id": 166
        }, 
        {
            "title": "Finch", 
            "url": "https://coffeemap.ru/finch/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 11:00-21:00", 
            "note": "https://www.instagram.com/finch.coffee/", 
            "address": "Ул. Лесная, 10-16", 
            "lat": 55.77877174355546, 
            "lng": 37.58940464418029, 
            "id": 167
        }, 
        {
            "title": "FINE | кофе бар", 
            "url": "https://coffeemap.ru/fine-kofe-bar/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "https://www.instagram.com/fine_coffee_moscow/", 
            "address": "Ул. Волхонка, 9с2", 
            "lat": 55.74714827720553, 
            "lng": 37.60802398902434, 
            "id": 168
        }, 
        {
            "title": "Flip", 
            "url": "https://coffeemap.ru/flip/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Милютинский пер, 3", 
            "lat": 55.76141535914645, 
            "lng": 37.631537318229675, 
            "id": 170
        }, 
        {
            "title": "Flip", 
            "url": "https://coffeemap.ru/flip/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 9:00-23:00", 
            "note": "", 
            "address": "Новодевичий проезд, д. 2", 
            "lat": 55.72792268975325, 
            "lng": 37.560190879762295, 
            "id": 171
        }, 
        {
            "title": "Flip", 
            "url": "https://coffeemap.ru/flip/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 9:00-23:00", 
            "note": "", 
            "address": "Оболенский переулок, 9с1", 
            "lat": 55.73032720261949, 
            "lng": 37.57922887802124, 
            "id": 172
        }, 
        {
            "title": "Flip", 
            "url": "https://coffeemap.ru/flip/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 9:00-23:00", 
            "note": "", 
            "address": "Ул. 1-я Тверская-Ямская, 2/1", 
            "lat": 55.7703597732414, 
            "lng": 37.59650081104509, 
            "id": 173
        }, 
        {
            "title": "Flip", 
            "url": "https://coffeemap.ru/flip/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "", 
            "address": "Ул. Пятницкая, 73", 
            "lat": 55.7305897, 
            "lng": 37.6260676, 
            "id": 174
        }, 
        {
            "title": "Flip", 
            "url": "https://coffeemap.ru/flip/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: выходной", 
            "note": "", 
            "address": "Пресненская наб., 8, стр. 1", 
            "lat": 55.7470086, 
            "lng": 37.5389015, 
            "id": 175
        }, 
        {
            "title": "Flip", 
            "url": "https://coffeemap.ru/flip/", 
            "time": "ПН: выходной, ВТ-ВС: 12:00-21:00", 
            "note": "", 
            "address": "Ул. Петровка, 25", 
            "lat": 55.76721389999999, 
            "lng": 37.61393100000001, 
            "id": 176
        }, 
        {
            "title": "Flip", 
            "url": "https://coffeemap.ru/flip/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 9:00-23:00", 
            "note": "", 
            "address": "Ул. Валовая, 2-4/44", 
            "lat": 55.73145416580449, 
            "lng": 37.63519347420501, 
            "id": 177
        }, 
        {
            "title": "Flip", 
            "url": "https://coffeemap.ru/flip/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/flip.and.co/", 
            "address": "Ул. Большая Татарская, 7/4", 
            "lat": 55.74115470675154, 
            "lng": 37.63460040092468, 
            "id": 178
        }, 
        {
            "title": "Floo", 
            "url": "https://coffeemap.ru/kof-coffee-lab/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "https://www.instagram.com/floo.coffee/", 
            "address": "Ул. Новодмитровская, 1с1", 
            "lat": 55.80644864288034, 
            "lng": 37.584331117721604, 
            "id": 179
        }, 
        {
            "title": "FOUND", 
            "url": "https://coffeemap.ru/found/", 
            "time": "ПН-ЧТ: 11:00-23:00, ПТ-СБ: 11:00-00:00, ВС: 11:00-23:00", 
            "note": "https://www.instagram.com/found.moscow/", 
            "address": "Цветной Бульвар, 15/1, 5 этаж", 
            "lat": 55.77120379999999, 
            "lng": 37.62018279999999, 
            "id": 180
        }, 
        {
            "title": "Gentle", 
            "url": "https://coffeemap.ru/gentle/", 
            "time": "ПН-ВС: 08:00-00:00", 
            "note": "https://www.instagram.com/cafe.gentle/", 
            "address": "Тверской бульвар, 3", 
            "lat": 55.758221841947616, 
            "lng": 37.59797326560669, 
            "id": 182
        }, 
        {
            "title": "Gift Coffee", 
            "url": "https://coffeemap.ru/gift-coffee/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/gift_coffee/", 
            "address": "Ул. 1-я Бресткая, 33/2, магазин Wrapme", 
            "lat": 55.7725672, 
            "lng": 37.5891128, 
            "id": 183
        }, 
        {
            "title": "Greenwich", 
            "url": "https://coffeemap.ru/greenwich/", 
            "time": "ПН-СБ: 7:58-22:01, ВС: 9:57-22:03", 
            "note": "", 
            "address": "Ул. Оптиков, 34/1", 
            "lat": 59.99867509999999, 
            "lng": 30.21607589999999, 
            "id": 189
        }, 
        {
            "title": "Habit", 
            "url": "https://coffeemap.ru/habit/", 
            "time": "ПН-ПТ: 7:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/habit.moscow/", 
            "address": "Шоссе Энтузиастов 86а, корпус 3", 
            "lat": 55.763580801908795, 
            "lng": 37.79847048853299, 
            "id": 191
        }, 
        {
            "title": "Habit Coffee", 
            "url": "https://coffeemap.ru/habit-coffee/", 
            "time": "ПН-ВС: 10:00 - 22:00", 
            "note": "", 
            "address": "Проспект мира, 211к2", 
            "lat": 55.84553759051249, 
            "lng": 37.660474030163556, 
            "id": 192
        }, 
        {
            "title": "Habit Coffee", 
            "url": "https://coffeemap.ru/habit-coffee/", 
            "time": "ПН-ВС: 9:00-22:00", 
            "note": "https://www.instagram.com/myhabitcoffee/", 
            "address": "Нижняя Красносельская, 35с49", 
            "lat": 55.77549660567164, 
            "lng": 37.67207383617629, 
            "id": 194
        }, 
        {
            "title": "Hav.Palass", 
            "url": "https://coffeemap.ru/hav-palass/", 
            "time": "ПН-ПТ: 9:00 - 21:00, СБ-ВС: 11:00 - 21:00", 
            "note": "https://www.instagram.com/havpalass_kaffe/?hl=ru", 
            "address": "ул. Машкова, д. 21", 
            "lat": 55.7647279, 
            "lng": 37.6538041, 
            "id": 195
        }, 
        {
            "title": "Holy Berry", 
            "url": "https://coffeemap.ru/holy-berry/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "https://www.instagram.com/holy_berry/", 
            "address": "Новый Арбат, 21", 
            "lat": 55.75213439175603, 
            "lng": 37.58645865205381, 
            "id": 198
        }, 
        {
            "title": "Holy Berry", 
            "url": "https://coffeemap.ru/holy-berry/", 
            "time": "ПН-ПТ: 8:00-19:00, СБ-ВС: закрыто", 
            "note": "", 
            "address": "Варшавское шоссе, д.7 корпус 1", 
            "lat": 55.70091363762368, 
            "lng": 37.62232031918791, 
            "id": 199
        }, 
        {
            "title": "HQ! coffee", 
            "url": "https://coffeemap.ru/hq-coffee/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 9:00-18:00", 
            "note": "", 
            "address": "ул. Красная Пресня, д.16", 
            "lat": 55.7622537, 
            "lng": 37.57177960000001, 
            "id": 200
        }, 
        {
            "title": "HQ! coffee", 
            "url": "https://coffeemap.ru/hq-coffee/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 9:00-18:00", 
            "note": "https://www.instagram.com/headquarters_coffee/", 
            "address": "Ул. Перерва, 53", 
            "lat": 55.65034300000001, 
            "lng": 37.7311737, 
            "id": 202
        }, 
        {
            "title": "HUAN", 
            "url": "https://coffeemap.ru/huan/", 
            "time": "ПН-ПТ: 08:00-20:00, СБ-ВС: 9:00-19:00", 
            "note": "", 
            "address": "Волоколамское шоссе, 10", 
            "lat": 55.8089171, 
            "lng": 37.49706070000002, 
            "id": 203
        }, 
        {
            "title": "HUAN", 
            "url": "https://coffeemap.ru/huan/", 
            "time": "ПН-ПТ: 08:00-19:00, СБ-ВС: 9:00-19:00", 
            "note": "https://www.instagram.com/huan_coffeeman/", 
            "address": "1-й проезд Перова Поля, 9с1", 
            "lat": 55.75029271188651, 
            "lng": 37.77042104662701, 
            "id": 204
        }, 
        {
            "title": "Injir", 
            "url": "https://coffeemap.ru/injir/", 
            "time": "ПН-ВС: 09:00-21:00", 
            "note": "", 
            "address": "Цветной бульвар, 15", 
            "lat": 55.771151, 
            "lng": 37.62037399999997, 
            "id": 206
        }, 
        {
            "title": "Injir", 
            "url": "https://coffeemap.ru/injir/", 
            "time": "ПН-ВС: 09:00-21:00", 
            "note": "https://www.instagram.com/injirdesserts/", 
            "address": "ул. Мытная, 74", 
            "lat": 55.712178, 
            "lng": 37.620643, 
            "id": 207
        }, 
        {
            "title": "INTROVERT. place", 
            "url": "https://coffeemap.ru/introvert-place/", 
            "time": "ПН-ВС: 08:00-22:00", 
            "note": "https://www.instagram.com/h.trvrt/", 
            "address": "Ул. Мясницкая, 41/3", 
            "lat": 55.768300478203585, 
            "lng": 37.64253598584446, 
            "id": 208
        }, 
        {
            "title": "Jungle Brothers", 
            "url": "https://coffeemap.ru/jungle-brothers/", 
            "time": "ПН-ПТ: 09:00-19:00, СБ-ВС: выходной", 
            "note": "https://www.instagram.com/jungle.brothers/", 
            "address": "Ул. Профсоюзная, 76, БЦ Галерея", 
            "lat": 55.6609421, 
            "lng": 37.543807, 
            "id": 209
        }, 
        {
            "title": "Kafedra coffee", 
            "url": "https://coffeemap.ru/kafedra-coffee/", 
            "time": "ПН–ПТ: 8:30–22:00, СБ–ВС: 10:00–22:00", 
            "note": "https://www.instagram.com/kafedracoffee/", 
            "address": "Ул. Профсоюзная, 118", 
            "lat": 55.6358616, 
            "lng": 37.52100999999993, 
            "id": 210
        }, 
        {
            "title": "Kafema", 
            "url": "https://coffeemap.ru/kafema/", 
            "time": "ПН–ПТ: 9:00–21:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Ул. 4-я Тверская-Ямская, 9", 
            "lat": 55.772082, 
            "lng": 37.59735509999996, 
            "id": 211
        }, 
        {
            "title": "Kafema", 
            "url": "https://coffeemap.ru/kafema/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 10:00-20:00", 
            "note": "", 
            "address": "Дмитровское ш., 7 корпус 2", 
            "lat": 55.8142143, 
            "lng": 37.575768700000026, 
            "id": 212
        }, 
        {
            "title": "Kafema", 
            "url": "https://coffeemap.ru/kafema/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/kafema_msk/", 
            "address": "23-й км, Киевское ш., д. 1", 
            "lat": 55.6235408, 
            "lng": 37.4221186, 
            "id": 215
        }, 
        {
            "title": "Kaffebröd", 
            "url": "https://coffeemap.ru/kaffebrod/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "23-й км, Киевское ш., д. 1", 
            "lat": 55.62393119999999, 
            "lng": 37.42116820000001, 
            "id": 216
        }, 
        {
            "title": "Kaffebröd", 
            "url": "https://coffeemap.ru/kaffebrod/", 
            "time": "ПН-ВС: 11:00-23:00", 
            "note": "", 
            "address": "Крымская набережная, владение 2", 
            "lat": 55.73475957780845, 
            "lng": 37.60276185963994, 
            "id": 217
        }, 
        {
            "title": "Kaffebröd", 
            "url": "https://coffeemap.ru/kaffebrod/", 
            "time": "ПН-ВС: 09:30-22:00", 
            "note": "", 
            "address": "Ул. Маршала Рыбалко, 1", 
            "lat": 55.7953073, 
            "lng": 37.495390499999985, 
            "id": 218
        }, 
        {
            "title": "Kaffebröd", 
            "url": "https://coffeemap.ru/kaffebrod/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/kaffebrodmoscow/", 
            "address": "Проспект Мира, 109, кинотеатр Космос", 
            "lat": 55.818714, 
            "lng": 37.636781, 
            "id": 219
        }, 
        {
            "title": "KALABASA", 
            "url": "https://coffeemap.ru/kalabasa/", 
            "time": "ПН-ПТ: 9:00-21:00, СБ-ВС: 10:00-22:00", 
            "note": "https://instagram.com/kalabasa?igshid=u3k3ikgise6y", 
            "address": "Набережная Академика Туполева, 15/26", 
            "lat": 55.76260449999999, 
            "lng": 37.6797312, 
            "id": 220
        }, 
        {
            "title": "KK 12/10", 
            "url": "https://coffeemap.ru/kk-12-10/", 
            "time": "ПН-ВС: 08:00-23:00", 
            "note": "https://www.instagram.com/kk12.10", 
            "address": "Кривоколенный переулок, 12с10", 
            "lat": 55.76201645534246, 
            "lng": 37.63590663967284, 
            "id": 222
        }, 
        {
            "title": "KNIGEVARKE", 
            "url": "https://coffeemap.ru/knigevarke/", 
            "time": "ПН-ВС: 8:00-21:00", 
            "note": "https://instagram.com/knigevarke", 
            "address": "Богословский переулок, 16/6 стр.1", 
            "lat": 55.76355399034246, 
            "lng": 37.59830574695179, 
            "id": 223
        }, 
        {
            "title": "Kollektiv Coffee", 
            "url": "https://coffeemap.ru/kollektiv/", 
            "time": "ПН-ВС: 9:00-20:00", 
            "note": "https://www.instagram.com/kollektiv.coffee/", 
            "address": "Кутузовский проспект, 24", 
            "lat": 55.744550765505544, 
            "lng": 37.54540333313521, 
            "id": 224
        }, 
        {
            "title": "La Poste", 
            "url": "https://coffeemap.ru/la-poste/", 
            "time": "ПН-ВС: 8:00-21:00", 
            "note": "", 
            "address": "Ленинградский проспект, 48", 
            "lat": 55.79614709999999, 
            "lng": 37.54345, 
            "id": 227
        }, 
        {
            "title": "La Poste", 
            "url": "https://coffeemap.ru/la-poste/", 
            "time": "ПН-ВС: 8:00-21:00", 
            "note": "https://www.instagram.com/laposte.moscow/", 
            "address": "Ул. Мясницкая, 13/3", 
            "lat": 55.76270893973854, 
            "lng": 37.63463561033455, 
            "id": 228
        }, 
        {
            "title": "Laboratoria Coffee. Магазин и Шоурум", 
            "url": "https://coffeemap.ru/laboratoria-coffee-magazin-i-shourum/", 
            "time": "ПН-ВС: 10:00 - 19:00", 
            "note": "https://www.instagram.com/laboratoriacoffee/", 
            "address": "1-й Красногвардейский проезд, 9", 
            "lat": 55.7529813, 
            "lng": 37.5436701, 
            "id": 229
        }, 
        {
            "title": "Lagöm", 
            "url": "https://coffeemap.ru/lagom/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "https://www.instagram.com/lagom_msk/", 
            "address": "ул. Донецкая, 34к1", 
            "lat": 55.64563395187871, 
            "lng": 37.70370307143211, 
            "id": 230
        }, 
        {
            "title": "Lavendiya", 
            "url": "https://coffeemap.ru/lavendiya/", 
            "time": "ПН-ПТ: 08:00-21:00, СБ-ВС: 09:00-21:00", 
            "note": "https://www.instagram.com/lavendiya_simvol/", 
            "address": "Проезд Невельского, 3к1", 
            "lat": 55.751015450077354, 
            "lng": 37.69778652313993, 
            "id": 232
        }, 
        {
            "title": "Lawanda Store", 
            "url": "https://coffeemap.ru/lawanda-store/", 
            "time": "ПН-ПТ: 10:00-21:00, СБ-ВС: 11:00-21:00", 
            "note": "https://www.instagram.com/lawanda.store/", 
            "address": "Ул. Малая Бронная, 21/13с1", 
            "lat": 55.76287728972514, 
            "lng": 37.594787310450755, 
            "id": 233
        }, 
        {
            "title": "LES", 
            "url": "https://coffeemap.ru/les/", 
            "time": "ПН–ПТ: 9:00–21:00, СБ–ВС: 10:00–21:00", 
            "note": "https://www.instagram.com/lescoffee/", 
            "address": "Зубовский б-р, 2/5", 
            "lat": 55.73680690586084, 
            "lng": 37.59453850901491, 
            "id": 235
        }, 
        {
            "title": "Lila", 
            "url": "https://coffeemap.ru/lila/", 
            "time": "ПН-ВС: 8:00-23:00", 
            "note": "https://www.instagram.com/lila.gtgroup/", 
            "address": "Ул. Сретенка, 22/1с1", 
            "lat": 55.76952527044045, 
            "lng": 37.63233767850417, 
            "id": 236
        }, 
        {
            "title": "LISObon", 
            "url": "https://coffeemap.ru/lisobon/", 
            "time": "ПН-ВС: 8:00 - 22:00 ", 
            "note": "https://www.instagram.com/liso_bon/", 
            "address": "Ул. Сретенка, 26/1", 
            "lat": 55.770028, 
            "lng": 37.6334089, 
            "id": 239
        }, 
        {
            "title": "LOBBY", 
            "url": "https://coffeemap.ru/lobby/", 
            "time": "ПН-СР: 12:00 - 22:00, ЧТ-СБ: 12:00-00:00, ВС: 12:00 - 22:00", 
            "note": "https://www.instagram.com/lobby.moscow/", 
            "address": "Ул. Варварка, 3", 
            "lat": 55.75278669999999, 
            "lng": 37.6265625, 
            "id": 240
        }, 
        {
            "title": "Loft Intelligent", 
            "url": "https://coffeemap.ru/loft-intelligent/", 
            "time": "ПН–ПТ: 8:00–20:00, СБ–ВС: выходной", 
            "note": "", 
            "address": "Головинское ш., 5А»", 
            "lat": 55.8402949, 
            "lng": 37.49168199999997, 
            "id": 241
        }, 
        {
            "title": "Loft Intelligent", 
            "url": "https://coffeemap.ru/loft-intelligent/", 
            "time": "ПН–ПТ: 8:00–20:00, СБ–ВС: 9:00–17:00", 
            "note": "https://www.instagram.com/iloftcoffee/", 
            "address": "Ул. Новодмитровская, 2к1", 
            "lat": 55.80511309999999, 
            "lng": 37.5898881, 
            "id": 242
        }, 
        {
            "title": "Long Day Coffee", 
            "url": "https://coffeemap.ru/long-day-coffee/", 
            "time": "ПН-ВС: 9:00-21:00", 
            "note": "", 
            "address": "Ул. Болотниковская, 12", 
            "lat": 55.65687828673817, 
            "lng": 37.60738399734498, 
            "id": 243
        }, 
        {
            "title": "Long Day Coffee", 
            "url": "https://coffeemap.ru/long-day-coffee/", 
            "time": "ПН-ЧТ: 10:00-23:00, ПТ-СБ: 10:00-00:00, ВС: выходной", 
            "note": "https://www.instagram.com/longday.coffee/", 
            "address": "Рождественский бульвар, 1", 
            "lat": 55.7667816, 
            "lng": 37.624053199999935, 
            "id": 244
        }, 
        {
            "title": "MakeCupCoffee", 
            "url": "https://coffeemap.ru/makecupcoffee/", 
            "time": "ПН-ВС: 10:00–22:00", 
            "note": "https://www.instagram.com/makecup.coffee", 
            "address": "Ул. Бутырская, 8", 
            "lat": 55.79741010000001, 
            "lng": 37.58464409999999, 
            "id": 248
        }, 
        {
            "title": "MARGARITA BISTRO", 
            "url": "https://coffeemap.ru/margarita-bistro/", 
            "time": "ПН-ВС: 09:00 - 23:00", 
            "note": "https://www.instagram.com/margarita__bistro/", 
            "address": "Ул. Малая Бронная, 28", 
            "lat": 55.7638001, 
            "lng": 37.593866, 
            "id": 250
        }, 
        {
            "title": "Mates", 
            "url": "https://coffeemap.ru/mates/", 
            "time": "ПН-ПТ: 8:00- 22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Малая Бронная, 16", 
            "lat": 55.76158095336774, 
            "lng": 37.596085037364965, 
            "id": 252
        }, 
        {
            "title": "Mates", 
            "url": "https://coffeemap.ru/mates/", 
            "time": "ПН-ПТ: 8:00- 22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Мантулинская, 5с11", 
            "lat": 55.756140632584795, 
            "lng": 37.55489319562912, 
            "id": 253
        }, 
        {
            "title": "Mates", 
            "url": "https://coffeemap.ru/mates/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "https://instagram.com/mates.msk", 
            "address": "Ленинградский проспект, 29к3", 
            "lat": 55.784138045887914, 
            "lng": 37.56262375631983, 
            "id": 254
        }, 
        {
            "title": "MONSO", 
            "url": "https://coffeemap.ru/monso/", 
            "time": "ПН-ВС: 8:00 - 22:00", 
            "note": "https://www.instagram.com/monso_coffee", 
            "address": "Авиаконструктора Сухого, 2к2", 
            "lat": 55.78718381397236, 
            "lng": 37.54263021891024, 
            "id": 257
        }, 
        {
            "title": "Nook Coffee", 
            "url": "https://coffeemap.ru/nook-coffee/", 
            "time": "ПН-ВТ: 11:00-20:00, СР-ЧТ: 12:00-21:00, ПТ-ВС: 11:00-20:00", 
            "note": "", 
            "address": "Ленинградский пр-т, 15с1, Музей русского импрессионизма", 
            "lat": 55.7803435, 
            "lng": 37.57020060000002, 
            "id": 261
        }, 
        {
            "title": "Nook Coffee", 
            "url": "https://coffeemap.ru/nook-coffee/", 
            "time": "ПН–ПТ: 8:30–21:00, СБ–ВС: 9:00–21:00", 
            "note": "", 
            "address": "Берёзовой Рощи пр-д, 4", 
            "lat": 55.7866388, 
            "lng": 37.5204698, 
            "id": 262
        }, 
        {
            "title": "Nook Coffee", 
            "url": "https://coffeemap.ru/nook-coffee/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Кухмистерова, 4, кинотеатр Тула", 
            "lat": 55.685844, 
            "lng": 37.71859399999994, 
            "id": 263
        }, 
        {
            "title": "Nook Coffee", 
            "url": "https://coffeemap.ru/nook-coffee/", 
            "time": "ПН-ПТ: 8:30-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/nook_coffee/", 
            "address": "Ул. Гризодубовой, 4к1", 
            "lat": 55.78315844907059, 
            "lng": 37.528843839178464, 
            "id": 264
        }, 
        {
            "title": "Nord Coffee", 
            "url": "https://coffeemap.ru/nord-coffee/", 
            "time": "ПН-ПТ: 9:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/nordcoffeemsk/", 
            "address": "1-я Тверская-Ямская ул, 12", 
            "lat": 55.77255771256738, 
            "lng": 37.592569637434394, 
            "id": 265
        }, 
        {
            "title": "Nude", 
            "url": "https://coffeemap.ru/nude/", 
            "time": "ПН–ПТ: 9:00–23:00, СБ–ВС: 10:00–23:00", 
            "note": "https://www.instagram.com/nude.coffeewine/", 
            "address": "Ул. Спиридоновка, 24/1", 
            "lat": 55.76187111032996, 
            "lng": 37.592822313308716, 
            "id": 267
        }, 
        {
            "title": "O.K. Coffee", 
            "url": "https://coffeemap.ru/o-k-coffee/", 
            "time": "ПН-ВС: 10:00-21:00", 
            "note": "https://www.instagram.com/o.k.koffee/", 
            "address": "Ул. Смольная, 63Б", 
            "lat": 55.86994079999999, 
            "lng": 37.4698232, 
            "id": 268
        }, 
        {
            "title": "Old Grinder", 
            "url": "https://coffeemap.ru/old-grinder/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 10:00-20:00", 
            "note": "https://www.instagram.com/oldgrinder", 
            "address": "Кропоткинский переулок, 9", 
            "lat": 55.737981, 
            "lng": 37.59287100000006, 
            "id": 270
        }, 
        {
            "title": "Pa Pa Power", 
            "url": "https://coffeemap.ru/pa-pa-power/", 
            "time": "ПН-ЧТ: 10:00-22:00, ПТ-СБ: 10:00-01:00, ВС: 10:00-22:00", 
            "note": "", 
            "address": "Проспект Вернадского, 86В, фуд-корт Eat Market", 
            "lat": 55.662201, 
            "lng": 37.4803431, 
            "id": 275
        }, 
        {
            "title": "PARK47", 
            "url": "https://coffeemap.ru/park47/", 
            "time": "ПН-ПТ: 8:00-21:30, СБ-ВС: 9:30-21:30", 
            "note": "https://www.instagram.com/park47coffee/", 
            "address": "Ул. Архитектора Власова, 47", 
            "lat": 55.666530512530116, 
            "lng": 37.54383444786072, 
            "id": 277
        }, 
        {
            "title": "petit bla__nc", 
            "url": "https://coffeemap.ru/petit-bla__nc/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/petit_blanc_msk/", 
            "address": "Ул. Архитектора Щусева, 2к1", 
            "lat": 55.700379, 
            "lng": 37.635221, 
            "id": 278
        }, 
        {
            "title": "PINCH", 
            "url": "https://coffeemap.ru/pinch/", 
            "time": "ПН-ВС: 8:30–00:00", 
            "note": "https://www.instagram.com/pinch.moscow/", 
            "address": "Большой Палашёвский пер., 2", 
            "lat": 55.7632987, 
            "lng": 37.59701419999999, 
            "id": 279
        }, 
        {
            "title": "PINK MILK CAFE", 
            "url": "https://coffeemap.ru/pink-milk-cafe/", 
            "time": "ПН-СБ: 08:00-22:00, ВС: 09:00-22:00", 
            "note": "https://instagram.com/pinkmilk.cafe", 
            "address": "Ул. Совхозная, 17к1", 
            "lat": 55.8994674, 
            "lng": 37.4729903, 
            "id": 280
        }, 
        {
            "title": "Point 242", 
            "url": "https://coffeemap.ru/point-242/", 
            "time": "ПН–ПТ: 8:00–21:00, СБ–ВС: 9:00–21:00", 
            "note": "", 
            "address": "Ул. Петра Романова, 6", 
            "lat": 55.70821919999999, 
            "lng": 37.680605499999956, 
            "id": 285
        }, 
        {
            "title": "Point 242", 
            "url": "https://coffeemap.ru/point-242/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 9:00–22:00", 
            "note": "", 
            "address": "Ул. Октябрьская, 9/1", 
            "lat": 55.78636216188517, 
            "lng": 37.61364698410034, 
            "id": 286
        }, 
        {
            "title": "Point 242", 
            "url": "https://coffeemap.ru/point-242/", 
            "time": "ПН–ПТ: 8:00–21:00, СБ–ВС: 9:00–21:00", 
            "note": "https://www.instagram.com/point242/", 
            "address": "Проспект Мира, 61", 
            "lat": 55.7859559, 
            "lng": 37.63451029999999, 
            "id": 287
        }, 
        {
            "title": "Pro Coffee", 
            "url": "https://coffeemap.ru/pro-coffee/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 10:00-21:00", 
            "note": "https://www.instagram.com/pro.coffeee/", 
            "address": "Ул. Краснобогатырская, 90к2", 
            "lat": 55.8003025, 
            "lng": 37.71139399999993, 
            "id": 288
        }, 
        {
            "title": "Profitrolly", 
            "url": "https://coffeemap.ru/profitrolly/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 9:00-23:00", 
            "note": "https://instagram.com/profitrolly.cafe", 
            "address": "Краснобогатырская улица, 90 строение 2", 
            "lat": 55.800528097166925, 
            "lng": 37.71018708462523, 
            "id": 289
        }, 
        {
            "title": "Projector Coffee", 
            "url": "https://coffeemap.ru/project-or-coffee/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/projector_coffee/", 
            "address": "Ул. Воронцово Поле, 2", 
            "lat": 55.7528396038768, 
            "lng": 37.647539377212524, 
            "id": 290
        }, 
        {
            "title": "PROSVET", 
            "url": "https://coffeemap.ru/prosvet/", 
            "time": "ПН-ВС: 10-22:00", 
            "note": "", 
            "address": "Ул. Ильинка, 4, Гостиный Двор, подъезд 7", 
            "lat": 55.7546975, 
            "lng": 37.6256317, 
            "id": 291
        }, 
        {
            "title": "PROSVET", 
            "url": "https://coffeemap.ru/prosvet/", 
            "time": "ПН-ВС: 10-22:00", 
            "note": "", 
            "address": "Манежная площадь, 1", 
            "lat": 55.7534116, 
            "lng": 37.61229110000001, 
            "id": 292
        }, 
        {
            "title": "PROSVET", 
            "url": "https://coffeemap.ru/prosvet/", 
            "time": "ПН-ВС: 8:00 - 23:00", 
            "note": "https://www.instagram.com/prosvetcoffee/", 
            "address": "Ул. Фадеева, 10", 
            "lat": 55.77586551072212, 
            "lng": 37.596719563007355, 
            "id": 293
        }, 
        {
            "title": "Raw to go", 
            "url": "https://coffeemap.ru/raw-to-go/", 
            "time": "ПН-ЧТ: 10:00 - 23:00, ПТ-СБ: 10:00-00:00, ВС: 10:00 - 23:00", 
            "note": "", 
            "address": "Ул. Лесная, 20, фудмолл Депо", 
            "lat": 55.780239392429046, 
            "lng": 37.593166870114146, 
            "id": 295
        }, 
        {
            "title": "Raw to go", 
            "url": "https://coffeemap.ru/raw-to-go/", 
            "time": "ПН-СБ: 10:00-22:00, ВС: 11:00-22:00", 
            "note": "", 
            "address": "Цветной бульвар, 15с1", 
            "lat": 55.77101973330291, 
            "lng": 37.61995213002467, 
            "id": 296
        }, 
        {
            "title": "Raw to go", 
            "url": "https://coffeemap.ru/raw-to-go/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Большой Патриарший переулок, 12", 
            "lat": 55.76328618606999, 
            "lng": 37.59330646130753, 
            "id": 297
        }, 
        {
            "title": "Raw to go", 
            "url": "https://coffeemap.ru/raw-to-go/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 9:00-22:00", 
            "note": "https://www.instagram.com/rawtogomsk/", 
            "address": "Ул. Балчуг, 5, Гастромаркет Балчуг", 
            "lat": 55.7472004, 
            "lng": 37.62605620000001, 
            "id": 298
        }, 
        {
            "title": "Rébellion Clubhouse Moscow", 
            "url": "https://coffeemap.ru/rebellion-clubhouse/", 
            "time": "ПН-ЧТ: 11:00-22:00, ПТ-СБ: 11:00-00:00, ВС: 11:00-22:00", 
            "note": "https://www.instagram.com/rebellion____clubhouse/", 
            "address": "Петровский бульвар, 8/1", 
            "lat": 55.76774400000001, 
            "lng": 37.6158951, 
            "id": 299
        }, 
        {
            "title": "Roaster Coffee", 
            "url": "https://coffeemap.ru/roaster-coffee/", 
            "time": "ПН–ПТ: 7:30–23:00, СБ–ВС: 9:00–23:00", 
            "note": "", 
            "address": "Ул. 4-я Тверская-Ямская, 2/11с2", 
            "lat": 55.7719114, 
            "lng": 37.598395799999935, 
            "id": 300
        }, 
        {
            "title": "Roaster Coffee", 
            "url": "https://coffeemap.ru/roaster-coffee/", 
            "time": "ПН–ПТ: 7:30–23:00, СБ–ВС: 9:00–23:00", 
            "note": "https://www.instagram.com/roaster_coffee/", 
            "address": "Ул. Бауманская, 7", 
            "lat": 55.776568194723815, 
            "lng": 37.67601399867249, 
            "id": 301
        }, 
        {
            "title": "Roasting Brew", 
            "url": "https://coffeemap.ru/bryou/", 
            "time": "ПН-ПТ: 10:00-19:00, СБ-ВС: закрыто", 
            "note": "https://www.instagram.com/roasting_brew", 
            "address": "Переведеновский переулок, 18c2", 
            "lat": 55.77948399999999, 
            "lng": 37.69010209999999, 
            "id": 302
        }, 
        {
            "title": "Roombox", 
            "url": "https://coffeemap.ru/borodatyj-pyos/", 
            "time": "ПН-ВС: 7:30-22:00", 
            "note": "https://www.instagram.com/roombох.coffee", 
            "address": "Новинский бульвар, 22", 
            "lat": 55.7566309, 
            "lng": 37.5848301, 
            "id": 303
        }, 
        {
            "title": "Seadog Coffee Roasters", 
            "url": "https://coffeemap.ru/seadog-coffee-roasters/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/seadogcoffee.msc/", 
            "address": "Ул. Большая Ордынка, 7 ", 
            "lat": 55.74454796550291, 
            "lng": 37.62489599814759, 
            "id": 304
        }, 
        {
            "title": "Search", 
            "url": "https://coffeemap.ru/search/", 
            "time": "ПН-ПТ: 8:00-19:00, СБ-ВС: выходной", 
            "note": "", 
            "address": "Ул. Нобеля, 5", 
            "lat": 55.6845945, 
            "lng": 37.3417399, 
            "id": 305
        }, 
        {
            "title": "Search", 
            "url": "https://coffeemap.ru/search/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 9:00-20:00", 
            "note": "https://instagram.com/search.msk", 
            "address": "ул. Зворыкина д.1с1", 
            "lat": 55.6943511, 
            "lng": 37.3498912, 
            "id": 306
        }, 
        {
            "title": "Skuratov Coffee", 
            "url": "https://coffeemap.ru/skuratov-coffee/", 
            "time": "ПН-ВС: 6:55–22:05", 
            "note": "", 
            "address": "Калашный пер., 5", 
            "lat": 55.75490440000001, 
            "lng": 37.60153279999997, 
            "id": 308
        }, 
        {
            "title": "Skuratov Coffee", 
            "url": "https://coffeemap.ru/skuratov-coffee/", 
            "time": "ПН-ВС: 6:55–22:05", 
            "note": "", 
            "address": "Мира пр-т, 26с1", 
            "lat": 55.77811018249384, 
            "lng": 37.63301655650139, 
            "id": 309
        }, 
        {
            "title": "Skuratov Coffee", 
            "url": "https://coffeemap.ru/skuratov-coffee/", 
            "time": "ПН-ВС: 6:55–22:05", 
            "note": "", 
            "address": "Кутузовский пр-т., 36с39", 
            "lat": 55.73959199999999, 
            "lng": 37.52752600000001, 
            "id": 310
        }, 
        {
            "title": "Skuratov Coffee", 
            "url": "https://coffeemap.ru/skuratov-coffee/", 
            "time": "ПН-ВС: 6:55–22:05", 
            "note": "", 
            "address": "Ул. Верхняя Радищевская, 19/3, стр. 2", 
            "lat": 55.74324576442925, 
            "lng": 37.65311231232397, 
            "id": 311
        }, 
        {
            "title": "Smart Coffee", 
            "url": "https://coffeemap.ru/smart-coffee/", 
            "time": "ПН-ВС: 10:00–20:00", 
            "note": "", 
            "address": "Мира пр-т, 119c47, ВДНХ, пав. 47, «Дом Ремёсел»", 
            "lat": 55.837313, 
            "lng": 37.62407189999999, 
            "id": 320
        }, 
        {
            "title": "Smart Coffee", 
            "url": "https://coffeemap.ru/smart-coffee/", 
            "time": "ПН-ЧТ: 11:00-20:00, ПТ-ВС: 10:00-20:00", 
            "note": "https://www.instagram.com/smartcoffee_vdnh/", 
            "address": "Проспект Мира, 119с581, Фудкорт ВДНХ", 
            "lat": 55.83205274481218, 
            "lng": 37.63093863112249, 
            "id": 321
        }, 
        {
            "title": "Smart_cafe", 
            "url": "https://coffeemap.ru/smart_cafe/", 
            "time": "ПН-ПТ: 08:00-20:00, СБ-ВС: 09:00-19:00", 
            "note": "https://www.instagram.com/smart_cafe_moscow/", 
            "address": "Спартаковская площадь, 16/15 стр. 2, деловой центр Басманный двор", 
            "lat": 55.7761611783335, 
            "lng": 37.679122760483814, 
            "id": 322
        }, 
        {
            "title": "SML cafe", 
            "url": "https://coffeemap.ru/sml-cafe/", 
            "time": "ПН-ВС: 10:00-21:00", 
            "note": "", 
            "address": "ул. Мытная, 74с3", 
            "lat": 55.711779069464185, 
            "lng": 37.6207709312439, 
            "id": 323
        }, 
        {
            "title": "SML cafe", 
            "url": "https://coffeemap.ru/sml-cafe/", 
            "time": "ПН-ПТ: 8:30-22:00, СБ: 8:30-20:00, ВС: 8:30-18:00", 
            "note": "", 
            "address": "ул. Лужники, 24, стр. 48", 
            "lat": 55.72568001142118, 
            "lng": 37.545491384616156, 
            "id": 324
        }, 
        {
            "title": "SML cafe", 
            "url": "https://coffeemap.ru/sml-cafe/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/sml_cafe/", 
            "address": "Трехпрудный переулок, 11/13с2", 
            "lat": 55.765449, 
            "lng": 37.5956981, 
            "id": 325
        }, 
        {
            "title": "STIM", 
            "url": "https://coffeemap.ru/stim/", 
            "time": "ПН-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/stimcoffee_msk/", 
            "address": "Ул. Бауманская, 15, Басманный двор", 
            "lat": 55.77607176451556, 
            "lng": 37.67837661248095, 
            "id": 330
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ул. Мясницкая, 16", 
            "lat": 55.76109109999999, 
            "lng": 37.63239870000007, 
            "id": 334
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ул. Никольская, 8/1", 
            "lat": 55.757095, 
            "lng": 37.62334390000001, 
            "id": 335
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ул. Новый Арбат, 7А", 
            "lat": 55.75264, 
            "lng": 37.59772399999997, 
            "id": 336
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ул. Солянка, 1/2", 
            "lat": 55.754036, 
            "lng": 37.637345900000014, 
            "id": 337
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 12:00–23:00", 
            "note": "", 
            "address": "Берсеневская набережная, 14/8", 
            "lat": 55.7423259, 
            "lng": 37.60998560000007, 
            "id": 338
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ул. Нижняя Сыромятническая, 10", 
            "lat": 55.7522381, 
            "lng": 37.67120980000004, 
            "id": 339
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ул. Тверская 25/12", 
            "lat": 55.7675023, 
            "lng": 37.59961240000007, 
            "id": 340
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "", 
            "note": "", 
            "address": "Тестовская улица, 1", 
            "lat": 55.747924617552044, 
            "lng": 37.531914744705205, 
            "id": 341
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 9:00 - 22:00, СБ-ВС: 10:00 - 22:00", 
            "note": "", 
            "address": "Конный переулок, 12", 
            "lat": 55.72169653499528, 
            "lng": 37.611708305311836, 
            "id": 343
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 8:00 - 22:00, СБ-ВС: 10:00 - 22:00", 
            "note": "", 
            "address": "Ул. Дмитрия Ульянова, 4к1", 
            "lat": 55.69355168753452, 
            "lng": 37.557637095451355, 
            "id": 344
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 8:00 - 23:00, СБ-ВС: 10:00 - 23:00", 
            "note": "", 
            "address": "Ул. Новослободская, 16а", 
            "lat": 55.782189, 
            "lng": 37.59958800000004, 
            "id": 345
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 8:00–23:00,  СБ-ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ул. Бутырский Вал, 4", 
            "lat": 55.77730695111656, 
            "lng": 37.585215003605754, 
            "id": 346
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ: 10:00-18:00, ВС: выходной", 
            "note": "", 
            "address": "Стремянный переулок, 38", 
            "lat": 55.727231, 
            "lng": 37.62688800000001, 
            "id": 347
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: выходной", 
            "note": "", 
            "address": "Пресненская набережная, 12", 
            "lat": 55.74724181536835, 
            "lng": 37.54059447168879, 
            "id": 348
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ВС: 8:00-22:00", 
            "note": "", 
            "address": "Ул. Нижняя Красносельская, 35с49, комплекс Loftec", 
            "lat": 55.775778707932275, 
            "lng": 37.671818791043734, 
            "id": 349
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 8:00–23:00, СБ-ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ул. Покровка, 31с1", 
            "lat": 55.76067091751422, 
            "lng": 37.64970113683694, 
            "id": 350
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "", 
            "address": "Ул. Долгоруковская, 5/27/2", 
            "lat": 55.77351241946724, 
            "lng": 37.603763673016374, 
            "id": 351
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ВС: 8:00–22:00", 
            "note": "", 
            "address": "Ул. Усачева, 62", 
            "lat": 55.72468815870643, 
            "lng": 37.562408138098135, 
            "id": 352
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ВС: 8:00-23:00", 
            "note": "", 
            "address": "ул. Крымский Вал, 9, стр. 45", 
            "lat": 55.73229223357955, 
            "lng": 37.603041190490785, 
            "id": 353
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 8:00–22:00, СБ-ВС: 9:00–22:00", 
            "note": "", 
            "address": "Ул. Маршала Бирюзова, 18", 
            "lat": 55.79501699999999, 
            "lng": 37.49119100000007, 
            "id": 354
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ВС: 8:00-23:00", 
            "note": "", 
            "address": "Ул. Сретенка, 23/25с1", 
            "lat": 55.77082079794425, 
            "lng": 37.63214066497767, 
            "id": 355
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 8:00–22:00, СБ-ВС: 10:00–22:00", 
            "note": "", 
            "address": "ул. Красная Пресня, 30, стр. 1", 
            "lat": 55.76228145635841, 
            "lng": 37.56833575470471, 
            "id": 356
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 9:00–22:00, СБ-ВС: 10:00–22:00", 
            "note": "", 
            "address": "ул. Усачева 3", 
            "lat": 55.7300913, 
            "lng": 37.5757329, 
            "id": 357
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 07:30–22:00, СБ-ВС: 09:00–22:00", 
            "note": "", 
            "address": "пр. Аэропорта, 8, стр. 9", 
            "lat": 55.79790360876612, 
            "lng": 37.52206512626663, 
            "id": 358
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 10:00-21:00", 
            "note": "", 
            "address": "Ул. Садовническая, 42с1", 
            "lat": 55.74473442425389, 
            "lng": 37.637013253458534, 
            "id": 359
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ВС: 9:30-22:00", 
            "note": "", 
            "address": "Новоясеневский просп., 11", 
            "lat": 55.606813443508344, 
            "lng": 37.53636992621336, 
            "id": 360
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ЧТ: 10:00–22:00, ПТ-СБ: 10:00–23:00, ВС: 10:00–22:00", 
            "note": "", 
            "address": "Ходынский бул., 4, ТРЦ Авиапарк", 
            "lat": 55.78975828000568, 
            "lng": 37.5283475480629, 
            "id": 367
        }, 
        {
            "title": "Surf Coffee", 
            "url": "https://coffeemap.ru/surf-coffee/", 
            "time": "ПН-ПТ: 08:00–22:00, СБ-ВС: 09:00–22:00", 
            "note": "", 
            "address": "Ул. 1-я Тверская-Ямская, 10, магазин Республика", 
            "lat": 55.7722431, 
            "lng": 37.59265159999999, 
            "id": 368
        }, 
        {
            "title": "t [кофейня]", 
            "url": "https://coffeemap.ru/kofejnya-t/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/tecomoscow/", 
            "address": "Проспект Вернадского, 86б строение 2", 
            "lat": 55.6617377, 
            "lng": 37.4800971, 
            "id": 373
        }, 
        {
            "title": "Table", 
            "url": "https://coffeemap.ru/table/", 
            "time": "ПН–ПТ: 10:00–22:00, СБ–ВС: 10:00–21:00", 
            "note": "https://www.instagram.com/tablecafemoscow/", 
            "address": "Ул. Лесная, 45", 
            "lat": 55.7809702, 
            "lng": 37.59147600000006, 
            "id": 374
        }, 
        {
            "title": "Terroir Cafe", 
            "url": "https://coffeemap.ru/terroir-cafe/", 
            "time": "ПН-ПТ: 7:30-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://instagram.com/terroir__coffee", 
            "address": "Ул. Шаболовка, 59к1А", 
            "lat": 55.715366, 
            "lng": 37.608262, 
            "id": 375
        }, 
        {
            "title": "The First Cup", 
            "url": "https://coffeemap.ru/the-first-cup/", 
            "time": "ПН–ПТ: 8:30–22:00, СБ–ВС: 11:00–21:00", 
            "note": "https://www.instagram.com/tfcroasting/", 
            "address": "Ул. Нижняя Сыромятническая, 10с9", 
            "lat": 55.75281773365003, 
            "lng": 37.66809843754277, 
            "id": 376
        }, 
        {
            "title": "Tilda Food & Bar", 
            "url": "https://coffeemap.ru/tilda-food-bar/", 
            "time": "ПН-ПТ: 12:00-00:00, СБ-ВС: 11:00-00:00", 
            "note": "https://www.instagram.com/tilda.moscow/", 
            "address": "Сытинский тупик, 5", 
            "lat": 55.7639376, 
            "lng": 37.6000368, 
            "id": 377
        }, 
        {
            "title": "TÖK", 
            "url": "https://coffeemap.ru/tok/", 
            "time": "ПН-ПТ: 8:30-18:00, СБ-ВС: выходной", 
            "note": "https://www.instagram.com/tok.cfe/", 
            "address": "Ленинградский проспект, 36с10", 
            "lat": 55.78857428540074, 
            "lng": 37.567476895770255, 
            "id": 378
        }, 
        {
            "title": "TOTO", 
            "url": "https://coffeemap.ru/toto/", 
            "time": "ПН-ВС: 9:00-00:00", 
            "note": "https://www.instagram.com/toto.moscow/", 
            "address": "Столешников переулок, 7с3", 
            "lat": 55.763660539831534, 
            "lng": 37.61391985096021, 
            "id": 379
        }, 
        {
            "title": "Twins Garden Restaurant", 
            "url": "https://coffeemap.ru/twins-garden-restaurant/", 
            "time": "ПН-ВС: 12:00-00:00", 
            "note": "https://www.instagram.com/twinsgardenmoscow/", 
            "address": "Страстной б-р., 8А ", 
            "lat": 55.76623, 
            "lng": 37.61079599999994, 
            "id": 380
        }, 
        {
            "title": "udcкафе", 
            "url": "https://coffeemap.ru/udckafe/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ул. Большая Грузинская, 76", 
            "lat": 55.77361879999999, 
            "lng": 37.58674210000004, 
            "id": 381
        }, 
        {
            "title": "udcкафе", 
            "url": "https://coffeemap.ru/udckafe/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 10:00–23:00", 
            "note": "", 
            "address": "Мира пр-т, 26с1", 
            "lat": 55.7774675, 
            "lng": 37.63299219999999, 
            "id": 382
        }, 
        {
            "title": "udcкафе", 
            "url": "https://coffeemap.ru/udckafe/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–23:00", 
            "note": "", 
            "address": "Камергерский пер., 5/7", 
            "lat": 55.76035929733058, 
            "lng": 37.61420579496769, 
            "id": 383
        }, 
        {
            "title": "udcкафе", 
            "url": "https://coffeemap.ru/udckafe/", 
            "time": "9:00–22:00", 
            "note": "", 
            "address": "Ул. Ярцевская, 19", 
            "lat": 55.73869999999999, 
            "lng": 37.41067799999996, 
            "id": 384
        }, 
        {
            "title": "udcкафе", 
            "url": "https://coffeemap.ru/udckafe/", 
            "time": "9:00–23:00", 
            "note": "", 
            "address": "Ленинградское ш., 16Аc4", 
            "lat": 55.823387, 
            "lng": 37.49715809999998, 
            "id": 385
        }, 
        {
            "title": "udcкафе", 
            "url": "https://coffeemap.ru/udckafe/", 
            "time": "10:00–22:00", 
            "note": "", 
            "address": "Пресненская наб., 2", 
            "lat": 55.7491164, 
            "lng": 37.539529000000016, 
            "id": 386
        }, 
        {
            "title": "udcкафе", 
            "url": "https://coffeemap.ru/udckafe/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Павелецкая пл., 2с3", 
            "lat": 55.7299647, 
            "lng": 37.63573580000002, 
            "id": 388
        }, 
        {
            "title": "udcкафе", 
            "url": "https://coffeemap.ru/udckafe/", 
            "time": "ПН–ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/udc_moscow/", 
            "address": "Кутузовский пр-т, 57, ТЦ Океания", 
            "lat": 55.728207735538184, 
            "lng": 37.47693852957764, 
            "id": 389
        }, 
        {
            "title": "Uno Coffe", 
            "url": "https://coffeemap.ru/uno-coffe/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 9:00-20:00", 
            "note": "https://www.instagram.com/uno.coffe/", 
            "address": "Ул. Миклухо-Маклая, 33", 
            "lat": 55.64593604112245, 
            "lng": 37.51952826976776, 
            "id": 390
        }, 
        {
            "title": "Utopian coffee", 
            "url": "https://coffeemap.ru/utopian-coffee/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/utopian.coffee", 
            "address": "Ул. Кантемировская, 47", 
            "lat": 55.6378273, 
            "lng": 37.6561265, 
            "id": 391
        }, 
        {
            "title": "Veter Grocery", 
            "url": "https://coffeemap.ru/veter-grocery/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 10:00-21:00", 
            "note": "https://www.instagram.com/vetergrocery/", 
            "address": "Ул. Верхняя Радищевская, 13/1", 
            "lat": 55.74371386113739, 
            "lng": 37.65124894603272, 
            "id": 395
        }, 
        {
            "title": "Vigor Maker", 
            "url": "https://coffeemap.ru/vigor-maker/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Проспект Мира, 119", 
            "lat": 55.826096996558164, 
            "lng": 37.63708047691837, 
            "id": 396
        }, 
        {
            "title": "Vigor Maker", 
            "url": "https://coffeemap.ru/vigor-maker/", 
            "time": "ПН-ПТ: 9:00-20:00, СБ-ВС: 10:00-20:00", 
            "note": "https://www.instagram.com/vigor_maker/", 
            "address": "Ул. Бутырская, 46", 
            "lat": 55.8000896468003, 
            "lng": 37.584163828836076, 
            "id": 397
        }, 
        {
            "title": "Wake Up Cafe", 
            "url": "https://coffeemap.ru/wake-up-cafe/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 11:00–23:00", 
            "note": "", 
            "address": "Ул. Тимура Фрунзе, 20", 
            "lat": 55.73483359999999, 
            "lng": 37.5887209, 
            "id": 399
        }, 
        {
            "title": "Wake Up Cafe", 
            "url": "https://coffeemap.ru/wake-up-cafe/", 
            "time": "ПН-ПТ: 08:00 - 21:00, СБ-ВС: 11:00 - 21:00", 
            "note": "https://www.instagram.com/wakeupcafemoscow/", 
            "address": "Ул. Покровка, 40, стр.1", 
            "lat": 55.761975027140096, 
            "lng": 37.65207191897967, 
            "id": 400
        }, 
        {
            "title": "West 4", 
            "url": "https://coffeemap.ru/west-4/", 
            "time": "ПН–СБ: 10:00–20:00, ВС: закрыто", 
            "note": "https://www.instagram.com/west4coffee/", 
            "address": "арт-пространство «Авиатор»", 
            "lat": 55.774881, 
            "lng": 37.670388, 
            "id": 401
        }, 
        {
            "title": "WTFcoffee", 
            "url": "https://coffeemap.ru/wtfcoffee/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/Wtfcoffeeshop", 
            "address": "Ул. Артюхиной, 14/8 стр1 ", 
            "lat": 55.699075, 
            "lng": 37.73772299999999, 
            "id": 402
        }, 
        {
            "title": "Yumbaker", 
            "url": "https://coffeemap.ru/yumbaker/", 
            "time": "ПН-ВС: 9:00–21:00", 
            "note": "", 
            "address": "Проспект Мира, 26/1", 
            "lat": 55.7774675, 
            "lng": 37.63299219999999, 
            "id": 409
        }, 
        {
            "title": "Yumbaker", 
            "url": "https://coffeemap.ru/yumbaker/", 
            "time": "ПН-ВС: 8:00-20:00", 
            "note": "https://www.instagram.com/yumbaker/", 
            "address": "Ул. Пятницкая, 66/1", 
            "lat": 55.73247, 
            "lng": 37.62688449999996, 
            "id": 410
        }, 
        {
            "title": "Альпака и кофе", 
            "url": "https://coffeemap.ru/alpaka-i-kofe/", 
            "time": "ПН-ПТ: 09:00-20:00, СБ-ВС: 11:00-21:00", 
            "note": "https://www.instagram.com/alpa.coffee/", 
            "address": "Староконюшенный переулок, 25", 
            "lat": 55.747160637491206, 
            "lng": 37.59498953819275, 
            "id": 412
        }, 
        {
            "title": "Аппо mini", 
            "url": "https://coffeemap.ru/appo-mini/", 
            "time": "ПН-ПТ: 8:00 - 18:00, СБ-ВС: выходной", 
            "note": "https://www.instagram.com/appocup.mini/", 
            "address": "Ул. Донская, 8", 
            "lat": 55.72383869427674, 
            "lng": 37.60715186322936, 
            "id": 413
        }, 
        {
            "title": "Аэроплан кофе", 
            "url": "https://coffeemap.ru/aeroplan-kofe/", 
            "time": "ПН-ВС: 8:00-20:00", 
            "note": "", 
            "address": "Ул. Пятницкая, 65/10", 
            "lat": 55.73266761396914, 
            "lng": 37.62746985152055, 
            "id": 414
        }, 
        {
            "title": "Аэроплан кофе", 
            "url": "https://coffeemap.ru/aeroplan-kofe/", 
            "time": "ПН-ВС: 8:00-20:00", 
            "note": "https://www.instagram.com/aeroplancoffee/", 
            "address": "Ул. Садовническая, 80", 
            "lat": 55.73745440639602, 
            "lng": 37.639993172528555, 
            "id": 415
        }, 
        {
            "title": "Аэрофоб&Я", 
            "url": "https://coffeemap.ru/aerofob-ya/", 
            "time": "ПН-ВС: 8:00 - 22:00", 
            "note": "https://www.instagram.com/aerofobiyacafe/", 
            "address": "Ул. Авиаконструктора Сухого, 2к2", 
            "lat": 55.7872244, 
            "lng": 37.5421454, 
            "id": 416
        }, 
        {
            "title": "Бамбл Кофе", 
            "url": "https://coffeemap.ru/bambl-kofe/", 
            "time": "ПН-ВС: 09:00-21:00", 
            "note": "https://www.instagram.com/bumble.mos/", 
            "address": "Свободный проспект, 37/18", 
            "lat": 55.748256625167784, 
            "lng": 37.81634021593856, 
            "id": 417
        }, 
        {
            "title": "Батон", 
            "url": "https://coffeemap.ru/baton/", 
            "time": "ПН-ВС: 8:00–21:00", 
            "note": "", 
            "address": "Ул. Мытная, 74", 
            "lat": 55.71217799999999, 
            "lng": 37.62064299999997, 
            "id": 419
        }, 
        {
            "title": "Батон", 
            "url": "https://coffeemap.ru/baton/", 
            "time": "ПН-ВС: 8:00–21:00", 
            "note": "https://www.instagram.com/batonbakery/", 
            "address": "Ул. Ленинский пр. 60/2", 
            "lat": 55.6960083, 
            "lng": 37.557948099999976, 
            "id": 420
        }, 
        {
            "title": "Без Названия", 
            "url": "https://coffeemap.ru/one-teaspoon/", 
            "time": "ПН: 12:00–22:00, ВТ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/untitledmoscow", 
            "address": "Яузский б-р, 14/8", 
            "lat": 55.75094130000001, 
            "lng": 37.64366270000005, 
            "id": 421
        }, 
        {
            "title": "Без Рецепта", 
            "url": "https://coffeemap.ru/bez-retsepta/", 
            "time": "ПН-ЧТ: 08:00-21:00, СБ: 10:00-23:00, ВС: 10:00-21:00", 
            "note": "https://www.instagram.com/bez_recepta/", 
            "address": "Ул. Кутузовский проспект, 1/7,  Friends Social Club", 
            "lat": 55.74999706130121, 
            "lng": 37.57142200343242, 
            "id": 422
        }, 
        {
            "title": "Блэк by Даблби", 
            "url": "https://coffeemap.ru/blek-by-dablbi/", 
            "time": "ПН-ЧТ: 09:00-23:00, ПТ: 09:00-00:00, СБ: 10:00-00:00, ВС: 10:00-23:00", 
            "note": "https://www.instagram.com/blackbydoubleb/", 
            "address": "Якиманская набережная, 2", 
            "lat": 55.73969294407356, 
            "lng": 37.61157820633741, 
            "id": 424
        }, 
        {
            "title": "Блэк Милк", 
            "url": "https://coffeemap.ru/black-milk/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 10:00–23:00", 
            "note": "", 
            "address": "Чистопрудный б-р, 12к4", 
            "lat": 55.76158840946894, 
            "lng": 37.64300459755326, 
            "id": 425
        }, 
        {
            "title": "Блэк Милк", 
            "url": "https://coffeemap.ru/black-milk/", 
            "time": "ПН-ПТ: 08:00–23:00, СБ-ВС: 10:00–23:00", 
            "note": "https://www.instagram.com/black_milk_coffee/", 
            "address": "Малый Сухаревский пер., 9с1", 
            "lat": 55.77050598491359, 
            "lng": 37.624358385801315, 
            "id": 426
        }, 
        {
            "title": "Бодрый Макс", 
            "url": "https://coffeemap.ru/stim-2/", 
            "time": "ПН-ПТ: 8:30-21:30, СБ-ВС: 9:00-21:30", 
            "note": "https://www.instagram.com/bodryimaks", 
            "address": "Ул. Бульвар Генерала Карбышева, 13А", 
            "lat": 55.78112851913547, 
            "lng": 37.46895790100098, 
            "id": 427
        }, 
        {
            "title": "Борис Сонный", 
            "url": "https://coffeemap.ru/boris-sonnyj/", 
            "time": "ПН–ПТ: 8:30-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/razbudi_borisa/", 
            "address": "Ул. Селезневская, 32", 
            "lat": 55.7808928, 
            "lng": 37.61184879999999, 
            "id": 429
        }, 
        {
            "title": "Буше", 
            "url": "https://coffeemap.ru/bushe/", 
            "time": "ПН-ПТ: 9:00-22:00, СБ-ВС: 10:00-23:00", 
            "note": "", 
            "address": "Театральный пр-д, д.5/1", 
            "lat": 55.759896085897864, 
            "lng": 37.62479657976223, 
            "id": 433
        }, 
        {
            "title": "Буше", 
            "url": "https://coffeemap.ru/bushe/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Киевское шоссе, 23-й километр, 1, ТРЦ Саларис", 
            "lat": 55.623378950969006, 
            "lng": 37.42242347381897, 
            "id": 434
        }, 
        {
            "title": "Буше", 
            "url": "https://coffeemap.ru/bushe/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/bushe.moscow/", 
            "address": "Ул. Солянка, 1/2", 
            "lat": 55.75430676223728, 
            "lng": 37.637550830841064, 
            "id": 435
        }, 
        {
            "title": "Вайт by Даблби", 
            "url": "https://coffeemap.ru/vajt-by-dablbi/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Арбат, 10", 
            "lat": 55.751318976382564, 
            "lng": 37.596429786508196, 
            "id": 436
        }, 
        {
            "title": "Вайт by Даблби", 
            "url": "https://coffeemap.ru/vajt-by-dablbi/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/doublebcoffeetea/", 
            "address": "Ул. Автозаводская, 13/1", 
            "lat": 55.705806986567154, 
            "lng": 37.656283378601074, 
            "id": 437
        }, 
        {
            "title": "Ворона. Кофе & сыр", 
            "url": "https://coffeemap.ru/vorona-kofe-syr/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ: 10:00-18:00, ВС: выходной", 
            "note": "https://www.instagram.com/vorona.coffee/", 
            "address": "Пресненская набережная, 12", 
            "lat": 55.75001253544968, 
            "lng": 37.53764470055967, 
            "id": 438
        }, 
        {
            "title": "Второе кафе", 
            "url": "https://coffeemap.ru/vtoroe-kafe/", 
            "time": "ПН-ВС: 8:00-21:00", 
            "note": "https://www.instagram.com/vtoroecafe/", 
            "address": "Колокольников пер., 2", 
            "lat": 55.7678775, 
            "lng": 37.62431879999997, 
            "id": 440
        }, 
        {
            "title": "Грамотный кофе", 
            "url": "https://coffeemap.ru/gramotnyj-kofe/", 
            "time": "ПН: выходной, ВТ-СБ: 8:00-22:00, ВС: 10:00-20:00", 
            "note": "", 
            "address": "Страстной бульвар, 8, Библиотека им. А.П. Чехова", 
            "lat": 55.76606446424534, 
            "lng": 37.60928555396731, 
            "id": 441
        }, 
        {
            "title": "Грамотный кофе", 
            "url": "https://coffeemap.ru/gramotnyj-kofe/", 
            "time": "ПН: выходной, ВТ-СБ: 8:00-22:00, ВС: 10:00-20:00", 
            "note": "https://www.instagram.com/literate_coffee/", 
            "address": "Чистопрудный бульвар, 23, библиотека Ф.М. Достоевского", 
            "lat": 55.76032877854537, 
            "lng": 37.64658987522125, 
            "id": 442
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 9:00–23:00", 
            "note": "", 
            "address": "Новодевичий проезд, 4", 
            "lat": 55.729013260196986, 
            "lng": 37.55850117404339, 
            "id": 443
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 11:00–22:00", 
            "note": "", 
            "address": "4-я Тверская-Ямская, 27", 
            "lat": 55.77319000000001, 
            "lng": 37.59544900000003, 
            "id": 444
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Трехпрудный пер., 10/2", 
            "lat": 55.7654262, 
            "lng": 37.59759610000003, 
            "id": 445
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Ул. Никольская, 10/2б", 
            "lat": 55.758107036000126, 
            "lng": 37.62539312222907, 
            "id": 446
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–20:00, СБ–ВС: 10:00–20:00", 
            "note": "", 
            "address": "Самарская улица 1 БЦ «Новион»", 
            "lat": 55.7841898, 
            "lng": 37.62862960000007, 
            "id": 447
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–20:00, СБ–ВС: закрыто", 
            "note": "", 
            "address": "Павелецкая пл., 2/2", 
            "lat": 55.7302, 
            "lng": 37.63587600000005, 
            "id": 448
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ЧТ, ВС: 10:00–22:00, ПТ–СБ: 10:00–23:00", 
            "note": "", 
            "address": "Ходыкинский б-р, 4, ТРК «Авиапарк»", 
            "lat": 55.7900457, 
            "lng": 37.53088090000006, 
            "id": 449
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 9:00–23:00, СБ–ВС: 11:00–23:00", 
            "note": "", 
            "address": "Берсеневская наб., 8с1", 
            "lat": 55.74120906321107, 
            "lng": 37.6091194152832, 
            "id": 450
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ЧТ: 9:00–22:00, ПТ: 9:00–23:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Пресненская наб., 2, ТЦ «Афимолл Сити»", 
            "lat": 55.74928547423352, 
            "lng": 37.54023710317995, 
            "id": 451
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–21:00, СБ–ВС: 11:00–21:00", 
            "note": "", 
            "address": "Цветной б-р, 2, БЦ «Легенда Цветного»", 
            "lat": 55.7679832, 
            "lng": 37.62303099999997, 
            "id": 452
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:30–21:00, СБ–ВС: 10:30–21:00", 
            "note": "", 
            "address": "Ул. Бутырский Вал, 5", 
            "lat": 55.77877239999999, 
            "lng": 37.58503310000003, 
            "id": 453
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 11:00–23:00", 
            "note": "", 
            "address": "Ул. Волхонка, 9с1", 
            "lat": 55.7470728, 
            "lng": 37.60764100000006, 
            "id": 454
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 9:00–23:00", 
            "note": "", 
            "address": "Чистопрудный б-р, 12с4", 
            "lat": 55.76147723296398, 
            "lng": 37.643253207206726, 
            "id": 455
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Ул. Неглинная, 18", 
            "lat": 55.7654885, 
            "lng": 37.62065770000004, 
            "id": 456
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–21:00, СБ: 11:00–19:00, ВС: закрыто", 
            "note": "", 
            "address": "Пресненская набережная, 8с1", 
            "lat": 55.7470285, 
            "lng": 37.539257200000065, 
            "id": 457
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Мира пр-т, 26с1, сад «Аптекарский огород»", 
            "lat": 55.7779319591485, 
            "lng": 37.63301807539369, 
            "id": 458
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Ул. Каланчевская, 17с1", 
            "lat": 55.773028, 
            "lng": 37.65141900000003, 
            "id": 459
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–23:00, СБ–ВС: 11:00–23:00", 
            "note": "", 
            "address": "Ул. Трехгорный Вал, 24", 
            "lat": 55.76186, 
            "lng": 37.56268899999998, 
            "id": 460
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ленинградское ш., 16Ас4", 
            "lat": 55.823725, 
            "lng": 37.49807050000004, 
            "id": 461
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 10:00–22:00, СБ–ВС: закрыто", 
            "note": "", 
            "address": "2-ой Сыромятнический пер., 1", 
            "lat": 55.753754, 
            "lng": 37.662237600000026, 
            "id": 462
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ВС: 10:00–22:00", 
            "note": "", 
            "address": "МКАД, 66 км (внешняя сторона), Box City", 
            "lat": 55.8224503, 
            "lng": 37.38489040000002, 
            "id": 463
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–19:00, СБ–ВС: закрыто", 
            "note": "", 
            "address": "22-й км Киевского шоссе, домовладение 6с1", 
            "lat": 55.6347171, 
            "lng": 37.43069830000002, 
            "id": 464
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–19:30, СБ–ВС: 11:00–21:00", 
            "note": "", 
            "address": "Ул. Воздвиженка, 10", 
            "lat": 55.753237, 
            "lng": 37.60641199999998, 
            "id": 465
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ВС: 9:00-21:00", 
            "note": "", 
            "address": "Крымский вал, 9, стр. 18, Парк Горького", 
            "lat": 55.7264805125173, 
            "lng": 37.60137209176085, 
            "id": 466
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ–ВС: 9:00–21:00", 
            "note": "", 
            "address": "Нижний Сусальный пер., 5, стр. 9", 
            "lat": 55.760738, 
            "lng": 37.66374289999999, 
            "id": 467
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "ул. Таганская, д. 17-23", 
            "lat": 55.7401636, 
            "lng": 37.66299200000003, 
            "id": 468
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "", 
            "address": "Ул. Шаболовка, 29/2", 
            "lat": 55.7214953, 
            "lng": 37.61073829999998, 
            "id": 469
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН–ПТ: 8:00–21:00, СБ–ВС: 10:00–21:00", 
            "note": "", 
            "address": "22-й км Киевское шоссе 4", 
            "lat": 55.63362640185457, 
            "lng": 37.43978970411479, 
            "id": 470
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 09:00-22:00", 
            "note": "", 
            "address": "ул. Бахрушина, 12с2", 
            "lat": 55.73558689999999, 
            "lng": 37.63471759999993, 
            "id": 471
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ВС: 9:00-23:00", 
            "note": "", 
            "address": "Ул. Новый Арбат, 24, к/т Октябрь", 
            "lat": 55.75287369999999, 
            "lng": 37.586863300000005, 
            "id": 472
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ломоносовский проспект, 23", 
            "lat": 55.69178726059281, 
            "lng": 37.537619138513264, 
            "id": 473
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Охотный ряд, 2", 
            "lat": 55.756833304809206, 
            "lng": 37.61759857943912, 
            "id": 474
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 08:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "", 
            "address": "Ул. Покровка, 2/1 стр. 1", 
            "lat": 55.7583093023319, 
            "lng": 37.63972130493141, 
            "id": 475
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. 4-я Тверская-Ямская, 27", 
            "lat": 55.77319000000001, 
            "lng": 37.59544900000003, 
            "id": 476
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00–22:00, СБ-ВС: 10:00–22:00", 
            "note": "", 
            "address": "Весковский переулок, 3", 
            "lat": 55.77869800000001, 
            "lng": 37.59883309999998, 
            "id": 477
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ВС: 10:00–23:00", 
            "note": "", 
            "address": "Калужское шоссе, 21-й километр, с1, ТЦ Мега Теплый Стан", 
            "lat": 55.60336115723877, 
            "lng": 37.490635996772994, 
            "id": 478
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00–23:00, СБ-ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ул. Тверская, 6с1", 
            "lat": 55.760996, 
            "lng": 37.610686999999984, 
            "id": 479
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00–22:00, СБ-ВС: 10:00–22:00", 
            "note": "", 
            "address": "Коровий Вал, 5, БЦ Оазис", 
            "lat": 55.7283319, 
            "lng": 37.62015900000006, 
            "id": 481
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00–23:00, СБ-ВС: 10:00–23:00", 
            "note": "", 
            "address": "Большой Патриарший переулок, 8 стр 1", 
            "lat": 55.76284690457992, 
            "lng": 37.59242153459502, 
            "id": 482
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: выходной", 
            "note": "", 
            "address": "Пресненская набережная, 12", 
            "lat": 55.7476063656721, 
            "lng": 37.54077203787733, 
            "id": 483
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00–22:00, СБ-ВС: 10:00–22:00", 
            "note": "", 
            "address": "Пресненская набережная, д.4, стр.1", 
            "lat": 55.748942046385245, 
            "lng": 37.54305232926879, 
            "id": 484
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-20:00", 
            "note": "https://www.instagram.com/doublebcoffeetea/", 
            "address": "Проспект Вернадского, 41", 
            "lat": 55.674340168947175, 
            "lng": 37.50295807412424, 
            "id": 485
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Большая Якиманка, 54", 
            "lat": 55.73141095888174, 
            "lng": 37.611723591903825, 
            "id": 489
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Мясницкая, 16", 
            "lat": 55.760961518776355, 
            "lng": 37.632387039719525, 
            "id": 490
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Большой Толмачевский переулок, 4с1", 
            "lat": 55.7408859431445, 
            "lng": 37.62284696102142, 
            "id": 491
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Новорязанское ш., 8", 
            "lat": 55.6609187, 
            "lng": 37.8793739, 
            "id": 492
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Ул. Большая Тульская, 13", 
            "lat": 55.70820401309988, 
            "lng": 37.622008535258765, 
            "id": 493
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ВС: 9:00-22:00", 
            "note": "", 
            "address": "Солянский проезд, 1", 
            "lat": 55.75409269999999, 
            "lng": 37.6358201, 
            "id": 495
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 09:00–18:00, СБ-ВС: выходной", 
            "note": "", 
            "address": "Ленинградский проспект, 36с11", 
            "lat": 55.788289602109806, 
            "lng": 37.56782404430845, 
            "id": 496
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "", 
            "address": "Большой Кисловский переулок, 1с2", 
            "lat": 55.7535651, 
            "lng": 37.605596, 
            "id": 497
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: выходной", 
            "note": "", 
            "address": "Смоленская площадь, 5", 
            "lat": 55.75041848337385, 
            "lng": 37.577669453227024, 
            "id": 498
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/doublebcoffeetea/", 
            "address": "Ул. Долгоруковская, 6", 
            "lat": 55.77582989999999, 
            "lng": 37.6036, 
            "id": 499
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "", 
            "address": "1-я улица Леонова, 18", 
            "lat": 55.8449115, 
            "lng": 37.6391709, 
            "id": 500
        }, 
        {
            "title": "Даблби", 
            "url": "https://coffeemap.ru/dablbi/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/doublebcoffeetea/", 
            "address": "Ул. Тимура Фрунзе, 11с33", 
            "lat": 55.73525834106062, 
            "lng": 37.587608180789324, 
            "id": 501
        }, 
        {
            "title": "Дегтярный", 
            "url": "https://coffeemap.ru/degtyarnyj/", 
            "time": "ПН-ПТ: 7:30 - 21:00, СБ-ВС: 9:30-21:00", 
            "note": "https://www.instagram.com/degtyarny/", 
            "address": "Дегтярный переулок, 5с1", 
            "lat": 55.76805599999999, 
            "lng": 37.6016369, 
            "id": 502
        }, 
        {
            "title": "Делюсь Душой", 
            "url": "https://coffeemap.ru/delyus-dushoj/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 9:00–22:00", 
            "note": "https://www.instagram.com/ddcoffeemoscow/", 
            "address": "Ул. Пятницкая, 54с1", 
            "lat": 55.734295783115066, 
            "lng": 37.627430474660514, 
            "id": 503
        }, 
        {
            "title": "ДоброЛавка", 
            "url": "https://coffeemap.ru/dobrolavka/", 
            "time": "ПН-ВС: 9:00-21:00", 
            "note": "https://instagram.com/dobrolavka.ru", 
            "address": "Столярный переулок, 3к13", 
            "lat": 55.7644174, 
            "lng": 37.56853029999999, 
            "id": 507
        }, 
        {
            "title": "Дядька", 
            "url": "https://coffeemap.ru/dyadkakofe/", 
            "time": "ПН-ВС: 9:00-20:00", 
            "note": "", 
            "address": "ул. Электрозаводская, 21, проходная №3 «Мраморная»", 
            "lat": 55.78742388719701, 
            "lng": 37.70566284656525, 
            "id": 508
        }, 
        {
            "title": "Дядька", 
            "url": "https://coffeemap.ru/dyadkakofe/", 
            "time": "ПН-ПТ: 8:30-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Милютинский переулок, 19/4с1", 
            "lat": 55.765628590919, 
            "lng": 37.63217031955719, 
            "id": 509
        }, 
        {
            "title": "Дядька", 
            "url": "https://coffeemap.ru/dyadkakofe/", 
            "time": "ПН-ВС: 9:00-20:00", 
            "note": "https://www.instagram.com/dyadkacoffee/", 
            "address": "ул. Электрозаводская, 21, этаж 3", 
            "lat": 55.78744400000001, 
            "lng": 37.70544, 
            "id": 510
        }, 
        {
            "title": "Забыли Сахар", 
            "url": "https://coffeemap.ru/zabyli-sahar/", 
            "time": "ПН-ПТ: 9:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "www.instagram.com/zabylisahar", 
            "address": "Кулешевская дорога, 3/7", 
            "lat": 59.9874211, 
            "lng": 30.3715663, 
            "id": 512
        }, 
        {
            "title": "ЗАРЯ", 
            "url": "https://coffeemap.ru/zarya/", 
            "time": "ПН-ПТ: 8:45-23:00, СБ-ВС: 10:00-23:00", 
            "note": "", 
            "address": "Ул. Петровка, 30/7", 
            "lat": 55.76817217837363, 
            "lng": 37.61497548413081, 
            "id": 514
        }, 
        {
            "title": "ЗАРЯ", 
            "url": "https://coffeemap.ru/zarya/", 
            "time": "ПН-ВС: 10:00-23:00", 
            "note": "https://www.instagram.com/zaryacoffee", 
            "address": "Ул. Новодмитровская, 1с9", 
            "lat": 55.8069443, 
            "lng": 37.5832255, 
            "id": 515
        }, 
        {
            "title": "ЗДРАСТЕ Подольск", 
            "url": "https://coffeemap.ru/zdraste-podolsk/", 
            "time": "ПН-ПТ: 8:00-22:00", 
            "note": "https://www.instagram.com/zdraste.podolsk/", 
            "address": "Проспект Ленина, 113/62", 
            "lat": 55.4315848, 
            "lng": 37.5469914, 
            "id": 516
        }, 
        {
            "title": "Зерно Кофейня", 
            "url": "https://coffeemap.ru/zerno-kofejnya/", 
            "time": "ПН-ВС: 8:00 - 20:00, СБ-ВС: 9:00 - 21:00", 
            "note": "https://www.instagram.com/cofeynia.zerno/", 
            "address": "Шелепихинская набережная, д. 34, корп. 2", 
            "lat": 55.76268218923833, 
            "lng": 37.50896224151794, 
            "id": 517
        }, 
        {
            "title": "Иди Обниму", 
            "url": "https://coffeemap.ru/idi-obnimu/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "", 
            "address": "Проспект Вернадского, 44к2", 
            "lat": 55.67475427214352, 
            "lng": 37.497285618385305, 
            "id": 519
        }, 
        {
            "title": "Иди Обниму", 
            "url": "https://coffeemap.ru/idi-obnimu/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/obnimicoffee/", 
            "address": "Ул. Малая Филёвская, 18", 
            "lat": 55.73707599999999, 
            "lng": 37.468072, 
            "id": 520
        }, 
        {
            "title": "Импульс", 
            "url": "https://coffeemap.ru/impuls/", 
            "time": "ПН-ПТ: 08:00-21:00, СБ-ВС: 09:00-21:00", 
            "note": "https://www.instagram.com/impulsecoffeebar/", 
            "address": "Ул. Автозаводская, 23б к2 ", 
            "lat": 55.70111176356229, 
            "lng": 37.65183902090149, 
            "id": 521
        }, 
        {
            "title": "Кафе О Ле", 
            "url": "https://coffeemap.ru/kafe-o-le/", 
            "time": "ПН-ВТ: 8:00-20:00, СР-ПТ: 8:00-22:00, СБ: 10:00-22:00, ВС: 10:00-20:00", 
            "note": "https://www.instagram.com/cafe_au_lait_moscow/", 
            "address": "ул. Малая Пироговская, 13, стр. 3", 
            "lat": 55.72867530000001, 
            "lng": 37.56965279999997, 
            "id": 523
        }, 
        {
            "title": "Коза", 
            "url": "https://coffeemap.ru/koza/", 
            "time": "ПН-ВС: 09:00-21:00", 
            "note": "https://www.instagram.com/cosa_coffee/", 
            "address": "Черняховского, 19", 
            "lat": 55.80848752174212, 
            "lng": 37.53893163539786, 
            "id": 524
        }, 
        {
            "title": "Кооператив Чёрный", 
            "url": "https://coffeemap.ru/kooperativ-chernyj/", 
            "time": "ПН: 8:00–19:00 ВТ–ПТ: 8:00–23:00, СБ–ВС: 10:00–23:00", 
            "note": "https://www.instagram.com/chernyicooperative/", 
            "address": "Лялин переулок, 5с1", 
            "lat": 55.75998472019435, 
            "lng": 37.65181944047549, 
            "id": 526
        }, 
        {
            "title": "Котомка", 
            "url": "https://coffeemap.ru/kotomka/", 
            "time": "ПН-ПТ: 09:00—21:00, СБ-ВС: 10:00—21:00", 
            "note": "", 
            "address": "Малый Казенный переулок, 16", 
            "lat": 55.761278729289415, 
            "lng": 37.65539911593851, 
            "id": 527
        }, 
        {
            "title": "Котомка", 
            "url": "https://coffeemap.ru/kotomka/", 
            "time": "ПН-ВС: 10:00-21:00", 
            "note": "https://instagram.com/kotomka.coffee.food", 
            "address": "1-я Тверская-Ямская, 11", 
            "lat": 55.77275392039302, 
            "lng": 37.59026778636933, 
            "id": 528
        }, 
        {
            "title": "Кофе—Москва", 
            "url": "https://coffeemap.ru/kofe-moskva/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: выходной", 
            "note": "https://www.instagram.com/kofemoskva/", 
            "address": "Ул. Краснопролетарская 16, стр.2 ", 
            "lat": 55.778095967326536, 
            "lng": 37.606667914016725, 
            "id": 529
        }, 
        {
            "title": "Кофе Бюро", 
            "url": "https://coffeemap.ru/kofe-byuro/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "https://www.instagram.com/coffeeburo/", 
            "address": "Славянская пл., 2/5/4с3", 
            "lat": 55.75318679999999, 
            "lng": 37.634707599999956, 
            "id": 530
        }, 
        {
            "title": "Кофе нон стоп", 
            "url": "https://coffeemap.ru/kofe-non-stop/", 
            "time": "ПН-ПТ: 08:00-00:00, СБ-ВС: 10:00-00:00", 
            "note": "https://www.instagram.com/kebarnonstop/", 
            "address": "Ул. Мясницкая, 32 с2", 
            "lat": 55.76550794457313, 
            "lng": 37.63922462579498, 
            "id": 533
        }, 
        {
            "title": "Кофе Советы", 
            "url": "https://coffeemap.ru/kofe-sovety/", 
            "time": "ПН-ЧТ: 8:30-19:30, ПТ: 8:30-18:30, СБ-ВС: закрыто", 
            "note": "https://www.instagram.com/coffee.soveti/", 
            "address": "Ул. Воздвиженка, 4/7c2", 
            "lat": 55.75324410814776, 
            "lng": 37.60998574225846, 
            "id": 534
        }, 
        {
            "title": "КОФЕ&MOLOKO", 
            "url": "https://coffeemap.ru/kofe-moloko/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Кутузовский пр-т, 9к1", 
            "lat": 55.7484419, 
            "lng": 37.56099459999996, 
            "id": 535
        }, 
        {
            "title": "КОФЕ&MOLOKO", 
            "url": "https://coffeemap.ru/kofe-moloko/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Кутузовский пр-т, 35", 
            "lat": 55.7402579, 
            "lng": 37.5373472, 
            "id": 536
        }, 
        {
            "title": "КОФЕ&MOLOKO", 
            "url": "https://coffeemap.ru/kofe-moloko/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "Ул. 1812 года,  2", 
            "lat": 55.73638614269012, 
            "lng": 37.524656653404236, 
            "id": 537
        }, 
        {
            "title": "КОФЕ&MOLOKO", 
            "url": "https://coffeemap.ru/kofe-moloko/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "ул. Авиационная, 77к1", 
            "lat": 55.807774858157, 
            "lng": 37.450809112303205, 
            "id": 538
        }, 
        {
            "title": "КОФЕ&MOLOKO", 
            "url": "https://coffeemap.ru/kofe-moloko/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "", 
            "address": "ул. Сергея Макеева, 9к2", 
            "lat": 55.762246, 
            "lng": 37.55101519999999, 
            "id": 539
        }, 
        {
            "title": "КОФЕ&MOLOKO", 
            "url": "https://coffeemap.ru/kofe-moloko/", 
            "time": "ПН–ЧТ: 9:00–21:00, ПТ: 9:00-22:00 СБ–ВС: 10:00–22:00", 
            "note": "https://www.instagram.com/kofemolokomoscow", 
            "address": "Ул. Производственная, 12, корпус 2, секция 3", 
            "lat": 55.6404131, 
            "lng": 37.3807935, 
            "id": 540
        }, 
        {
            "title": "Кофебар «Спесь»", 
            "url": "https://coffeemap.ru/spes-kofebar/", 
            "time": "ПН-ВС: 9:00-21:00", 
            "note": "https://instagram.com/spescoffeebar", 
            "address": "Ул. Шереметьевская, 2с1", 
            "lat": 55.7936802, 
            "lng": 37.6189249, 
            "id": 541
        }, 
        {
            "title": "КОФЕДЕЙ", 
            "url": "https://coffeemap.ru/kofedej/", 
            "time": "ПН-ПТ: 8:30-19:00, СБ-ВС: закрыто", 
            "note": "ttps://www.instagram.com/kofedei/", 
            "address": "Медовый переулок, 5, стр. 1, БЦ «Улей Плаза»", 
            "lat": 55.7844396, 
            "lng": 37.710022500000036, 
            "id": 543
        }, 
        {
            "title": "КОФЕДЕЙ", 
            "url": "https://coffeemap.ru/kofedej/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 10:00-20:00", 
            "note": "https://www.instagram.com/kofedei/", 
            "address": "Ул. Садово-Триумфальная, 18-20", 
            "lat": 55.7716538725356, 
            "lng": 37.60262955092617, 
            "id": 545
        }, 
        {
            "title": "Кофейня Московской Школы Бариста", 
            "url": "https://coffeemap.ru/kofejnya-moskovskoj-shkoly-barista/", 
            "time": "ПН-ПТ: 9:00-22:00, СБ-ВC: 10:00-22:00", 
            "note": "https://instagram.com/baristaschool_coffee", 
            "address": "3-й Красносельский переулок, 19с4 ЖК «Красная стрела»", 
            "lat": 55.7841179, 
            "lng": 37.65600560000007, 
            "id": 549
        }, 
        {
            "title": "Кофейня РОСИЗО", 
            "url": "https://coffeemap.ru/kofejnya-rosizo/", 
            "time": "ПН-ВС: 10:00-22:00", 
            "note": "https://instagram.com/rosizo?igshid=po6w7r9fee5w", 
            "address": "Ул. Проспект Мира, 119 строение 516", 
            "lat": 55.830107198313435, 
            "lng": 37.61997699737549, 
            "id": 550
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 9:00–00:00", 
            "note": "", 
            "address": "Ленинградское ш., 16Ас4", 
            "lat": 55.823917857938426, 
            "lng": 37.49789883862309, 
            "id": 551
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 8:00–00:00", 
            "note": "", 
            "address": "Ул. Усачева, 25", 
            "lat": 55.72748199999999, 
            "lng": 37.56786890000001, 
            "id": 552
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН–ЧТ: 8:00–00:00, ПТ: 8:00–2:00, СБ: 10:00–2:00, ВС: 10:00–00:00", 
            "note": "", 
            "address": "Малый Черкасский пер., 2", 
            "lat": 55.75836349999999, 
            "lng": 37.62621999999999, 
            "id": 553
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 24 часа", 
            "note": "", 
            "address": "Кривоколенный пер., 10с4", 
            "lat": 55.7611824, 
            "lng": 37.63599210000007, 
            "id": 554
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН–ЧТ: 8:00–00:00, ПТ–СБ: 24 часа, ВС: 8:00–00:00", 
            "note": "", 
            "address": "Ул. Новый Арбат, 19", 
            "lat": 55.751914, 
            "lng": 37.58914900000002, 
            "id": 556
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН–ВС: 8:00-00:00", 
            "note": "", 
            "address": "Ул. Большая Полянка, 2/2", 
            "lat": 55.741768, 
            "lng": 37.615795299999945, 
            "id": 557
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 10:00–22:00", 
            "note": "", 
            "address": "Красная пл., 3, «ГУМ»", 
            "lat": 55.7546967, 
            "lng": 37.62152160000005, 
            "id": 558
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 8:00-00:00", 
            "note": "", 
            "address": "Ул. Тверская, 22", 
            "lat": 55.767701, 
            "lng": 37.601109199999996, 
            "id": 559
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 24 часа", 
            "note": "", 
            "address": "Ул. Большая Никитская, 13/6с1", 
            "lat": 55.75635399999999, 
            "lng": 37.60491999999999, 
            "id": 560
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 24 часа", 
            "note": "", 
            "address": "Кудринская пл., 46/54", 
            "lat": 55.75819079999999, 
            "lng": 37.58549479999999, 
            "id": 561
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 24 часа", 
            "note": "", 
            "address": "Кутузовский пр-т, 17", 
            "lat": 55.74695, 
            "lng": 37.55687499999999, 
            "id": 562
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 24 часа", 
            "note": "", 
            "address": "Ул. Покровка, 18/18с3", 
            "lat": 55.759201, 
            "lng": 37.646089000000075, 
            "id": 563
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 24 часа", 
            "note": "", 
            "address": "Трубная пл., 2", 
            "lat": 55.7661016, 
            "lng": 37.6226236, 
            "id": 564
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 24 часа", 
            "note": "", 
            "address": "Комсомольский пр-т, 21с2", 
            "lat": 55.727853272668746, 
            "lng": 37.5839804649429, 
            "id": 565
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 24 часа", 
            "note": "", 
            "address": "Ул. Лесная, 5", 
            "lat": 55.7778681, 
            "lng": 37.58705880000002, 
            "id": 566
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН–ПТ: 8:00–00:00, СБ–ВС: 10:00–00:00", 
            "note": "", 
            "address": "Ул. Садовническая, 82с2", 
            "lat": 55.7348731, 
            "lng": 37.64239500000008, 
            "id": 567
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 9:00–22:00", 
            "note": "", 
            "address": "Хорошевское ш., 27, ТЦ «Хорошо»", 
            "lat": 55.7771917, 
            "lng": 37.52349000000004, 
            "id": 568
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 8:00-00:00", 
            "note": "", 
            "address": "Ул. 1-я Тверская-Ямская, 21", 
            "lat": 55.7745334, 
            "lng": 37.58723259999999, 
            "id": 577
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 8:00-00:00", 
            "note": "", 
            "address": "Ул. Валовая, 35", 
            "lat": 55.7292522, 
            "lng": 37.625948600000015, 
            "id": 578
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 09:00-21:00", 
            "note": "", 
            "address": "ул. Осенняя, 11", 
            "lat": 55.76240910114662, 
            "lng": 37.404426634311676, 
            "id": 580
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ВС: 10:00–23:00", 
            "note": "", 
            "address": "Ул. Лесная, 20/3, фудмолл Депо", 
            "lat": 55.7804566, 
            "lng": 37.5920618, 
            "id": 581
        }, 
        {
            "title": "Кофемания", 
            "url": "https://coffeemap.ru/kofemaniya/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 9:00-23:00", 
            "note": "https://www.instagram.com/coffeemania.ru/", 
            "address": "Ул. Мосфильмовская, вл.1а", 
            "lat": 55.72178659999999, 
            "lng": 37.52860270000001, 
            "id": 582
        }, 
        {
            "title": "КОФЕМАУС", 
            "url": "https://coffeemap.ru/kofemaus/", 
            "time": "ПН–ПТ: 8:00–20:00, СБ–ВС: 10:00–20:00", 
            "note": "https://www.instagram.com/coffeemouse/", 
            "address": "Ул. Садовая-Каретная, 4-6с1", 
            "lat": 55.772388, 
            "lng": 37.60633000000007, 
            "id": 583
        }, 
        {
            "title": "Кофепровод", 
            "url": "https://coffeemap.ru/kofeprovod/", 
            "time": "ПН–ПТ: 8:30–21:00, СБ–ВС: 12:00–21:00", 
            "note": "", 
            "address": "Яковоапостольский пер., 9с1", 
            "lat": 55.7587866, 
            "lng": 37.654385700000034, 
            "id": 584
        }, 
        {
            "title": "Коффмарт", 
            "url": "https://coffeemap.ru/koffmart/", 
            "time": "ПН-ПТ: 8:00 - 21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/coffmart/", 
            "address": "Волгоградский проспект, 16", 
            "lat": 55.72907609954933, 
            "lng": 37.67553361838533, 
            "id": 585
        }, 
        {
            "title": "Культура Кофе", 
            "url": "https://coffeemap.ru/kultura-kofe/", 
            "time": "ПН–ПТ: 8:30–19:00, СБ–ВС: 10:00–19:00", 
            "note": "https://www.instagram.com/cultura.coffee/", 
            "address": "Ул. Усачева, 33с1", 
            "lat": 55.723201, 
            "lng": 37.56116399999996, 
            "id": 587
        }, 
        {
            "title": "Кутята Coffee Shop", 
            "url": "https://coffeemap.ru/kutyata/", 
            "time": "ПН-ПТ: 7:00 - 22:00, СБ-ВС: 8:00 - 22:00", 
            "note": "", 
            "address": "Ул. Земляной Вал, 54с1", 
            "lat": 55.74878635366799, 
            "lng": 37.65519409747526, 
            "id": 590
        }, 
        {
            "title": "Кутята Coffee Shop", 
            "url": "https://coffeemap.ru/kutyata/", 
            "time": "ПН-ПТ: 7:00 - 22:00, СБ-ВС: 8:00 - 22:00", 
            "note": "", 
            "address": "Проектируемый проезд, 2554", 
            "lat": 55.77954962837111, 
            "lng": 37.599221748036484, 
            "id": 591
        }, 
        {
            "title": "Кутята Coffee Shop", 
            "url": "https://coffeemap.ru/kutyata/", 
            "time": "ПН-ПТ: выходной, СБ: 12:00 - 21:00, ВС: 9:00 - 21:00", 
            "note": "https://www.instagram.com/kootyata.coffee.shop/", 
            "address": "Ул. Павла Корчагина, 2А", 
            "lat": 55.810866, 
            "lng": 37.65523499999999, 
            "id": 592
        }, 
        {
            "title": "Может, кофе?", 
            "url": "https://coffeemap.ru/mozhet-kofe/", 
            "time": "ПН-ПТ: 7:30-22:00, СБ-ВС: 9:00-22:00", 
            "note": "", 
            "address": "Шмитовский провезд, д.12", 
            "lat": 55.75950877879335, 
            "lng": 37.55180505026249, 
            "id": 596
        }, 
        {
            "title": "Может, кофе?", 
            "url": "https://coffeemap.ru/mozhet-kofe/", 
            "time": "ПН-ПТ: 7:30-22:00, СБ-ВС: 9:00-22:00", 
            "note": "https://www.instagram.com/maybe.coffee/", 
            "address": "Лужнецкая набережная, 2/4 стр. 46", 
            "lat": 55.713699, 
            "lng": 37.56940590000001, 
            "id": 597
        }, 
        {
            "title": "Молния", 
            "url": "https://coffeemap.ru/molniya/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/molnia.coffee/", 
            "address": "Ул. Земляной вал, 38-40/15с9", 
            "lat": 55.75501859571992, 
            "lng": 37.65660064418032, 
            "id": 598
        }, 
        {
            "title": "Молодо Зелено", 
            "url": "https://coffeemap.ru/molodo-zeleno/", 
            "time": "ПН-ЧТ: 9:00-22:00, ПТ-СБ: 9:00-23:00, ВС: 9:00-22:00", 
            "note": "https://www.instagram.com/molodo_cafe", 
            "address": "Варшавское шоссе, 141к10", 
            "lat": 55.58927189165895, 
            "lng": 37.60267674922943, 
            "id": 600
        }, 
        {
            "title": "Мысли кофе", 
            "url": "https://coffeemap.ru/mysli-kofe/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 9:00-20:00", 
            "note": "https://www.instagram.com/thoughtsofcoffee/", 
            "address": "Духовской пер., д.17с11", 
            "lat": 55.704543, 
            "lng": 37.61521199999993, 
            "id": 604
        }, 
        {
            "title": "Неслучайно 08|08", 
            "url": "https://coffeemap.ru/nesluchajno-08-08/", 
            "time": "ПН-ПТ: 08:00-22:00, СБ-ВС: 09:00-22:00", 
            "note": "", 
            "address": "Шмитовский проезд, 10/7", 
            "lat": 55.75951895778391, 
            "lng": 37.552643813491805, 
            "id": 605
        }, 
        {
            "title": "Неслучайно 08|08", 
            "url": "https://coffeemap.ru/nesluchajno-08-08/", 
            "time": "ПН-ПТ: 08:00-22:00, СБ-ВС: 09:00-22:00", 
            "note": "https://www.instagram.com/nesluchajno08.08/", 
            "address": "улица Ленина, 30с1", 
            "lat": 55.76124049204479, 
            "lng": 37.24312119767088, 
            "id": 606
        }, 
        {
            "title": "Ни свет ни заря", 
            "url": "https://coffeemap.ru/ni-svet-ni-zarya/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "https://www.instagram.com/nisvet.nizarya/?hl=ru", 
            "address": "Ул. Покровка, 41с1", 
            "lat": 55.762283077620125, 
            "lng": 37.6520397994751, 
            "id": 609
        }, 
        {
            "title": "Нитка", 
            "url": "https://coffeemap.ru/nitka/", 
            "time": "ПН-ВС: 10:00-21:00", 
            "note": "https://www.instagram.com/nitkatea/", 
            "address": "Ул. Большая Ордынка, 46с3, Культурный Центр Андрея Вознесенского", 
            "lat": 55.73554069999999, 
            "lng": 37.6241387, 
            "id": 610
        }, 
        {
            "title": "Новатор Кофе", 
            "url": "https://coffeemap.ru/novator-kofe/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 9:00-22:00", 
            "note": "", 
            "address": "Ул. Новаторов, 36к1", 
            "lat": 55.6616981, 
            "lng": 37.52369420000002, 
            "id": 611
        }, 
        {
            "title": "Новатор Кофе", 
            "url": "https://coffeemap.ru/novator-kofe/", 
            "time": "ПН-ПТ: 7:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "", 
            "address": "Ленинский проспект, 77/1", 
            "lat": 55.685794089274005, 
            "lng": 37.54305417216494, 
            "id": 612
        }, 
        {
            "title": "Новатор Кофе", 
            "url": "https://coffeemap.ru/novator-kofe/", 
            "time": "ПН-ПТ: 7:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "", 
            "address": "Ленинский проспект, 70/11, под. 12", 
            "lat": 55.6877044778786, 
            "lng": 37.540972844342654, 
            "id": 613
        }, 
        {
            "title": "Новатор Кофе", 
            "url": "https://coffeemap.ru/novator-kofe/", 
            "time": "ПН-ВС: 08:00-22:00", 
            "note": "", 
            "address": "Ермолаевский переулок, 18А", 
            "lat": 55.765732, 
            "lng": 37.593616, 
            "id": 614
        }, 
        {
            "title": "Новатор Кофе", 
            "url": "https://coffeemap.ru/novator-kofe/", 
            "time": "ПН-ВС: 9:00-22:00", 
            "note": "https://www.instagram.com/novatorcoffee/", 
            "address": "Ленинский проспект, 85", 
            "lat": 55.68012573435125, 
            "lng": 37.534896303952024, 
            "id": 615
        }, 
        {
            "title": "Оазис кофе и завтраки", 
            "url": "https://coffeemap.ru/oazis-kofe-i-zavtraki/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 10:00-20:00", 
            "note": "https://www.instagram.com/oasiscoffee_breakfast/", 
            "address": "Ул. Хромова, 3", 
            "lat": 55.800236476921, 
            "lng": 37.71630160926202, 
            "id": 616
        }, 
        {
            "title": "Овсянки", 
            "url": "https://coffeemap.ru/ovsyanki/", 
            "time": "ПН-ВС: 8:00-21:00", 
            "note": "https://www.instagram.com/ovsyanky/", 
            "address": "Столярный переулок, 3к12", 
            "lat": 55.76423971449383, 
            "lng": 37.568283433729555, 
            "id": 618
        }, 
        {
            "title": "Он Мой", 
            "url": "https://coffeemap.ru/on-moj/", 
            "time": "ПН-ПТ: 7:30-19:30, СБ-ВС: 10:30-19:00", 
            "note": "https://www.instagram.com/coffeeonmoy/", 
            "address": "Проспект Мира, 45", 
            "lat": 55.78265099999999, 
            "lng": 37.63370199999997, 
            "id": 621
        }, 
        {
            "title": "Петровская кофейня", 
            "url": "https://coffeemap.ru/petrovskaya-kofejnya/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/petrovka_coffee/ ", 
            "address": "ул. Петровка, 28/5", 
            "lat": 55.7668509, 
            "lng": 37.61506110000005, 
            "id": 626
        }, 
        {
            "title": "Пнин", 
            "url": "https://coffeemap.ru/pnin/", 
            "time": "ПН-ПТ: 8:00 - 21:00, СБ-ВС: 10:00 - 21:00", 
            "note": "https://www.instagram.com/pnin.cafe/", 
            "address": "Большой Сухаревский переулок, 4", 
            "lat": 55.770459213112716, 
            "lng": 37.626317739486694, 
            "id": 627
        }, 
        {
            "title": "Подоконник", 
            "url": "https://coffeemap.ru/podokonnik/", 
            "time": "ПН-ПТ: 9:00-18:00, СБ-ВС: выходной", 
            "note": "https://www.instagram.com/podokonnik__coffee/", 
            "address": "Варшавское ш. 9 стр 1", 
            "lat": 55.6985986, 
            "lng": 37.6242657, 
            "id": 628
        }, 
        {
            "title": "После обсудим", 
            "url": "https://coffeemap.ru/posle-obsudim/", 
            "time": "ПН-ПТ: 8:00-20:00, СБ-ВС: 9:00-20:00", 
            "note": "https://instagram.com/posle_obsudim", 
            "address": "Большой Тишинский пер, 45", 
            "lat": 55.76945813224218, 
            "lng": 37.56692290306091, 
            "id": 629
        }, 
        {
            "title": "Почитательная", 
            "url": "https://coffeemap.ru/pochitatelnaya/", 
            "time": "ПН-ВС: 9:00-20:00", 
            "note": "https://www.instagram.com/pochitatelnaya/", 
            "address": "Ул. Сущевская, 14, Библиотека искусств им. Боголюбова", 
            "lat": 55.7813531, 
            "lng": 37.60211069999999, 
            "id": 630
        }, 
        {
            "title": "Практика Кофе", 
            "url": "https://coffeemap.ru/praktika-kofe/", 
            "time": "ПН-ПТ: 08:00–22:00, СБ-ВС: 09:00–22:00", 
            "note": "", 
            "address": "Чонгарский бул., 26А, корп. 1", 
            "lat": 55.653777266409215, 
            "lng": 37.602016175463106, 
            "id": 631
        }, 
        {
            "title": "Практика Кофе", 
            "url": "https://coffeemap.ru/praktika-kofe/", 
            "time": "ПН-ПТ: 08:00–22:00, СБ-ВС: 09:00–22:00", 
            "note": "", 
            "address": "Ул. Берзарина, 28А к2", 
            "lat": 55.790466264779425, 
            "lng": 37.47549227976226, 
            "id": 632
        }, 
        {
            "title": "Практика Кофе", 
            "url": "https://coffeemap.ru/praktika-kofe/", 
            "time": "ПН-СБ: 10:00-21:00, ВС: 10:00-19:00", 
            "note": "https://www.instagram.com/praktika.coffee/", 
            "address": "Щёлковское шоссе, вл75, ТРЦ Щелковский", 
            "lat": 55.8110125, 
            "lng": 37.8001306, 
            "id": 633
        }, 
        {
            "title": "Прогресс", 
            "url": "https://coffeemap.ru/progress/", 
            "time": "ПН-ВС: 11:00–00:00", 
            "note": "", 
            "address": "Ул. Пресненский Вал, 38с1", 
            "lat": 55.771354, 
            "lng": 37.57037289999994, 
            "id": 634
        }, 
        {
            "title": "Прогресс", 
            "url": "https://coffeemap.ru/progress/", 
            "time": "ПН–ПТ: 8:30–23:00, СБ–ВС: 11:00–23:00", 
            "note": "", 
            "address": "Ул. Садовая-Триумфальная, 4/10", 
            "lat": 55.770824278155786, 
            "lng": 37.599982849212665, 
            "id": 635
        }, 
        {
            "title": "Прогресс", 
            "url": "https://coffeemap.ru/progress/", 
            "time": "ПН–ВС: 11:00–00:00", 
            "note": "", 
            "address": "Волоколамское ш., 1", 
            "lat": 55.8065116, 
            "lng": 37.50466860000006, 
            "id": 636
        }, 
        {
            "title": "Прогресс", 
            "url": "https://coffeemap.ru/progress/", 
            "time": "ПН–ВС: 11:00–00:00", 
            "note": "", 
            "address": "Фрунзенская набережная, 30/5", 
            "lat": 55.7250773, 
            "lng": 37.58272420000003, 
            "id": 637
        }, 
        {
            "title": "Прогресс", 
            "url": "https://coffeemap.ru/progress/", 
            "time": "ПН-ВС: 11:00-23:00", 
            "note": "https://www.instagram.com/progresscoffeecraft/", 
            "address": "Ул. Гиляровского, 68с1", 
            "lat": 55.78882489999999, 
            "lng": 37.63345819999995, 
            "id": 638
        }, 
        {
            "title": "Ранние Пташки", 
            "url": "https://coffeemap.ru/rannie-ptashki/", 
            "time": "ПН-ВС: 9:00 - 21:00", 
            "note": "https://www.instagram.com/earlybirds.coffee/", 
            "address": "Ул. 11-я Парковая, 9/35", 
            "lat": 55.791419656254746, 
            "lng": 37.80534163911966, 
            "id": 641
        }, 
        {
            "title": "Раф&Стафф", 
            "url": "https://coffeemap.ru/raf-staff/", 
            "time": "ПН-ПТ: 8:00-22:00, СБ-ВС: 9:00-22:00", 
            "note": "https://www.instagram.com/rafstaff_coffee/", 
            "address": "Каширское шоссе, 65 корпус 1", 
            "lat": 55.599438386282024, 
            "lng": 37.72489160299301, 
            "id": 643
        }, 
        {
            "title": "Ровесник", 
            "url": "https://coffeemap.ru/rovesnik/", 
            "time": "ПН-ЧТ: 09:00-01:00, ПТ-СБ: 9:00-06:00, ВС: 09:00-01:00", 
            "note": "https://www.instagram.com/rovesnik.bar/", 
            "address": "Малый Гнездниковский переулок, 9с2", 
            "lat": 55.7624118, 
            "lng": 37.6059109, 
            "id": 645
        }, 
        {
            "title": "Розетка и кофе", 
            "url": "https://coffeemap.ru/hygge-kofejnya-rozetka-i-kofe/", 
            "time": "ПН–ПТ: 8:30–22:00, СБ–ВС: 10:00–22:00", 
            "note": "https://www.instagram.com/rozetkaicoffee_pokrovka17", 
            "address": "Ул. Покровка, 17с1", 
            "lat": 55.7595493, 
            "lng": 37.6455545, 
            "id": 646
        }, 
        {
            "title": "Роко Бэй (Мох и кофе)", 
            "url": "https://coffeemap.ru/moh-i-kofe-roco-bay/", 
            "time": "ПН-ВС: 08:00 - 20:00", 
            "note": "", 
            "address": "Бульвар Маршала Рокоссовского, 6к1Б", 
            "lat": 55.81059365874276, 
            "lng": 37.72639364004135, 
            "id": 647
        }, 
        {
            "title": "Роко Бэй (Мох и кофе)", 
            "url": "https://coffeemap.ru/moh-i-kofe-roco-bay/", 
            "time": "ПН-ВС: 8:00-20:00", 
            "note": "https://www.instagram.com/roco_bay/", 
            "address": "Ул. Донецкая, 34к1", 
            "lat": 55.6453527, 
            "lng": 37.703333, 
            "id": 648
        }, 
        {
            "title": "Салют", 
            "url": "https://coffeemap.ru/salyut/", 
            "time": "ПН-ВС: 8:00-23:00", 
            "note": "https://www.instagram.com/salutecoffee/", 
            "address": "Страстной бульвар, 12с5", 
            "lat": 55.7669240068506, 
            "lng": 37.612389707557895, 
            "id": 649
        }, 
        {
            "title": "Свежий номер", 
            "url": "https://coffeemap.ru/svezhij-nomer/", 
            "time": "ПН–ПТ: 8:00–22:00, СБ–ВС: 10:00–22:00", 
            "note": "https://www.instagram.com/svezhiynomer/", 
            "address": "Кронштадтский б-р, 6к5", 
            "lat": 55.84060729999999, 
            "lng": 37.49379109999995, 
            "id": 651
        }, 
        {
            "title": "Своя жизнь", 
            "url": "https://coffeemap.ru/svoya-zhizn/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/coffee.food.mitino", 
            "address": "Ул. Барышиха, 14", 
            "lat": 55.8409882, 
            "lng": 37.3575692, 
            "id": 652
        }, 
        {
            "title": "Северяне", 
            "url": "https://coffeemap.ru/severyane/", 
            "time": "ПН-ВС: 9:00–00:00", 
            "note": "https://www.instagram.com/severyane.moscow/", 
            "address": "Ул. Большая Никитская, 12", 
            "lat": 55.75648818905385, 
            "lng": 37.60649893981167, 
            "id": 654
        }, 
        {
            "title": "Синкопа", 
            "url": "https://coffeemap.ru/kofejnya-sinkopa/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 09:00-21:00", 
            "note": "", 
            "address": "Ул. Марксистская, 34к8", 
            "lat": 55.73471296771671, 
            "lng": 37.664704187566485, 
            "id": 655
        }, 
        {
            "title": "Синкопа", 
            "url": "https://coffeemap.ru/kofejnya-sinkopa/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 09:00-21:00", 
            "note": "", 
            "address": "Ул. Вавилова, 17", 
            "lat": 55.70184995974699, 
            "lng": 37.580591885913805, 
            "id": 656
        }, 
        {
            "title": "Синкопа", 
            "url": "https://coffeemap.ru/kofejnya-sinkopa/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 09:00-21:00", 
            "note": "", 
            "address": "Ул. Верхняя Красносельская, 10", 
            "lat": 55.784225, 
            "lng": 37.66106300000001, 
            "id": 657
        }, 
        {
            "title": "Синкопа", 
            "url": "https://coffeemap.ru/kofejnya-sinkopa/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 09:00-21:00", 
            "note": "", 
            "address": "Ул. Новоостаповская, 6Б", 
            "lat": 55.71964149999999, 
            "lng": 37.66996990000007, 
            "id": 658
        }, 
        {
            "title": "Синкопа", 
            "url": "https://coffeemap.ru/kofejnya-sinkopa/", 
            "time": "ПН-ПТ: 8:00-21:00, СБ-ВС: 9:00-21:00", 
            "note": "https://www.instagram.com/syncopecoffee/", 
            "address": "Волгоградский проспект, 16", 
            "lat": 55.728949228262344, 
            "lng": 37.67573746627046, 
            "id": 659
        }, 
        {
            "title": "Скворец", 
            "url": "https://coffeemap.ru/skvorets/", 
            "time": "ПН-ПТ: 9:00-22:00, СБ-ВС: 11:00-22:00", 
            "note": "https://www.instagram.com/skvoretzdiner/", 
            "address": "Ул. Малая Бронная, 4", 
            "lat": 55.759562018380954, 
            "lng": 37.597372340475474, 
            "id": 660
        }, 
        {
            "title": "Сначала сюда", 
            "url": "https://coffeemap.ru/snachala-syuda/", 
            "time": "ПН-ВС: 12:00 - 22:00", 
            "note": "https://www.instagram.com/snachala_suda/", 
            "address": "Ул.Солянка, 1/2с2", 
            "lat": 55.7546161, 
            "lng": 37.638502, 
            "id": 664
        }, 
        {
            "title": "Сойка Напела", 
            "url": "https://coffeemap.ru/sojka-napela/", 
            "time": "ПН-ПТ: 08:00 - 23:00, СБ-ВС: 10:00-23:00", 
            "note": "www.instagram.com/soyka.napela", 
            "address": "Ул. Красная Пресня, 36с1", 
            "lat": 55.76248675438584, 
            "lng": 37.56694139175568, 
            "id": 665
        }, 
        {
            "title": "Соседи.Кофе", 
            "url": "https://coffeemap.ru/sosedi-kofe/", 
            "time": "ПН-ПТ: 7:30-22:00, СБ-ВС: 9:00-21:00", 
            "note": "https://instagram.com/sosedi_coffee", 
            "address": "Ул. Видная, 3", 
            "lat": 55.84144329999999, 
            "lng": 37.34595779999999, 
            "id": 667
        }, 
        {
            "title": "СПЕШИLOVE PLACE•ART•COFFEE", 
            "url": "https://coffeemap.ru/speshilove-place-art-coffee/", 
            "time": "ПН-ПТ: 08:00-22:00, СБ-ВС: 10:00-22:00", 
            "note": "https://www.instagram.com/speshilove_/", 
            "address": "Ул. Земляной Вал, 52/16с1", 
            "lat": 55.74922309999999, 
            "lng": 37.6552586, 
            "id": 670
        }, 
        {
            "title": "Табера", 
            "url": "https://coffeemap.ru/tabera/", 
            "time": "ПН-ПТ: 10:00-19:00, СБ-ВС: 10:00-18:00", 
            "note": "https://www.instagram.com/taberacoffee/", 
            "address": "Большой Сухаревский переулок д.15, стр.1", 
            "lat": 55.7708075, 
            "lng": 37.62853919999998, 
            "id": 672
        }, 
        {
            "title": "Так сказала моя мама", 
            "url": "https://coffeemap.ru/tak-skazala-moya-mama/", 
            "time": "ПН-ВС: 9:00-20:00", 
            "note": "https://www.instagram.com/tsmmcoffee/", 
            "address": "Большой Симоновский переулок, 2", 
            "lat": 55.7282175, 
            "lng": 37.6726549, 
            "id": 673
        }, 
        {
            "title": "Территория Кофе", 
            "url": "https://coffeemap.ru/territoriya-kofe/", 
            "time": "ПН-ВС: 10:00-21:00", 
            "note": "https://www.instagram.com/coffeestate.ru/", 
            "address": "Ул. Правды, 17/19", 
            "lat": 55.786993, 
            "lng": 37.579440999999974, 
            "id": 674
        }, 
        {
            "title": "Тинто", 
            "url": "https://coffeemap.ru/tinto/", 
            "time": "ПН-ВС: 9:00 - 24:00", 
            "note": "https://instagram.com/_tinto_coffee_", 
            "address": "Большой Казëнный переулок, 1/2 стр. 1", 
            "lat": 55.759960018350164, 
            "lng": 37.6526642956314, 
            "id": 675
        }, 
        {
            "title": "Тираж", 
            "url": "https://coffeemap.ru/tirazh/", 
            "time": "ПН: выходной, ВТ-ВС: 11:00-20:00", 
            "note": "https://www.instagram.com/zinecafe_tirage/", 
            "address": "Ул. Новопесчаная, 23к7", 
            "lat": 55.79292299999999, 
            "lng": 37.513093, 
            "id": 676
        }, 
        {
            "title": "Циники", 
            "url": "https://coffeemap.ru/tsiniki/", 
            "time": "ПН-ПТ: 8:00-23:00, СБ-ВС: 10:00-23:00", 
            "note": "https://www.instagram.com/cynic_vegan/", 
            "address": "Богословский пер., 8/15с1", 
            "lat": 55.7625609, 
            "lng": 37.59955609999997, 
            "id": 685
        }, 
        {
            "title": "Человек и Пароход", 
            "url": "https://coffeemap.ru/chelovek-i-parohod/", 
            "time": "ПН-ВС: 8:00–21:00", 
            "note": "", 
            "address": "Ул. Мытная, 74", 
            "lat": 55.71194832372832, 
            "lng": 37.62051425396726, 
            "id": 686
        }, 
        {
            "title": "Человек и Пароход", 
            "url": "https://coffeemap.ru/chelovek-i-parohod/", 
            "time": "ПН-ВС: 8:00-21:00", 
            "note": "", 
            "address": "Ул. Триумфальная площадь 4", 
            "lat": 55.7698059563308, 
            "lng": 37.5954523471172, 
            "id": 687
        }, 
        {
            "title": "Черный", 
            "url": "https://coffeemap.ru/chernyj/", 
            "time": "ПН - ПТ: 9:00 - 21:00, СБ - ВС 10:00 - 23:00", 
            "note": "", 
            "address": "Ул. Льва Толстого, 20", 
            "lat": 55.735312164673, 
            "lng": 37.585091671758285, 
            "id": 689
        }, 
        {
            "title": "Черный", 
            "url": "https://coffeemap.ru/chernyj/", 
            "time": "ПН - ЧТ: 10:00 - 22:00, ПТ - СБ: 10:00 - 23:00, ВС: 10:00 - 22:00", 
            "note": "https://www.instagram.com/cherniy_coffee/", 
            "address": "Ленинградский проспект, 70, Eat Market Алкон", 
            "lat": 55.80516, 
            "lng": 37.5222399, 
            "id": 690
        }, 
        {
            "title": "Школьник Кофе", 
            "url": "https://coffeemap.ru/shkolnik-kofe/", 
            "time": "ПН-ПТ: 8:30-22:00, СБ-ВС: 9:30-22:00", 
            "note": "https://www.instagram.com/shkolnikcoffee/", 
            "address": "Ул. Земляной Вал, 12/7с1 ", 
            "lat": 55.761769, 
            "lng": 37.656631999999945, 
            "id": 691
        }, 
        {
            "title": "Эклерная Клер", 
            "url": "https://coffeemap.ru/eklernaya-kler/", 
            "time": "ПН–ВС: 9:00–21:00", 
            "note": "", 
            "address": "Ул. Сретенка, 26/1", 
            "lat": 55.7704964, 
            "lng": 37.63316199999997, 
            "id": 693
        }, 
        {
            "title": "Эклерная Клер", 
            "url": "https://coffeemap.ru/eklernaya-kler/", 
            "time": "ПН-ВС: 8:00-21:00", 
            "note": "https://www.instagram.com/eklernayakler/", 
            "address": "Ул. Спартаковская, 16", 
            "lat": 55.7724907171968, 
            "lng": 37.675997614860535, 
            "id": 694
        }, 
        {
            "title": "ЭРНА", 
            "url": "https://coffeemap.ru/erna/", 
            "time": "ПН: 8:00-19:30, ВТ-ПТ: 8:00-21:00, СБ-ВС: 9:30-21:00", 
            "note": "https://www.instagram.com/erna.coffee/", 
            "address": "Ул. Большая Полянка, 44", 
            "lat": 55.732910901351076, 
            "lng": 37.61831646014932, 
            "id": 695
        }
]

api = overpy.Overpass()
mindist = 100000000000000

print("Введите имя станции:")
metrostation=input()

askcoords=f"""
node["railway"="station"]["station"="subway"][name="{metrostation}"];
out;"""

mcoords=api.query(askcoords)      

metrolat=mcoords.nodes[0].lat
metrolng=mcoords.nodes[0].lon     
      
     
for i in range(495):
	dlon = places[i]["lng"] - float(metrolng)
	dlat = places[i]["lat"] - float(metrolat)
	a = (math.sin(dlat/2))**2 + math.cos(float(metrolat)) * math.cos(places[i]["lat"]) * (math.sin(dlon/2))**2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = 6371 * c * 1000
	if d<mindist:
		mindist=d
		minx=i
		minlat=places[i]["lat"]
		minlng=places[i]["lng"]
	
print(end="\n")	
print("Вот ближайшая кофейня:")
print(end="\n")
print(places[minx]["title"])
print(places[minx]["address"])
