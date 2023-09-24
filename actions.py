from flask import Blueprint, request, render_template, redirect, url_for, flash, Response, jsonify
import re
import os
import xml.dom.minidom
import logging
import textwrap

# Cấu hình logging
logging.basicConfig(filename='logfile.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('#################################################')
logging.info('#                 Start APP                     #')
logging.info('#################################################')

actions = Blueprint('actions', __name__, template_folder='templates')

import requests
from bs4 import BeautifulSoup
from vnstock import *

#print(listing_companies())
#print(company_events(symbol='TPB', page_size=15, page=0))
print(dividend_history("VNM"))