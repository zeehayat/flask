from app import app 

@app.route('/')
@app.route('/index')  

def index():
    user={'username': 'Zeeshan Hayat'}
    return '''
<html><head><title>Home Page Microblogger</title></head>
<body>
<h1> Hello ''' + user.username + '''!</h1>
</body></html>
    '''
    