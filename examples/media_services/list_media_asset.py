"""
Copyright (c) 2016, Marcelo Leal
Description: Simple Azure Media Services Python library
License: MIT (see LICENSE.txt file for details)
"""
import os
import json
import azurerm
import time
#import pytz
import logging
import datetime

###########################################################################################
##### DISCLAIMER ##### ##### DISCLAIMER ##### ##### DISCLAIMER ##### ##### DISCLAIMER #####
###########################################################################################

# ALL CODE IN THIS DIRECTOY (INCLUDING THIS FILE) ARE EXAMPLE CODES THAT  WILL  ACT ON YOUR
# AMS ACCOUNT.  IT ASSUMES THAT THE AMS ACCOUNT IS CLEAN (e.g.: BRAND NEW), WITH NO DATA OR
# PRODUCTION CODE ON IT.  DO NOT, AGAIN: DO NOT RUN ANY EXAMPLE CODE AGAINST PRODUCTION AMS
# ACCOUNT!  IF YOU RUN ANY EXAMPLE CODE AGAINST YOUR PRODUCTION  AMS ACCOUNT,  YOU CAN LOSE
# DATA, AND/OR PUT YOUR AMS SERVICES IN A DEGRADED OR UNAVAILABLE STATE. BE WARNED!

###########################################################################################
##### DISCLAIMER ##### ##### DISCLAIMER ##### ##### DISCLAIMER ##### ##### DISCLAIMER #####
###########################################################################################

# Load Azure app defaults
try:
	with open('config.json') as configFile:
		configData = json.load(configFile)
except FileNotFoundError:
	print("ERROR: Expecting config.json in current folder")
	sys.exit()

account_name = configData['accountName']
account_key = configData['accountKey']

# Get the access token...
response = azurerm.get_ams_access_token(account_name, account_key)
resjson = response.json()
access_token = resjson["access_token"]

#Initialization...
print ("\n-----------------------= AMS Py =----------------------");
print ("Simple Python Library for Azure Media Services REST API");
print ("-------------------------------------------------------\n");

### list assets
print ("\n001 >>> Listing Media Assets")
response = azurerm.list_media_asset(access_token)
if (response.status_code == 200):
	resjson = response.json()
	print("POST Status.............................: " + str(response.status_code))
	for ma in resjson['d']['results']:
		print("Media Asset Name........................: " + ma['Id'])
		print("Media Asset Id..........................: " + ma['Name'])
else:
	print("POST Status.............................: " + str(response.status_code) + " - Media Asset Listing ERROR." + str(response.content))

