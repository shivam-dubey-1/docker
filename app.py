from flask import Flask
import numpy as np
import os
from datetime import datetime
app = Flask(__name__)

count = 0
filepath = "/data/count.txt"
file = open (filepath, "a+")

@app.route("/visit")
def visit():
    global count
    global file
    count = count + 1
    dateStr =  datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    content = "Visit " + str (count) + " @ " + dateStr + "\n"
    file.write (content)
    file.flush ()
    return content, 200

def init():
    if os.path.exists (filepath):
        fp = open (filepath, "r")
        for line in fp:
            global count
            count = count + 1
        fp.close()

init()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
