from selenium import webdriver
import time 
from sys import exit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import random

def execute_erratic():
	print('Logging in...')
	driver = webdriver.Chrome('/home/j/Downloads/chromedriver')

	driver.get('https://10fastfingers.com/typing-test/english')


	words = list()
	for i in range(100):
		words.append(driver.find_element_by_xpath('//*[@id="row1"]/span[%s]' % str(i+1)).get_attribute('innerHTML'))
		print('Reading %d' % i)
		print('-' * (i+1))

	print('Finished reading!')

	print(words)

	for i in range(len(words)):
		number = random.uniform(0,1)
		if number <= 0.1:
			input_field = driver.find_element_by_id('inputfield').send_keys(str(hex(id(number))) + ' ')
		else:
			input_field = driver.find_element_by_id('inputfield').send_keys(words[i] + ' ')


def execute_genius():
	print('Logging in...')
	driver = webdriver.Chrome('/home/j/Downloads/chromedriver')

	driver.get('https://10fastfingers.com/typing-test/english')


	words = list()
	for i in range(205):
		words.append(driver.find_element_by_xpath('//*[@id="row1"]/span[%s]' % str(i+1)).get_attribute('innerHTML'))
		print('Reading %d' % i)
		print('-' * (i+1))

	print('Finished reading!')

	print(words)

	for i in range(len(words)):
		input_field = driver.find_element_by_id('inputfield').send_keys(words[i] + ' ')


def wait():
	while True:
		time.sleep(1)


def main():
	execute_genius()
	wait()


if __name__ == '__main__':

	main()