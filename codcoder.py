# Codes coder for raports.
import random
# Welcome
print ("მოგესალმებით. ეს პროგრამა გთავაზობთ 7-ნიშნა კოდების შექმნას.")
print ("**************************************************************************")
print ("**************************************************************************")
print ("პირველი ორი ასო -- დედის სახელის პირველი ორი ასოა;")
print ("მეორე ორი ასო -- მამის სახელის პირველი ორი ასოა;")
print ("პირველი ციფრი -- '1'->მამაკაცი, '2'->ქალი;")
print ("ბოლო ორი ციფრი -- დაბადების წლის ბოლო ორი ციფრი;")
print ("*************************************************************************")
print ("*************************************************************************")

# Ask to enter number how many codes we wish to get
print ("რამდენი კოდის მიღება გსურთ.")
codnum = input ("შეიყვანეთ თქვენთვის სასირველი რიცხვი: ")
print ("***************")

# Arrays for codes elements
women = [
'ag', 'az', 'ai', 'al', 'an', 'ar', 'as', 'aR', 'aS',
'ba', 'be', 'bo', 'br',
'ga', 'ge', 'gv', 'gi', 'go', 'gu',
'da', 'de', 'di', 'do', 'du',
'ev', 'eT', 'ek', 'el', 'en', 'es', 'ep', 'ef', 'eS',
'va', 've', 'vi',
'za', 'ze', 'zi', 'zo',
'Ta', 'Te', 'Tv', 'Ti',
'ia', 'iv', 'iz', 'in', 'ir', 'iu',
'ka', 'ke', 'kl', 'kr',
'la', 'le', 'li', 'lo', 'lu',
'ma', 'me', 'mz', 'mT', 'mi', 'mo', 'mc',
'na', 'ne', 'ni', 'no', 'nu',
'ol',
'pa', 'pe', 'pi', 'po',
'Ja', 'Je', 'Ju',
'ra', 'ri', 'ro', 'ru',
'sa', 'se', 'sv', 'si', 'so', 'su',
'ta', 'te', 'tr', 'tu',
'ut', 'ul', 'um',
'fa', 'fe', 'fi', 'fo', 'fu',
'qa', 'qe', 'qi', 'qo', 'qr', 'qs', 
'Ra',
'ya',
'Sa', 'Sv', 'Si', 'So', 'Su',
'Ci',
'ca', 'ce', 'ci', 'co', 'cu',
'Za', 'Zi',
'xa',
'ja', 'ju'
]

men = [
'ab', 'ag', 'ad', 'av', 'az', 'aT', 'ak', 'al', 'am', 'an', 'ap', 'ar', 'as', 'af',
'ba', 'be', 'bi', 'bo', 'bu',
'ga', 'ge', 'gv', 'gi', 'gl', 'go', 'gr', 'gu',
'da', 'de', 'di', 'do', 'du',
'eg', 'ed', 'ev', 'el', 'em', 'en', 'ep', 'er', 'es', 'ef', 'eq',
'va', 've', 'vi', 'vl',
'za', 'ze', 'zv', 'zu',
'Ta', 'Te', 'To', 'Tu',
'ia', 'ig', 'ie', 'iv', 'il', 'im', 'io', 'ip', 'ir', 'is', 'iu', 'iC',
'ka', 'kv', 'ki', 'ko', 'ku',
'la', 'le', 'li', 'lo', 'lu',
'ma', 'me', 'mz', 'mi', 'mo', 'mu',
'na', 'ne', 'ni', 'no', 'nu',
'oT', 'ol', 'om', 'on', 'or', 'os', 'ot', 'oq',
'pa', 'pe', 'pi', 'pl', 'po', 'pr',
'Ja', 'Je', 'Ju',
'ra', 're', 'ri', 'ro', 'ru',
'sa', 'se', 'si', 'so', 'sp', 'st', 'su',
'ta', 'te', 'ti', 'tr', 'tu',
'un', 'ut', 'uS', 'uC',
'pa', 'pi', 'po', 'pr',
'qa', 'qv', 'qi', 'qo', 'qr', 'qu',
'Rv', 'Ru',
'ya', 'yv',
'Sa', 'Se', 'Si', 'Sm', 'So', 'Su',
'Ca', 'Ci',
'ca', 'ci', 'co', 'cq',
'Za', 'Zi',
'wa', 'wi', 'wy',
'Wa', 'Wi', 'Wo', 'Wu',
'xa', 'xv', 'xi', 'xo', 'xu',
'ja', 'je', 'jv', 'ji', 'jo', 'ju',
'ha', 'he', 'hi'
]

birthyear = ['59',
'60', '61', '62', '63', '64', '65', '66', '67', '68', '69',
'70', '71', '72', '73', '74', '75', '76', '77', '78', '79',
'80', '81', '82', '83', '84', '85', '86', '87', '88', '89',
'90', '91', '92', '93', '94', '95', '96', '97', '98', '99',
'00', '01', '02', '03', '04', '05']

# Output
for i in range(int(codnum)):
	print(random.choice(women)+random.choice(men)+'1'+random.choice(birthyear))
