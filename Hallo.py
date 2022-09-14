from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
from crypt import methods
from typing import ParamSpecKwargs
from flask import Flask
import datetime
import jdatetime
from time import sleep

dam = datetime.datetime.now()
ym = dam.year
mm = dam.month
sm = dam.day

from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import os

app = Flask(__name__)


@app.route('/login/')
def log_in(name=None):
    return render_template('post.html', name=name)






@app.route("/", methods=['GET', 'POST'])
def Hallo(name=None):
    print("debug")
    var = False
    ip = request.remote_addr
    print("debug")
    #--------------------------------------
    ww = open("ip.html", "w")
    ww.write(ip)
    ww.close()
    # --------------------------------------
    gam1 = request.form.get('gam11')
    gam2 = request.form.get('gam22')
    gamm = request.form.get('gammm')
    print("________________")

    men1 = request.form.get('men11')
    men2 = request.form.get('men22')
    menn = request.form.get('mennn')
    print("debug")

    zab1 = request.form.get('zab1')
    zab2 = request.form.get('zab2')
    zabb = request.form.get('zabb')
    print("debug")

    tag1 = request.form.get('tag1')
    tag2 = request.form.get('tag2')
    tagg = request.form.get('tagg')
    print("debug")

    bag1 = request.form.get('bag1')
    bag2 = request.form.get('bag2')
    bagg = request.form.get('bagg')
    print("debug")

    tav1 = request.form.get('tav1')
    tav2 = request.form.get('tav2')
    tavv = request.form.get('tavv')
    print("debug")

    lest = [gam1, men1, zab1, tag1, bag1, tav1]

    print("debug")
    a = datetime.datetime.now()
    n = -1
    
    for i in lest:
        n += 1
        print(i)
        print(n)
        if i != None:
            if n == 0:
                # gam
                f = open(f"{ip}.txt", "a")
                a1 = f"((({a})))|||(({gam1}))++++(({gam2}))===((((({gamm}))))) \n"
                f.write(a1)
                f.close()


                pass
            if n == 1:
                # men
                f = open(f"{ip}.txt", "a")
                a1 = f"((({a})))|||(({men1}))----(({men2}))=((((({menn}))))) \n"
                f.write(a1)
                f.close()
                

                pass
            if n == 2:
                # zab
                f = open(f"{ip}.txt", "a")
                a1 = f"((({a})))|||(({zab1}))****(({zab2}))=((((({zabb}))))) \n"
                f.write(a1)
                f.close()

                pass
            if n == 3:
                # tag
                f = open(f"{ip}.txt", "a")
                a1 = f"((({a})))|||(({tag1}))÷÷÷÷(({tag2}))=((((({tagg}))))) \n"
                f.write(a1)
                f.close()

                pass
            if n == 4:
                # bag
                f = open(f"{ip}.txt", "a")
                a1 = f"((({a})))|||(({bag1}))%%%%(({bag2}))=((((({bagg}))))) \n"
                f.write(a1)
                f.close()

                pass
            if n == 5:
                # tav
                f = open(f"{ip}.txt", "a")
                print("----------------------------")
                print(tav1)
                print(tav2)
                print("----------------------------")
                a1 = f"((({a})))|||(({tav1}))tavan^(({tav2}))=((((({tavv}))))) \n"
                f.write(a1)
                f.close()

                pass
                

    ip = request.remote_addr
    ff=open(ip+".txt","a")
    ff.close()
    ff=open(ip+".txt","r")
    d=ff.read()
    data={
        "da":d,
        "gam":gamm,
        "gam1":gam1,
        "gam2":gam2,
        "men":menn,
        'men1':men1,
        'men2':men2,
        "zab":zabb,
        "zab1":zab1,
        "zab2":zab2,
        "tag":tagg,
        "tag1":tag1,
        "tag2":tag2,
        "bag":bagg,
        "bag1":bag1,
        "bag2":bag2,
        "tav":tavv,
        "tav1":tav1,
        "tav2":tav2

    }
    return render_template("home.html", name=name,data=data)
    ff.close()


@app.route("/login/", methods=['GET', 'POST'])
def login():
    print("------------------------------------")
    print("Hi")
    print(request.form['email'], request.form['pass'])
    print("------------------------------------")
    if request.form['email'] == 'test@test.ts' and request.form['pass'] == 'cplasplas':
        return "<p> logged in </p>"
    else:
        return "<p> wrong </p>"
@app.route('/json/',methods=['GET','POST'])
def jsan():
    return r'./package.json'
