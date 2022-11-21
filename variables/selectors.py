
el_img_count = '//*[@id="ikind-titleSorter"]/div/div/div[2]/div[1]/a/div[1]/img'
el_donation_Vis = '//*[@id="donate-close-button"]'
#-----------------Book Details from Web--------------------
el_title = '//*[@id="maincontent"]//span[@itemprop="name"]'
el_Author = '//*[@id="maincontent"]//*[@class="metadata-definition"][1]//span'
# el_Publication_date = '//*[@id="maincontent"]//*[@class="metadata-definition"]/dd/a/span'
# el_Publisher = '//*[@id="maincontent"]//*[@class="metadata-definition"][3]//dd//span'
# el_Collection = '//*[@id="maincontent"]//*[@class="metadata-definition"][4]//dd'
# el_Contributor = '//*[@id="maincontent"]//*[@class="metadata-definition"][6]//dd'
# el_Identifier = '//*[@id="maincontent"]//*[@class="metadata-expandable-list row"]//dl[5]//dd'
#------------------------------------------------------------------------------------------------

#----------------Siblings Selectors for Publication date, Publisher, Collection, Contributor, Identifier---------------
el_Publication_date = '//*[contains(text(),"Publication date")]/following-sibling::dd'
el_Publisher = '//*[contains(text(),"Publisher")]/following-sibling::dd'
el_Collection = '//*[contains(text(),"Collection")]/following-sibling::dd'
el_Contributor = '//*[contains(text(),"Contributor")]/following-sibling::dd'
el_Identifier = '//*[@class="metadata-definition"]//*[contains(text(),"Identifier")]/following-sibling::dd'


