# Given  a string find the len from the start to the
# end element  Converts half of a string into upper case  and lowercase# x= “childrenareplayinplaygroud “
# range()

# x="childrenareplayinplaygroud"
# range():
# for y in x:
#    y=len(x)
# print(min(y))
# range() 

x = "childrenplayinplayground"
half_index = len(x)/2
new=""
for indx in range (len(x)):
    if indx >= half_index:
        new+=x[indx].upper()
    else:
         new +=x[indx]
         
print(new) 



def half_captalize(sentence):
    k=len(sentence)//2
    z= sentence[:k].upper() + sentence [k:].lower()
    return z
print(half_captalize("children are playing in the playgroud"))







