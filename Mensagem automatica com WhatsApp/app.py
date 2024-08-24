# Codigo para enviar mensagem automatica no WhatsApp

import pywhatkit
phone_number = '+555197354558'
message = 'Teste mensagem pelo python'
hours = 14
minutes = 37
pywhatkit.sendwhatmsg(phone_number, message, hours,minutes)
print ('Mensagem enviada!')

