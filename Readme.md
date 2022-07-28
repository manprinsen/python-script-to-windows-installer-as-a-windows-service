```python 
IF YOU == "have headache trying to deploy your python script as a windows service?":
    print("please follow along!")
```
    

### Disclaimer
Steps below is tested on python 3.10 and windows server 2019

### Preperations
* Download and install Inno Setup
https://jrsoftware.org/download.php/is.exe
* Download and unzip NSSM - the Non-Sucking Service Manager
https://nssm.cc/ci/nssm-2.24-101-g897c7ad.zip

### Step by step
* Create a folder at C:\inno-setup
* Copy the nssm.exe from the unzipped NSSM directory ```.\nssm-2.24-101-g897c7ad\win64\``` to ```C:\inno-setup\```
* Create a python script inside ```C:\inno-setup\``` called ```program.py```
* Copy and paste the code below to ```program.py```
```python
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s :: %(levelname)s :: %(message)s',
    filename="debug.log",
    filemode="w"
)

while True:
    logging.debug("loop is running")
    time.sleep(1)
```

#### We then need to install pyinstaller 
* Open Powershell or CMD and run ```pip install pyinstaller```
* Using the same prompt run ```cd C:\inno-setup\```
* Convert the python script to executable by using ```pyinstaller -w --add-data "nssm.exe;." .\program.py```
All your files and the executable are located at ```C:\inno-setup\dist\program\```
* Copy the ```inno-setup.iss``` to ```C:\inno-setup\```
* Double click on it to open it in the Inno Setup program

For future preferences; you can change the variables at the top of the script
```pascal
#define MyAppName "my-service"
#define MyAppVersion "1.0"
#define MyAppExeName "program.exe"
#define SourceLocation "C:\inno-setup\dist\program"
#define OutputLocation "C:\inno-setup\output"
```

* Edit the line ```AppId={{80B065A7-2B18-4547-A87E-EC1B544881C2}``` remove the ```{80B065A7-2B18-4547-A87E-EC1B544881C2}``` to is looks like this: ```AppId={``` (yes its correct). 
* Place your cursor at the end of the {
* At the top menu go to Tools then Generate GUID
* At the top menu go to Build then Compile
A output folder should now be created together with the setup file at ```C:\inno-setup\output\mysetup.exe```
* Double click on it to install the program and service.

Your service should now be located at ```C:\Program Files (x86)\my-service\```
Open the ```debug.log``` file to verify that the service is actually running.

Also verify the the service exist in the windows services. Go to Run and type ```services.msc```
You should have a windows service called ```my-service```

Over and out

```python
ELSE:
    return False
```
