
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

# Создание модели нейронной сети
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(3, activation='softmax')  # 3 класса: кабарга, косуля, олень
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Подготовка данных для обучения
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    '/Users/mikudym/Downloads/train_minprirodi_Parnokopitnie/train',  # Укажите путь к папке с тренировочными данными
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical'
)

# Подготовка данных для валидации
val_datagen = ImageDataGenerator(rescale=1./255)
val_generator = val_datagen.flow_from_directory(
    '/Users/mikudym/Downloads/train_minprirodi_Parnokopitnie/validation',  # Укажите путь к папке с валидационными данными
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical'
)



# Обучение модели
history = model.fit(
    train_generator,
    epochs=25,
    validation_data=val_generator,
    verbose=1
)



# Сохранение модели
model.save('animal_classifier_model.h5')

# Построение графика ошибок
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.title('Loss Over Epochs')

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.title('Accuracy Over Epochs')

plt.show()