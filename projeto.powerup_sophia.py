from flask import Flask, request, redirect, url_for, render_template_string, session

app = Flask(__name__)
app.secret_key = "power_up_sophia_2026"


# =========================================================
# BANCO DE EXERCÍCIOS
# =========================================================

EXERCICIOS = {

    "gluteos": [
        {
            "nome": "Elevação de quadril",
            "imagem": "elevacao_quadril.jpg",
            "musculos": "Glúteos",
            "execucao": "Apoie as costas, mantenha os pés firmes no chão e eleve o quadril de forma controlada."
        },
        {
            "nome": "Abdução de quadril",
            "imagem": "abducao_quadril.jpg",
            "musculos": "Glúteo médio e glúteo mínimo",
            "execucao": "Mantenha o tronco estável e afaste as pernas lateralmente de maneira controlada."
        },
        {
            "nome": "Extensão de quadril",
            "imagem": "extensao_quadril.jpg",
            "musculos": "Glúteos",
            "execucao": "Leve a perna para trás mantendo o movimento controlado e o tronco estável."
        },
        {
            "nome": "Agachamento",
            "imagem": "agachamento.jpg",
            "musculos": "Glúteos e pernas",
            "execucao": "Mantenha os pés firmes, flexione os joelhos e quadris e retorne de forma controlada."
        },
        {
            "nome": "Stiff",
            "imagem": "stiff.jpg",
            "musculos": "Glúteos e posteriores",
            "execucao": "Incline o tronco mantendo a coluna estável e retorne controladamente."
        }
    ],

    "quadriceps": [
        {
            "nome": "Agachamento",
            "imagem": "agachamento.jpg",
            "musculos": "Quadríceps e glúteos",
            "execucao": "Flexione os joelhos e quadris mantendo o movimento controlado."
        },
        {
            "nome": "Leg press",
            "imagem": "leg_press.jpg",
            "musculos": "Quadríceps, glúteos e posteriores",
            "execucao": "Empurre a plataforma de maneira controlada, sem realizar movimentos bruscos."
        },
        {
            "nome": "Cadeira extensora",
            "imagem": "cadeira_extensora.jpg",
            "musculos": "Quadríceps",
            "execucao": "Estenda os joelhos de maneira controlada e retorne lentamente."
        }
    ],

    "posteriores": [
        {
            "nome": "Mesa flexora",
            "imagem": "mesa_flexora.jpg",
            "musculos": "Posteriores da coxa",
            "execucao": "Flexione os joelhos de maneira controlada e retorne lentamente."
        },
        {
            "nome": "Stiff",
            "imagem": "stiff.jpg",
            "musculos": "Posteriores e glúteos",
            "execucao": "Mantenha a coluna estável durante a inclinação do tronco."
        },
        {
            "nome": "Flexão nórdica",
            "imagem": "flexao_nordica.jpg",
            "musculos": "Posteriores da coxa",
            "execucao": "Realize o movimento lentamente, mantendo o controle durante a descida."
        }
    ],

    "panturrilhas": [
        {
            "nome": "Elevação de panturrilha",
            "imagem": "elevacao_panturrilha.jpg",
            "musculos": "Panturrilhas",
            "execucao": "Eleve os calcanhares e retorne lentamente à posição inicial."
        },
        {
            "nome": "Panturrilha no leg press",
            "imagem": "panturrilha_leg_press.jpg",
            "musculos": "Panturrilhas",
            "execucao": "Movimente os pés de forma controlada, realizando a elevação dos calcanhares."
        }
    ],

    "costas": [
        {
            "nome": "Puxada frontal",
            "imagem": "puxada_frontal.jpg",
            "musculos": "Costas",
            "execucao": "Puxe a barra em direção ao tronco mantendo os movimentos controlados."
        },
        {
            "nome": "Remada baixa",
            "imagem": "remada_baixa.jpg",
            "musculos": "Costas",
            "execucao": "Puxe o equipamento em direção ao tronco mantendo a postura estável."
        },
        {
            "nome": "Remada unilateral",
            "imagem": "remada_unilateral.jpg",
            "musculos": "Costas",
            "execucao": "Puxe o peso em direção ao corpo mantendo o tronco estável."
        },
        {
            "nome": "Pulldown",
            "imagem": "pulldown.jpg",
            "musculos": "Costas",
            "execucao": "Puxe o equipamento para baixo de maneira controlada."
        }
    ],

    "peito": [
        {
            "nome": "Supino",
            "imagem": "supino.jpg",
            "musculos": "Peitoral",
            "execucao": "Empurre o equipamento de maneira controlada e retorne lentamente."
        },
        {
            "nome": "Crucifixo",
            "imagem": "crucifixo.jpg",
            "musculos": "Peitoral",
            "execucao": "Abra e feche os braços de maneira controlada."
        },
        {
            "nome": "Flexão de braços",
            "imagem": "flexao.jpg",
            "musculos": "Peitoral, braços e ombros",
            "execucao": "Mantenha o corpo alinhado e realize a flexão de forma controlada."
        }
    ],

    "ombros": [
        {
            "nome": "Elevação lateral",
            "imagem": "elevacao_lateral.jpg",
            "musculos": "Ombros",
            "execucao": "Eleve os braços lateralmente até uma posição confortável e retorne lentamente."
        },
        {
            "nome": "Desenvolvimento de ombros",
            "imagem": "desenvolvimento_ombros.jpg",
            "musculos": "Ombros",
            "execucao": "Empurre o equipamento para cima mantendo o movimento controlado."
        },
        {
            "nome": "Elevação frontal",
            "imagem": "elevacao_frontal.jpg",
            "musculos": "Ombros",
            "execucao": "Eleve os braços à frente de maneira controlada."
        }
    ],

    "biceps": [
        {
            "nome": "Rosca direta",
            "imagem": "rosca_direta.jpg",
            "musculos": "Bíceps",
            "execucao": "Flexione os cotovelos mantendo os braços estáveis."
        },
        {
            "nome": "Rosca martelo",
            "imagem": "rosca_martelo.jpg",
            "musculos": "Bíceps e antebraços",
            "execucao": "Flexione os cotovelos mantendo as mãos em posição neutra."
        },
        {
            "nome": "Rosca alternada",
            "imagem": "rosca_alternada.jpg",
            "musculos": "Bíceps",
            "execucao": "Realize a flexão dos cotovelos alternando os braços."
        }
    ],

    "triceps": [
        {
            "nome": "Tríceps na polia",
            "imagem": "triceps_polia.jpg",
            "musculos": "Tríceps",
            "execucao": "Estenda os cotovelos mantendo os braços próximos ao corpo."
        },
        {
            "nome": "Tríceps francês",
            "imagem": "triceps_frances.jpg",
            "musculos": "Tríceps",
            "execucao": "Flexione e estenda os cotovelos de maneira controlada."
        }
    ],

    "abdomen": [
        {
            "nome": "Abdominal tradicional",
            "imagem": "abdominal.jpg",
            "musculos": "Abdômen",
            "execucao": "Realize a flexão do tronco de maneira controlada, evitando movimentos bruscos."
        },
        {
            "nome": "Prancha",
            "imagem": "prancha.jpg",
            "musculos": "Abdômen e estabilizadores",
            "execucao": "Mantenha o corpo alinhado e sustente a posição com controle."
        },
        {
            "nome": "Abdominal bicicleta",
            "imagem": "abdominal_bicicleta.jpg",
            "musculos": "Abdômen",
            "execucao": "Realize o movimento de forma controlada, mantendo a postura estável."
        }
    ]
}


