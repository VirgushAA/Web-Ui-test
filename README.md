
# Web Ui tests pack
    некоторые тесты с pytest и playwright, знакомство с тестированием сайтов

## Requirements

Python 3.10

Playwright

Allure

## Installation

pip install -r requirements.txt

playwright install

## Run tests

pytest --alluredir=allure-results

## Run in Docker

docker build -t effective-tests .

docker run -it effective-tests

## Known Issues
