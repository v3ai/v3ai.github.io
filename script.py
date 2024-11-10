import markdown

top = """
<!DOCTYPE HTML>
<html>
	<head>
		<link rel="stylesheet" href="style-list.css">

	</head>
	<body>
    <h1 class="top" >Todo List</h1>
"""
bottom = """

	</body>
</html>

"""

css = """

body {
	margin: 0;
	max-width: 50em;
	margin: auto;
	padding: 4em;
}

p {
	color: #566b78;
}

h1,
h2,
h3,
h4,
h5 {
    text-align: center;
}

"""

with open('/var/www/rhettapplestone/list.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)
    f.close()

with open ('/var/www/rhettapplestone/list.html', 'w') as f:
    f.write(top)
    f.write(html)
    f.write(bottom)

with open ('/var/www/rhettapplestone/style-list.css', 'w') as f:
    f.write(css)
    f.close()
