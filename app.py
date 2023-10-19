from flask import Flask

app = Flask(__name__)

@app.route("/")
# @ is a decorator
def hello_world():
    return "<p>Hello, world!</p>"

print("hello world")

if __name__=="__main__":
  print("i'm inside the if now")
  app.run(host="0.0.0.0",debug=True)#host is 0.0.0.0 so that the app runs locally
  