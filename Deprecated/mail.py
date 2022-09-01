import smtplib, ssl

port = 465 # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "alarma_bloques@yahoo.com"  # Correo del que se envía alarma
receiver_email = "lrojas@lcm.go.cr"  # Correo que recibe notificación
password = "alarma.bloques"
message = """\
alarma.calibracion

Proceso de calibracion termino exitosamente."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
