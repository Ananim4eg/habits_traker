# Трекер привычек
***

## Описание

"Трекер привычек" - это ***DRF*** проект для создания и отслеживания выполнения привычек,<br> вознаграждения за полезные 
привычки.

## Установка зависимостей проекта

В проекте используется виртуальное окружение ***poetry***.<br> Для установки зависимостей используйте команду 
```
poetry install
```

## Локальный запуск приложения

Локальный запуск приложения осуществляется через модуль ***manage.py*** в корне проекта.<br>
Используйте команду
```
python manage.py runserver
```

после перейдите по ссылке [habit_traker][1]

[1]: http://127.0.0.1:8000/ "Ссылка на страницу приложения"

## Docker-compose упаковка приложения
 + Для упаковки проекта в контейнеры Docker, и его последующего запуска, воспользуйтесь командой
```
docker-compose up -d --build
```

 + Для просмотра запущенных контейнеров

``` 
docker-compose ps
```

 + Для проверки логов контейнера

``` 
docker-compose logs -f <Имя контейнера>
```

 + Проверка redis. В ответ на команду в терминале должен быть ответ -PONG

``` 
docker exec -it redis redis-cli ping
```

 + Проверка celery и celery-beat. 

``` 
docker exec -it celery celery -A celery inspect active
```

## CI/CD и деплой на сервер

### Настройка GitHub Secrets

Для работы CI/CD необходимо добавить следующие секреты в настройках репозитория:
`Settings` → `Secrets and variables` → `Actions`

| Secret | Описание                                         |
|--------|--------------------------------------------------|
| `SERVER_IP` | IP-адрес вашего сервера                          |
| `SSH_USER` | Имя пользователя для SSH                         |
| `SSH_KEY` | Приватный SSH ключ для подключения               |
| `DEPLOY_DIR` | Директория для деплоя  (например /home/project/) |
| `SECRET_KEY` | Django секретный ключ                            |
| `POSTGRES_USER` | Пользователь PostgreSQL                          |
| `POSTGRES_PASSWORD` | Пароль PostgreSQL                                |
| `POSTGRES_DB` | Название базы данных                             |
| `POSTGRES_PORT` | Порт PostgreSQL (обычно 5432)                    |
| `POSTGRES_HOST` | Хост PostgreSQL (обычно db)                      |

##  Подготовка сервера

## 1. Настройка сервера

### Обновление установленных пакетов сервера

```
sudo apt update 
sudo apt upgrade
```

### Настройка портов

``` 
sudo ufw status - проверка состояния файрвола
sudo ufw enable - запуск, если выключен
sudo ufw allow 80/tcp - открыть порт 80 для доступа к приложению через веб
sudo ufw allow 443/tcp - открыть порт 443 для доступа к приложению через веб
sudo ufw allow 22/tcp - открыть порт 22 для доступа к серверу через ssh
sudo ufw status - проверка статуса файрвола
```

## 2. Установка Docker и Docker Compose

### Установка Docker

``` 
curl -fsSL https://get.docker.com -o get-docker.sh<br>
sudo sh get-docker.sh<br>
Инструкция с официального сайта -  https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository.
``` 

### Добавление пользователя в группу docker

``` 
sudo usermod -aG docker <Имя_пользователя>
``` 

### Установка Docker Compose

``` 
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose<br>
sudo chmod +x /usr/local/bin/docker-compose
``` 

### Проверка установки

``` 
docker --version<br>
docker-compose --version
``` 

## 3. Создание структуры директорий

### Создание директории для проекта

``` 
mkdir -p DEPLOY_DIR/habit_traker
``` 

## 4. Настройка .env файла

### Создайте файл с переменными окружения

``` 
nano DEPLOY_DIR/.env.habits
``` 

### Добавьте в него

``` 
Заполните его в соответствии с .env.example
``` 
