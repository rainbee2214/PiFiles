import sys
from twilio.rest import TwilioRestClient
 
def sendSMS(message):
    # Your Account Sid and Auth Token from twilio.com/user/account
    fromNumber = "+19027019415"
    toNumber = "+19028188219"
    account_sid = "AC159a87ecb340d7f1791f2959c9a951fa"
    auth_token  = "d96192096e44d9dd87c3f4e8aaafa8cd"
    client = TwilioRestClient(account_sid, auth_token)
     
    message = client.messages.create(body=message,
        to=toNumber,    
        from_=fromNumber) 

def main(argv):
    script, message = sys.argv
    sendSMS(message)

if __name__ == "__main__":
   main(sys.argv[1:])