# EAD_Alarm
Scrapes USCIS website every 10 minutes and checks status of your application!
Requirements: Linux, Python2
How to use:
On command line, execute: python uscis2.py CASE_NUMBER & > out.txt
It will keep checking results every 10 minutes. You can see latest results in out.txt.
When the status changes, It will give out a alarm with beep.
Its a crude but simple script! Android app on the way..
