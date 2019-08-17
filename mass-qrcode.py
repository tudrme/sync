magic_array = []

import qrcode

for url in magic_array:
    print("Now encoding", url)
    img = qrcode.make('https://link.tudrme.com/' + url)
    img.save('e/' + url + '.png', 'PNG')