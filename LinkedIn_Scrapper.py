from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep   
from parsel import Selector    

driver = webdriver.Chrome()                        
driver.get('https://www.linkedin.com')           #for linked in login purpose  
print("Enter Linked-In User Name ")
user_id = input()
print("Enter Linked-In Password")
user_pass = input()

driver.find_element_by_id('login-email') 
          
username = driver.find_element_by_class_name('login-email')               
                                 
username.send_keys(user_id)                                 
sleep(0.5)
password = driver.find_element_by_class_name('login-password')            

password.send_keys(user_pass) 
sleep(0.5)
log_in_button = driver.find_element_by_id('login-submit')                

log_in_button.click()
sleep(0.5)

driver.get('https://www.google.com')
sleep(3)
print("Enter query for google to scrap list of Linked-In profile URLs")
search_q = input()
search_query = driver.find_element_by_name('q') 
search_query.send_keys(search_q) #getting user linkes through a google search
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(3)

linkedin_urls = driver.find_elements_by_class_name('iUh30')
linkedin_urls = [url.text for url in linkedin_urls] #list of user links
sleep(0.5)

def validate_field(field): # used for avoiding null values
	if not field:
		field = 'No results'
		return field
	else:
		return field

user_details = []
for linkedin_url in linkedin_urls:
   driver.get(linkedin_url)
   sleep(5)
   sel = Selector(text=driver.page_source) 
   user_name = name = sel.xpath('//*[starts-with(@class, "topcard__name")]/text()').extract_first()
   user_name = validate_field(user_name)
   user_headline = sel.xpath('//*[starts-with(@class, "topcard__headline")]/text()').extract_first()
   user_headline = validate_field(user_headline)
   user_location = sel.xpath('//*[starts-with(@class, "topcard__location")]/text()').extract_first()
   user_location = validate_field(user_location)
   user_industry = sel.xpath('//*[starts-with(@class, "topcard__industry")]/text()').extract_first()
   user_industry = validate_field(user_industry)
   dic = {"name":user_name,"headline":user_headline,"location":user_location,"industry":user_industry,"url":linkedin_url}
   user_details.append(dic)
   dic = {}
driver.quit()  
#for x in user_details:
	#print("name : ",x["name"])
#writer = csv.writer(open(parameters.file_name, 'w'))
#writer.writerow(['Name','Job Title','Location','Industry','URL'])
#for x in user_details:
	#writer.writerow([x["name"], x["headline"], x["location"], x["industry"], x["url"]]) #writing to csv file
for x in user_details:
    print(" user name : ",x["name"]," Designation": x["headline"]," Location": x["location"]," Industry": x["industry"]," URL : " x["url"])
