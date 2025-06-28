# hi i am Sameer Mishra i us in this code flask , pyperclip and pyshorteners
# A simple Flask app to shorten URLs using pyshorteners and copy using pyperclip

from flask import Flask, render_template, request
import pyshorteners
import pyperclip

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    error = None

    if request.method == "POST":
        long_url = request.form.get("long_url")

        if long_url and long_url.startswith("http"):
            try:
                s = pyshorteners.Shortener()
                short_url = s.tinyurl.short(long_url)

                # Copy to clipboard
                pyperclip.copy(short_url)

            except Exception as e:
                error = f"❌ Error: {e}"
        else:
            error = "⚠️ Please enter a valid URL starting with http:// or https://"

    return render_template("index.html", short_url=short_url, error=error)

if __name__ == "__main__":
    app.run(debug=True)
