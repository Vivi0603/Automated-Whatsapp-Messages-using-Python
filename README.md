Automated Bulk Messaging via WhatsApp using Python

This Python script automates the process of sending messages through the WhatsApp web application using stored contact numbers. It is primarily designed for sending promotional messages to customers by reading data from an Excel sheet and delivering tailored messages accordingly.

Setup Requirements
To successfully run this script, your system should have the following installed. Note that the contact numbers must already be saved in your phone (you may utilize bulk contact number saving methods like email). An alternative method exists for unsaved contacts, but it does not support sending attachments.

Python 3.8: Available at Python's official website.
Selenium WebDriver: Use the WebDriver included in this repository or download it from ChromeDriver - WebDriver for Chrome.
Google Chrome: Download from Google Chrome website.
Pandas: Install via the command pip install pandas.
Xlrd: Install via the command pip install xlrd.
Selenium: Install via the command pip install selenium.

Workflow
The user initiates by scanning a QR code to access the WhatsApp web application.
The script fetches a custom message from the Excel sheet.
It processes each row, searching for the contact number in WhatsApp. If the contact is found, it sends the pre-configured message; otherwise, it proceeds to the next row.
This loop continues until all rows are processed.
