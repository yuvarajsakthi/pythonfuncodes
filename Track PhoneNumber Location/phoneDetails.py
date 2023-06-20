import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# getting input from user
phone = input("Enter Phone Number with Country Code:")
phone_number = phonenumbers.parse(phone)

# to know the country name
country_name = geocoder.description_for_number(phone_number, 'en')

service_provider = carrier.name_for_number(phone_number, 'en')

# to know the timezone
time_zone = timezone.time_zones_for_number(phone_number)

print("Country Name:", country_name)
print("Service Provider:", service_provider)
print("Time Zone:", time_zone)
