#!/bin/sh
#*************************************************************
#* Welcome to Django folder and files readiness script Part #1
#* Created by Chia Tham. 
#* 2018.02.10. Free. No Warranty. Used As Is.
#* 
#* V1.00 - Initial 
#*************************************************************
clear
echo "*************************************************************"
#******************************
echo ">python manage.py makemigrations"
python manage.py makemigrations 
echo "*************************************************************"
#******************************
echo ">python manage.py migrate"
python manage.py migrate 
echo "*************************************************************"