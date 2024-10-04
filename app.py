from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", url_path=request.path)

# @app.route("/about")
# def about():
#     return render_template("about.html")

@app.route("/media")
def media():
    return render_template("media.html", url_path=request.path)

@app.route("/service_management")
def service_management():
    return render_template("service_management.html", url_path=request.path)

@app.route("/custom_services")
def custom_services():
    return render_template("custom_services.html", url_path=request.path)

@app.route("/overseerr")
def overseerr():
    return render_template("overseerr.html", url_path=request.path)

if __name__ == "__main__":
    app.run(debug=True)
