import os, datetime
os.chdir('.')
date = datetime.datetime.now()
today = date.strftime('%Y-%m-%d')

folders = []
for folder in os.listdir():
    folders.append(folder)
    #print(folder)
    i = 1
while True:
    if today + '_' + str(i) in folders or today in folders:
        i += 1
        date = today + '_' + str(i)
        if date in folders:
            continue
        os.mkdir(date)
        break
    else:
        os.mkdir(today)
        break
