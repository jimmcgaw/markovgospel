
import pickle

f = open('Gospels.txt', 'r')
lines = []
for line in f:
  lines.append(line.replace('\n', ' '))
# bible = ' '.join( bible.split('\n') )
# bible = bible.replace('\\n', ' ')
# 
# print lines
bible = ' '.join(lines)
print bible
