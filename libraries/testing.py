def pdf_name(string):    
    # string = "https://archive.org/download/Buffalo_NY_Death_Index_1885-1891/Reclaim_The_Records_-_Buffalo_NY_Death_Index_-_1885-1891_-.pd"
    words = string.split('/')
    for i in words:
        check = i.__contains__(".pdf")
        
    if check == True:
            print(i)
            return i
    else:
        print('0')
        return 0
# pdf_name('https://archive.org/download/Buffalo_NY_Death_Index_1885-1891/Reclaim_The_Records_-_Buffalo_NY_Death_Index_-_1885-1891_-.pdf')   
