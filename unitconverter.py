#python program for weight converter)

try:
    #input the weight
    value=float(input('enter the value:'))
    
    #choose the conversion
    unit=input('Choose conversion direction (1 for kg to pounds, 2 for pounds to kg):')

    #converting kilograms to pounds
    if unit == '1':
        pounds=value*2.20462
        print(f'{value}kgs is equal to {pounds}lbs.')

    #converting pounds to kilograms
    elif unit == '2':
            kilograms=value/2.20462
            print(f'{value}lbs is equal to {kilograms}kgs.')
            
    else:
        print(f'{unit} is not a vaild option')

except valueError:
    print('Invalid input. Please enter a valid number for value.')
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    


