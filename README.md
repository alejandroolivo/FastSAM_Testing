# FastSAM_Testing
Este proyecto utiliza FastSAM para llevar a cabo tareas de segmentación en imágenes. Ofrece dos scripts: uno para segmentar todos los elementos en una imagen y otro para segmentar un objeto específico en la imagen mediante texto descriptivo.

## Requisitos
Paquetes de Python
Instale los paquetes de Python necesarios enumerados en el archivo requirements.txt con el siguiente comando:

```
pip install -r requirements.txt
```

## Dependencias Adicionales
Ejecute los siguientes comandos para instalar FastSAM y otras dependencias relacionadas:

```
!git clone https://github.com/CASIA-IVA-Lab/FastSAM.git
!pip -q install -r FastSAM/requirements.txt
!pip -q install git+https://github.com/openai/CLIP.git roboflow supervision
!pip -q install git+https://github.com/facebookresearch/segment-anything.git
!wget -P FastSAM/weights https://huggingface.co/spaces/An-619/FastSAM/resolve/main/weights/FastSAM.pt
!wget -P FastSAM/weights https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
```

## Uso
#### Segmentar Todo en la Imagen
Este script segmenta todos los objetos en las imágenes de la carpeta images/carne/:

```
python segment_everything.py
```

#### Segmentar un Objeto Específico
Este script permite segmentar un objeto específico en las imágenes de la carpeta images/carne/ mediante texto descriptivo:

```
python segment_by_text.py
```
Para segmentar un objeto específico, cambie la variable prompt_texto en el script.

## Estructura del Proyecto

```
.
├── segment_everything.py
├── segment_by_text.py
├── requirements.txt
├── FastSAM/
│   ├── weights/
│   │   └── FastSAM.pt
├── images/
│   └── carne/
└── output/
```

## Documentación Adicional
Para obtener más información, visite How to Use FastSAM.