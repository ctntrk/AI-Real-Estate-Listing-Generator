import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
checkpoint = "HuggingFaceTB/SmolLM2-1.7B-Instruct"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

# Listing generation function
def generate_listing(location, size, rooms, features, amenities, nearby):
    if not all([location.strip(), size.strip(), rooms.strip(), features.strip(), amenities.strip(), nearby.strip()]):
        return "⚠️ Please fill in all the fields. The listing cannot be generated with missing information. ⚠️"

    input_text = (
        "Write a catchy, engaging and professional real estate listing with a creative title "
        "based on the following property details:\n"
        f"- Location: {location}\n"
        f"- Size: {size}\n"
        f"- Rooms: {rooms}\n"
        f"- Features: {features}\n"
        f"- Amenities: {amenities}\n"
        f"- Nearby: {nearby}\n\n"
        "Listing:\n"
        "Title:"
    )

    inputs = tokenizer.encode(input_text, return_tensors="pt").to(device)

    output = model.generate(
        inputs,
        max_new_tokens=500,
        temperature=0.8,
        top_p=0.9,
        do_sample=True,
        eos_token_id=tokenizer.eos_token_id
    )

    generated_text = tokenizer.decode(output[0][inputs.shape[-1]:], skip_special_tokens=True)
    return generated_text.strip()

# Clear inputs and output
def clear_fields():
    return "", "", "", "", "", "", ""

# Example inputs
examples = [
    [
        "New York, Manhattan",
        "1200 sq ft",
        "3 bedrooms, 2 bathrooms",
        "balcony, hardwood floors, fireplace",
        "pool, gym, 24/7 security",
        "Central Park, subway station, shopping mall"
    ],
    [
        "San Francisco, Bay Area",
        "850 sq ft",
        "2 bedrooms, 1 bathroom",
        "modern kitchen, large windows",
        "parking, pet-friendly",
        "schools, cafes, public transport"
    ],
    [
        "London, Kensington",
        "1500 sq ft",
        "4 bedrooms, 3 bathrooms",
        "garden, renovated interiors",
        "garage, elevator",
        "museum, parks, restaurants"
    ]
]

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown(
        """
        # 🏠 AI Real Estate Listing Generator

        👋 Welcome to your intelligent assistant for real estate listings! This AI-powered tool helps you instantly create **high-quality, attention-grabbing, and professional real estate listings** based on just a few details you provide. Whether you're a real estate agent 🧑‍💼, a property owner 🏘️, or a marketing specialist 🎯—this tool is designed to save you time and boost the appeal of your property descriptions.

         ## 🧠 Technologies Used

        - **Gradio**
        - **PyTorch**
        - **Transformers (by Hugging Face)**
        - **SmolLM2-1.7B-Instruct**
        - **CUDA (optional)**

        ## ℹ️ How it works:

        1. 📝 Simply enter the property's key information, such as:
           - **📍 Location**
           - **📏 Size**
           - **🛏️ Rooms**
           - **🏡 Features**
           - **💎 Amenities**
           - **🌆 Nearby Places**

        2. 🤖 The AI will craft a compelling title and an attractive property description based on your inputs.

        3. 🚀 Try the example entries below or type your own!

        👉 Let AI handle the wording—focus on closing deals! 🏡💼

        
         **⚠️ Note:** Loading the model and generating the text might take a few moments, please be patient. ⚠️
         
        """
    )

    with gr.Row():
        with gr.Column():
            location = gr.Textbox(label="📍 Location")
            size = gr.Textbox(label="📏 Size")
            rooms = gr.Textbox(label="🛏️ Rooms")
            features = gr.Textbox(label="🏡 Features")
            amenities = gr.Textbox(label="💎 Amenities")
            nearby = gr.Textbox(label="🌆 Nearby")

            with gr.Row():
                submit_btn = gr.Button("Generate")
                clear_btn = gr.Button("Clear")

        with gr.Column():
            output = gr.Textbox(label="🏡 Generated Real Estate Listing 💼", lines=10)

    submit_btn.click(
        fn=generate_listing,
        inputs=[location, size, rooms, features, amenities, nearby],
        outputs=output
    )

    clear_btn.click(
        fn=clear_fields,
        inputs=[],
        outputs=[location, size, rooms, features, amenities, nearby, output]
    )

    gr.Examples(
        examples=examples,
        inputs=[location, size, rooms, features, amenities, nearby],
        outputs=output
    )

demo.launch()