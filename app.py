from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jenkins CI/CD on k3s</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f4f8;
                text-align: center;
                margin-top: 100px;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 18px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Welcome to Jenkins CI/CD on k3s!</h1>
        <p>Your deployment is up and running.</p>
    </body>
    </html>
    """)

@app.route('/healthz')
def healthz():
    return "OK", 200

@app.route('/readyz')
def readyz():
    return "READY", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
