import gradio as gr
from fastai.vision.all import *


def classify_image(image):
    categories = ("Black", "Grizzly", "Teddy")
    learn = load_learner("export.pkl")
    prediction, index, probabilities = learn.predict(image)
    return dict(zip(categories, map(float, probabilities)))


image = gr.Image(height=256, width=256)
label = gr.Label()
examples = ["black.png", "grizzly.png", "teddy.png"]
interface = gr.Interface(
    fn=classify_image, inputs=image, outputs=label, examples=examples
)
interface.launch()
