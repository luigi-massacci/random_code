#######################################################################################################
# Retrieves stock data from the website of the "Conoscere la borsa" ("Get to know the Stock Exchange")
# competition
# 
#  19/11/2020, with (very very major) contributions by Luca Monegaglia
########################################################################################################


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import pandas as pd
import datetime

##############################################################################################
#OTTIENI CREDENZIALI E OS 
##############################################################################################

config_file = open(sys.path[0] + "/config.txt", "r")
config_data = config_file.read().splitlines()
OS = config_data[0]
USERNAME = config_data[1]
PASSWORD = config_data[2]

path = ""
if OS == "LX":
    path = "/usr/lib/chromium-browser/chromedriver"
elif OS == "WS":
    path = sys.path[0] + "/chromedriver.exe"


#############################################################################################
#RACCOLTA DATI
#############################################################################################
driver = webdriver.Chrome(executable_path=path)
driver.set_window_size(1080,900)
driver.get("https://www.planspiel-boerse.de/cgiG24/depot?shs=32c12fa30a69231c014bbdeeed16401a&LNK=4431#")

user = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div/form/div[1]/input")))
user.send_keys(USERNAME)
user = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div/form/div[2]/input")))
user.send_keys(PASSWORD)
conferma = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[1]/div[3]/div/div/form/div[3]/input"))).click()
time.sleep(1)
mercato = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/header/div/div[2]/ul/li[3]/a")))
ActionChains(driver).move_to_element(mercato).perform()
quotazioni = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/header/div/div[2]/ul/li[3]/div/ul/li[1]/a"))).click()
table = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/table")))
rows = table.find_elements(By.TAG_NAME, "tr")
table = []
for j in range(1, len(rows)):
    cells = rows[j].find_elements(By.TAG_NAME, "td") 
    cellslist = []
    for i in range(0, len(cells)):
        if i == 3 or i == 5:
            continue
        cellslist.append(cells[i].text) #da salvare in appropriata struttura
    table.append(cellslist)

table = pd.DataFrame(table)
ct = datetime.datetime.now().strftime("%d-%m-%y_%H-%M-%S")
table.to_csv(sys.path[0] + '/' + str(ct) + ".csv")

########################################################################################
#ANALISI DATI
#######################################################################################