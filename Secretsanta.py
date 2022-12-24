import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import time

user = []

class player:
  def __init__(self, username, email):
    self.username = username
    self.email = email

pcount = int(input('how many players will be playing today?:'))
pcount1 = pcount
pcount2 = pcount
pcount3 = pcount
pcount4 = pcount

for i in range(pcount):
  name = pcount
  user.append(name)
  pcount = pcount - 1
  
print(user)

def playerinput(pcount1, user, player, pcount2):
  pcount3 = pcount1
  user1 = user
  player1 = player
  pcount21 = pcount2
  
  for i in range(pcount1):
    user[pcount1 - 1] = player(input('Enter Player Name:'), input('Enter Player Email:'))
    pcount1 = pcount1 - 1
  print('\n' * 40)
  for i in range(pcount2):
    print(user[pcount2-1].username + ' has the email of ' + user[pcount2-1].email)
    pcount2 = pcount2 - 1
  print('\n'*5)
  x = input("Is this Correct? Y?N:")
  if x != 'Y':
    playerinput(pcount3, user1, player1, pcount21)
  else:
    pass

playerinput(pcount2, user, player, pcount2)

random.shuffle(user)
random.shuffle(user)
random.shuffle(user)
random.shuffle(user)
random.shuffle(user)
random.shuffle(user)
random.shuffle(user)
random.shuffle(user)
random.shuffle(user)

print('\n' * 40)


optionalemail = input('Would you like to see who is emailed what? Y/N:')

print('\n' * 40)

if optionalemail == 'Y':
  for i in range(pcount3):
    print(user[int(pcount3) - 1].email + ' is emailed ' + user[int(pcount3) - 2].username)
    pcount3 = pcount3 - 1
else: pass

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login('username', 'password')

for i in range(pcount4):
  message = MIMEMultipart()
  message['From'] = 'username'  
  message['To'] = user[pcount4-1].email
  message['Subject'] = 'Secret Santa' + str(user[pcount4-1].username)
  message.attach(MIMEText(str('You must give a Gift to  ' + user[pcount4 - 2].username)))
  text = message.as_string()
  session.sendmail('username', user[pcount4 - 1].email, text)
  pcount4 = pcount4 - 1
  time.sleep(1)
session.quit()
