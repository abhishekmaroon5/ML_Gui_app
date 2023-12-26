from taipy.gui import Gui
from tensorflow.keras import models
from PIL import Image
import numpy as np

model = models.load_model("/Users/abhishek1.dhiman/Desktop/prep_interview/ml_gui_app/starterFiles/baseline_mariya.keras")
class_names = {
    0: 'airplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck',
}
def predict(model, path_to_img):
    img = Image.open(path_to_img)
    # Conver the image to desire format
    img = img.convert("RGB")
    img = img.resize((32,32))
    data = np.array(img)
    print(f"before: {data[0][0]}")
    # normalize the array
    data = data/255
    print(f"after: {data[0][0]}")
    probs = model.predict(np.array([data])[:1])
    top_prob = probs.max()
    top_pred = class_names[np.argmax(probs)]
    return top_prob, top_pred

content = ""
img_path = "placeholder_image.png"
prob = 0
pred = ""

index = """
<|text-center|>
<|{"logo.png"}|image|width=25vw|>

<|{content}|file_selector|extensions=.png|>
select an image from your file 
system

<|{pred}|>

<|{img_path}|image|>

<|{prob} |indicator|value={prob}|min=0|max=100|width=25vw|>

"""
def on_change(state, var_name, var_value):
    if(var_name == "content"):
        top_prob, top_pred = predict(model, var_value)
        state.prob = round(top_prob*100)
        state.pred = "this is a "+ top_pred
        state.img_path = var_value
    # print(f"var_name: {var_name}, var_value: {var_value}")
app = Gui(page=index)




if __name__=="__main__":
    print("opening the gui")
    app.run(port=5001, use_reloader=True)