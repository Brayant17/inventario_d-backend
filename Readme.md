# Inventario D Backend

Backend API desarrollado con FastAPI para la gestión de inventario.

---

## Tecnologías utilizadas

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone git@github.com:Brayant17/inventario_d-backend.git
```

o usando HTTPS:

```bash
git clone https://github.com/Brayant17/inventario_d-backend.git
```

---

### 2. Entrar al proyecto

```bash
cd inventario_d-backend
```

---

### 3. Crear entorno virtual

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

---

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

Servidor local:

```text
http://127.0.0.1:8000
```

---

## Documentación automática

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Estructura del proyecto

```text
inventario_d-backend/
│
├── app/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   └── services/
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Variables de entorno

Crear un archivo `.env` en la raíz del proyecto.

Ejemplo:

```env
APP_NAME=Inventario D Backend
DEBUG=True
```

---

## Comandos útiles

### Generar requirements.txt

```bash
pip freeze > requirements.txt
```

### Ver estado de git

```bash
git status
```

### Subir cambios

```bash
git add .
git commit -m "Descripción del cambio"
git push
```

---

## Autor

Brayant17

---

## Licencia

Este proyecto está bajo la licencia MIT.