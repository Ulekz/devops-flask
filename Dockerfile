# Usar una imagen base oficial de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la aplicación
COPY app/ app/

# Exponer el puerto en el que correrá Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app/app.py"]
