print("Starting HTML generation...")

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Python CI/CD to S3</title>
</head>
<body>
    <h1>✅ SUCCESS: Python generated this page!</h1>
    <p>Deployed using GitHub Actions to AWS S3.</p>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("✅ index.html generated successfully")