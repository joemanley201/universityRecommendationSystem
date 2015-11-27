__author__ = 'joemanley'

userProfileLinkMap = {}
uniqueUserProfileLinkListFile = open("univJSON/uniqueUsers.txt", "w")
for entry in open("univJSON/allColleges.json"):
    userProfileLinkMap[eval(entry)['userName']] = eval(entry)['userProfileLink']
for user in userProfileLinkMap:
    uniqueUserProfileLinkListFile.write(user + "," + userProfileLinkMap[user] + "\n")
uniqueUserProfileLinkListFile.close()