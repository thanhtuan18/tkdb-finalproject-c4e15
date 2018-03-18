import mlab
from models.service import Service

mlab.connect()

id_to_find = '5a9bc0e74506282460cfa6ea'

service = Service.objects.with_id(id_to_find)

if service is not None:
    service.update(set__description="Naruto Uzumaki (うずまきナルト, Uzumaki Naruto) is a shinobi of Konohagakure and a descendant of the Uzumaki clan. He became the jinchūriki of the Nine-Tails on the day of his birth — a fate that caused him to be shunned by most of Konoha throughout his childhood. After joining Team Kakashi, Naruto worked hard to gain the village's acknowledgement all the while chasing his dream to become Hokage.") # Update thông tin trên database
    service.reload() # Load lại thông tin mới trên dtb về máy
    print(service.to_mongo())
else:
    print('Not found')
