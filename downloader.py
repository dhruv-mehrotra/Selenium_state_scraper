from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

website = 'https://vahan.parivahan.gov.in/vahan4dashboard/vahan/view/reportview.xhtml'

service = Service(executable_path=r'/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)

state_labels = ['Andaman & Nicobar Island(8)', 'Andhra Pradesh(80)', 'Arunachal Pradesh(26)', 'Assam(36)', 'Bihar(49)', 'Chhattisgarh(30)', 'Delhi(23)', 'Haryana(179)', 'Jharkhand(30)', 'Maharashtra(53)', 'Madhya Pradesh(52)', 'Chandigarh(1)', 'UT of DNH and DD(3)', 'Goa(13)', 'Gujarat(37)', 'Himachal Pradesh(113)', 'Jammu and Kashmir(21)', 'Karnataka(68)', 'Kerala(87)', 'Ladakh(3)', 'Meghalaya(13)', 'Manipur(12)', 'Mizoram(10)', 'Nagaland(9)', 'Odisha(39)', 'Puducherry(8)', 'Sikkim(8)', 'Tamil Nadu(146)', 'Tripura(9)', 'West Bengal(56)', 'Punjab(93)', 'Rajasthan(142)', 'Uttarakhand(21)', 'Uttar Pradesh(78)']
vehicle_classes = ['VhClass:19', 'VhClass:20', 'VhClass:58', 'VhClass:59']

for state_label in state_labels:
    # select state
    print(state_label)
    state_box = driver.find_element(By.ID, "j_idt35_label")
    time.sleep(0.25)
    state_box.click()
    time.sleep(0.25)
    state = driver.find_element(By.XPATH, '//li[@data-label="' + state_label + '"]')
    time.sleep(0.25)
    state.click()
    time.sleep(0.25)
    
    # get RTOs list
    select_rto = driver.find_element(By.ID, "selectedRto_label")
    time.sleep(0.25)
    select_rto.click()
    time.sleep(0.25)
    rto_items = driver.find_elements(By.ID, "selectedRto_items")
    text = rto_items[0].get_attribute('innerHTML')
    indices = [i for i in range(len(text)) if text.startswith('data-label="', i)]
    rtos_list = []
    for i in indices[1:]:
        temp_rto = ""
        j = 12
        while(text[i+j] != '"'):
            temp_rto = temp_rto + text[i+j]
            j = j + 1
        rtos_list.append(temp_rto)
        print(temp_rto)
    # select_rto.click()
    
    for rto in rtos_list:
        # select an rto in the list
        if rto != rtos_list[0]:
            select_rto = driver.find_element(By.ID, "selectedRto_label")
            time.sleep(0.25)
            select_rto.click()
        time.sleep(0.5)
        rto_click = driver.find_element(By.XPATH, '//li[@data-label="' + rto + '"]')
        time.sleep(0.5)
        rto_click.click()
        
        if state_label == state_labels[0] and rto == rtos_list[0]:
            # select maker as Y axis
            y_axis = driver.find_element(By.XPATH, "//label[@id='yaxisVar_label']")
            time.sleep(0.25)
            y_axis.click()
            time.sleep(0.25)
            maker_select = driver.find_element(By.XPATH, '//li[@data-label="Maker"]')
            time.sleep(0.25)
            maker_select.click()
            time.sleep(0.5)
            
            # select month wise as X axis
            x_axis = driver.find_element(By.XPATH, "//label[@id='xaxisVar_label']")
            time.sleep(0.25)
            x_axis.click()
            time.sleep(0.25)
            month_wise = driver.find_element(By.XPATH, '//li[@data-label="Month Wise"]')
            time.sleep(0.25)
            month_wise.click()
            time.sleep(0.25)
        
            # select year as 2023
            select_year = driver.find_element(By.XPATH, "//div[@id='selectedYear']")
            time.sleep(0.25)
            select_year.click()
            time.sleep(0.25)
            yr_2022 = driver.find_element(By.XPATH, '//li[@data-label="2023"]')
            time.sleep(0.25)
            yr_2022.click()
            time.sleep(0.25)
        
        # refresh with selected fields
        refresh_1 = driver.find_element(By.ID, "j_idt61")
        time.sleep(0.25)
        refresh_1.click()
        time.sleep(1)
        
        if state_label == state_labels[0] and rto == rtos_list[0]:
            # expand further filters
            print("expand called")
            expand_butt = driver.find_element(By.XPATH, '//span[@class="ui-icon ui-icon-arrow-4-diag"]')
            time.sleep(0.25)
            expand_butt.click()
            time.sleep(2.5)
        
        # set as BOV
        bov_fuel = driver.find_element(By.XPATH, '//label[@for="fuel:7"]')
        time.sleep(1)
        bov_fuel.click()
        print("bov called")
        time.sleep(3)

        # cycle through vehicle classes
        for vehicle_class in vehicle_classes:
            # select vehicle classes
            type = driver.find_element(By.XPATH, '//label[@for="' + vehicle_class + '"]')
            time.sleep(0.25)
            type.click()
            time.sleep(3)
            
            # refresh
            refresh_2 = driver.find_element(By.ID, "j_idt66")
            time.sleep(0.25)
            refresh_2.click()
            time.sleep(6)
            
            # download sheet
            download_butt = driver.find_element(By.ID, "groupingTable:j_idt75")
            time.sleep(2)
            download_butt.click()
            time.sleep(5)
            
            # de-select vehicle type
            type = driver.find_element(By.XPATH, '//label[@for="' + vehicle_class + '"]')
            time.sleep(0.5)
            type.click()
            time.sleep(2)

    print(state_label + "========over==========")