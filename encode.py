str="this is string example..wow";
str=str.encode('base64','strict');
print("encoded string:"+str)
print("decoded string:"+str.decode('base64','string'))