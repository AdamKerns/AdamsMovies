import csv

# If file (200MoviesWatched.csv) exists do this
'''
    used to test the database by initializing movies
    will progress to updating functionality / inputing movies directly throught the software
'''
def initialMovies(testing):
    
    with open(".venv/AdamsMovies/movies/static/200MoviesWatched.csv", 'r') as CSVfile:
        movieReader = csv.DictReader(CSVfile)
        i = 0
        for row in movieReader:
            title = row["Title"].strip()
            title = title.replace("`", ",") # USE
            pScore = row["Prime Score"].strip() # rated out of 5    USE
            rtScore = row["Rotten Tomatoes Score"].strip() # rated out of 10    USE
            iScore= row["IMDb Score"].strip() # rated out of 10     USE
            averageScore = ((2 * float(pScore)) + float(rtScore) + float(iScore)) / 3   # USE
            if testing:
                i += 1
                print("~~~~~~~~~~~~~~~~~~")
                print(f"{i}. {title}")
                print("---------")
                print(f"Prime Score: {pScore}/5     Rotten Tomatoes Score: {rtScore}/10     IMDb Score: {iScore}/10")
                print(f"Average Score: {averageScore:.1f}/10")
                print("---------")
                print("~~~~~~~~~~~~~~~~~~")
            
            link = row["OnionPlay Link"].strip()    # USE
            genres = row["Genre List"].strip()  
            genreList = genres.split(" ")   # USE
            if testing:
                print(genreList)
            myScore = row["My Score"].strip()   # USE
            iSummary = row["IMDb Summary"].strip()  # USE
            awards = row["Awards"].strip()
            awardAmount = 0     # USE
            awardsList = awards.split(" + ")    # USE
            if testing:
                print(awardsList)
            for award in awardsList:
                amount = 0 if award == '' else 1
                if "s" == award[-1:] or (award.find("Awards") != -1 and award.find("Academy") != -1):
                    if testing:
                        print(award)
                    amount = float(award[0])
                awardAmount += amount    
            if testing:
                print(awardAmount)
            mustWatch = row["Must Watch"].strip()
            mustWatch = True if mustWatch == "True" else False  # USE 
            
            # put into database
             
           
            
initialMovies(True)