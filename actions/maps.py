import webbrowser


def showMe( text:str):  # query imput module :  , Location Paris , Location of Paris
    text=text.replace("of","") # to elimin the of
    city=text[text.index('location') + 8:].strip()
    webbrowser.open(r"https://www.google.com/maps/search/"+city)
    print(city)
    return "Here Sir"




def getDirections(text:str):  # get me from City1 to City2

    remainderText=text[text.index("from") + 5:]
    city1=remainderText.split(" ")[0].strip()
    city2=remainderText[remainderText.index("to") + 3:].split(" ")[0].strip()
    webbrowser.open(r"https://www.google.com/maps/dir/"+city1+"/"+city2)
    return "Drive Safelly"

