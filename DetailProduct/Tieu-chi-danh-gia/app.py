from flask import *
from models.evaluate import Evaluate
import mlab

mlab.connect()

app = Flask(__name__)


@app.route('/danhgiasanpham',methods = ['GET','POST'])
def evaluate():
    designlist = []
    screenlist = []
    funclist = []
    explist = []
    camlist = []
    pinlist = []

    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        form = request.form
        design = int(form['design'])
        screen = int(form['screen'])
        func = int(form['func'])
        exp = int(form['exp'])
        cam = int(form['cam'])
        pin = int(form['pin'])
        comment = form['comment']

        new_eva = Evaluate(design = design,
                           screen = screen,
                           func = func,
                           exp = exp,
                           cam = cam,
                           pin = pin,
                           comment = comment)

        new_eva.save()

        totalEva = Evaluate.objects()
        for object in totalEva:
            designlist.append(object['design'])
            screenlist.append(object['screen'])
            funclist.append(object['func'])
            explist.append(object['exp'])
            camlist.append(object['cam'])
            pinlist.append(object['pin'])

        designsum = sum(designlist)
        avgdesign = designsum / len(designlist)
        screensum = sum(screenlist)
        avgscreen = screensum/ len(designlist)
        funcsum = sum(funclist)
        avgfunc = funcsum / len(designlist)
        expsum = sum(explist)
        avgexp = expsum / len(designlist)
        camsum = sum(camlist)
        avgcam = camsum / len(designlist)
        pinsum = sum(pinlist)
        avgpin = pinsum / len(designlist)
        total = avgdesign + avgscreen + avgfunc + avgexp + avgcam + avgpin

        average = total / 6

        return render_template("index.html", average = average)

if __name__ == '__main__':
  app.run(debug=True)
