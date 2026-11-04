from PIL import Image
import glob

for caminho in glob.glob("frontend/static/img/imagens/*.jpg"):
    img = Image.open(caminho)
    w, h = img.size
    lado = min(w, h)
    esq = (w - lado) // 2
    topo = (h - lado) // 2
    img.crop((esq, topo, esq + lado, topo + lado)).resize((600, 600)).save(caminho, quality=90)