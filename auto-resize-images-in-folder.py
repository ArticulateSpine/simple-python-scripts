from PIL import Image  
[Image.open(f).resize((800,600)).save(f"resized_{f}") for f in os.listdir() if f.endswith(".png")]
