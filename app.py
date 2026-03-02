import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Coming Soon</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #1f2937, #111827);
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            color: white;
            text-align: center;
        }
        .card {
            padding: 3rem;
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 40px rgba(0,0,0,0.4);
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        p {
            opacity: 0.8;
            font-size: 1.1rem;
        }
        .badge {
            margin-top: 2rem;
            font-size: 0.9rem;
            opacity: 0.6;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Coming Soon</h1>
        <p>We’re building something great.<br>Check back soon.</p>
        <div class="badge">© 2026</div>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

