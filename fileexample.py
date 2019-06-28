def count():

  num_words = 0
  with open("alice.txt",'r') as file1:
    for line in file1:
      words = line.split()
      num_words += len(words)
  return num_words
print("The number of words is ",count())



def count_the():
  num_the = {'the': 0}
  file2 = open("alice.txt", 'r')
  
  for word in file2.read().split():
    if word == "a":
      num_the['the'] += 1
  
  return num_the['the']
  
print("The number of occurances of the word the: ",count_the())



