import qrcode
import shutil

def Qr(link):

    img = qrcode.make(link)
    imagem = (f'{link}.png'.replace('www.', '').replace('.com', '').replace('/', '').replace('https:', ''))
    
    img.save(imagem)
   
    source = f'{imagem}'
    destination = 'qrs'
    shutil.move(source,destination)
    
link = Qr(link= input("Insira um link para o QR code: "))



