from bs4 import BeautifulSoup
import requests

with open('cocktails_data.csv', 'w+') as file:
    num_cocktails = 0

    for i in range(1000):
        try:
            html = requests.get('http://drinkboy.com/Cocktails/Recipe.aspx?itemid={}'.format(i)).text

            bs_data = BeautifulSoup(html, 'lxml')

            ingredients = bs_data.findAll('li', {'class': 'ingredient'})

            name = bs_data.find('h2', {'class': 'name'}).text
            file.write('{}\t'.format(name))

            for ingredient in ingredients:
                measure = ingredient.find('span', {'class': 'measure'}).text
                product = ingredient.find('span', {'class': 'product'}).text
                amount = ingredient.find('span', {'class': 'amount'}).text
                file.write('{}:{} {}'.format(product, amount, measure))
                file.write(',')

            file.write('\n')
            num_cocktails = num_cocktails + 1
            print('Current cocktail: {}. Cocktails so far: {}'.format(name, num_cocktails))
        except:
            pass