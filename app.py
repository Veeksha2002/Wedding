from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def wedding_invitation():
    # Render the Wed.html file from the templates folder
    return render_template("Wed.html")

if __name__ == "__main__":
    app.run(debug=True)
