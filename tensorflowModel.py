from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
def checkFruitQuality():
    loaded_classifier = load_model('banana_rotten_tf_2_1_0.h5')
    test_image = image.load_img('fruit_images/fruit.jpg',target_size=(64,64))
    test_image = img_to_array(test_image)
    test_image = np.expand_dims(test_image,axis=0)
    result = loaded_classifier.predict(test_image)
    if result[0][0] == 1:
        prediction = 'Rotten'
        print(prediction)
    else:
        prediction = 'Normal'
        print(prediction)
    return prediction
