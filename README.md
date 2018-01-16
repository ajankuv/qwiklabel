#qwiklabel v1 for vipparcel
---

Uses datamade.us's usaddress lib to parse and format single line USA addresses into a printable label format for shipping.

My wife and I run a online store, and one of our good channels for sales is Mercari. She normally pastes me one line addresses from the app into skype. I have emailed them over and over to have some sort of web based backend for sellers/labels since one line addresses are horrid.


The only things that need to be set are following below.

vipkey="xxxxx"

sfname="xxxxx"

slname="xxxxx"

scompany="xxxxx"

saddress="xxxxx"

scity="xxxxx"

sstate="xxxxx"

spostcode="xxxxx"


These are your sending from details. You need to change these to match where you are sending from.  sfname=firstname slname=lastname and so on.


By default the api url is set to dev, so you don't go spending money on shit postage while testing. Flip these once you feel its ready.


#dev
lurl="https://vipparcel.com/api-test/v1/shipping/label/print"
#prod lurl="https://vipparcel.com/api/v1/shipping/label/print"



required pip installs = flask, usaddress, requests


![alt text](https://i.imgur.com/7RkDBjD.png)



There are a few bugs with the usaddress lib, I have contacted them about it for longer addresses and back country roads.
---
Shout out to @rogerallen on github for providing the dictionary file for states abbreviations https://gist.github.com/rogerallen/1583593

Also to datamade for their badass lib for formatting https://parserator.datamade.us/usaddress
