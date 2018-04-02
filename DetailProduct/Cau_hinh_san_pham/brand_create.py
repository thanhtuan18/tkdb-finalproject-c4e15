from urllib.request import urlopen
import mlab
from models.brand import Brand

mlab.connect()

brand = Brand(
    brand_name = 'Xiaomi',
    description = '',
    logo = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Xiaomi_logo.svg/180px-Xiaomi_logo.svg.png',
)
brand.save()
