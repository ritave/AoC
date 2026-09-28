import hashlib

def leading_zeros(string):
  for index, char in enumerate(string + 'x'):
    if char != '0':
      return index
  else:
    return 0

def md5_hex(string):
  m = hashlib.md5()
  m.update(string.encode('UTF-8'))
  return m.hexdigest()

secret = input()
salt = 1

while True:
  hash = md5_hex(secret + str(salt))
  if leading_zeros(hash) >= 6:
    print(salt)
    break
  salt += 1