import requests
import json
import base64
from project.key import Key
from flask import Response
from project import app


class MPI:
  
    mMpiPubKey = ""
    mTrxnId = ""
    mMerchantId = ""
    mUrl = app.config['MPI_URL']
    pubkey = ""

    def __init__(self, mid, trxnId):
        self.mTrxnId = trxnId
        self.mMerchantId = mid

    def InitGw(self):

        headers = { 
            'Content-Type' : 'application/json'
        }

        k = Key(self.mMerchantId, self.mTrxnId)
        k.GenKeys()
        self.pubkey = k.GetPublicKey()
        body = {
            "merchantId" : self.mMerchantId,
            "pubKey" : self.pubkey,
            "purchaseId" : self.mTrxnId
        }

        try:
            url = self.mUrl + "/mkReq"
            r = requests.post(url, headers = headers, data = json.dumps(body), verify=False)
            result=f"{r.status_code} {r.content}"    
            
            #r.content.decode("utf-8") # Convert the binary result to string
            j = json.loads(r.content.decode("utf-8"))

            if j['errorCode'] == '000':
                self.mMpiPubKey = j['pubKey']
                result = self.mTrxnId

        except Exception as e:
            error = str(e)
            result=error
        
        #return Response(result, status=200)
        print(result)
        return result

    def Sign(self, data):

        k = Key()
        k.pubkey = self.pubkey
        return k.Sign(data)

    def KeySign(self, data):

        headers = { 
            'Content-Type' : 'application/json'
        }

        k = Key(self.mMerchantId, self.mTrxnId)
        #k.GenKeys()
        self.pubkey = k.GetPublicKey()
        body = {
            "merchantId" : self.mMerchantId,
            "pubKey" : self.pubkey,
            "purchaseId" : self.mTrxnId
        }

        try:
            url = self.mUrl + "/mkReq"
   
            r = requests.post(url, headers = headers, data = json.dumps(body), verify=False)
            #r.content.decode("utf-8") # Convert the binary result to string
            j = json.loads(r.content.decode("utf-8"))

            print(j)

            # Intentionally removed. To enabled testing
            if j['errorCode'] != '000':
                self.mMpiPubKey = j['pubKey']
                result = self.mTrxnId
                return result

        except Exception as e:
            print("in exception")
            error = str(e)
            print(error)
        
        # No error -> sign it
        return k.Sign(data)