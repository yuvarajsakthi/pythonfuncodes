from barcode import EAN13
# importing imagewritter to generate an image file
from barcode.writer import ImageWritter

number = '5896548554234'

generated_barcode = EAN13(number, writer=ImageWritter())
generated_barcode.save("bar-code")
