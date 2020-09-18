import phonenumbers
from phonenumbers import geocoder 
from phonenumbers import carrier
from phonenumbers import phonemetadata

phone_number=phonenumbers.parse('+919392272652')

print(geocoder.description_for_number(phone_number,'en'))
print(carrier.name_for_number(phone_number,'en'))
print(phonemetadata.NumberFormat(phone_number,'en'))