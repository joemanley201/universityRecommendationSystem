__author__ = 'joemanley'
import requests
from lxml import html
import json
import time

def populateJSONForUniversityId(univId):
    page = requests.get("http://www.edulix.com/unisearch/univreview.php?stid=36&univid=" + univId)
    tree = html.fromstring(page.content)

    hrefPrefix = "http://www.edulix.com/unisearch/"
    collegeName = tree.xpath('//*[@id="page"]/div/table/tr/td/b/text()')[0]
    print collegeName
    admits = tree.xpath('//*[@id="page"]/div/div[1]/table/tr[2]/td/a[@class="admit"]/text()')
    admitsHref = tree.xpath('//*[@id="page"]/div/div[1]/table/tr[2]/td/a[@class="admit"]/@href')
    rejects = tree.xpath('//*[@id="page"]/div/div[1]/table/tr[2]/td/a[@class="reject"]/text()')
    rejectsHref = tree.xpath('//*[@id="page"]/div/div[1]/table/tr[2]/td/a[@class="reject"]/@href')

    collegeName = collegeName.replace("/", " ")
    print collegeName, "Admits: ", len(admits), "Rejects: ", len(rejects)
    #collegeName = ""

    finalString = ""
    for i in range(len(admits)):
        record = {'univId': univId, "admit": "1", "userName": admits[i], "userProfileLink": hrefPrefix + admitsHref[i]}
        finalString += json.dumps(record, collegeJSON) + "\n"

    for i in range(len(rejects)):
        record = {'univId': univId, "admit": "0", "userName": rejects[i], "userProfileLink": hrefPrefix + rejectsHref[i]}
        finalString += json.dumps(record, collegeJSON) + "\n"

    collegeJSON.write(finalString)

universityIdList = ['432', '1370', '1852', '1911', '1876', '1780', '920', '918', '917', '153', '812', '583', '582',
                    '1410', '1366', '419', '1319', '1222', '1220', '1127', '1024', '658', '145', '144', '142', '139',
                    '138', '136', '136', '980', '880', '1613', '1586', '1585', '133', '1471', '252', '1464', '647',
                    '1202', '408', '570', '1559', '1463', '397', '1301', '390', '206', '1819', '1510', '1507', '1678',
                    '716', '48', '969']



startTime = time.time()
collegeJSON = open("univJSON/" + "allColleges.json", "w")
for universityId in universityIdList:
    populateJSONForUniversityId(universityId)
collegeJSON.close()
print "Time taken: ", time.time() - startTime