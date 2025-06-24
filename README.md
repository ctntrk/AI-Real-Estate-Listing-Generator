# 🏡 AI Real Estate Listing Generator

**An AI-powered tool to create engaging and professional real estate listings effortlessly.**

This project helps real estate agents, property owners, and marketers generate high-quality property listings by simply entering basic property details. It leverages a powerful language model to save time and boost creativity in writing.

---

## AI Real Estate Listing Generator Demo Introduction Video

https://github.com/user-attachments/assets/4cf57bfa-0cc8-40f1-8a56-67fe9c8bb0a4

---

## 🌐 Live Demo

Try the app instantly via Hugging Face Spaces:
🔗 Hugging Face Demo Link : [**Real Estate Demo**](https://huggingface.co/spaces/ctntrk/real-estate)

---

## Real-Estate-HuggingFace-Space

![Alt text](https://github.com/ctntrk/AI-Real-Estate-Listing-Generator/blob/main/Real-Estate-HuggingFace-Space.png)

---

## Real-Estate-HuggingFace-Space-Web-Interface

![Alt text](https://github.com/ctntrk/AI-Real-Estate-Listing-Generator/blob/main/Real-Estate-HuggingFace-Space-Web-Interface.png)

---

## 🚀 Features

* ✨ Automatically generates catchy titles and compelling property descriptions
* 🧠 Powered by a transformer-based AI model (SmolLM2-1.7B-Instruct)
* 💻 Simple and clean web interface using Gradio
* ⚙️ Includes example inputs and a reset function for quick testing
* 🌍 Can be extended with multilingual or image-based input features

---

## 🧠 Technologies Used

* **Gradio** – for interactive UI
* **PyTorch** – for model computation
* **Hugging Face Transformers** – for pre-trained model loading and generation
* **SmolLM2-1.7B-Instruct** – the core language model
* **CUDA** (optional) – for GPU acceleration

---

## 🚀 How It Works

1. **🧠 Model Loading**
   Loads the `SmolLM2-1.7B-Instruct` model and tokenizer from Hugging Face using PyTorch.

2. **🖥️ User Interface (UI)**
   Built with Gradio, featuring input fields for:

   * 📍 Location
   * 📐 Size
   * 🛏️ Rooms
   * 🧰 Features
   * 🏡 Amenities
   * 🗺️ Nearby

3. **✍️ User Input**
   Users fill in property details and click **“Generate”**.

4. **🧾 Prompt Creation**
   A custom prompt is created using the inputs to instruct the AI to generate a catchy listing.

5. **🤖 AI Text Generation**
   The model generates a **title** and **detailed description**, using sampling for creativity.

6. **📋 Display Output**
   The result is shown on the interface. Users can also reset inputs with **“Clear”**.

7. **🧪 Examples Included**
   Pre-filled examples are available for quick testing.

---

## AI Real Estate Listing Generator Web Interface

![Alt text](https://github.com/ctntrk/AI-Real-Estate-Listing-Generator/blob/main/AI-Real-Estate-Listing-Generator-Web-Interface.jpg)

---

## Sample Entries for Real Estate Listing

![Alt text](https://github.com/ctntrk/AI-Real-Estate-Listing-Generator/blob/main/Sample-Entries-for-Real-Estate-Listing.jpg)

---

## Result Screen After Model Run

![Alt text](https://github.com/ctntrk/AI-Real-Estate-Listing-Generator/blob/main/Result-Screen-After-Model-Run.jpg)

---

## 🔧 Getting Started

To run the app locally:

### 1. Install the dependencies:

```bash
pip install -r requirements.txt
```

### 2. Start the application:

```bash
python app.py
```

> 💡 The app uses Gradio to launch a browser-based interface. It may take a few seconds to load the model—please be patient.

---

## ✅ Why Use This App?

* No coding required — generate listings in seconds
* Fast and accurate text generation using state-of-the-art AI
* User-friendly design tailored for both technical and non-technical users
* Fully open-source and easy to customize for your own needs

---

## 🧩 Potential Improvements

* Add multilingual support (e.g., Turkish, Spanish)
* Allow image or property type input
* Advanced configuration (tone, length, format)
* Deploy via Streamlit Cloud or Hugging Face Spaces

---
## ✅ Conclusion

This project is a practical example of how modern Python tools like Gradio, Transformers, and PyTorch can be combined to solve real-world problems efficiently. It simplifies the task of crafting attractive real estate listings for both technical and non-technical users.

---

## 📬 Feedback & Contributions

We welcome feedback, ideas, and contributions! Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open-source and available under the **MIT License**.
