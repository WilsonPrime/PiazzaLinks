import re


f = open('links.txt','r')

string = f.read()


parser = re.findall("https://youtu.be/\w{11}",string)


new_file = open("linsktovideos.txt", 'w')

for links in parser:
    new_file.write(f"{links}\n")
