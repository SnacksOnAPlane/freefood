from bs4 import BeautifulSoup
import requests
import json
import boto

url = 'https://postmates.com/atlanta'

webpage = requests.get(url)
soup = BeautifulSoup(webpage.text, 'html.parser')


free_food = [s for s in soup.body.stripped_strings if 'free' in s.lower()]

if free_food or True:
  conn = boto.connect_ses()
  body = 'Free Postmates!\n\n' + '\n'.join(free_food)
  conn.send_email('freefood@hotdonuts.info', 'Free Food Notice', body, 'rsmiley@gmail.com')
