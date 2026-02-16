import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv  # pip install python-dotenv

# 1️⃣ Carrega variáveis do arquivo .env
load_dotenv()

# 2️⃣ Lê as variáveis de ambiente
remetente = os.getenv("EMAIL_USER")
senha = os.getenv("EMAIL_PASS")
destinatario = "pedrolimaesilva@gmail.com"

# 3️⃣ Monta o e-mail
msg = MIMEMultipart()
msg["From"] = remetente
msg["To"] = destinatario
msg["Subject"] = "Descobri como atuomatizar e-mail"

# Corpo em HTML
html = """
<html>
  <body>
    <h2 style="color:blue;">Escute pedro!</h2>
    <p>Os ninjas de hoshido foram longe demais</p>
    <p><b>OLHA:</b> eles malaram muita waifu! </p>
    <p>como pode?</p>
    <p>Junte-se ao meu exercito do corrin,e teremos justiça</p>

  </body>
</html>
"""
msg.attach(MIMEText(html, "html"))

# 4️⃣ Conecta ao servidor SMTP do Gmail
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()  # inicia criptografia
        servidor.login(remetente, senha)
        servidor.send_message(msg)
        print("✅ E-mail enviado com sucesso!")

except smtplib.SMTPAuthenticationError:
    print("❌ Erro de autenticação. Verifique a senha de app e o e-mail.")
except Exception as e:
    print("⚠️ Erro inesperado:", e)
