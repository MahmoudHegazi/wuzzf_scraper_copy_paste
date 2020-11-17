#!/usr/bin/python
from bs4 import BeautifulSoup
from tablib import Dataset
import numpy as np
import excel
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from flask import session as login_session
import string
import excel
# IMPORTS FOR THIS STEP
import httplib2
import json
from flask import make_response
import requests
import pandas as pd
from tablib import Dataset
import numpy as np
import excel
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# IMPORTS FOR THIS STEP
import pprint
import httplib2
import json
import sqlite3
from flask import make_response
import requests


app = Flask(__name__)

APPLICATION_NAME = "skaner"





# You need install :
# pip install PyPDF2 - > Read and parse your content pdf
# pip install requests - > request for get the pdf
# pip install BeautifulSoup - > for parse the html and find all url hrf with ".pdf" final
from PyPDF2 import PdfFileReader
import requests
import io
from bs4 import BeautifulSoup
import requests



@app.route('/target')
def targeter():
    wuzzuf_domain = 'https://wuzzuf.net/search/jobs/?q='
    wuzzuf_7bshtknat = '&a=navbg%7Cso&start=' + str(0)
    keyword = 'python'
    alink = str(wuzzuf_domain + keyword + wuzzuf_7bshtknat)
    response = requests.get(alink)
    if response.status_code != 200:
        return "Error fetching page"
        exit()
    else:
        content = response.content
        return content





if __name__ == '__main__':
    app.secret_key = 'AS&S^1234Aoshsheo152h23h5j7ks9-1---3*-s,#k>s'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
