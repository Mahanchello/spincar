from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class SignInPage(object):

	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(self.driver, 10)

	def setEmail(self, email = 'tester3@spincar.com', locator = 'email'):
		self.driver.find_element_by_id(locator).send_keys(email)

	def setPassword(self, password = 'password', locator = 'password'):
		self.driver.find_element_by_id(locator).send_keys(password)

	def Submitbtn(self):
		self.driver.find_element_by_id('submit').click()

	def goToDashboard(self):
		return DashboardPage(self.driver) 

class DashboardPage(SignInPage):
	
	def  goToOnboard(self): 
		self.driver.find_element_by_css_selector('span[class="glyphicon glyphicon-cog"]').click()
		self.driver.find_element_by_css_selector('li.dropdown.open > ul > li:nth-child(2) > a').click()

	def createCustomer(self, UserName, S3folder):
		self.driver.find_element_by_id('lastpass-disable-search-u').send_keys(UserName)
		self.driver.find_element_by_id('lastpass-disable-search-s').send_keys(S3folder)
		self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-create > input.form-control.btn.btn-primary.rbutton25'))).click()

	def goToCustomerList(self):
		self.driver.find_element_by_css_selector('ul:nth-child(1) > li:nth-child(2) > a').click()
		self.driver.find_element_by_css_selector('li.dropdown.open > ul > li:nth-child(1) > a').click()

	def sortRecentCustomer(self):
		self.driver.find_element_by_css_selector('th.table-right').click()
		self.driver.find_element_by_css_selector('th.table-right > span').click()	

	def getId(self):
		initialId = self.driver.find_element_by_css_selector('tr:nth-child(1) > td.table-right > a').get_attribute('value')
		return initialId

	def goToEditPage(self):
		self.driver.find_element_by_css_selector('tr:nth-child(1) > td.table-right > a').click()
		return EditPage(self.driver)

	def getErrorsNoName(self):
		err1 = self.driver.find_element_by_css_selector('#errors > li:nth-child(1)');
		err2 = self.driver.find_element_by_css_selector('#errors > li:nth-child(2)');
		return err1, err2 

	def getErrorNoS3(self):
		errMes = self.driver.find_element_by_css_selector('#errors > li')
		return errMes
		
class EditPage(SignInPage):

	def getParameters(self):
		CheckId = self.driver.find_element_by_css_selector('tr:nth-child(2) > td:nth-child(2)').get_attribute('value')
		CheckName = self.driver.find_element_by_id('name').get_attribute('value')
		CheckS3Folder = self.driver.find_element_by_css_selector('[name="s3_folder"]').get_attribute('value')
		MaxSize = self.driver.find_element_by_css_selector('[name="max_size"]').get_attribute('value')
		PanoMaxSize = self.driver.find_element_by_css_selector('[name="pano_max_size"]').get_attribute('value')
		CheckBox = self.driver.find_element_by_css_selector('input[type="checkbox"][name="is_spin_customer').get_attribute('checked')
		return CheckId, CheckName, CheckS3Folder, MaxSize, PanoMaxSize, CheckBox