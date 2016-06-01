#!/usr/bin/env pyhton
# -*- coding:utf-8 -*-

import os
import time


ssh_login_panel_ico = """
#########################################################
#       PYTHON - SSH LOGIN PANEL - GH0ST S0FTWARE       #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################	
"""

def ssh_login_panel():
	print ssh_login_panel_ico
	ssh_host_adresi = raw_input("SSH bağlantısı için bir host adresi giriniz :")		
	os.system("ssh" + " " + ssh_host_adresi)

ssh_login_panel()

