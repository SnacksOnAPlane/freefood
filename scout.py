from bs4 import BeautifulSoup
import requests
import smtplib
import json

with open('creds.json') as data_file:
  data = json.load(data_file)
  user = data['user']
  passwd = data['pass']
url = 'https://postmates.com/atlanta'

webpage = requests.get(url)
soup = BeautifulSoup(webpage.text, 'html.parser')


free_food = [s for s in soup.body.stripped_strings if 'free' in s.lower()]

if free_food:
  smtp = smtplib.SMTP("email-smtp.us-east-1.amazonaws.com")
  smtp.starttls()
  smtp.login(user, passwd)
  body = 'Free Postmates!\n\n' + '\n'.join(free_food)
  smtp.sendmail("freefood@hotdonuts.info", "rsmiley@gmail.com", body)
