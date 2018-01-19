# qwiklabel v1 for vipparcel
---

Uses datamade.us's usaddress lib to parse and format single line USA addresses into a printable label format for shipping.

My wife and I run a online store, and one of our good channels for sales is Mercari. She normally pastes me one line addresses from the app into skype. I have emailed them over and over to have some sort of web based backend for sellers/labels since one line addresses are horrid.


The only things that need to be set are following below.

`vipkey="xxxxx"  <br />
sfname="xxxxx"  <br />
slname="xxxxx"  <br />
scompany="xxxxx"  <br />
saddress="xxxxx"  <br />
scity="xxxxx"  <br />
sstate="xxxxx"  <br />
spostcode="xxxxx"`


These are your sending from details. You need to change these to match where you are sending from.  sfname=firstname slname=lastname and so on.


By default the api url is set to dev, so you don't go spending money on shit postage while testing. Flip these once you feel its ready.

`
#dev
lurl="https://vipparcel.com/api-test/v1/shipping/label/print"
#prod lurl="https://vipparcel.com/api/v1/shipping/label/print"`



### required pip installs = flask, usaddress, requests



There are a few bugs with the usaddress lib, I have contacted them about it for longer addresses and back country roads.
---
Shout out to @rogerallen on github for providing the dictionary file for states abbreviations https://gist.github.com/rogerallen/1583593

Also to datamade for their badass lib for formatting https://parserator.datamade.us/usaddress




![alt text](https://i.imgur.com/7RkDBjD.png)


Will convert address from "joe shmoe 1231 turtle rd. Miami Florida 33492" to


Joe Shmoe </br>
1231 turtle rd. </br>
Miami Florida 33492 </br>


For shipping label printing.


---
## Running the software

You can run this anyway you wish, I was running this just as `"python server.py"` off my mac for awhile just to ship fast. I ended up dockerizing it after finding the need to have it run 24/7.

By default it runs on port 5611

I prefer to run it via docker on my vm server. Here is how below..

`docker build --no-cache -t qwiklabel && docker run --name qwiklabel -p 5611:5611 qwiklabel`
