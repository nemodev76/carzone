@echo off

call "Del Cache.cmd"

py manage.py makemigrations
py manage.py migrate

pause