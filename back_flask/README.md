# FLASK + REST

## activate VENV
```bash
$ . ./init.sh
```
## stop VENV
```bash
$ deactivate
```

### Structure backend
```
src
 |-- bp_component   # нициализации/подключения
 |-- models         # база данных
 |-- static         # статические данные
 |-- lib            # подключения библиотек
 |-- config         # глобальные параметры
 |-- data           # данные подгружаемые в процессе работы + логи
 |-- data           # данные подгружаемые в процессе работы + логи
 |-- utils          # скрипты
 |__ ...
```