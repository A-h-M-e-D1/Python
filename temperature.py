#Convert Temperatures

def convert_cel_to_far():
    """
    Return degrees Celsius To Fahrenheit
    """
    degree_celsius=int(input("Enter a temperature in degrees F: "))
    F=float(degree_celsius * 9 / 5 + 32)
    return f"{degree_celsius} degress F ={F} degrees C"
print(convert_cel_to_far())
