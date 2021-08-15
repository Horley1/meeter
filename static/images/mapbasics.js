function init () {
    /**
     * Создаем мультимаршрут.
     * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/multiRouter.MultiRoute.xml
     */
    var multiRoute = new ymaps.multiRouter.MultiRoute({
        referencePoints: [
            '{{a}}',
            '{{address}}',
            '{{b}}'
        ],
        params: {
            routingMode: 'masstransit'
        }
    }, {
        // Автоматически устанавливать границы карты так, чтобы маршрут был виден целиком.
        boundsAutoApply: true
    });
    var myMap = new ymaps.Map('map', {
            center: [55.751574, 37.573856],
            zoom: 11,
            controls: ["zoomControl", "fullscreenControl"]
        }, {
            searchControlProvider: 'yandex#search'
        }),

        // Создаём макет содержимого.
        MyIconContentLayout = ymaps.templateLayoutFactory.createClass(
            '<div style="color: #FFFFFF; font-weight: bold;">$[properties.iconContent]</div>'
        ),
        myPlacemark3 = new ymaps.Placemark([55.769504, 37.609047], {
            hintContent: 'Собственный значок метки',
            balloonContent: 'Это красивая метка'
        }, {
            // Опции.
            // Необходимо указать данный тип макета.
            iconLayout: 'default#image',
            // Своё изображение иконки метки.
            iconImageHref: 'static/images/cafe.png',
            // Размеры метки.
            iconImageSize: [40, 40],
            // Смещение левого верхнего угла иконки относительно
            // её "ножки" (точки привязки).
            iconImageOffset: [10, -40]
        });



    // Добавляем мультимаршрут на карту.
    myMap.geoObjects
            .add(myPlacemark3)
            .add(multiRoute);



}

ymaps.ready(init);
