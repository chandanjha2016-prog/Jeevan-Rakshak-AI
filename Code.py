
import gradio as gr

def rakshak(text):
    text = text.lower()
    if "insaan" in text or "manav" in text:
        return "🚨 Jeevan Rakshak: INSAAN detect hua! Turant 112/Ambulance call karo."
    elif "janwar" in text or "kutte" in text:
        return "🐾 Jeevan Rakshak: JANWAR detect hua! Pashu doctor ko call karo."
    elif "paudha" in text or "ped" in text:
        return "🌿 Jeevan Rakshak: PAUDHA detect hua! Paani do aur dhoop me rakho."
    else:
        return "🤔 Jeevan Rakshak: Likho: Insaan, Janwar ya Paudha"

iface = gr.Interface(
    fn=rakshak,
    inputs="text",
    outputs="text",
    title="Jeevan Rakshak AI 🇮🇳"
)
iface.launch()
