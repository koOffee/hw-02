## Решение задачи детекции штрихкодов на фото

### Датасет

Размеченная доступная выборка содержит 481 изображение с различными разрешениями
Посмотреть датасет можно [здесь](https://disk.yandex.ru/d/pRFNuxLQUZcDDg).

Посмотреть что там внутри можно в [тетрадке](notebooks/DataExplore.ipynb).
### Подготовка пайплайна

1. Создание и активация окружения
    ```
    python3 -m venv /path/to/new/virtual/environment
    ```
    ```
    source /path/to/new/virtual/environment/bin/activate
    ```

2. Основные рецепты

    Установка зависимостей:
    ```
    make install
    ```
   Установка dev зависимостей
   ```
   make install_dev
   ```
   Линтеры
   ```
   make lint
   ```
   Проверки перед commit push
   ```
   make pre_push_test
   ```

3. Настраиваем [config.yaml](configs/config.yaml) под себя.
В `data_config.data_path`, нужно указать папку куда скачали датасет из п. Датасет.

### Обучение

Запуск тренировки:

```
make train
```

### Инференс

Посмотреть результаты работы обученной сети можно в [тетрадке](notebooks/inference.ipynb).


### TODO
Текущий BEST - [ClearML](https://app.clear.ml/projects/95002e4a916d47e4b681cd502a639cbe/experiments/9862f8f4125647c3bc88466ebe321467/output/execution)

Что ещё можно попробовать:

1. Взвесить BCELoss (веса есть в файлике с DataExplore)
2. Заменить лосс на Focall
3. Покрутить ауги, подумать что сделать с миноритарными классами
