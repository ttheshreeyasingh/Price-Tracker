import time
import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

email_id = 'rgoel7394@gmail.com'
email_pass = 'Shreeya@123'
# set the headers and user string
headers = {
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0"
}

# send a request to fetch HTML of the page
response = requests.get('https://www.amazon.in/Bose-Comfort-Wireless-Headphone-Silver/dp/B0756GB78C', headers=headers)

# create the soup object
soup = BeautifulSoup(response.content, 'html.parser')

# change the encoding to utf-8
soup.encode('utf-8')

#print(soup.prettify())

# function to check if the price has dropped below a certain amount
def check_price():
  title = soup.find(id= "productTitle").get_text()
  price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
  #print(price)

  #converting the string amount to float
  converted_price = float(price[0:5])
  print(converted_price)
  if(converted_price < 30000):
    send_mail()

  #using strip to remove extra spaces in the title
  # print(title.strip())

# function that sends an email if the prices fell down
def send_mail():
  msg = EmailMessage()
  msg['Subject']  = "price has dropped !!"
  msg['From'] = email_id
  msg['To'] = "singhshreeya29@gmail.com"
  msg.set_content("Hey check this amazon link : https://www.amazon.in/Bose-Comfort-Wireless-Headphone-Silver/dp/B0756GB78C")

  with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)

while True:
  check_price()
  time.sleep(60 * 60)
#loop that allows the program to regularly check for prices
# while(True):
#   check_price()
