# 📦 Sistema de Gestión de Despachos (Logística)

## 📋 Descripción

Sistema de gestión de despachos para un centro de logística que implementa un **Gestor de Envíos** para organizar, administrar y manipular paquetes de forma eficiente.

El sistema funciona mediante un menú de opciones interactivo que permite realizar diversas operaciones de gestión de envíos.

---

## ✨ Funcionalidades

### 1. 📥 Alta de Envíos

Agregar nuevos envíos al gestor con los siguientes campos:

- **Número de Seguimiento** (Tracking ID - único)
- **Destinatario**
- **Categoría de Servicio** (EXPRESS, Estándar, INTERNACIONAL)
- **Fecha de Ingreso al Depósito** (con hora)

### 2. ✏️ Modificación y Eliminación Individual

- Modificar los datos de un envío existente usando su número de seguimiento
- Eliminar envíos del sistema (paquetes retirados manualmente o cancelados)

### 3. 📊 Visualización General

Mostrar un listado completo y ordenado de todos los envíos almacenados, detallando la totalidad de sus campos de información.

### 4. 🕐 Actualización Masiva de Prioridad (Hora)

Modificar la hora de ingreso de todos los envíos dentro de un rango de fechas definido por el usuario. Útil para reajustar cronogramas de salida por retrasos en la carga.

### 5. 📚 Generación de Pila de Despacho Prioritario

Crear una nueva **Pila** (LIFO) que contenga solo los envíos ingresados entre dos fechas determinadas:

- El último paquete en ingresar será el primero en ser procesado
- La pila se imprime automáticamente en pantalla

### 6. 🧹 Depuración por Temporada (Mes)

Eliminar del gestor original todos los registros de envíos cuya fecha de ingreso corresponda a un mes específico. Útil para limpiar registros de temporadas pasadas.

---

**Sintaxis y Semántica del Lenguaje – 2026**
