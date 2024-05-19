import os
from keras.models import load_model
from PIL import Image
import numpy as np

# Путь к модели
MODEL_PATH = 'C:\ Users\ User\ Desktop\ па\ animal_classifier_model.h5'

# Размер изображения, который ожидает модель
IMG_SIZE = (224, 224)

# Классы животных
CLASSES = ['олень', 'косуля', 'кабарга']

def predict_animal(image_path):
    # Загрузка модели
    if not os.path.exists(MODEL_PATH):
        print("Модель не найдена!")
        return None
    model = load_model(MODEL_PATH)

    # Открытие и подготовка изображения
    if not os.path.exists(image_path):
        print("Изображение не найдено!")
        return None
    img = Image.open(image_path)
    img = img.resize(IMG_SIZE)
    img_array = np.array(img)
    img_array = img_array / 255.0  # Нормализация

    # Добавление размерности
    img_array = np.expand_dims(img_array, axis=0)

    # Предсказание
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class = CLASSES[predicted_class_index]

    return predicted_class

# Пример использования
if __name__ == "__main__":
    image_path = 'C:/Users/User/Pictures/train_minprirodi_Parnokopitnie/deer/Im_0000008_1.jpg'  # Путь к изображению
    result = predict_animal(image_path)
    if result is not None:
        print(f"Предсказано: {result}")
    else:
        print("Ошибка при обработке изображения или загрузке модели.")