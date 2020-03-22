# geo details

import phonenumbers												#Import phonenumbers module
from phonenumbers import geocoder								#import geocoder from phonenumbers module

number=input("Enter the phone number to check location: ")		#store user input phone number in number variable
ch_num=phonenumbers.parse(number,'CH')							#create another variable and store the parsed phone number in that variable

print(geocoder.description_for_number(ch_num,"en"))				#print the geography detail using function geocoder.descriptionfornumber

# Carrier details

from phonenumbers import carrier 								#import carrier module from phonenumbers
s_num=phonenumbers.parse(number,'RO')							#in a variable, parse the phone number and store it in the variable
print(carrier.name_for_number(s_num,"en"))						#print the carrier detail using function carrier.namefornumber
