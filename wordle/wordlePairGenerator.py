__author__ = 'joemanley'
from PIL import Image
from os.path import dirname, isfile, join
from os import listdir
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

def getFinalUGCollName(collName):
    if collName.find("IIT") != -1:
        return "IIT"
    if collName.find("NIT") != -1:
        return "NIT"
    if collName.find("BITS") != -1:
        return "BITS"
    collName = collName.replace(" ", "").replace("of", "").replace("Of", "").replace(".", "").replace(",", "").replace("&", "")
    collName = collName.replace("-", "").replace("'","").replace("Information", "Info").replace("information", "info")
    collName = collName.replace("university", "Univ").replace("University", "Univ").replace("Institute", "Inst")
    collName = collName.replace("Institute", "Inst").replace("College", "Coll").replace("college", "Coll")
    collName = collName.replace("Engineering", "Engg").replace("engineering", "Engg").replace("Technology", "Tech")
    collName = collName.replace("technology", "Tech").replace("Science", "Sci").replace("science", "Sci")
    return collName

#generate input for wordle generator
def generateUnivVsUGCollegeMapForWordleGenerator():
    univVsUGCollegeMap = {}
    for entry in open(dirname(__file__) + '/../scraper/univJSON/allUsersFinal typo correct.csv'):
        if entry.startswith("userName"):
            continue
        parts = entry.split(",")
        univ = parts[24]
        ugCollege = parts[18]

        if univ in univVsUGCollegeMap:
            if ugCollege.strip() != "":
                univVsUGCollegeMap[univ].append(ugCollege)
        else:
            univVsUGCollegeMap[univ] = [ugCollege]
    return univVsUGCollegeMap

#create input files from the map
def createInputFilesForWordleGenerator(univVsUGCollegeMap):
    for univ in univVsUGCollegeMap:
        outputFile = open("input/" + univ.replace("/", " ") + ".txt", "w")
        ugCollegeArray = univVsUGCollegeMap[univ]
        ugCollegeArray = [getFinalUGCollName(ugCollege) for ugCollege in ugCollegeArray]
        outputFile.write('\n'.join(ugCollegeArray))
        outputFile.close()

def generateWordleForInput(textFile):
    text = open("input/" + textFile).read()
    wordcloud = WordCloud().generate(text)
    '''image = wordcloud.to_image()
    image.show()'''

    '''plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()'''

    wordcloud = WordCloud(min_font_size=10, max_font_size=60, relative_scaling=.5).generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("output/" + textFile + ".png")
    plt.close()

    #mask
    '''wordCloud = WordCloud(background_color="white", max_words=2000, mask=msMask)
    wordCloud.generate(text)
    wordCloud.to_file("output/" + textFile.replace(".txt", "") + ".png")'''

'''univVsUGCollegeMap = generateUnivVsUGCollegeMapForWordleGenerator()
createInputFilesForWordleGenerator(univVsUGCollegeMap)'''
#msMask = np.array(Image.open("mask.png"))

'''inputFiles = [f for f in listdir("input/") if isfile(join("input/", f))]
for inputFile in inputFiles:
    if ".txt" in inputFile:
        generateWordleForInput(inputFile)
        print inputFile, " done"'''
generateWordleForInput("allUGCollegesList.txt")