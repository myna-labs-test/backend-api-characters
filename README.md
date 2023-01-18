# Character API 
Репозиторий содержащий сервис генерирующий ответы на сообщения и TTS. 
## Требования для установки
- `Make` версии 4.4 и выше
- `Python` версии 3.10 и выше
- `Poetry` версии 1.3.1 и выше
- (Опционально)`Docker` версии 20.10.22 и выше
## Подготовка к запуску
### Заполнение .env
Необходимо создать в корневой папке проекта файл `.env` с переменными окружения.
Пример заполнения:
```shell
DEBUG=True
FASTAPI_PORT=8001
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_NAME=myna_labs_test
DB_HOST=postgresql
```
### Установка зависимостей
Для локального запуска:
```shell
make prepare
```
Для запуска в докере:
```shell
make build
```
## Запуск
### Запуск в докере
```shell
make run-docker
```
### Локальный запуск
```shell
make run
```