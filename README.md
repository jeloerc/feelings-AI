# 😊 Analizador de Sentimiento Multilingüe (Inglés/Español)

Una simple aplicación web creada con Streamlit que utiliza un modelo de lenguaje pre-entrenado de Hugging Face (`cardiffnlp/twitter-xlm-roberta-base-sentiment`) para analizar el sentimiento (Positivo, Negativo, Neutral) de un texto introducido por el usuario. La aplicación funciona tanto para texto en **inglés** como en **español**.

Este proyecto demuestra la integración de modelos de Procesamiento del Lenguaje Natural (NLP) en una interfaz de usuario interactiva.

##  Demo

[ **¡Añade tu captura de pantalla o GIF aquí!** ]

*Ejemplo de cómo añadir una imagen (¡reemplaza el enlace!):*
![Demo de la Aplicación](link_a_tu_captura_de_pantalla_o_gif.png)
*(Sube tu archivo de imagen/gif al repositorio de GitHub y usa el enlace relativo o absoluto aquí)*

## Características Clave

*   **Análisis de Sentimiento:** Clasifica el texto en tres categorías: Positivo, Negativo o Neutral.
*   **Soporte Multilingüe:** Funciona con texto de entrada tanto en inglés como en español.
*   **Modelo Pre-entrenado:** Utiliza el potente modelo `cardiffnlp/twitter-xlm-roberta-base-sentiment` de Hugging Face, afinado para tareas de sentimiento.
*   **Interfaz Interactiva:** Interfaz web sencilla y fácil de usar creada con Streamlit.
*   **Feedback Visual:** Muestra el resultado con iconos y colores distintivos, incluyendo un pequeño efecto de "globos" para resultados positivos.

## Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x
*   **Framework Web UI:** Streamlit
*   **Librería NLP:** Hugging Face `transformers`
*   **Backend Deep Learning:** PyTorch (usado por `transformers`)
*   **Modelo NLP:** `cardiffnlp/twitter-xlm-roberta-base-sentiment`

## Configuración y Ejecución Local

Sigue estos pasos para ejecutar la aplicación en tu máquina local:

1.  **Clona el Repositorio:**
    ```bash
    git clone [URL de tu repositorio de GitHub aquí]
    cd [Nombre de la carpeta de tu repositorio]
    ```

2.  **Crea y Activa un Entorno Virtual:** (Recomendado)
    ```bash
    python -m venv venv
    ```
    *   En Windows: `.\venv\Scripts\activate`
    *   En macOS/Linux: `source venv/bin/activate`

3.  **Instala las Dependencias:**
    Asegúrate de tener el archivo `requirements.txt` en la carpeta.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la Aplicación Streamlit:**
    ```bash
    streamlit run app.py
    ```

5.  **Abre la Aplicación:** Streamlit abrirá automáticamente la aplicación en tu navegador web predeterminado. La primera vez que se ejecute después de clonar (o si limpiaste el caché), el modelo de Hugging Face se descargará, lo que puede tardar unos minutos dependiendo de tu conexión a internet.

## ¿Por Qué Este Proyecto es Valioso? (Valor para Portafolio)

*   **Integración de IA:** Demuestra la capacidad de cargar y utilizar eficazmente un modelo de NLP pre-entrenado de una fuente líder como Hugging Face.
*   **Desarrollo Web Rápido:** Muestra habilidades en el uso de Streamlit para crear rápidamente prototipos y aplicaciones web interactivas basadas en datos o modelos.
*   **Aplicación Práctica de NLP:** Ilustra un caso de uso común y comprensible del NLP: el análisis de sentimiento.
*   **Manejo de Dependencias:** Incluye un archivo `requirements.txt` para una fácil replicación del entorno.
*   **Capacidad Multilingüe:** Aborda el desafío de procesar texto en más de un idioma usando un modelo adecuado.
*   **Resolución de Problemas:** El proceso de desarrollo (como se vio en nuestra conversación) implicó depurar problemas de dependencias, caché y lógica de código, demostrando habilidades de resolución de problemas.

## Posibles Mejoras Futuras

*   Mostrar la puntuación de confianza visualmente (ej. una barra de progreso).
*   Permitir al usuario elegir entre diferentes modelos de sentimiento.
*   Añadir manejo de errores más detallado para la entrada del usuario.
*   Implementar análisis por lotes (subir un archivo con múltiples textos).
*   Desplegar la aplicación en una plataforma como Streamlit Community Cloud para acceso público.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. (Puedes cambiar esto si prefieres otra licencia)
