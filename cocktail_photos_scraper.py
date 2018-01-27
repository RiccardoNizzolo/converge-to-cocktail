from bs4 import BeautifulSoup
import requests
import codecs

with codecs.open('cocktails_photos.csv', 'w', encoding='utf-8') as file:
    num_cocktails = 0
    for i in range(300):
        try:
            html = requests.get('http://drinkboy.com/Cocktails/Recipe.aspx?itemid={}'.format(i)).text

            bs_data = BeautifulSoup(html, 'lxml')

            name = bs_data.find('h2', {'class': 'name'}).text
            description = bs_data.find('span', {'class': 'description'}).text
            description = description.replace('\n', '')
            description = description.replace('\r', '')
            garnish = bs_data.find('div', {'class': 'garnish'})
            garnish = garnish.text if garnish != None else ''

            instructions = bs_data.find('div', {'class': 'instructions'})
            instructions = instructions.text if instructions != None else ''
            instructions = instructions.replace('\n', '')
            instructions = instructions.replace('\r', '')
            recipe = bs_data.find('div', {'class': 'hrecipe'})
            image_url = recipe.find('img', {'class': 'u-photo'})['src']


            file.write('{};-{};-{};-{};-{};-{}'.format(i, name, description, garnish, instructions, image_url))
            file.write('\n')

            print('{}. Name: {}, Image: {}'.format(i, name, image_url))
        except:
            pass