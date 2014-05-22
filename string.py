
print("--------------------- (1)Test Capitalize --------------------------") #Return a copy of the string with its first character capitalized.
print("peace".capitalize())
print("LEARN".capitalize())
print("330Crescent".capitalize())
print("##$##$$@".capitalize())
print("b'eyonce".capitalize())

print("-------------------- (2)Test Center ------------------------------")
print("girl".center(15))
print("$^%*#@".center(30))
print("is this not pretty enoug'h? : ".center(75))
print("yogithebearwashere".center(-10))
print("2222".center(3))

print("-------------------- (3)Test Count ------------------------------")
print("twitter".count('i'))
print("ontamonopia".count('o')) 
print("howmanyletterscanproducethemostoutofherecanpythonhandleastringsobigitwisheditneverwas".count('e'))
print("didyouknowtheboy'whocriedworlf?".count('?'))  
print("*****".count('*'))    

print("-------------------- (4)Ends With ------------------------------")
print("doesthisendwithwhatIwantittoENDW".endswith('w'))
print("catchmeifyoucan".endswith('n'))
print("thisisprettyrad$".endswith('$'))
print("LIKEITORNOW".endswith('W'))
print("thisisgoingtobetotallywrong".endswith('r'))

print("-------------------- (5)Expands Tabs ------------------------------")
print("01\t012\t0123\t01234".expandtabs(30))
print("hello\thithere\tdoesthisworkisthiebigone?\t?".expandtabs(11))
print("1\tlookatme\rmaybe\twerk".expandtabs(45))
print("i'm\tstarting\ttothink\tthese\tare\tnot\tmy\tfav".expandtabs(2))
print("just\tdo\tit".expandtabs(100))

print("-------------------- (6)find ------------------------------")
print("linkedin".find('ed'))
print("linkedin".find('lin'))
print("magicbanners".find('nn'))
print("perezhiltonismaybeanaddiction".find('a'))
print("itonlyprintsthelast".find('the'))

print("-------------------- (6)index ------------------------------")
print("letmesee".index('e'))
print("ohcanyou^countthis".index('^'))
print("pEACelove".index('E'))
print("cat".index('c'))
print("faster".index('st'))

print("-------------------- (7)isnalum ------------------------------")
#helllo, help.
print("hey".isalnum())
print("weeee111 ".isalnum())
print("whatareyou**".isalnum())
print(" ".isalnum())
print("idontthinkicanmasterth^spelling".isalnum())

print("-------------------- (8) isalpha ------------------------------")
print("string".isalpha())
print("***".isalpha())
print("lovelyauttocrect11 ".isalpha())
print("13343".isalpha())
print(" %~`".isalpha())

print("-------------------- (9) isdigit ------------------------------")
print("111".isdigit())
print("lovely ".isdigit())
print("33%3".isdigit())
print("\\\rg".isdigit())
print("6gtr ".isdigit())

print("-------------------- (10) islower ------------------------------")
print("hellyel".islower())
print("HIELEOE".islower())
print("1243".islower())
print("@#*".islower())
print("oNe".islower())

print("-------------------- (11) isspace ------------------------------")
print(" ".isspace())
print("hello ".isspace())
print("  feet".isspace())
print(" *7".isspace())
print("read".isspace())

print("-------------------- (12) join------------------------------")
print(" ".join(['hey', 'there', 'man']))
print("  ".join(['hi', 'there','man']))
print("/".join(['hey']))
print("/".join('puppies'))
print("".join('hey'))     

print("-------------------- (13) ljust------------------------------")  
print("hitmeup".ljust(44, '8'))
print("787583".ljust(100,'6'))                                
print("beiber".ljust(100, '&'))
print("cakesarede ".ljust(44, '^'))
print('ruhroh   '.ljust(66, '*'))

print("-------------------- (14) lower------------------------------")  
print("-IU".lower())
print("arEEyouGOIng".lower())
print("$%^%$".lower())
print(" IKR".lower())
print(" sunlovefFFs".lower())

print("-------------------- (15) lstrip------------------------------")
print('www.example.com'.lstrip('cmowz.'))
print("LINKEYYYkjd".lstrip('LINKE'))
print("hellohellohello".lstrip('h'))
print("letustryrandomness".lstrip('lte'))
print(" 77jff".lstrip())

print("-------------------- (16) replace------------------------------")
print("I can't do this anymore.").replace("can't", "can")
print("yada yada yada love").replace("yada", "   peace")
print("3 * 6").replace("3 *", "4 //")
print("^664343  face").replace("  ", "<3") 
print("i love frozen yogurt").replace("frozen yogurt", "not eating cakes")

print("-------------------- (17) rfind------------------------------")
print("hello how are you doing today?").rfind("a", 0, 17)
print("ontcamponipiaacad").rfind("a", 0, 14)
print("yogurts yogurts make you gogurts").rfind("ogur", 0, 16)
print("55 garoni and cheese 55").rfind("55", 5, 15)
print("kimcheese such a cheese").rfind('ees', 0, )

print("-------------------- (18) rindex------------------------------")
##print("hey how are you").rindex("w", 0, 15 ))



print("-------------------- (19) rjust------------------------------")
print("hey how are you doing what od you like about this?").rjust(100)
print("li^^fuydf**&").rjust(299)
print(" // u fsUI HELLO").rjust(15)
print("ssoglad").rjust(400)
print("tohavefigures   this   one  out").rjust(100)

print("-------------------- (19) split------------------------------")
print("1 2 3".split())
print("1,2,3".split())
print("1,2,3".split(","))
print("               1, 2, 3".split())

print("-------------------- (20) rsplit------------------------------")
##print("Yolo, 1, 2, 3").rspilt()

print("-------------------- (21) rsstrip------------------------------")
print("hello there    .....     '").rstrip()
print("tata does this work").rstrip()
print("why do you think trails affect the page???").rstrip()
print("this def has to work      '").rstrip()
print("nearly there!!!!!! ").rstrip()

print("-------------------- (22) splitlines -----------------------------")
print("this\is\n asplit\ line").splitlines()
print("trying to figure out what you do").splitlines()
print('ah i think i may see it').splitlines()
print("88**").splitlines()
print("A").splitlines()

print("-------------------- (23) startswith -----------------------------")
print("so it just picks what i started with if i tell it to?").startswith('so')
print("ican wonder if it can pick up the first letter").startswith('i')
print("&* thants really cool").startswith('*')
print("17").startswith('17')
print("LI").startswith('I')

print("-------------------- (24) swapcase -----------------------------")
print("THiS").swapcase()
print("iiiS").swapcase()
print("17").swapcase()
print("*^%").swapcase()
print("YoU CanT saAY nO").swapcase()

print("-------------------- (25) title -----------------------------")
print("HOW WOULD MY BOOK LOOK").title()
print("7777 77 gassssy").title()
print("Can't you see i don't waNt to gO").title()
print("the book of pooh").title()
print("&&^ hush pupps").title()

print("-------------------- (26) upper -----------------------------")
print("hello friends").upper()
print("UPPER IS A COOL FUNCTION").upper()
print("whereevertHereisaWill").upper()
print("can't").upper()
print("77 &6 / ;pea").upper()

print("-------------------- (27) isnumeric -----------------------------")
print("isthis numeric or what<").isnumeric()
print(" 77 ").isnumeric()
print("Yolo be yogurtlow8*8888").isnumeric()
print("&").isnumeric()
print("  8").isnumeric()