print("Loading Word Chain Game ...")
#DB : word_dictionary_kor.txt

import time, sys
import korean_dictionary_api as kda
from utils import humanEg, computerEg, defaultEg

dicData = [] #사전목록
useData = [] #이미사용된 단어 저장
time.sleep(2)

print("""

    *************************[ Rule ]****************************
    1. DB에 있는 단어만 사용 가능
    2. DB에 없는 단어를 입력 할 경우,
       DB에 저장되어 다음 게임에서 사용 가능
    3. 직접 DB를 수정하고 싶을 경우,
       word_dictionary_kor.txt파일 수정
    *************************************************************

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""", end="")
time.sleep(3)

try:
    f = open("db/word_dictionary_kor.txt","r")
except:
    print("[Error] DB file not found")
    print("[Fail] Loading Word Chain Game ...")
    time.sleep(1)
    sys.exit()

while True:
    data = f.readline().rstrip('\r\n')
    dicData.append(data)
    if data == "":
        break

#스타트 엔진
def countdown(n):
    if n == 0:
        print("Please enter a word")
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)

print("Start Game !!!")
time.sleep(1)
countdown(3)
lastChar = ""
f = open("db/word_dictionary_kor.txt","r")

while True:
    hmWord = humanEg.humanInput(lastChar) #사람이 단어를 입력함
    hmWord = humanEg.humanConnectChar(hmWord,lastChar) #사람이 입력 한 단어를 가공함
    hmCanUse = humanEg.humanWordDefine(hmWord,dicData) #사람이 입력한 단어가 있는지 확인
    if hmCanUse:
        #word_dictionary_kor DB에 구성되지 않은 단어 일 경우, add_words DB 추가
        korean = hmWord
        check = kda.posCheck(korean)
        if check == "true":
            print("[Error] '{}'은(는) DB에 구성되지 않은 단어입니다.".format(hmWord))
            print("'{}'이(가) DB에 추가되었습니다. 다음 게임에서 적용됩니다.".format(hmWord))
            f = open("db/word_dictionary_kor.txt", 'a')
            f.write(hmWord + '\n')
            f.close()
        else:
            print("[Error] '{}'은(는) 명사가 아닙니다.".format(hmWord))
        continue

    isuse = humanEg.humanUseWord(hmWord,useData)
    if isuse:
        print("Game End")
        sys.exit()
    else:
        useData.append(hmWord)

    #사람이 입력할것이 완료됨
    #컴퓨터의 시작
    lastChar = defaultEg.getLastChar(hmWord)
    comWord = computerEg.useWord(lastChar,dicData)
    if comWord == []:
        print("Mopy : ", lastChar[-1])
        print("[Error] DB에 {}(으)로 시작하는 단어가 없을 경우 종료됩니다.".format(lastChar[-1]))
        time.sleep(3)
        print("Ending Word Chain Game ...")
        time.sleep(1)
        sys.exit()

    comWord = computerEg.useAgain(comWord,useData)
    if comWord == []:
        print("Word Chain Game Ending...")
        time.sleep(5)
        sys.exit()

    #comWord  변수에 총 사용가능한 단어들이 모여있습니다.
    computerUse = computerEg.selectWord(comWord)
    print("Mopy : ", computerUse)
    useData.append(computerUse)
    lastChar = defaultEg.getLastChar(computerUse)
