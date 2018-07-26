from flask import Flask, render_template
import socket
import datetime
import psutil

app = Flask(__name__)

sname=socket.gethostname()

sdate=datetime.datetime.now().strftime("%Y-%m-%d")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

sip=get_ip()

posts =[{'sname':sname,'sdate':sdate,'sip':sip}]

@app.route('/')
def home():
	stime=datetime.datetime.now().strftime("%H:%M:%S")
	scpu=str(psutil.cpu_percent(interval=0))

	dyv =[{'stime':stime,'scpu':scpu}]

	return render_template('home.html', posts=posts, dyv=dyv)

if __name__ == '__main__':
	app.run(debug=True)