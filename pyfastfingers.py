from selenium import webdriver
import time 
from sys import exit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import random

def soloplayer(mode, driver, errors_boolean):
	print('Starting normal mode')
	if mode == 'normal':
		driver.get('https://10fastfingers.com/typing-test/english')
	elif mode == 'advanced':
		driver.get('https://10fastfingers.com/advanced-typing-test/english')

	words = list()
	for i in range(200):
		words.append(driver.find_element_by_xpath('//*[@id="row1"]/span[%s]' % str(i+1)).get_attribute('innerHTML'))
		print('Reading %d' % i)
		print('-' * (i+1))

	print('Finished reading!')

	print(words)

	if errors_boolean is True:
		for i in range(len(words)):
			number = random.uniform(0,1)
			if number <= 0.05:
				# input_field = driver.find_element_by_id('inputfield').send_keys(str(hex(id(number))) + ' ')
				input_field = driver.find_element_by_id('inputfield').send_keys('oops' + ' ')
			else:
				input_field = driver.find_element_by_id('inputfield').send_keys(words[i] + ' ')
	else:
		for i in range(len(words)):
			input_field = driver.find_element_by_id('inputfield').send_keys(words[i] + ' ')


def multiplayer(driver, errors_boolean):
	print('Starting advanced mode')

	driver.get('https://10fastfingers.com/advanced-typing-test/english')

	words = list()
	for i in range(200):
		words.append(driver.find_element_by_xpath('//*[@id="row1"]/span[%s]' % str(i+1)).get_attribute('innerHTML'))
		print('Reading %d' % i)
		print('-' * (i+1))

	print('Finished reading!')

	print(words)

	if errors_boolean is True:
		for i in range(len(words)):
			number = random.uniform(0,1)
			if number <= 0.05:
				# input_field = driver.find_element_by_id('inputfield').send_keys(str(hex(id(number))) + ' ')
				input_field = driver.find_element_by_id('inputfield').send_keys('oops' + ' ')
			else:
				input_field = driver.find_element_by_id('inputfield').send_keys(words[i] + ' ')
	else:
		for i in range(len(words)):
			input_field = driver.find_element_by_id('inputfield').send_keys(words[i] + ' ')


# WIP: does not detect field multiplayer_input
def multiplayer(driver, errors_boolean):
	print('Starting multiplayer mode')

	driver.get('https://10fastfingers.com/multiplayer')

	time.sleep(5)
	close_cookies = driver.find_element_by_id('CybotCookiebotDialogBodyLevelButtonAccept')
	close_cookies.click()
	username_input = driver.find_element_by_name('username')
	enter_button = driver.find_element_by_xpath('//*[@id="auth"]/input[2]')
	username_input.send_keys('jasperan')
	enter_button.click()
	multiplayer_input = driver.find_element_by_xpath('//*[@id="game"]/div[3]/div[2]/div[2]/div[1]/input')
	time.sleep(10) # Wait for the game to start
	words = list()
	for i in range(200):
		try:
			multiplayer_input.send_keys(driver.find_element_by_xpath('//*[@id="game"]/div[3]/div[2]/div[1]/div/span[%s] % (i+1)') + ' ')
		except Exception:
			print('Not more words found. You probably won ;)')


def train(driver, errors_bolean):
	driver.get('https://10fastfingers.com/login')

	username_input.send_keys(os.environ['FINGERS_USERNAME'])
	password_input.send_keys(os.environ['FINGERS_PASSWORD'])


def login(driver):
	pass



def wait():
	while True:
		time.sleep(1)



def main():
	driver = webdriver.Chrome('/home/j/Downloads/chromedriver')

	mode = input('Please, introduce which mode you want to play: (normal/advanced/multiplayer) ')
	fails = input('Do you want failures to happen? (yes/no) ')

	if mode == 'normal' or mode == 'advanced':
		soloplayer(mode, driver, True)
	elif mode == 'multiplayer':
		multiplayer(driver, True)
	elif mode == 'train':
		training(driver, True)
	else:
		print('Something went wrong. Exiting...')
		exit(-1)

	wait()



if __name__ == '__main__':

	main()