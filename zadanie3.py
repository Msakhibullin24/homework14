import cv2
import matplotlib.pyplot as plt

image = cv2.imread('file:///C:/Users/Black/Downloads/sdfsdfaaaaaa.jpg') # тут мы вставляем на нашу картинку путь ( например вот мойтам ссылка на спанчбоба)
image_resized = cv2.resize(image, (300, 500)) #изменение размера изображения до 300x500 пикселей

#Преобразование изображения в RGB и в градации серого
# OpenCV использует формат BGR, поэтому конвертируем в RGB
rgb_img = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))# matplotlib выводим изображение

# RGB изображение
axes[0].imshow(rgb_img)
axes[0].set_title("Full Color (RGB)")
axes[0].axis('off')

# Отображаем изображение где от черного до белого все отсальные цвета серого
axes[1].imshow(gray_img, cmap='gray')
axes[1].set_title("Grayscale")
axes[1].axis('off')

plt.tight_layout()
plt.show()
