from PIL import Image
im = Image.open('GAO_RUI.jpg')
w, h = im.size
print('Original image size:%sx%s' % (w, h))
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
im.save('GAO_RUI_resized.jpg', 'jpeg')