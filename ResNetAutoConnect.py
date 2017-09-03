try:
    import httplib
except:
    import http.client as httplib
import requests

#change your password here
password="password"
#change your username here
user="user"

def have_internet():
    conn = httplib.HTTPConnection("www.bing.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        resp = conn.getresponse()
        print(resp.getcode())
        conn.close()
        if resp.getcode() == 302:
            print("Need login")
            return False
        else:
            print("Connected")
            return True
    except:
        conn.close()
        print("Disconnected")
        return False


if not have_internet():
    payload = {"Login": "Log In",
               "cmd": "authenticate",
               "password":  password,
               "user": user}
    r = requests.post("https://securelogin.net.cuhk.edu.hk/cgi-bin/login", data=payload, verify=False)
    print(r.status_code)
    # print(r.headers)
    # print(r.text)
