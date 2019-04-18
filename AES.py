import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
import os
#Padding
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

#AES MODE = CBC
class CBC:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv)
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:]))
#AES MODE = ECB
class ECB:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_ECB )
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt( enc[16:]))

#AES MODE = OFB
class OFB:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_OFB, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_OFB , iv )
        return unpad(cipher.decrypt( enc[16:]))

#AES MODE = CTR
class CTR:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        ctr = Counter.new(128)
        cipher = AES.new( self.key, AES.MODE_CTR, counter =ctr )
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        ctr = Counter.new(128)
        cipher = AES.new(self.key, AES.MODE_CTR, counter = ctr )
        return unpad(cipher.decrypt( enc[16:]))


key = os.urandom(16)
C=CBC(key).encrypt('NikhilBishnoi')
print(C)
C=CBC(key).decrypt(C)
print(C)
C=ECB(key).encrypt('NikhilBishnoi')
print(C)
C=ECB(key).decrypt(C)
print(C)
C=OFB(key).encrypt('NikhilBishnoi')
print(C)
C=OFB(key).decrypt(C)
print(C)
C=CTR(key).encrypt('NikhilBishnoi')
print(C)
C=CTR(key).decrypt(C)
print(C)
