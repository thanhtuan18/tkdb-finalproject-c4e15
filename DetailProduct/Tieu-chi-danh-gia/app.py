from flask import *
from models.evaluate import Evaluate
import mlab

mlab.connect()

app = Flask(__name__)


@app.route('/danhgiasanpham',methods = ['GET','POST'])
def evaluate():
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
        return "Saved"

if __name__ == '__main__':
  app.run(debug=True)
