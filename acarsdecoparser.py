#!/usr/bin/env python
import socket, MySQLdb
from datetime import datetime

def read_line(s):
  ret = ''
  while True:
    c = s.recv(1)
    if c == '\n' or c == '':
      break
    else:
      ret += c
  return ret

TCP_IP = '127.0.0.1'
TCP_PORT = 30008
msg = []

db_host = '127.0.0.1'
db_name = 'acars'
db_user = 'acars'
db_psw = 'YourStrongPasswordGoesHere'

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((TCP_IP, TCP_PORT))

try:
  db = MySQLdb.connect(host = db_host, user = db_user, passwd = db_psw, db = db_name)
  cursor = db.cursor()
except MySQLdb.Error, e:
  print (datetime.now().strftime('%d.%m. %H:%M') + " (E) MySQL server not available.")
  print (datetime.now().strftime('%d.%m. %H:%M') + " (E) MySQL Error [%d]: %s" % (e.args[0], e.args[1]))

msg = read_line(sc)
msg = msg.split(",")

while 1:
  while len(msg) < 10:
    msg = read_line(sc)
    msg = msg.split(",")
  if len(msg)>10:
    for i in range(11,len(msg)):
      msg[10]=msg[10]+","+msg[i]
  sqlins = "insert into acars.messages (timestamp, msgfreq, mode, reg, label, blockid, msgno, flight, message) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"
  timestmp = msg[0]+" "+msg[1]
  qry = sqlins % (timestmp,msg[2],msg[3],msg[4],msg[6],msg[7],msg[8],msg[9],msg[10])
  try:
    cursor.execute(qry)
  except MySQLdb.Error, e:
    print (datetime.now().strftime('%d.%m. %H:%M') + " (W) Unsuccessful execution of query: " + qry)
    print (datetime.now().strftime('%d.%m. %H:%M') + " (W) MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
  try:
    db.commit()
  except MySQLdb.Error, e:
    print (datetime.now().strftime('%d.%m. %H:%M') + " (W) Unsuccessful commit to DB.")
    print (datetime.now().strftime('%d.%m. %H:%M') + " (W) MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
  msg = []

db.close()
cursor.close()
sc.close()
