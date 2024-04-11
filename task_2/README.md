В файле _test.py представлен тест - функция "test_screenshot", которая делает скриншоты отдельных элементов на 
веб-странице:https://www.avito.ru/avito-care/eco-impact. Изначально в декораторе функции в параметры заданы элементы 
'.desktop-content-HDB3N' и '.desktop-impact-items-F7T6E', которые соответсвуют тест кейсам с ID eco-impact-1 и eco-impact-2
При желании с помощью это функции можно получить скриншот любого элемента, нужно только добавить класс этого элемента в параметры,
например:
@pytest.mark.parametrize(('element', 'screenshot_name'), [('.desktop-content-HDB3N', 'eco-impact-1'), ('.desktop-impact-items-F7T6E', 'eco-impact-2'), ('.desktop-impact-item-eeQO3', 'eco-impact-3')])

В данном примере eco-impact-3 это ID вашего тест кейса, а '.desktop-impact-item-eeQO3' - класс элемента DOM дерева страницы - https://www.avito.ru/avito-care/eco-impact

