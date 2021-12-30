import re

mails = ''' 
    sg704992@gmail.com 
    12345 
    dfhsdikfjh 
    355 
    hackingwithbhai@gmail.com 
    hacker.hell@planet.iq
'''

names = '''
        Mr. Smith
        Mrs. Teena
        Mrs. Priya
        Mr. Prem
        Mr. Balram
        Ms Anu
        Mr Alok
        Mrs. Anamika
        Mr. K
        987-117-8255
        807-676-1043
        847-008-2705
        959-970-3055
'''

urls = '''
        http://gigsforpics.co.in
        https://www.youtube.com/Rage
        ftp://fileserver.io
        smtp:34567//sendmails.in
        localhost:63026//home/desktop/file.html
'''

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(names)
for match in matches:
    print(match)
pattern2 = re.compile(r'\d{3}-\d{3}-\d{4}')
matches2 = pattern2.finditer(names)
for match in matches2:
    print(match)

pattern3 = re.compile(r'[a-zA-Z0-9.]+@[a-z]+\.[a-z]{2,4}')
matches3 = pattern3.finditer(mails)
for match in matches3:
    print(match)

pattern4 = re.compile(r'(http|https|ftp|smtp|localhost):[0-9]*//[w]?[a-zA-Z0-9./]+[a-z/]+')
matches4 = pattern4.finditer(urls)
for match in matches4:
    print(match)
