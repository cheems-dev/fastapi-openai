# Proyecto FastAPI + OpenAI + MongoDB Atlas

Este proyecto utiliza FastAPI, la API de OpenAI y MongoDB Atlas para crear una aplicación web. Aquí encontrarás instrucciones para ejecutar el proyecto en local y detalles sobre su implementación en un servidor.

## Contenido

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Requisitos](#requisitos)
3. [Configuración del Entorno Local](#configuración-del-entorno-local)
    1. [Clonar el Repositorio](#clonar-el-repositorio)
    2. [Configurar Variables de Entorno](#configurar-variables-de-entorno)
    3. [Instalar Dependencias](#instalar-dependencias)
    4. [Ejecutar la Aplicación](#ejecutar-la-aplicación)
4. [Aplicación en Producción](#aplicación-en-producción)
5. [Documentación de la API](#documentación-de-la-api)

## Descripción del Proyecto

Este proyecto fue desarrollado utilizando FastAPI para el backend, OpenAI para funcionalidades de inteligencia artificial y MongoDB Atlas para la base de datos.

## Requisitos

- Python 3.8 o superior
- Acceso a internet para instalar dependencias y conectar con MongoDB Atlas
- Cuenta en MongoDB Atlas y en OpenAI para obtener las claves de API correspondientes

## Configuración del Entorno Local

### Clonar el Repositorio

Primero, clona el repositorio a tu máquina local:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

Abre el archivo .env y completa las siguientes variables:

```bash
OPENAI_API_KEY=tu_clave_de_openai
MONGODB_URI=tu_uri_de_mongodb_atlas
```

### Instalar Dependencias
Instala las dependencias necesarias usando pip:
```bash
pip install -r requirements.txt
```

### Ejecutar la Aplicación

Finalmente, ejecuta la aplicación.
```bash
uvicorn main:app --reload
```
La aplicación debería estar corriendo en http://127.0.0.1:8000.


## Aplicación en Producción
El proyecto está actualmente desplegado en Render. Puedes acceder a la aplicación en producción a través del siguiente enlace:
[https://fastapi-openai.onrender.com/docs](https://fastapi-openai.onrender.com/docs)

## Documentación de la API
FastAPI genera documentación interactiva automáticamente. Puedes acceder a la documentación de la API en:

- `/docs` para Swagger UI

Para la versión en producción, visita [https://fastapi-openai.onrender.com/docs](https://fastapi-openai.onrender.com/docs).
