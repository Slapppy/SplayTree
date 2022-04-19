# Splay-дерево
## Суть
Расширенные деревья — это самонастраивающиеся бинарные деревья поиска, т. е. они корректируют свои узлы после доступа к ним. Таким образом, после поиска, вставки или удаления узла дерево будет скорректировано.
## Инструкция
В файле SplayTree.py находиться реализация splay-дерева.
В папке benchmark содержаться тесты методов добавления и удаления и поиска и датасеты для теста, а в папке result 
содержатся результы скорости выполнения методов.
##Как создать дерево?
Cоздаем обьект класса SplayTree и Node.
Вызываем метод insert для добавления, метод search для поиска и delete для удаления.
Также есть метод splay для поднятия ноды в корень дерева.