def convert(number):
    sounds = {3:"Pling", 5:"Plang", 7:"Plong"}
    output = ""
    for i in [3,5,7]:
        if number % i == 0:
            output += sounds[i]
    if output != "":
        return output
    else:
        return str(number)