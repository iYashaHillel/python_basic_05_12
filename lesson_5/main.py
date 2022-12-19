# import re
#
# name = 'Petr'
#
# print( 'Hello ' + 'world' )
# print( 'Hello' * 3 )
# print( f'Hello {name}' )
# email_pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
# email = 'admin@admin.ua'
#
# print( bool(re.match(email_pattern, email)) )

# _one = 0x01
# bin_one = 0b01
# 0b00 = 0
# 0b01 = 1
# 0b10 = 2
# 0b11 = 3
# 0b100 = 4
# 0b101 = 5
# 0b110 = 6
# 0b111 = 7
# 0b1000 = 8
# 9999 = 0b10011100001111

# print( bin(8) )
# print( hex(199) )
# print( hex(id('Test')) )
# print( bin_one )

# print( b'...' )
# 'AB' = '65_66' => bin(65) + bin(66) => 0b1000001 + 0b1000010
# 0b1000011 = 67 = 'C'

# byte_str = 'Hello world'.encode('utf-8')
# print( byte_str.decode('cp1256') )

# name = 'Petr'
# print( name.encode('utf-8') )

# text = 'Hello world'
# sub_str = 'Hello'

# print( sub_str in text )
# number = input('Enter your digit: ')
# if number.isdigit():
#    number = int(number)
#    print(number)
# else:
#    print(f'Error! {number} is not a number')
# print( '123a'.isdigit() )

# url = 'https://domain.com'
#
# print( url.startswith('https://') )
# print( url.endswith('.com') )

# index = text.index(sub_str)
#
# if index != -1:
#    print(f'Found at {index} position')
# else:
#    print('Not found')

# print('l', 'd')
# print( text[-2], text[-1],  )
# print( len(text) )
# print( text[0], text[1], text[2], text[3], text[-11] )
# [от:до:шаг]
# [от:до]
# print( text[:] )

text = 'Hello  Pet2r!'
has_digit = False

for char in text:
   print(char)
   if char.isdigit():
      has_digit = True
      break

if has_digit:
   print('+')
else:
   print('-')
