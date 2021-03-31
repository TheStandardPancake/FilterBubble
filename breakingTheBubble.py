#This code is open source and you can use it for whatever purposes you would like
#please just at least acknowledge credit to me - Boyd Kirkman - 31/3/2021
from selenium import webdriver
from selenium.webdriver.common.keys import keys
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
    search_bar.send_keys(keys.return)
    sleep(0.01)
    results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
    results[0].click(). # clicks the first one

def setupBubble(biasShift):
    if biasShift == "r":
        for x in rightList:
            searchTerm(rightList[x])
        driver.get('https://www.google.com')
        print("Filter bubble is now inflated :)")
    if biasShift == "l":
        for y in leftList:
            searchTerm(leftList[y])
        driver.get('https://www.google.com')
        print("Filter bubble is now inflated :)")


if __name__ == "__main__":
    Print("Welcome to the filter bubble generator - made by Boyd Kirkman \n\n")
    bias = input("Initiate Left or Right Bias Filter Bubble? (L/R) --> ")
    bias = bias.lower()
    if bias == "l" or bias == "r":
        setupBubble(bias)
    else:
        raise Exception("only 'L' and 'r' are accepted as valid inputs")
