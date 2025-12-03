from flask import Flask, render_template_string

app = Flask(__name__)

BOOT = """
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Loading</title></head>
<body>
<p>Loading...</p>
<script>
  (function() {
    const d = {{ data }};
    const k = d.map(x => String.fromCharCode(x ^ 7)).join("");
    sessionStorage.setItem("auth_token", k);
    window.location.replace("/home");
  })();
</script>
</body>
</html>
"""

HOME = """
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Home</title></head>
<body>
<h1>Welcome!</h1>
<p>Find the Key!!</p>
</body>
</html>
"""

@app.route("/")
def index():
    key = "9shufog9sudhohijbiueoubid="
    arr = [ord(c) ^ 7 for c in key]
    return render_template_string(BOOT, data=arr)

@app.route("/home")
def home():
    return render_template_string(HOME)

if __name__ == "__main__":
    app.run(debug=True, port=7007,host="0.0.0.0")
