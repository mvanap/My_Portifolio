from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#vercel handler
def handler(event,context):
    return app

#Local Deployment
if __name__ == "__main__":
    app.run(debug=True)