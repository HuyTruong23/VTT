import base64

#Taking input through the terminal.
welcomeInput= raw_input("Enter 1 to convert String to Base64, 2 to convert Base64 to String: ") 


    #Code to Convert String to Base 64.
if int(welcomeInput)==1:
    inputString= raw_input("Enter the String to be converted to Base64: ") 
    base64Value = base64.b64encode(inputString.encode())
    print "Base64 Value = " + base64Value
    #Code to Convert Base 64 to String.
elif int(welcomeInput)==2:
    inputString= raw_input("Enter the Base64 value to be converted to String:  ") 
    stringValue = base64.b64decode(inputString).decode('utf-8')
    print "Base64 Value = " + stringValue
    