# =========================================================
# RELAÇÃO ENTRE GRUPOS
# =========================================================

GRUPOS_RELACIONADOS = {
    "gluteos": ["posteriores", "quadriceps"],
    "quadriceps": ["gluteos", "posteriores"],
    "posteriores": ["gluteos", "quadriceps"],
    "costas": ["biceps"],
    "peito": ["triceps"],
    "ombros": ["triceps"],
    "biceps": ["costas"],
    "triceps": ["peito"],
    "panturrilhas": ["quadriceps"],
    "abdomen": []
}


# =========================================================
# LOGIN
# =========================================================

LOGIN_HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Power Up | Login</title>

<style>

* {
    box-sizing: border-box;
}

html {
    width: 100%;
    overflow-x: hidden;
}

body {
    margin: 0;
    width: 100%;
    min-height: 100vh;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #eee8ff, #ffffff, #f5efff);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #30263d;
    overflow-x: hidden;
}

.container {
    width: 950px;
    max-width: 94%;
    min-height: 580px;
    background: white;
    border-radius: 30px;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(83, 54, 150, 0.15);
    display: grid;
    grid-template-columns: 45% 55%;
}

.lado-esquerdo {
    background: linear-gradient(145deg, #7046d8, #9270e8);
    color: white;
    padding: 55px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.lado-esquerdo h1 {
    font-size: 48px;
    margin: 0 0 15px;
}

.lado-esquerdo p {
    line-height: 1.6;
    opacity: .9;
}

.icone {
    font-size: 65px;
    margin-bottom: 15px;
}

.lado-direito {
    padding: 55px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.logo {
    color: #7046d8;
    font-size: 30px;
    font-weight: bold;
}

h2 {
    font-size: 30px;
    margin-bottom: 8px;
}

.subtitulo {
    color: #777;
    margin-bottom: 25px;
}

input {
    width: 100%;
    padding: 14px;
    margin-bottom: 15px;
    border: 1px solid #ddd;
    border-radius: 12px;
    outline: none;
    font-size: 15px;
}

input:focus {
    border-color: #7046d8;
}

button {
    width: 100%;
    padding: 15px;
    border: none;
    border-radius: 13px;
    background: #7046d8;
    color: white;
    font-weight: bold;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background: #5d35c1;
}

.cadastro {
    text-align: center;
    margin-top: 20px;
    color: #777;
}

.cadastro a {
    color: #7046d8;
    font-weight: bold;
    text-decoration: none;
}

@media (max-width: 750px) {

    body {
        padding: 15px;
        align-items: flex-start;
    }

    .container {
        width: 100%;
        max-width: 100%;
        min-height: auto;
        display: block;
        border-radius: 22px;
        margin: 20px auto;
    }

    .lado-esquerdo {
        display: block;
        padding: 35px 25px;
        text-align: center;
    }

    .lado-esquerdo h1 {
        font-size: 36px;
    }

    .lado-esquerdo p {
        font-size: 14px;
    }

    .icone {
        font-size: 50px;
    }

    .lado-direito {
        padding: 30px 25px;
    }

    h2 {
        font-size: 25px;
    }

    input,
    button {
        font-size: 16px;
        padding: 14px;
    }
}

@media (max-width: 400px) {

    body {
        padding: 8px;
    }

    .container {
        margin: 10px auto;
    }

    .lado-esquerdo {
        padding: 25px 18px;
    }

    .lado-direito {
        padding: 25px 18px;
    }

    .lado-esquerdo h1 {
        font-size: 31px;
    }

    h2 {
        font-size: 23px;
    }
}

</style>

</head>

<body>

<div class="container">

    <div class="lado-esquerdo">

        <div class="icone">💜</div>

        <h1>POWER UP</h1>

        <p>
            Seu espaço para organizar seus treinos,
            descobrir exercícios e acompanhar seu
            planejamento semanal.
        </p>

        <p>
            ✨ Treinos personalizados<br>
            🤖 Assistente Wendy<br>
            📅 Planejamento semanal
        </p>

    </div>

    <div class="lado-direito">

        <div class="logo">POWER UP</div>

        <h2>Bem-vinda de volta!</h2>

        <p class="subtitulo">
            Entre para acessar seu planejamento.
        </p>

        <form method="POST">

            <input
                type="email"
                name="email"
                placeholder="E-mail"
                required
            >

            <input
                type="password"
                name="senha"
                placeholder="Senha"
                required
            >

            <button type="submit">
                Entrar
            </button>

        </form>

        <div class="cadastro">
            Ainda não possui uma conta?
            <a href="/cadastro">Criar conta</a>
        </div>

    </div>

</div>

</body>
</html>
"""


# =========================================================
# CADASTRO
# =========================================================

CADASTRO_HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Power Up | Cadastro</title>

<style>

* {
    box-sizing: border-box;
}

html,
body {
    width: 100%;
    overflow-x: hidden;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #eee8ff, #ffffff);
    color: #30263d;
    padding: 20px 0;
}

.container {
    width: 650px;
    max-width: 94%;
    margin: 25px auto;
    background: white;
    padding: 45px;
    border-radius: 28px;
    box-shadow: 0 15px 45px rgba(83, 54, 150, .12);
}

.logo {
    text-align: center;
    color: #7046d8;
    font-size: 32px;
    font-weight: bold;
}

h1 {
    text-align: center;
    margin-bottom: 8px;
}

.subtitulo {
    text-align: center;
    color: #777;
    margin-bottom: 30px;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
}

.campo {
    display: flex;
    flex-direction: column;
}

.campo-largo {
    grid-column: 1 / 3;
}

label {
    font-size: 14px;
    font-weight: bold;
    margin-bottom: 7px;
}

input {
    width: 100%;
    padding: 13px;
    border: 1px solid #ddd;
    border-radius: 11px;
    font-size: 15px;
    outline: none;
}

input:focus {
    border-color: #7046d8;
}

button {
    width: 100%;
    margin-top: 25px;
    padding: 15px;
    border: none;
    border-radius: 12px;
    background: #7046d8;
    color: white;
    font-weight: bold;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background: #5d35c1;
}

.voltar {
    display: block;
    text-align: center;
    margin-top: 20px;
    color: #7046d8;
    text-decoration: none;
    font-weight: bold;
}

@media (max-width: 600px) {

    body {
        padding: 10px 0;
    }

    .container {
        width: 95%;
        max-width: 100%;
        margin: 20px auto;
        padding: 28px 20px;
        border-radius: 20px;
    }

    .logo {
        font-size: 27px;
    }

    h1 {
        font-size: 25px;
    }

    .subtitulo {
        font-size: 14px;
    }

    .grid {
        grid-template-columns: 1fr;
        gap: 14px;
    }

    .campo-largo {
        grid-column: auto;
    }

    input {
        width: 100%;
        font-size: 16px;
        padding: 14px;
    }

    button {
        padding: 15px;
        font-size: 16px;
    }
}

@media (max-width: 400px) {

    .container {
        width: 96%;
        padding: 24px 16px;
    }

    h1 {
        font-size: 23px;
    }
}

</style>

</head>

<body>

<div class="container">

    <div class="logo">POWER UP 💜</div>

    <h1>Crie sua conta</h1>

    <p class="subtitulo">
        Preencha seus dados para começar.
    </p>

    <form method="POST">

        <div class="grid">

            <div class="campo campo-largo">
                <label>Nome completo</label>
                <input type="text" name="nome" required>
            </div>

            <div class="campo">
                <label>E-mail</label>
                <input type="email" name="email" required>
            </div>

            <div class="campo">
                <label>Telefone</label>
                <input type="tel" name="telefone" required>
            </div>

            <div class="campo">
                <label>CEP</label>
                <input type="text" name="cep" required>
            </div>

            <div class="campo">
                <label>Data de nascimento</label>
                <input type="date" name="nascimento" required>
            </div>

            <div class="campo campo-largo">
                <label>Academia onde você treina</label>
                <input
                    type="text"
                    name="academia"
                    placeholder="Ex.: Nova Fit"
                    required
                >
            </div>

            <div class="campo">
                <label>Senha</label>
                <input type="password" name="senha" required>
            </div>

            <div class="campo">
                <label>Confirmar senha</label>
                <input type="password" name="confirmar" required>
            </div>

        </div>

        <button type="submit">
            Criar minha conta
        </button>

    </form>

    <a class="voltar" href="/">
        Já tenho uma conta
    </a>

</div>

</body>

</html>
"""


# =========================================================
# HOME
# =========================================================

HOME_HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Power Up</title>

<style>

* {
    box-sizing: border-box;
}

html,
body {
    width: 100%;
    overflow-x: hidden;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f7f5ff;
    color: #30263d;
}

header {
    min-height: 75px;
    background: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 65px;
    box-shadow: 0 3px 15px rgba(0,0,0,.06);
}

.logo {
    color: #7046d8;
    font-size: 28px;
    font-weight: bold;
}

nav {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
}

nav a {
    color: #5f5869;
    text-decoration: none;
    margin-left: 28px;
    font-weight: 600;
}

nav a:hover {
    color: #7046d8;
}

.hero {
    max-width: 1100px;
    margin: 0 auto;
    padding: 75px 25px 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 40px;
}

.hero-text {
    max-width: 620px;
}

.tag {
    display: inline-block;
    background: #ebe3ff;
    color: #7046d8;
    padding: 8px 14px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: bold;
}

h1 {
    font-size: 47px;
    line-height: 1.1;
    margin: 18px 0;
}

h1 span {
    color: #7046d8;
}

.hero p {
    color: #6f6879;
    font-size: 18px;
    line-height: 1.6;
}

.botao {
    display: inline-block;
    margin-top: 20px;
    padding: 16px 28px;
    background: #7046d8;
    color: white;
    text-decoration: none;
    border-radius: 13px;
    font-weight: bold;
    box-shadow: 0 8px 20px rgba(112,70,216,.25);
}

.botao:hover {
    background: #5d35c1;
}

.hero-card {
    width: 290px;
    background: linear-gradient(145deg, #7046d8, #a188ed);
    border-radius: 30px;
    padding: 35px;
    color: white;
    box-shadow: 0 15px 35px rgba(112,70,216,.25);
}

.hero-card .emoji {
    font-size: 60px;
}

.hero-card h2 {
    margin: 15px 0 8px;
}

.cards {
    max-width: 1100px;
    margin: 30px auto;
    padding: 0 25px 80px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.card {
    background: white;
    padding: 27px;
    border-radius: 22px;
    box-shadow: 0 7px 25px rgba(0,0,0,.06);
}

.card .icon {
    font-size: 32px;
}

.card h3 {
    color: #7046d8;
}

.card p {
    color: #777;
    line-height: 1.5;
}

/* WENDY */

.wendy-button {
    position: fixed;
    right: 28px;
    bottom: 28px;
    width: 78px;
    height: 78px;
    border-radius: 50%;
    border: 5px solid white;
    background: linear-gradient(145deg, #7046d8, #9b80e8);
    box-shadow: 0 8px 25px rgba(0,0,0,.18);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 40px;
    cursor: pointer;
    z-index: 20;
}

.wendy-msg {
    position: fixed;
    right: 28px;
    bottom: 120px;
    background: white;
    padding: 14px 18px;
    border-radius: 18px;
    box-shadow: 0 7px 25px rgba(0,0,0,.12);
    z-index: 19;
    max-width: 240px;
    font-size: 14px;
}

.wendy-msg strong {
    color: #7046d8;
}

@media (max-width: 800px) {

    header {
        min-height: auto;
        padding: 18px 20px;
        flex-direction: column;
        gap: 15px;
    }

    .logo {
        font-size: 25px;
    }

    nav {
        width: 100%;
        justify-content: center;
        gap: 6px;
    }

    nav a {
        margin-left: 0;
        font-size: 14px;
        padding: 7px 8px;
    }

    .hero {
        width: 100%;
        padding: 40px 20px 20px;
        flex-direction: column;
        text-align: center;
        gap: 30px;
    }

    .hero-text {
        width: 100%;
        max-width: 100%;
    }

    h1 {
        font-size: 35px;
    }

    .hero p {
        font-size: 16px;
    }

    .botao {
        width: 100%;
        max-width: 320px;
    }

    .hero-card {
        width: 100%;
        max-width: 350px;
        padding: 28px;
    }

    .cards {
        width: 100%;
        padding: 10px 20px 100px;
        grid-template-columns: 1fr;
        gap: 15px;
    }

    .card {
        padding: 22px;
    }

    .wendy-button {
        width: 62px;
        height: 62px;
        right: 18px;
        bottom: 18px;
        font-size: 30px;
    }

    .wendy-msg {
        right: 18px;
        bottom: 92px;
        max-width: 210px;
        font-size: 13px;
    }
}

@media (max-width: 400px) {

    .hero {
        padding-top: 30px;
    }

    h1 {
        font-size: 30px;
    }

    .tag {
        font-size: 11px;
    }

    nav a {
        font-size: 12px;
        padding: 6px;
    }

    .hero-card {
        padding: 25px 20px;
    }
}

</style>

</head>

<body>

<header>

    <div class="logo">POWER UP</div>

    <nav>
        <a href="/home">Início</a>
        <a href="/treino">Montar treino</a>
        <a href="/sair">Sair</a>
    </nav>

</header>

<section class="hero">

    <div class="hero-text">

        <span class="tag">
            SEU TREINO, SUA ROTINA
        </span>

        <h1>
            Olá, <span>{{ nome }}</span>! 💜
        </h1>

        <p>
            Organize seus treinos da semana de forma
            prática e receba sugestões de exercícios
            de acordo com suas preferências.
        </p>

        <a class="botao" href="/treino">
            🏋️ Montar meu treino
        </a>

    </div>

    <div class="hero-card">

        <div class="emoji">👩🏻‍💻</div>

        <h2>Wendy</h2>

        <p>
            Sua assistente virtual do Power Up.
            Clique em mim quando tiver alguma dúvida!
        </p>

    </div>

</section>

<section class="cards">

    <div class="card">

        <div class="icon">🎯</div>

        <h3>Seus objetivos</h3>

        <p>
            Escolha até dois objetivos para
            personalizar sua experiência.
        </p>

    </div>

    <div class="card">

        <div class="icon">📅</div>

        <h3>Sua semana</h3>

        <p>
            Escolha os dias em que pode treinar
            e receba seu planejamento.
        </p>

    </div>

    <div class="card">

        <div class="icon">💪</div>

        <h3>Seus exercícios</h3>

        <p>
            Clique na seta de cada exercício
            para aprender como executá-lo.
        </p>

    </div>

</section>

<div class="wendy-msg">
    <strong>Wendy 💜</strong><br>
    Oii! Posso ajudar com suas dúvidas.
</div>

<div
    class="wendy-button"
    onclick="window.location.href='/wendy'"
>
    👩🏻‍💻
</div>

</body>

</html>
"""


# =========================================================
# WENDY
# =========================================================

WENDY_HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Wendy | Power Up</title>

<style>

* {
    box-sizing: border-box;
}

html,
body {
    width: 100%;
    overflow-x: hidden;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #eee8ff, #faf9ff);
    color: #30263d;
}

header {
    background: white;
    padding: 22px 60px;
    box-shadow: 0 2px 10px rgba(0,0,0,.06);
}

.logo {
    color: #7046d8;
    font-weight: bold;
    font-size: 27px;
}

.chat {
    width: 650px;
    max-width: 94%;
    margin: 50px auto;
    background: white;
    border-radius: 25px;
    overflow: hidden;
    box-shadow: 0 15px 45px rgba(0,0,0,.1);
}

.chat-top {
    background: linear-gradient(135deg, #7046d8, #9a82e7);
    color: white;
    padding: 25px;
    display: flex;
    align-items: center;
    gap: 15px;
}

.avatar {
    width: 58px;
    height: 58px;
    border-radius: 50%;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    flex-shrink: 0;
}

.chat-body {
    padding: 30px;
}

.mensagem {
    background: #f1ecff;
    padding: 17px;
    border-radius: 17px;
    margin-bottom: 25px;
    line-height: 1.5;
}

.pergunta {
    color: #7046d8;
    font-weight: bold;
    margin-bottom: 12px;
}

.opcoes a {
    display: block;
    padding: 14px;
    background: #faf9ff;
    border: 1px solid #e3ddf5;
    border-radius: 12px;
    text-decoration: none;
    color: #43394f;
    margin: 10px 0;
}

.opcoes a:hover {
    background: #eee8ff;
    border-color: #7046d8;
}

.voltar {
    display: inline-block;
    margin-top: 15px;
    color: #7046d8;
    text-decoration: none;
    font-weight: bold;
}

@media (max-width: 700px) {

    header {
        padding: 18px 20px;
    }

    .logo {
        font-size: 24px;
    }

    .chat {
        width: 95%;
        max-width: 100%;
        margin: 25px auto;
        border-radius: 20px;
    }

    .chat-top {
        padding: 20px;
    }

    .chat-body {
        padding: 20px;
    }

    .mensagem {
        padding: 14px;
        font-size: 14px;
    }

    .opcoes a {
        padding: 15px 12px;
        font-size: 14px;
    }

    .avatar {
        width: 50px;
        height: 50px;
        font-size: 25px;
    }
}

@media (max-width: 400px) {

    .chat {
        width: 96%;
    }

    .chat-body {
        padding: 16px;
    }

    .chat-top {
        padding: 18px;
    }
}

</style>

</head>

<body>

<header>
    <div class="logo">POWER UP</div>
</header>

<div class="chat">

    <div class="chat-top">

        <div class="avatar">
            👩🏻‍💻
        </div>

        <div>
            <strong>Wendy</strong><br>
            Assistente virtual
        </div>

    </div>

    <div class="chat-body">

        <div class="mensagem">

            Oii! Eu sou a Wendy 💜<br><br>

            Posso ajudar você com dúvidas sobre
            exercícios e também explicar como funciona
            o Power Up.

        </div>

        <div class="pergunta">
            Como posso ajudar?
        </div>

        <div class="opcoes">

            <a href="/wendy?duvida=agachamento">
                🏋️ O que é o agachamento?
            </a>

            <a href="/wendy?duvida=treino">
                📅 Como funciona o treino semanal?
            </a>

            <a href="/wendy?duvida=exercicios">
                💪 Como escolho meus exercícios?
            </a>

            <a href="/treino">
                ✨ Quero montar meu treino
            </a>

        </div>

        {% if resposta %}

        <div class="mensagem">

            <strong>Wendy:</strong><br><br>

            {{ resposta }}

        </div>

        {% endif %}

        <a class="voltar" href="/home">
            ← Voltar para início
        </a>

    </div>

</div>

</body>

</html>
"""


# =========================================================
# FORMULÁRIO DE TREINO
# =========================================================

TREINO_HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Montar treino | Power Up</title>

<style>

* {
    box-sizing: border-box;
}

html,
body {
    width: 100%;
    overflow-x: hidden;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f7f5ff;
    color: #30263d;
}

header {
    background: white;
    padding: 22px 60px;
    box-shadow: 0 2px 10px rgba(0,0,0,.06);
}

.logo {
    color: #7046d8;
    font-size: 27px;
    font-weight: bold;
}

.formulario {
    width: 750px;
    max-width: 94%;
    margin: 40px auto;
    background: white;
    padding: 40px;
    border-radius: 25px;
    box-shadow: 0 10px 35px rgba(0,0,0,.08);
}

h1 {
    color: #7046d8;
    margin-bottom: 8px;
}

.descricao {
    color: #777;
    margin-bottom: 30px;
    line-height: 1.5;
}

.secao {
    margin-top: 30px;
}

.secao h2 {
    font-size: 19px;
    margin-bottom: 7px;
}

.secao small {
    color: #777;
}

.opcoes {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-top: 15px;
}

.opcao {
    border: 1px solid #e2dcef;
    border-radius: 13px;
    padding: 13px;
    cursor: pointer;
    background: #faf9ff;
    transition: .2s;
}

.opcao:hover {
    border-color: #7046d8;
}

.opcao input {
    accent-color: #7046d8;
    margin-right: 8px;
}

select {
    width: 100%;
    padding: 14px;
    border: 1px solid #ddd;
    border-radius: 11px;
    margin-top: 12px;
    font-size: 15px;
    background: white;
}

button {
    width: 100%;
    padding: 16px;
    margin-top: 35px;
    border: none;
    border-radius: 13px;
    background: #7046d8;
    color: white;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
}

button:hover {
    background: #5d35c1;
}

.aviso {
    margin-top: 18px;
    background: #f3efff;
    padding: 13px;
    border-radius: 12px;
    color: #665b76;
    font-size: 13px;
    line-height: 1.5;
}

@media (max-width: 700px) {

    header {
        padding: 18px 20px;
    }

    .logo {
        font-size: 24px;
    }

    .formulario {
        width: 95%;
        max-width: 100%;
        margin: 25px auto;
        padding: 25px 18px;
        border-radius: 20px;
    }

    h1 {
        font-size: 27px;
        line-height: 1.25;
    }

    .descricao {
        font-size: 14px;
        line-height: 1.5;
    }

    .secao {
        margin-top: 25px;
    }

    .secao h2 {
        font-size: 17px;
        line-height: 1.4;
    }

    .opcoes {
        grid-template-columns: 1fr;
        gap: 9px;
    }

    .opcao {
        padding: 15px 12px;
        font-size: 14px;
    }

    .opcao input {
        transform: scale(1.15);
    }

    select {
        width: 100%;
        padding: 14px 10px;
        font-size: 16px;
    }

    button {
        margin-top: 28px;
        padding: 16px 12px;
        font-size: 15px;
    }

    .aviso {
        font-size: 12px;
        line-height: 1.5;
    }
}

@media (max-width: 400px) {

    .formulario {
        width: 96%;
        padding: 22px 15px;
    }

    h1 {
        font-size: 24px;
    }

    .secao h2 {
        font-size: 16px;
    }

    .opcao {
        font-size: 13px;
    }
}

</style>

<script>

function limitarObjetivos() {

    const marcados =
        document.querySelectorAll(
            'input[name="objetivos"]:checked'
        );

    if (marcados.length > 2) {

        marcados[marcados.length - 1].checked = false;

        alert(
            "Você pode selecionar no máximo 2 objetivos."
        );
    }
}


function limitarGrupos() {

    const marcados =
        document.querySelectorAll(
            'input[name="grupos"]:checked'
        );

    if (marcados.length > 3) {

        marcados[marcados.length - 1].checked = false;

        alert(
            "Você pode selecionar no máximo 3 grupos musculares."
        );
    }
}


function verificarDias() {

    const dias =
        document.querySelectorAll(
            'input[name="dias"]:checked'
        );

    if (dias.length === 0) {

        alert(
            "Escolha pelo menos um dia para treinar."
        );

        return false;
    }

    return true;
}

</script>

</head>

<body>

<header>

    <div class="logo">
        POWER UP 💜
    </div>

</header>

<div class="formulario">

    <h1>Vamos montar seu treino! 🏋️</h1>

    <p class="descricao">
        Responda algumas perguntas e o Power Up
        vai organizar uma sugestão para sua semana.
    </p>

    <form method="POST" onsubmit="return verificarDias()">

        <!-- OBJETIVOS -->

        <div class="secao">

            <h2>🎯 Quais são seus objetivos?</h2>

            <small>
                Escolha até 2 objetivos.
            </small>

            <div class="opcoes">

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="objetivos"
                        value="massa"
                        onchange="limitarObjetivos()"
                    >
                    Ganhar massa muscular
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="objetivos"
                        value="hipertrofia"
                        onchange="limitarObjetivos()"
                    >
                    Hipertrofia
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="objetivos"
                        value="forca"
                        onchange="limitarObjetivos()"
                    >
                    Aumentar força
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="objetivos"
                        value="resistencia"
                        onchange="limitarObjetivos()"
                    >
                    Melhorar resistência
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="objetivos"
                        value="condicionamento"
                        onchange="limitarObjetivos()"
                    >
                    Melhorar condicionamento
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="objetivos"
                        value="saude"
                        onchange="limitarObjetivos()"
                    >
                    Saúde e disposição
                </label>

            </div>

        </div>

        <!-- GRUPOS -->

        <div class="secao">

            <h2>💪 Quais grupos musculares você quer priorizar?</h2>

            <small>
                Escolha de 1 a 3 grupos.
            </small>

            <div class="opcoes">

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="grupos"
                        value="gluteos"
                        onchange="limitarGrupos()"
                    >
                    🍑 Glúteos
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="grupos"
                        value="quadriceps"
                        onchange="limitarGrupos()"
                    >
                    Quadríceps
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="grupos"
                        value="posteriores"
                        onchange="limitarGrupos()"
                    >
                    Posteriores
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="grupos"
                        value="panturrilhas"
                        onchange="limitarGrupos()"
                    >
                    Panturrilhas
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="grupos"
                        value="costas"
                        onchange="limitarGrupos()"
                    >
                    Costas
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="grupos"
                        value="peito"
                        onchange="limitarGrupos()"
                    >
                    Peito
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="grupos"
                        value="ombros"
                        onchange="limitarGrupos()"
                    >
                    Ombros
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="grupos"
                        value="biceps"
                        onchange="limitarGrupos()"
                    >
                    Bíceps
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="grupos"
                        value="triceps"
                        onchange="limitarGrupos()"
                    >
                    Tríceps
                </label>

                <label class="opcao">
                    <input
                        type="checkbox"
                        name="grupos"
                        value="abdomen"
                        onchange="limitarGrupos()"
                    >
                    Abdômen
                </label>

            </div>

        </div>

        <!-- EXPERIÊNCIA -->

        <div class="secao">

            <h2>📈 Qual é o seu nível?</h2>

            <select name="experiencia" required>

                <option value="">
                    Selecione
                </option>

                <option value="iniciante">
                    Iniciante
                </option>

                <option value="intermediario">
                    Intermediário
                </option>

                <option value="avancado">
                    Avançado
                </option>

            </select>

        </div>

        <!-- TEMPO -->

        <div class="secao">

            <h2>⏱️ Quanto tempo você tem por treino?</h2>

            <select name="tempo" required>

                <option value="">
                    Selecione
                </option>

                <option value="20">20 minutos</option>
                <option value="30">30 minutos</option>
                <option value="45">45 minutos</option>
                <option value="60">1 hora</option>
                <option value="75">1h15</option>
                <option value="90">1h30</option>
                <option value="105">1h45</option>
                <option value="120">2 horas</option>

            </select>

        </div>

        <!-- DIAS -->

        <div class="secao">

            <h2>📅 Em quais dias você pode treinar?</h2>

            <small>
                Selecione os dias disponíveis.
            </small>

            <div class="opcoes">

                <label class="opcao">
                    <input type="checkbox" name="dias" value="Segunda">
                    Segunda
                </label>

                <label class="opcao">
                    <input type="checkbox" name="dias" value="Terça">
                    Terça
                </label>

                <label class="opcao">
                    <input type="checkbox" name="dias" value="Quarta">
                    Quarta
                </label>

                <label class="opcao">
                    <input type="checkbox" name="dias" value="Quinta">
                    Quinta
                </label>

                <label class="opcao">
                    <input type="checkbox" name="dias" value="Sexta">
                    Sexta
                </label>

                <label class="opcao">
                    <input type="checkbox" name="dias" value="Sábado">
                    Sábado
                </label>

                <label class="opcao">
                    <input type="checkbox" name="dias" value="Domingo">
                    Domingo
                </label>

            </div>

        </div>

        <button type="submit">
            🤖 Gerar meu planejamento semanal
        </button>

        <div class="aviso">
            💜 O Power Up gera uma sugestão educativa
            automaticamente. Ela não substitui a orientação
            de um profissional de Educação Física.
        </div>

    </form>

</div>

</body>

</html>
"""


# =========================================================
# RESULTADO SEMANAL
# =========================================================

RESULTADO_HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Meu planejamento | Power Up</title>

<style>

* {
    box-sizing: border-box;
}

html,
body {
    width: 100%;
    overflow-x: hidden;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f7f5ff;
    color: #30263d;
}

header {
    background: white;
    padding: 22px 60px;
    box-shadow: 0 2px 10px rgba(0,0,0,.06);
}

.logo {
    color: #7046d8;
    font-size: 27px;
    font-weight: bold;
}

.container {
    width: 1000px;
    max-width: 94%;
    margin: 40px auto;
}

.topo {
    background: linear-gradient(135deg, #7046d8, #987de4);
    color: white;
    padding: 35px;
    border-radius: 25px;
    margin-bottom: 25px;
}

.topo h1 {
    margin: 0 0 12px;
}

.topo p {
    line-height: 1.5;
}

.infos {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 20px;
}

.info {
    background: rgba(255,255,255,.16);
    padding: 9px 13px;
    border-radius: 20px;
    font-size: 14px;
}

.dia {
    background: white;
    margin: 20px 0;
    padding: 25px;
    border-radius: 22px;
    box-shadow: 0 6px 25px rgba(0,0,0,.06);
}

.dia h2 {
    color: #7046d8;
    margin-top: 0;
}

.grupos {
    color: #777;
    margin-bottom: 18px;
}

.exercicio {
    border: 1px solid #e9e4f4;
    border-radius: 15px;
    margin: 10px 0;
    overflow: hidden;
}

.exercicio-cabecalho {
    padding: 17px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #fcfbff;
    font-weight: bold;
    gap: 10px;
}

.exercicio-cabecalho:hover {
    background: #f2edff;
}

.seta {
    color: #7046d8;
    font-size: 20px;
    flex-shrink: 0;
}

.exercicio-info {
    display: none;
    padding: 20px;
    border-top: 1px solid #eee;
    background: white;
}

.exercicio-info.aberto {
    display: flex;
    gap: 25px;
    align-items: flex-start;
}

.exercicio-info img {
    width: 400px;
    height: 300px;
    object-fit: cover;
    border-radius: 13px;
    flex-shrink: 0;
}

.texto-exercicio {
    line-height: 1.6;
}

.texto-exercicio h3 {
    color: #7046d8;
    margin-top: 0;
}

.voltar {
    display: inline-block;
    margin: 20px 0 50px;
    padding: 14px 24px;
    background: #7046d8;
    color: white;
    text-decoration: none;
    border-radius: 11px;
    font-weight: bold;
}

.aviso {
    background: #f0ebff;
    padding: 17px;
    border-radius: 14px;
    color: #655b73;
    margin-top: 25px;
    line-height: 1.5;
}

@media (max-width: 800px) {

    header {
        padding: 18px 20px;
    }

    .logo {
        font-size: 24px;
    }

    .container {
        width: 95%;
        max-width: 100%;
        margin: 25px auto;
    }

    .topo {
        padding: 25px 20px;
        border-radius: 20px;
    }

    .topo h1 {
        font-size: 27px;
        line-height: 1.25;
    }

    .topo p {
        font-size: 14px;
        line-height: 1.5;
    }

    .infos {
        display: grid;
        grid-template-columns: 1fr;
        gap: 8px;
    }

    .info {
        font-size: 13px;
        padding: 10px 12px;
    }

    .dia {
        padding: 18px 15px;
        border-radius: 18px;
    }

    .dia h2 {
        font-size: 20px;
    }

    .grupos {
        font-size: 13px;
    }

    .exercicio-cabecalho {
        padding: 15px 12px;
        font-size: 14px;
    }

    .seta {
        font-size: 18px;
    }

    .exercicio-info.aberto {
        display: flex;
        flex-direction: column;
        gap: 15px;
        padding: 15px;
    }

    .exercicio-info img {
        width: 100%;
        max-width: 100%;
        height: auto;
        max-height: 280px;
        object-fit: cover;
    }

    .texto-exercicio {
        font-size: 14px;
        line-height: 1.6;
    }

    .texto-exercicio h3 {
        font-size: 18px;
    }

    .voltar {
        width: 100%;
        text-align: center;
        margin-bottom: 30px;
    }

    .aviso {
        font-size: 13px;
        line-height: 1.5;
    }
}

@media (max-width: 400px) {

    .container {
        width: 96%;
    }

    .topo {
        padding: 22px 16px;
    }

    .topo h1 {
        font-size: 24px;
    }

    .dia {
        padding: 16px 12px;
    }

    .exercicio-cabecalho {
        font-size: 13px;
    }

    .exercicio-info.aberto {
        padding: 12px;
    }

    .texto-exercicio {
        font-size: 13px;
    }
}

</style>

<script>

function abrirExercicio(id) {

    const elemento =
        document.getElementById(id);

    elemento.classList.toggle("aberto");

}

</script>

</head>

<body>

<header>

    <div class="logo">
        POWER UP 💜
    </div>

</header>

<div class="container">

    <div class="topo">

        <h1>
            Seu planejamento semanal 🎉
        </h1>

        <p>
            O Power Up organizou uma sugestão
            de acordo com suas respostas.
        </p>

        <div class="infos">

            <div class="info">
                🎯 {{ objetivos }}
            </div>

            <div class="info">
                💪 {{ grupos }}
            </div>

            <div class="info">
                ⏱️ {{ tempo }} minutos
            </div>

            <div class="info">
                📈 {{ experiencia }}
            </div>

        </div>

    </div>

    {% for dia in semana %}

    <div class="dia">

        <h2>
            📅 {{ dia["dia"] }}
        </h2>

        <div class="grupos">
            {{ dia["grupos"] }}
        </div>

        {% for exercicio in dia["exercicios"] %}

        <div class="exercicio">

            <div
                class="exercicio-cabecalho"
                onclick="abrirExercicio('ex{{ loop.index }}{{ loop.index0 }}{{ dia['numero'] }}')"
            >

                <span>
                    💪 {{ exercicio["nome"] }}
                </span>

                <span class="seta">
                    ▾
                </span>

            </div>

            <div
                class="exercicio-info"
                id="ex{{ loop.index }}{{ loop.index0 }}{{ dia['numero'] }}"
            >

                <img
                    src="{{ url_for('static', filename='imagens/' + exercicio['imagem']) }}"
                    alt="{{ exercicio['nome'] }}"
                    onerror="this.style.display='none'"
                >

                <div class="texto-exercicio">

                    <h3>
                        {{ exercicio["nome"] }}
                    </h3>

                    <p>
                        <strong>
                            Músculos trabalhados:
                        </strong>
                        {{ exercicio["musculos"] }}
                    </p>

                    <p>
                        <strong>
                            Como executar:
                        </strong>
                    </p>

                    <p>
                        {{ exercicio["execucao"] }}
                    </p>

                </div>

            </div>

        </div>

        {% endfor %}

    </div>

    {% endfor %}

    <div class="aviso">

        💜 <strong>Power Up:</strong>
        esta é uma sugestão educativa gerada
        automaticamente pelo sistema.

        <br><br>

        Para qualquer atividade física, especialmente
        em caso de dúvidas sobre execução, cargas ou
        limitações, procure orientação profissional.

    </div>

    <a class="voltar" href="/treino">
        🔄 Criar outro planejamento
    </a>

</div>

</body>

</html>
"""


# =========================================================
# FUNÇÕES DE AUTOMAÇÃO
# =========================================================

def nome_grupo(grupo):

    nomes = {
        "gluteos": "Glúteos",
        "quadriceps": "Quadríceps",
        "posteriores": "Posteriores",
        "panturrilhas": "Panturrilhas",
        "costas": "Costas",
        "peito": "Peito",
        "ombros": "Ombros",
        "biceps": "Bíceps",
        "triceps": "Tríceps",
        "abdomen": "Abdômen"
    }

    return nomes.get(grupo, grupo)


def escolher_quantidade_exercicios(tempo, experiencia):

    tempo = int(tempo)

    if tempo <= 20:
        quantidade = 2

    elif tempo <= 30:
        quantidade = 3

    elif tempo <= 45:
        quantidade = 4

    elif tempo <= 60:
        quantidade = 5

    elif tempo <= 75:
        quantidade = 6

    elif tempo <= 90:
        quantidade = 7

    elif tempo <= 105:
        quantidade = 8

    else:
        quantidade = 9

    if experiencia == "iniciante":
        quantidade = max(2, quantidade - 1)

    return quantidade


def montar_semana(dias, grupos, tempo, experiencia):

    semana = []

    quantidade_total = escolher_quantidade_exercicios(
        tempo,
        experiencia
    )

    if not grupos:
        grupos = ["corpo_todo"]

    for indice, dia in enumerate(dias):

        grupo_principal = grupos[indice % len(grupos)]

        grupos_do_dia = [grupo_principal]

        if len(grupos) > 1 and indice % 2 == 0:

            segundo = grupos[
                (indice + 1) % len(grupos)
            ]

            if segundo != grupo_principal:
                grupos_do_dia.append(segundo)

        elif len(grupos) == 1:

            relacionados = GRUPOS_RELACIONADOS.get(
                grupo_principal,
                []
            )

            if relacionados:
                grupos_do_dia.append(
                    relacionados[indice % len(relacionados)]
                )

        exercicios_do_dia = []

        for grupo in grupos_do_dia:

            lista = EXERCICIOS.get(grupo, [])

            for exercicio in lista:

                if exercicio not in exercicios_do_dia:
                    exercicios_do_dia.append(exercicio)

        exercicios_do_dia = exercicios_do_dia[
            :quantidade_total
        ]

        semana.append({
            "numero": indice,
            "dia": dia,
            "grupos": " + ".join(
                nome_grupo(g)
                for g in grupos_do_dia
            ),
            "exercicios": exercicios_do_dia
        })

    return semana


# =========================================================
# ROTAS
# =========================================================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        senha = request.form.get("senha")

        session["email"] = email
        session["nome"] = email.split("@")[0].title()

        return redirect(url_for("home"))

    return render_template_string(LOGIN_HTML)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form.get("nome")
        email = request.form.get("email")

        session["nome"] = nome
        session["email"] = email

        return redirect(url_for("home"))

    return render_template_string(CADASTRO_HTML)


@app.route("/home")
def home():

    nome = session.get(
        "nome",
        "Usuário"
    )

    return render_template_string(
        HOME_HTML,
        nome=nome
    )


@app.route("/wendy")
def wendy():

    duvida = request.args.get("duvida")

    respostas = {

        "agachamento":
            "O agachamento é um exercício que pode trabalhar principalmente pernas e glúteos. A execução deve ser controlada e adequada ao nível de cada pessoa.",

        "treino":
            "O Power Up utiliza as informações escolhidas pelo usuário para organizar automaticamente uma sugestão de treino para os dias selecionados.",

        "exercicios":
            "Os exercícios são escolhidos a partir de uma base cadastrada no sistema. Ao clicar na setinha de um exercício, você pode visualizar sua explicação e imagem."
    }

    resposta = respostas.get(duvida)

    return render_template_string(
        WENDY_HTML,
        resposta=resposta
    )


@app.route("/treino", methods=["GET", "POST"])
def treino():

    if request.method == "POST":

        objetivos = request.form.getlist(
            "objetivos"
        )

        grupos = request.form.getlist(
            "grupos"
        )

        experiencia = request.form.get(
            "experiencia"
        )

        tempo = request.form.get(
            "tempo"
        )

        dias = request.form.getlist(
            "dias"
        )

        objetivos = objetivos[:2]
        grupos = grupos[:3]

        if not grupos:
            grupos = ["gluteos"]

        semana = montar_semana(
            dias,
            grupos,
            tempo,
            experiencia
        )

        nomes_objetivos = {

            "massa": "Ganhar massa muscular",
            "hipertrofia": "Hipertrofia",
            "forca": "Aumentar força",
            "resistencia": "Melhorar resistência",
            "condicionamento": "Melhorar condicionamento",
            "saude": "Saúde e disposição"
        }

        objetivos_formatados = ", ".join(

            nomes_objetivos.get(
                objetivo,
                objetivo
            )

            for objetivo in objetivos

        )

        if not objetivos_formatados:
            objetivos_formatados = "Não informado"

        grupos_formatados = ", ".join(

            nome_grupo(grupo)

            for grupo in grupos

        )

        experiencia_formatada = {

            "iniciante": "Iniciante",
            "intermediario": "Intermediário",
            "avancado": "Avançado"

        }.get(
            experiencia,
            experiencia
        )

        return render_template_string(

            RESULTADO_HTML,

            semana=semana,

            objetivos=objetivos_formatados,

            grupos=grupos_formatados,

            tempo=tempo,

            experiencia=experiencia_formatada

        )

    return render_template_string(
        TREINO_HTML
    )


@app.route("/sair")
def sair():

    session.clear()

    return redirect(url_for("login"))


# =========================================================
# INICIAR SERVIDOR
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )