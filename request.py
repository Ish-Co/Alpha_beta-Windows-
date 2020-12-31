import requests as req

def update():
    rq = req.get("http://192.168.0.14")
    content = rq.text
    print(content)

#uncomment function call for testing!
#update()
