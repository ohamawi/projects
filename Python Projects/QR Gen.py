import qrcode

data = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs'

img = qrcode.make(data)

img.save('C:/Users/Raid/OneDrive/Desktop/New Folder/DCIM/Camera/Pictures/qrcode.png')
