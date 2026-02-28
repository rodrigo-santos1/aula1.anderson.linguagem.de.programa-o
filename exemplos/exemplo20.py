from datetime import datetime
agora = datetime.now()
hora = agora.hour
minuto = agora.minute
segundo = agora.second

#quando for 6h da manha até 12:30 bom dia
#12:31 até 18:00 boa tarde
#18:01 até a 5:59 boa noite

if hora >= 0 and hora <6:
    print("madrugada, vai dormir colega")
elif hora >=6 and hora <12:
    print("bom dia")
elif hora >=12 and hora <18:
    print("boa tarde")
elif hora >=18 and hora <0:
    print("boa noite")