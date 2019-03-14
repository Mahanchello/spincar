1. Install pip for your python https://pip.pypa.io/en/stable/installing/
2. Install selenium:
pip install -U selenium
3. Put the chromedriver to the project folder: https://chromedriver.storage.googleapis.com/index.html?path=2.46/ 
You may need add path to chromedriver in line 26: self.driver = webdriver.Chrome('./chromedriver') depending on your system
4. Run python unittest:
python -m unittest -v test_newCustomer

Excpected output: 
g:\nastya>python -m unittest -v test_newCustomer
test_MissedName (test_newCustomer.TestNewCustomer) ...
DevTools listening on ws://127.0.0.1:57684/devtools/browser/9721b461-aa5a-4165-bbd8-63289883a001
ok
test_MissedS3folder (test_newCustomer.TestNewCustomer) ...
DevTools listening on ws://127.0.0.1:57717/devtools/browser/2b3731fa-7c68-4386-a44c-32dab9adc7c6
ok
test_newCustomer (test_newCustomer.TestNewCustomer) ...
DevTools listening on ws://127.0.0.1:57754/devtools/browser/5157adac-fbdc-4f42-97f3-bc39fafd3429
ok

----------------------------------------------------------------------
Ran 3 tests in 17.366s

OK

Script tested on Ubuntu 18.04, Windows 10, python 2.7  

Thanks,
Anastasiya