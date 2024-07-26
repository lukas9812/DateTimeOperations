print("<-- Celcius to Fahrenheit convertor -->")

user_input_celsius = float(input("Enter °C value to convert:"))


def celsius_to_fahrenheit(user_input_celsius):
    f = (9 / 5) * user_input_celsius + 32
    return f


fahrenheit_value = celsius_to_fahrenheit(user_input_celsius)

output = "{} °C is {} °F".format(user_input_celsius, fahrenheit_value)
print(output)
