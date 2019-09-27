from selenium import webdriver
import time 
from sys import exit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import random
import os



def soloplayer(mode, driver):
	print('Starting normal mode')
	if mode == 'normal':
		driver.get('https://10fastfingers.com/typing-test/english')
	elif mode == 'advanced':
		driver.get('https://10fastfingers.com/advanced-typing-test/english')

	n = driver.find_element_by_id('row1')
	children_xpath = n.find_elements_by_xpath('.//*')
	print('Size of words: %d' % len(children_xpath))

	words = list()
	for i in range(len(children_xpath)):
		words.append(driver.find_element_by_xpath('//*[@id="row1"]/span[%s]' % str(i+1)).get_attribute('innerHTML'))
		print('Reading %d' % i)
		if i < int(len(children_xpath)/3):
			print('_' * (i+1))
		elif i > int(len(children_xpath)/3) and i < int(2*len(children_xpath)/3):
			print('+' * (i+1))
		else:
			print('*' * (i+1))


	print('Finished reading!')

	print(words)

	for i in range(len(words)):
		number = random.uniform(0,1)
		if number <= 0.05:
			# input_field = driver.find_element_by_id('inputfield').send_keys(str(hex(id(number))) + ' ')
			driver.find_element_by_id('inputfield').send_keys('oops')
			driver.find_element_by_id('inputfield').send_keys(' ')
		else:
			driver.find_element_by_id('inputfield').send_keys(words[i])
			driver.find_element_by_id('inputfield').send_keys(' ')

		time.sleep(.42)


# WIP: does not detect field multiplayer_input
def multiplayer(driver):
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
	for i in range(num_iterations):
		try:
			multiplayer_input.send_keys(driver.find_element_by_xpath('//*[@id="game"]/div[3]/div[2]/div[1]/div/span[%s] % (i+1)') + ' ')
		except Exception:
			print('Not more words found. You probably won ;)')


def train(driver, groups, category=0):
	time.sleep(2)
	for i in range(category,2):
		for j in range(groups,10):
			for k in range(0, 7):
				driver.get('https://10fastfingers.com/top1000/english/sc-%s%s%s/' % (str(i), str(j), str(k)))
				n = driver.find_element_by_id('row1')
				children_xpath = n.find_elements_by_xpath('.//*')
				print('Size of words: %d' % len(children_xpath))
				soloplayer('special_mode', driver, errors_boolean, len(children_xpath))


def do_login(driver):
	driver.get('https://10fastfingers.com/login')

	placeholder = driver.find_element_by_xpath('/html/body')
	email = driver.find_element_by_xpath('//*[@id="UserEmail"]')
	password = driver.find_element_by_xpath('//*[@id="UserPassword"]')
	email.send_keys(os.environ['FINGERS_EMAIL'])
	password.send_keys(os.environ['FINGERS_PASSWORD'])
	login_button = driver.find_element_by_id('login-form-submit')
	login_button.click()
	# Login complete
	time.sleep(2)



def wait():
	while True:
		time.sleep(1)



def main():
	# driver = webdriver.Chrome('/home/j/Downloads/chromedriver')
	driver = webdriver.Firefox()

	mode = input('Please, introduce which mode you want to play: (normal/advanced/multiplayer/train/spam_normal) ')
	groups = ''
	category = ''
	num_games = ''

	if mode == 'train':
		groups = input('Which level group do you want to start at? ')
		category = input('Category? (0/1) ')
		try:
			groups = int(groups)
			category = int(category)
		except ValueError:
			print('Invalid number')
			exit(-1)
	if mode == 'spam_normal':
		try:
			num_games = int(input('How many games do you want to play? '))
		except ValueError:
			print('Invalid number of games')
			exit(-1)




	if mode == 'normal' or mode == 'advanced':
		soloplayer(mode, driver)
	elif mode == 'multiplayer':
		multiplayer(driver)
	elif mode == 'train':
		do_login(driver)
		train(driver, groups, category)
	elif mode == 'spam_normal':
		for i in range(num_games):
			do_login(driver)
			soloplayer('normal', driver)
	else:
		print('Something went wrong. Exiting...')
		exit(-1)

	wait()



if __name__ == '__main__':

	main()