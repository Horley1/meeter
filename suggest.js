ymaps.ready(init);

function init() {
    // Создаем выпадающую панель с поисковыми подсказками и прикрепляем ее к HTML-элементу по его id.
    var suggestView1 = new ymaps.SuggestView('suggest1', {provider: "yandex#map", results: 4, boundedBy: [[37.127149, 55.513034], [38.034596, 55.990945]]});
}
