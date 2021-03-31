#This code is open source and you can use it for whatever purposes you would like
#please just at least acknowledge credit to me - Boyd Kirkman - 31/3/2021
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

#initiate the selenium driver
driver = webdriver.Chrome("./chromedriver.exe")

#search terms associated with the right and the left
rightList = ["conservative","rightist", "the right","right-wing","traditionalist","capitalism","traditionalistic","Australian Liberal Party","Liberal","liberalist","reactionary faction","conformist","archconservative","paleoconservative","reactionary","Tory", "katter's Australian Party","pauline Hanson's One Nation","Jacqui Lambie Network",]
leftList = ["the Australian Labor Party","the African National Congress","Bolshevik","champagne socialist","communist","comrade","critical theory","the far left", "fellow traveller","critical theorist","Labour","The Labour party","left","leftist","the left","left-wing","maoism","maoist","Marxism","marxist","New Labour","politburo","red","red flag","social democracy","trotskyist"]

#A function to search a term
def searchTerm(term):
    driver.get('https://www.google.com')
    search_bar = driver.find_element_by_name('q')
    search_bar.send_keys(term)
    search_bar.send_keys(Keys.RETURN)
    sleep(0.01)
    try:
        results = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3')
        results.click()
    except:
        pass
    sleep(0.3)

#decide which term to use
def setupBubble(biasShift):
    if biasShift == "r":
        for terms in rightList:
            searchTerm(terms)
        driver.get('https://www.google.com')
        print("\n\nFilter bubble is now inflated :)\n\n")
    if biasShift == "l":
        for terms in leftList:
            searchTerm(terms)
        driver.get('https://www.google.com')
        print("Filter bubble is now inflated :)")

#Main initialisation handling input, function order and printing useful text
if __name__ == "__main__":
    print("\n\n\n\nWelcome to the filter bubble generator - made by Boyd Kirkman \n\n")
    bias = input("Initiate Left or Right Bias Filter Bubble? (L/R) --> ")
    bias = bias.lower()
    if bias == "l" or bias == "r":
        setupBubble(bias)
    else:
        raise Exception("only 'L' and 'r' are accepted as valid inputs")
