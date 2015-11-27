# universityRecommendationSystem
Recommendation system for Graduate Level Studies in the United States. Implemented as a part of CSE 255 - Data Mining and Predictive Analysis

### Nov 25, 2015
Started Scraping data from edulix.com

### Nov 26, 2015
Scrape completed. Started cleaning process

### Structure of scraped data
53,645 entries finally compiled.  
Each entry has the following properties:
- userName - username in edulix.com
- major - Major in which the user pursued / is pursuing
- researchExp - Research Experience in months
- industryExp - Industry Experience in months
- specialization - Intended specialization for higher studies
- toeflScore - TOEFL Score out of 110
- program - Intended Graduate Level Program 
- department - Department in which the user was / is enrolled
- toeflEssay - TOEFL Essay score out of 
- internExp - Internship Experience in months
- greV - GRE Verbal Score
- greQ - GRE Quants Score
- userProfileLink - Link to the userProfile in edulix.com
- journalPubs - number of Journal Publications
- greA - GRE AWA Score
- topperCgpa - toppers CGPA
- termAndYear - Intended joining term. Eg: Fall - 2015
- confPubs - number of conference publications
- ugCollege - Undergraduate college
- gmatA - GMAT AWA Score
- cgpa - user's CGPA
- gmatQ - GMAT Quants Score
- cgpaScale - CGPA Scale for the user's CGPA
- gmatV - GMAT Verbal Score
- univName - University Name applied to
- admit - Result of the application (0/1 - Reject/Admit)

Files  
-[scraper/getSingleUsersJSON.py](scraper/getSingleUsersJSON.py)  
	get data for single userName, userProfileLinkURL given. Used this in cases when the scraper failed encountering unicode characters and python failed to read it.  
-[scraper/getUniqueUsersFromEntireCollegeList.py](scraper/getUniqueUsersFromEntireCollegeList.py)  
	get unique users from the entire college vs user list. Used this list with profileLinkURL to scrape user data for individual users
-[scraper/getUserAdmitRejectListForEachUniversity.py](scraper/getUserAdmitRejectListForEachUniversity.py)  
	get admit reject list with userName and userProfile link
-[scraper/getUserAdmitRejectListForEachUniversitySingleFile.py](scraper/getUserAdmitRejectListForEachUniversitySingleFile.py)  
	get admit reject list with userName and userProfile link as a single file for all universities
-[scraper/getUserInfoFromUserList.py](scraper/getUserInfoFromUserList.py)  
	get userInfo from edulix based on the uniqueUser list
-[scraper/getUserProfileInfoVsUnivDetails.py](scraper/getUserProfileInfoVsUnivDetails.py)  
	get final CSV for userProfile vs college name vs admit/reject
-[scraper/ipython notebook scraper help.ipynb](scraper/ipython notebook scraper help.ipynb)  
	ipython notebook used for figuring out the html structure for edulix.com pages