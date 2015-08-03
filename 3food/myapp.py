#!/usr/bin/env python

import pdb
import time
import subprocess
import redis
from threading import Thread
import matplotlib.pyplot as plt
from flask import Flask, request, render_template
app = Flask(__name__)

r = redis.Redis()
key = "base1"

def adding_value(sleep=10, delta=5):
    while True:
	temp = float (subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"]).strip("temp='C\n"))
	r.rpush(key, temp)
	lenght = r.llen(key)
	x = range (lenght-delta, lenght)
	y = r.lrange(key,lenght - delta, lenght)
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	ax1.plot(x,y)
	fig.savefig("static/graph.png")
	time.sleep(sleep)

@app.route("/", methods=['GET'])
def main(delta=5):
    lenght = r.llen(key)
    d = r.lrange(key, lenght - delta, lenght)
    return render_template("template.html", 
		temperatures=d,
		delta=delta,
	)

if __name__ == "__main__":
    t = Thread(target=adding_value)
    t.start()
    app.debug = True
    app.run()
