from bs4 import BeautifulSoup as BS
import requests
import pickle

file = open('cocktails.csv', 'a+')
num_cocktails = 0

for i in range(10):
    try:
        html = requests.get('http://drinkboy.com/Cocktails/Recipe.aspx?itemid={}'.format(i)).text

        bs_data = BS(html)

        ingredients = bs_data.findAll('li', {'class': 'ingredient'})

        name = bs_data.find('h2', {'class': 'name'}).text
        file.write(name)

        for ingredient in ingredients:
            measure = ingredient.find('span', {'class': 'measure'}).text
            product = ingredient.find('span', {'class': 'product'}).text
            amount = ingredient.find('span', {'class': 'amount'}).text
            file.write('\t{}:{} {}\n'.format(product, amount, measure))

        num_cocktails = num_cocktails + 1
        print('Current cocktails: {}. Cocktails so far: {}'.format(name, num_cocktails))
    except:
        pass