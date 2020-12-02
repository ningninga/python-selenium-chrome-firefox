# python-selenium-chrome-firefox
use selenium to make web browser to do the web test  automaticly
=========

0.Ensure you have used selenium 
-----
If you have not imported selenium yet, open your ide, for example, mine is pycharm.
write down this line: 
```
from selenium import webdriver
```

1.Download chrome-driver
-----
Here is one of the download links, it is a mirror index of http://chromedriver.storage.googleapis.com/
For some secret reasons, it is not allowed to visit some foreign sites in China, LOL, but there is the helpful link.

2.Put the chrome-driver into the installation path of python
------
If you do not know the path, just open your terminal and the command is "python>>>import sys>>>print(sys.path)",
and then put the .exe into the Script directory.

3.Open your ide and get the chrome driver
----
The code is  
```
driver = webdriver.Chrome()
```
Here  you  go!
==========
In the two of the files which I upload, one of them is based on Chrome, and another one is based on Firefox.
My Chrome version is 86.0.4240.193.
My Firefox version is 83.0 (64).
I hope it can be helpful:)
