# Korean_dictionary API
import requests
import xml.etree.ElementTree as ET

def posCheck(korean):
    key = "{YOUR-KEY}"
    q = korean
    url = "https://opendict.korean.go.kr/api/search" \
          "?key={}" \
          "&q={}".format(key, q)

    postXML = requests.post(url=url)
    data = postXML.text
    # print(data)

    f = open("data.xml", 'w')
    f.write(data)
    f.close()

    file_name = "data.xml"
    doc = ET.parse(file_name)
    root = doc.getroot()

    wordList = []
    posList = []

    for item in root.iter("item"):
        word = item.findtext("word")
        wordList.append(word)

    for sense in root.iter("sense"):
        pos = sense.findtext("pos")
        posList.append(pos)

    print("word:", wordList[0], "pos:", posList[0])

    if posList[0] == '명사':
        check = 'true'
    else:
        check = 'false'

    return check
