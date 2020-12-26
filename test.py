import converters

c1 = converters.ScaleConverter('inches', 'mm', 25)
print(c1.description())
print("coverting 2 inches")
print(str(c1.convert(2)) + c1.units_to)