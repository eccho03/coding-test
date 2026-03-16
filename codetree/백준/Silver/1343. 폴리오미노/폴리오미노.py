poly1 = "AAAA"
poly2 = "BB"

input1 = "XXXX"
input2 = "XX"

input = input()

if input1 in input:
    input = input.replace(input1, poly1)
    if input2 in input:
        input = input.replace(input2, poly2)
if input2 in input:
    input = input.replace(input2, poly2)

#-------------------------------------------
if ('X' in input):
    print("-1")

else:
    print(input)