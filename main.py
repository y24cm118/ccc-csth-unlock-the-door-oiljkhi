from flask import Flask, request, render_template_string

app = Flask(__name__)

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <style>
      body{
        display: flex;
        justify-content: center;
        align-items:center;
        min-height: 85vh;
        text-align: center;
        font-family: Arial, sans-serif;
        background: #f3f3f3;
      }
      #container{
        background: white;
        padding: 30px 40px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
      }
      input{
        display: block;
        margin: 10px auto;
        padding: 8px;
        width: 200px;
      }
      button{
        padding: 8px 20px;
        cursor: pointer;
      }
      .error-msg{
        margin-top: 15px;
        color: #c0392b;
        font-weight: bold;
      }
    </style>
</head>
<body>
  <div id="container">
    <h1>Member Login</h1>
    <form method="POST">
      <input type="text" name="username" placeholder="Username" required/>
      <input type="password" name="password" placeholder="Password" required/>
      <button type="submit">Login</button>
    </form>

    {% if show_error %}
    <p class="error-msg">
      Server error. Check console for more info.
    </p>
    {% endif %}
  </div>

  <script>
    const showError = {{ show_error | tojson }};
    if (showError) {
      console.error("Server error: 604 Site Not Found");
    }
  </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return render_template_string(LOGIN_PAGE, show_error=True)
    return render_template_string(LOGIN_PAGE, show_error=False)

if __name__ == "__main__":
    app.run(debug=True,port=7000,host="0.0.0.0") 
