
# Web Ui tests pack
    некоторые тесты с pytest и playwright, знакомство с тестированием сайтов

## Requirements

Python 3.13

Playwright

Allure

## Installation

pip install -r requirements.txt

playwright install

## Run tests

pytest --alluredir=allure-results

## Run in Docker

docker build -t web-tests .

docker run -it web-tests

## Known Issues
