def convert(any_string):
    any_string = any_string.replace(":)","🙂")
    any_string = any_string.replace(":(","🙁")
    return any_string

def main():
    entered = input("")
    return convert(entered)
    

print(main())