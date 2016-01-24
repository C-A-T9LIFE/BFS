while True:
    import requests
    import winsound         # for sound :)
    from itertools import product
    for i, item in enumerate(product('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_',repeat=4)): # перебираемые символы и их количество 
     s = (str("http://www."+''.join(item)+ '.jpg' )) #адрес сайта и расширение файла
     r = requests.head(s)
     print (str((r.status_code))+s)
     if r.status_code == 200:
      my_file = open('file.txt', 'a')
      my_file.write(str((r.status_code))+s)
      my_file.close()
      winsound.Beep(300, 500)
      winsound.Beep(300, 500)
      winsound.Beep(300, 500)
      winsound.Beep(500, 500)
      winsound.Beep(350, 250)
      winsound.Beep(300, 500)
      winsound.Beep(500, 500)
      winsound.Beep(350, 250)
      winsound.Beep(300, 500)
      exit()
