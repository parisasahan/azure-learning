from flask import Flask, render_template_string, request

app = Flask(__name__)

# Netflix-style login HTML
login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Netflix Login</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: url('https://assets.nflxext.com/ffe/siteui/vlv3/6a9b681f-3277-438f-a9a6-719f80120f95/88000d5e-e2e4-4b58-a5c2-217dc8dd7f0e/IN-en-20240318-popsignuptwoweeks-perspective_alpha_website_medium.jpg') no-repeat center center fixed;
            background-size: cover;
            color: white;
        }
        .login-container {
            background-color: rgba(0, 0, 0, 0.75);
            padding: 60px 68px 40px;
            width: 300px;
            margin: 100px auto;
            border-radius: 4px;
        }
        h1 {
            margin-bottom: 30px;
        }
        input[type="email"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            background: #333;
            border: none;
            color: white;
        }
        button {
            width: 100%;
            padding: 10px;
            margin-top: 20px;
            background: #e50914;
            border: none;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }
        .footer {
            margin-top: 20px;
            font-size: 13px;
            color: #aaa;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Sign In</h1>
        <form action="/login" method="POST">
            <input type="email" name="email" placeholder="Email or phone number" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Sign In</button>
        </form>
        <div class="footer">
            New to Netflix? <a href="#" style="color: white;">Sign up now</a>.
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(login_page)

@app.route('/login', methods=['POST'])
def login():
    # You can handle authentication here
    email = request.form.get('email')
    password = request.form.get('password')
    return f"Welcome, {email}! (Password not displayed for security reasons)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
