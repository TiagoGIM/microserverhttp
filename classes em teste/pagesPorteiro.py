from db import*
page = Datapages('teste')
page.openDB()
home = """<!DOCTYPE html>
<html>
<head>
    <title>PORTA LAR</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>

<body>
    <div class="w3-container">
        <h1>Em testes</h1>
        <div class="w3-card-4">
            <div class="w3-container w3-green">
                <h2>Porteiro</h2>
            </div>
            <form class="w3-container" action="/">
                <P>
                    <input class="w3-input" type="text" name="Matricula" value="">
                    <label>Matricula</label>
                </p>
                <p>
                    <input  class="w3-input" type="submit" value="try open">
                </p>
            </form>
        </div>
    </div>
    <footer>
        <p> by: Tiago Herique </p>
    </footer></body>
</html>"""

page.addPage('home',home)