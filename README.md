# universityRecommendationSystem
Implemented as a part of CSE 255 - Data Mining and Predictive Analysis

For an aspiring graduate student, choosing which universities to apply to is a conundrum. Often, the students wonder if their profile is good enough for a certain university. We addressed this issue by building a recommendation system based on various classification algorithms. Since data was not readily available, we scraped data Edulix.com, and a dataset containing profiles of students with admits/rejects to 45 different universities in USA was built. Based on this data set, various models were trained and universities were suggested such that it maximizes the chances of a student getting an admit from that university.

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
	
### Nov 26, 2015
Scrape completed. Started cleaning process

### Nov 25, 2015
Started Scraping data from edulix.com