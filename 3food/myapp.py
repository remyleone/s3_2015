#!/usr/bin/env python

import time
import subprocess
from threading import Thread

import redis
import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

r = redis.Redis()
key = "base1"


def update_picture(x, y):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y)
    fig.savefig("static/graph.png")


def update(sleep=10, delta=5):
    while True:
        temp = float(subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"]).strip("temp='C\n"))
        r.rpush(key, temp)
        temp_list_length = r.llen(key)
        update_picture(
            x=range(temp_list_length - delta, temp_list_length),
            y=r.lrange(key, temp_list_length - delta, temp_list_length),
        )
        time.sleep(sleep)


@app.route("/", methods=['GET'])
def main(delta=5):
    temp_list_length = r.llen(key)
    d = r.lrange(key, temp_list_length - delta, temp_list_length)
    return render_template("template.html",
                           temperatures=d,
                           delta=delta,
                           )


if __name__ == "__main__":
    t = Thread(target=update)
    t.start()
    app.debug = True
    app.run()
