__author__ = 'joemanley'
import requests
import re
from bs4 import BeautifulSoup

def yearToMonths(durationString):
    yearStr, monStr = durationString.split(',')
    yearStr = yearStr.strip()
    monStr = monStr.strip()
    if ' ' in yearStr:
        year,text1 = yearStr.split(' ')
    else:
        year = 0
    if ' ' in monStr:
        months,text2 = monStr.split(' ')
    else:
        months = 0
    total = (int(year)*12) + int(months)
    return total

def getUserProfileObjectFromUrl(userProfileUrl):
    userObject = {}
    userObject['userProfileLink'] = userProfileUrl
    page=requests.get(userProfileUrl)
    soup = BeautifulSoup(page.content, 'html.parser')

    '''miscDetails = None

    for string in soup.table.stripped_strings:
        if miscDetails != None:
            miscDetails.append(string)
        if string == "Other Miscellaneous Details":
            miscDetails = []

    if miscDetails == None or len(miscDetails) == 0:
        miscDetails = [""]
    miscDetails = ''.join(miscDetails)
    miscDetails = re.sub(u"(\u2018|\u2019|\u201c|\u201d)", "'", miscDetails)
    miscDetails = re.sub(u"(\u2013)", "-", miscDetails)
    miscDetails = re.sub(u"(\u2022)", " ", miscDetails)
    miscDetails = re.sub(u"(\uf076)", " ", miscDetails)
    userObject['miscDetails'] = miscDetails'''


    allTDs = soup.table.find_all('td')
    for i in range(len(allTDs)):
        text = (allTDs[i].string or "").strip()
        if text == "Program":
            userObject['program'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Major":
            userObject['major'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Specialization":
            userObject['specialization'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Term and Year":
            userObject['termAndYear'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "GRE":
            userObject['greQ'] = (allTDs[i+2].string or "").strip()
            userObject['greV'] = (allTDs[i+4].string or "").strip()
            userObject['greA'] = (allTDs[i+6].string or "").strip()
            i += 6
        if text == "GMAT":
            userObject['gmatQ'] = (allTDs[i+2].string or "").strip()
            userObject['gmatV'] = (allTDs[i+4].string or "").strip()
            userObject['gmatA'] = (allTDs[i+6].string or "").strip()
            i += 6
        if text == "TOEFL":
            userObject['toeflScore'] = (allTDs[i+2].string or "").strip()
            userObject['toeflEssay'] = (allTDs[i+4].string or "").strip()
            i += 4
        if text == "University/College":
            userObject['ugCollege'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Department":
            userObject['department'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Grade":
            userObject['cgpa'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Topper's Grade":
            userObject['topperCgpa'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Grade Scale":
            userObject['cgpaScale'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Journal Publications":
            userObject['journalPubs'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Conference Publications":
            userObject['confPubs'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Industrial Experience":
            val = (allTDs[i+1].string or "").strip()
            userObject['industryExp'] = yearToMonths(val)
            i += 2
        if text == "Research Experience":
            val = (allTDs[i+1].string or "").strip()
            userObject['researchExp'] = yearToMonths(val)
            i += 2
        if text == "Internship Experience":
            val = (allTDs[i+1].string or "").strip()
            userObject['internExp'] = yearToMonths(val)
            i += 2

        #Check for missing properties, fill default values
        if "program" not in userObject:
            userObject['program'] = "MS"
        if "major" not in userObject:
            userObject['major'] = ""
        if "specialization" not in userObject:
            userObject['specialization'] = ""
        if "termAndYear" not in userObject:
            userObject['termAndYear'] = ""

        if "greQ" not in userObject:
            userObject['greQ'] = "0"
        if "greV" not in userObject:
            userObject['greV'] = "0"
        if "greA" not in userObject:
            userObject['greA'] = "0"

        if "gmatQ" not in userObject:
            userObject['gmatQ'] = "0"
        if "gmatV" not in userObject:
            userObject['gmatV'] = "0"
        if "gmatA" not in userObject:
            userObject['gmatA'] = "0"

        if "toeflScore" not in userObject:
            userObject['toeflScore'] = "0"
        if "toeflEssay" not in userObject:
            userObject['toeflEssay'] = "0"

        if "ugCollege" not in userObject:
            userObject['ugCollege'] = "0"
        if "department" not in userObject:
            userObject['department'] = "0"
        if "cgpa" not in userObject:
            userObject['cgpa'] = "0"
        if "topperCgpa" not in userObject:
            userObject['topperCgpa'] = "0"
        if "cgpaScale" not in userObject:
            userObject['cgpaScale'] = "0"
        if "journalPubs" not in userObject:
            userObject['journalPubs'] = "0"
        if "confPubs" not in userObject:
            userObject['confPubs'] = "0"
        if "industryExp" not in userObject:
            userObject['industryExp'] = "0"
        if "researchExp" not in userObject:
            userObject['researchExp'] = "0"
        if "internExp" not in userObject:
            userObject['internExp'] = "0"
        '''if "miscDetails" not in userObject:
            userObject['miscDetails'] = ""'''
    return userObject

propertyList = ["userName","major","researchExp","industryExp","specialization","toeflScore",
                "program","department","toeflEssay","internExp","greV","greQ","userProfileLink",
                "journalPubs","greA","topperCgpa","termAndYear","confPubs","ugCollege","gmatA","cgpa","gmatQ","cgpaScale","gmatV"]
userInfoJSON = open("univJSON/" + "allUsers_1.csv", "w")
count = 0
userInfoJSON.write(','.join(propertyList) + "\n")
for userInfo in open("univJSON/uniqueUsers_1.txt"):
    userName, userLink = userInfo.split(",")
    vals = []
    userInfoObj = getUserProfileObjectFromUrl(userLink)
    for key in userInfoObj:
        vals.append(userInfoObj[key])
    print "Fetched Information for: ", userLink, ",", userName
    print (userName + "," + userInfoObj["major"].replace(",", " ") + "," + str(userInfoObj["researchExp"]) + "," + str(userInfoObj["industryExp"]) + "," + userInfoObj["specialization"].replace(",", " ") + "," + str(userInfoObj["toeflScore"]) + "," + userInfoObj["program"] + "," + userInfoObj["department"] + "," + str(userInfoObj["toeflEssay"]) + "," + str(userInfoObj["internExp"]) + "," + str(userInfoObj["greV"]) + "," + str(userInfoObj["greQ"]) + "," + userInfoObj["userProfileLink"].strip() + "," + str(userInfoObj["journalPubs"]) + "," + str(userInfoObj["greA"]) + "," + str(userInfoObj["topperCgpa"]) + "," + userInfoObj["termAndYear"] + "," + str(userInfoObj["confPubs"]) + "," + userInfoObj["ugCollege"].replace(",", " ") + "," + str(userInfoObj["gmatA"]) + "," + str(userInfoObj["cgpa"]) + "," + str(userInfoObj["gmatQ"]) + "," + str(userInfoObj["cgpaScale"]) + "," + str(userInfoObj["gmatV"]))
    userInfoJSON.write(userName + "," + userInfoObj["major"].replace(",", " ") + "," + str(userInfoObj["researchExp"]) + "," + str(userInfoObj["industryExp"]) + "," + userInfoObj["specialization"].replace(",", " ") + "," + str(userInfoObj["toeflScore"]) + "," + userInfoObj["program"] + "," + userInfoObj["department"] + "," + str(userInfoObj["toeflEssay"]) + "," + str(userInfoObj["internExp"]) + "," + str(userInfoObj["greV"]) + "," + str(userInfoObj["greQ"]) + "," + userInfoObj["userProfileLink"].strip() + "," + str(userInfoObj["journalPubs"]) + "," + str(userInfoObj["greA"]) + "," + str(userInfoObj["topperCgpa"]) + "," + userInfoObj["termAndYear"] + "," + str(userInfoObj["confPubs"]) + "," + userInfoObj["ugCollege"].replace(",", " ") + "," + str(userInfoObj["gmatA"]) + "," + str(userInfoObj["cgpa"]) + "," + str(userInfoObj["gmatQ"]) + "," + str(userInfoObj["cgpaScale"]) + "," + str(userInfoObj["gmatV"]))
    userInfoJSON.write("\n")

    count += 1

    print "Count so far: ", count
userInfoJSON.close()