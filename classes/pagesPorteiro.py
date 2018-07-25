from classes.db import*
page = Datapages('teste')
page.openDB()
home = """<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Tiago Hérique">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <style>
        footer {
            padding: 1em;
            color: white;
            background-color: rgb(153, 161, 212);
            clear: left;
            text-align: center;
        }
    </style>
    <title>Login</title>
</head>
<body>
    <div align="center">
        <div class="w3-container">
            <h1>Em testes</h1>
            
            <div class="w3-card-4">
                <div class="w3-container w3-blue">
                    <h2>Porteiro</h2>
                </div>
                <form class="w3-container" action="/">
                    <P>
                        <input class="w3-input" type="text" name="Matricula" value="">
                        <label>Matricula</label>
                    </p>
                    <p>
                        <input class="w3-input" type="submit" value="open">
                    </p>
                </form>
            </div>
        </div>
        <br>
        <div class="w3-gray">
            <footer>Copyright &copy; Tiago GIM</footer>
        </div>
    </div>
    </div>
</body>
</html>"""

cadastro = """<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Tiago Hérique">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <style>
        footer {
            padding: 10px;
            color: white;
            background-color: rgb(153, 161, 212);
            clear: left;
            text-align: center;
        }
        .label-permissao {
            font-weight: bolder;
            color: rgb(255, 255, 255);
            background-color: rgb(206, 66, 148);
            margin-bottom: 5px;   
        }
        .label-tag {
            font-weight: bolder;
            color: rgb(255, 255, 255);
            background-color: rgb(2, 42, 65);
            margin-bottom: 5px;
            align-content: center;
        }
        .row {
            display: -webkit-flex;
            display: flex;
            width: 100%;
            height: 100%;
        }
        .col {
            height: 100%;
            width: 100%;
        }
    </style>
    <title>Cadastro</title>
</head>
<body>
    <div align="center">
        <div class="w3-container">
            <h1>Em testes</h1>
            <div class="w3-card-4">
                <div class="w3-container w3-blue">
                    <h2>New member</h2>
                </div>
                <form class="w3-container" action="https://www.w3schools.com/action_page.php" target="_blank" method="POST">
                    <P>
                        <input class="w3-input" type="text" name="Name" value="">
                        <label>Nome</label>
                    </p>
                    <P>
                        <input class="w3-input" type="text" name="Matricula" value="">
                        <label>Matricula</label>
                    </p>
                    <P>
                        <input class="w3-input" type="text" name="project" value="">
                        <label>Projeto</label>
                    </p>
                    <P>
                        <div class="row">
                            <div class="col" style="border: 2px;">
                                <div class="label-tag">
                                    <label>Cadastrar Tag?</label>
                                </div>
                                <input class="w3-input" type="radio" name="Tag" value="yes">SIM
                                <br>
                                <input class="w3-input" type="radio" name="Tag" value="no">NÃO
                            </div>
                            <div class="col">
                                <div class="label-permissao" style=" width:100%;">
                                    <label>Permissão</label>
                                </div>
                                <input class="w3-input" type="radio" name="who" value="Aluno">Aluno
                                <br>
                                <input class="w3-input" type="radio" name="who" value="Professor">Professor
                                <br>
                                <input class="w3-input" type="radio" name="who" value="Others">Outros
                            </div>
                        </div>
                    </p>
                    <p>
                        <input class="w3-input" type="submit" value="Cadastrar">
                    </p>
                </form>
            </div>
        </div>
        <br>
        <div class="w3-gray">
            <footer>Copyright &copy; Tiago GIM</footer>
        </div>
    </div>
    </div>
</body>
</html>"""

page.addPage('cadastro',cadastro)

page.addPage('home',home)
print('fim')