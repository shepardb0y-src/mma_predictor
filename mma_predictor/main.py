from django.shortcuts import render

# Create your views here.
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://wwww.tapology.com")
