
from flask import Flask, render_template, request, json, redirect
import usaddress, requests
from us_state_abbrev import *

#vipparcel sending from details + api key
vipkey="xxxxx"
sfname="xxxxx"
slname="xxxxx"
scompany="xxxxx"
saddress="xxxxx"
scity="xxxxx"
sstate="xxxxx"
spostcode="xxxxx"


#dev
lurl="https://vipparcel.com/api-test/v1/shipping/label/print"
#prod lurl="https://vipparcel.com/api/v1/shipping/label/print"

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cklabel', methods=['POST'])
def cklabel():
 if request.method == 'POST':
    rawaddress = request.form['addressraw']
    formatad = usaddress.tag(rawaddress)
    firstn, lastn = formatad[0]['Recipient'].split()
    return render_template('cklabel.html', fname=(firstn),lname=(lastn),zip=(formatad[0]['ZipCode']),addnum=(formatad[0]['AddressNumber']),addnam=(formatad[0]['StreetName']),addnst=(formatad[0]['StreetNamePostType']),state=(formatad[0]['StateName']),city=(formatad[0]['PlaceName']))


@app.route('/printlab', methods=['POST'])
def printlab():
     if request.method == 'POST':
         lfname = request.form['first_name']
         llname = request.form['last_name']
         fullstate = request.form['state']
         lstate = us_state_abbrev.get(fullstate)
         lcity = request.form['city']
         laddress = request.form['shipping_address']
         lzip = request.form['zip']
         llb = request.form['lbs']
         loz = request.form['ozs']
         lw = (int(llb)*16)
         headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
         labela = {
            "authToken": vipkey,
            "labelType": "domestic",
             "mailClass": "MediaMail",
             "weightOz": lw,
             "description": "Books and Comics",
             "sender": {
                "firstName": sfname,
                "lastName": slname,
                "streetAddress": saddress,
                "city": scity,
                "state": sstate,
                "postalCode": spostcode
                        },
             "recipient": {
                "state": lstate,
                "firstName": lfname,
                "lastName": llname,
                "streetAddress": laddress,
                "city": lcity,
                "postalCode": lzip
                          }
                    }

         r = requests.post(lurl, data=json.dumps(labela), headers=headers)
         dump = r.json()
         lid = dump['id']
         vipurl = ("https://vipparcel.com/package/detailed/" + str(lid))
         return render_template('labelprint.html', url=(vipurl))
     else:
         return """<html><body><h1>No Post data homeslice</h1></body></html>"""

@app.route('/error')
def error():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5611, passthrough_errors=True)
