# ComfyUI Custom Nodes

Este proyecto contiene nodos personalizados para ComfyUI.

## Instalación

1. Clona este repositorio en tu carpeta `custom_nodes` de ComfyUI:
   ```bash
   cd ComfyUI/custom_nodes
   git clone <tu-repositorio> Comfy-Custom-Nodes
   ```

2. Instala las dependencias (si las hay):
   ```bash
   cd Comfy-Custom-Nodes
   pip install -r requirements.txt
   ```

3. Reinicia ComfyUI

## Estructura del Proyecto

```
Comfy-Custom-Nodes/
├── __init__.py              # Punto de entrada principal
├── nodes/                   # Carpeta para todos los nodos personalizados
│   └── example_node.py      # Nodos de ejemplo
├── requirements.txt         # Dependencias del proyecto
└── README.md               # Este archivo
```

## Nodos Incluidos

### Example Text Node
Un nodo de ejemplo que procesa texto.

**Entradas:**
- `text`: Texto a procesar
- `multiplier`: Número de veces a repetir el texto (1-10)
- `prefix` (opcional): Prefijo a agregar al texto

**Salidas:**
- `output_text`: Texto procesado

### Image Info Node
Un nodo que extrae información básica de una imagen.

**Entradas:**
- `image`: Imagen de entrada

**Salidas:**
- `info`: String con información de la imagen
- `width`: Ancho de la imagen
- `height`: Alto de la imagen

## Crear Nuevos Nodos

Para crear un nuevo nodo personalizado:

1. Crea un nuevo archivo en la carpeta `nodes/`
2. Define tu clase de nodo con los métodos requeridos:
   - `INPUT_TYPES()`: Define las entradas del nodo
   - `RETURN_TYPES`: Define los tipos de salida
   - `FUNCTION`: Nombre del método a ejecutar
   - `CATEGORY`: Categoría para organizar en el menú

3. Registra tu nodo en el diccionario `NODE_CLASS_MAPPINGS`
4. Importa tu nodo en `__init__.py`

### Ejemplo de Nodo Básico

```python
class MyCustomNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_name": ("TYPE", {
                    "default": "value"
                }),
            },
        }
    
    RETURN_TYPES = ("TYPE",)
    FUNCTION = "process"
    CATEGORY = "Custom Nodes/MyCategory"
    
    def process(self, input_name):
        # Tu lógica aquí
        result = input_name
        return (result,)

NODE_CLASS_MAPPINGS = {
    "MyCustomNode": MyCustomNode,
}
```

## Tipos de Datos Comunes en ComfyUI

- `STRING`: Texto
- `INT`: Número entero
- `FLOAT`: Número decimal
- `IMAGE`: Tensor de imagen (B, H, W, C)
- `LATENT`: Espacio latente
- `CONDITIONING`: Conditioning para modelos
- `MODEL`: Modelo de difusión
- `VAE`: Autoencoder variacional
- `CLIP`: Modelo CLIP

## Desarrollo

Para agregar más nodos:
1. Crea un nuevo archivo en `nodes/`
2. Actualiza `__init__.py` para importar los nuevos nodos
3. Reinicia ComfyUI para ver los cambios

## Recursos

- [Documentación de ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [Ejemplos de Custom Nodes](https://github.com/comfyanonymous/ComfyUI/tree/master/custom_nodes)

## Licencia

MIT
