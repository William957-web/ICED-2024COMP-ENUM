from flask import *
app = Flask(__name__)

@app.route('/')
def main():
    response = make_response(redirect('/@1'))
    return response

@app.route('/@<id>')
def chk(id):
  if id=="523":
    return "ICED{3nUmeration_is_a_basic_sk1ll_4_h@cK3Rs}"
  else:
    return "Wrong ID qq"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
