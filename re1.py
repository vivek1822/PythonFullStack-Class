import re
str1 = "My name is m.vivek and i am purshing my b.tech in kl uiversity and i am a cse student and "\
      " i am intrested in doing coding and i recently completed my hackton challenge i learn lot in that challenge"\

matches1 = re.findall("is" , str1)
print(matches1)
matches2 = re.search("recently",str1)
print(matches2)
matches3=re.split(str1 , "i")
print(matches3)
matches4=re.match(str1,"intrested")
print(matches4)