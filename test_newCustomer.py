import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages import SignInPage, DashboardPage
import random
import string
		
URL = 'https://test-selenium-manager.spincar.com/'
MAX_SIZE = '640'
PANO_MAX_SIZE = '1712'
CHECK_BOX = 'true'

letters = string.ascii_lowercase 
S3FOLDER = "TestFolder_" + ''.join(random.choice(letters) for i in range(8))
ERR_MSG1 = 'Customer name required'
ERR_MSG2 = 'Invalid email address'

USER_NAME = "TestUser_" + ''.join(random.choice(letters) for i in range(8))
ERR_S3 = 'S3 folder required'

class TestNewCustomer(unittest.TestCase):
	"""Unittest test class
	"""

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.wait = WebDriverWait(self.driver, 10)

		signInPage = SignInPage(self.driver) 
		self.driver.get(URL)
		signInPage.setEmail()
		signInPage.setPassword()
		signInPage.Submitbtn()

	def test_newCustomer(self):
		"""Verify customer record was created"""
		dashboardPage = DashboardPage(self.driver)
		dashboardPage.goToOnboard()


		dashboardPage.createCustomer(USER_NAME, S3FOLDER)
		dashboardPage.goToCustomerList()
		dashboardPage.sortRecentCustomer()

		initialId = dashboardPage.getId()
		editPage = dashboardPage.goToEditPage() 
		checkId, checkName, checkS3Folder, maxSize, panoMaxSize, checkBox = editPage.getParameters()


		self.assertEqual(initialId, checkId)
		self.assertEqual(checkName, USER_NAME)
		self.assertEqual(checkS3Folder, S3FOLDER)
		self.assertEqual(maxSize, MAX_SIZE)
		self.assertEqual(panoMaxSize, PANO_MAX_SIZE)
		self.assertEqual(CHECK_BOX, checkBox)
		
	def test_MissedName(self):
		"""Test mandatory name field"""
	
		dashboardPage = DashboardPage(self.driver)
		dashboardPage.goToOnboard()
		dashboardPage.createCustomer("", S3FOLDER)

		err1, err2 = dashboardPage.getErrorsNoName()
		self.assertEqual(err1.text, ERR_MSG1)
		self.assertEqual(err2.text, ERR_MSG2)


	def test_MissedS3folder(self):
		"""Test mandatory s3folder field"""
		dashboardPage = DashboardPage(self.driver)
		dashboardPage.goToOnboard()
		dashboardPage.createCustomer(USER_NAME, "")

		errMes = dashboardPage.getErrorNoS3()
		self.assertEqual(errMes.text, ERR_S3)

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()





