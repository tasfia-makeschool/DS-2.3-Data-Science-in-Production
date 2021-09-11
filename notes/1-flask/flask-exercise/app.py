from flask import Flask, request, jsonify, render_template
from flask_restplus import Api, Resource, fields
from wtforms import Form, FloatField, validators

app = Flask(__name__)

# wt3 forms
class InputForm(Form):
    a = FloatField(validators=[validators.InputRequired()])
    b = FloatField(validators=[validators.InputRequired()])

# flask_restplus, argparse
api = Api(app, version='1.0', title='Add API', description='argparse with flask demonstration')
ns = api.namespace('add', description='Add two numbers')
single_parser = api.parser()
single_parser.add_argument('n', type=int, required=True, help='first number')
single_parser.add_argument('m', type=int, required=True, help='second number')

def get_sum(a,b):
    return a + b

# @app.route("/", methods=["GET", "POST"])
# def index():

    """ command line """
    # a = request.args.get("a", type=int)
    # b = request.args.get("b", type=int)
    # res = get_sum(a, b)
    # return jsonify({ "sum": res})

    """ form """
    # if request.method == "POST":
    #     a = request.form.get("num1", type=int)
    #     b = request.form.get("num2", type=int)
    #     res = get_sum(a, b)
    #     return render_template("index.html", sum=res)
    # else:
    #     return render_template("index.html")
    
    """ wt3 forms """
    # form = InputForm(request.form)
    # if request.method == 'POST' and form.validate():
    #     a = form.a.data
    #     b = form.b.data
    #     s = get_sum(a,b)
    # else:
    #     s = None

    # return render_template("view.html", form=form, s=s)
    
""" restplus """
@ns.route("/")
class Addition(Resource):
    @api.doc(parser=single_parser, description='Enter Two Integers')
    def get(self):
        args = single_parser.parse_args()
        n1 = args.n
        m1 = args.m
        r = get_sum(n1, m1)
        return jsonify({'add': r})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
