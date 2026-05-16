# Reporte de Estructura del Software - ADC CCC

## 1. Resumen General

El proyecto **ADC CCC** (Asociación para el Desarrollo Campesino - Circuito Corto de Comercialización) es una aplicación fullstack diseñada para gestionar pedidos, productos, productores y eventos (mingas) dentro de una red de comercialización agrícola. La arquitectura se compone de un **Frontend** en Next.js 16, un **Backend** en Express.js con TypeScript, una base de datos **PostgreSQL**, caché con **Redis**, proxy inverso con **Nginx**, y orquestación de mensajes con **Apache Kafka** (opcional).

---

## 2. Estructura de Carpetas Raíz

```
ADC-CCC/
├── .git/                       # Repositorio Git
├── backend/                    # API REST (Node.js + Express + TypeScript)
├── database/
│   └── init/
│       └── 01-init.sql         # Script de inicialización de PostgreSQL
├── frontend/                   # Aplicación Web (Next.js + React + TypeScript)
├── nginx/
│   └── nginx.conf              # Configuración del proxy inverso
├── temp/                       # Scripts temporales de migración/generación de datos
├── .env.example                # Variables de entorno de ejemplo
├── .gitignore
├── docker-compose.yml          # Orquestación de todos los servicios
├── package.json                # Dependencias raíz (xlsx)
├── DEPLOYMENT.md               # Guía de despliegue
└── PROMPT_OPTIMIZACION...md    # Prompts de optimización
```

---

## 3. Backend (`/backend`)

### 3.1. Tecnologías y Dependencias Principales

| Tecnología            | Versión | Propósito                                      |
| --------------------- | ------- | ---------------------------------------------- |
| Node.js               | —       | Runtime de JavaScript                          |
| TypeScript            | ^6.0.3  | Tipado estático                                |
| Express.js            | ^5.2.1  | Framework Web / API REST                       |
| PostgreSQL (`pg`)     | ^8.20.0 | Driver de base de datos relacional             |
| Redis (`redis`)       | ^5.12.1 | Caché y gestión de sesiones/rate limiting      |
| KafkaJS               | ^2.2.4  | Mensajería asíncrona (eventos/notificaciones)  |
| JWT (`jsonwebtoken`)  | ^9.0.3  | Autenticación basada en tokens                 |
| Bcrypt                | ^6.0.0  | Hashing de contraseñas                         |
| Zod                   | ^4.4.3  | Validación de esquemas                         |
| Winston               | ^3.19.0 | Logging estructurado con rotación diaria       |
| Puppeteer             | ^24.43.0| Generación de PDFs                             |
| Sharp                 | ^0.34.5 | Procesamiento de imágenes                      |
| Multer                | ^2.1.1  | Manejo de subida de archivos                   |
| Helmet                | ^8.1.0  | Headers de seguridad HTTP                      |
| CORS                  | ^2.8.6  | Control de acceso cross-origin                 |
| Express Rate Limit    | ^8.5.1  | Limitación de peticiones                       |
| Jest / Supertest      | ^30.4.2 | Testing unitario y de integración              |

### 3.2. Estructura de Carpetas del Backend

```
backend/
├── src/
│   ├── config/               # Configuraciones globales
│   │   ├── db.ts             # Pool de conexiones a PostgreSQL
│   │   ├── logger.ts         # Configuración de Winston
│   │   ├── kafka.ts          # Configuración de Kafka
│   │   ├── migrate.ts        # Migraciones automáticas de notificaciones
│   │   ├── order-migration.ts# Migraciones de pedidos
│   │   ├── event-migration.ts# Migraciones de eventos
│   │   ├── notification.config.ts
│   │   └── migrations/       # Scripts SQL de migración (001-017)
│   ├── controllers/          # Controladores HTTP (handlers de rutas)
│   │   ├── user.controller.ts
│   │   ├── unit-type.controller.ts
│   │   ├── statistics.controller.ts
│   │   └── __tests__/        # Tests de controladores
│   ├── middlewares/          # Middlewares de Express
│   │   ├── auth.middleware.ts          # Verificación JWT
│   │   ├── role.middleware.ts          # Verificación de roles
│   │   ├── validation.middleware.ts    # Validación Zod
│   │   ├── rate-limit.middleware.ts    # Rate limiting global
│   │   ├── logger.middleware.ts        # Logging de peticiones HTTP
│   │   ├── correlation.middleware.ts # IDs de correlación
│   │   ├── errorHandler.middleware.ts# Manejo centralizado de errores
│   │   └── auditLog.middleware.ts      # Auditoría de operaciones
│   ├── models/               # Interfaces/Types de dominio
│   │   ├── user.model.ts
│   │   ├── product.model.ts
│   │   ├── producer-product.model.ts
│   │   ├── order-status.model.ts
│   │   ├── notification.model.ts
│   │   ├── minga.model.ts
│   │   ├── live-purchases.model.ts
│   │   ├── attendance-list.model.ts
│   │   ├── announcement.model.ts
│   │   └── ...
│   ├── repositories/         # Acceso a datos (Patrón Repository)
│   │   ├── user.repository.ts
│   │   ├── product.repository.ts
│   │   ├── producer.repository.ts
│   │   ├── order.repository.ts
│   │   ├── event.repository.ts
│   │   ├── admin-*.repository.ts (repositorios administrativos)
│   │   └── ...
│   ├── routes/               # Definición de endpoints de la API
│   │   ├── auth.routes.ts
│   │   ├── product.routes.ts
│   │   ├── order.routes.ts
│   │   ├── producer.routes.ts
│   │   ├── producer-product.routes.ts
│   │   ├── producer-admin.routes.ts
│   │   ├── admin.routes.ts
│   │   ├── user.routes.ts
│   │   ├── minga.routes.ts
│   │   ├── announcement.routes.ts
│   │   ├── notification.routes.ts
│   │   ├── statistics.routes.ts
│   │   ├── unit-type.routes.ts
│   │   ├── product-request.routes.ts
│   │   ├── attendance-list.routes.ts
│   │   ├── live-purchases.routes.ts
│   │   ├── invoice.routes.ts
│   │   ├── order-period.routes.ts
│   │   ├── event.routes.ts
│   │   ├── event-attendance.routes.ts
│   │   ├── dashboard.routes.ts
│   │   └── upload.routes.ts
│   ├── schemas/              # Esquemas de validación Zod
│   │   ├── producer.schema.ts
│   │   ├── event.schema.ts
│   │   ├── order.schema.ts
│   │   └── search.schema.ts
│   ├── services/             # Lógica de negocio (Patrón Service)
│   │   ├── auth.service.ts
│   │   ├── session.service.ts
│   │   ├── rate-limit.service.ts
│   │   ├── product.service.ts
│   │   ├── producer.service.ts
│   │   ├── order.service.ts
│   │   ├── invoice.service.ts
│   │   ├── pdf.service.ts
│   │   ├── image.service.ts
│   │   ├── notification.service.ts
│   │   ├── event.service.ts
│   │   ├── dashboard.service.ts
│   │   └── admin-producer.service.ts
│   ├── kafka/                # Productores y consumidores de Kafka
│   │   ├── producer.ts
│   │   ├── consumer.ts
│   │   └── events.ts
│   ├── types/                # Tipos globales de TypeScript
│   │   └── express.d.ts
│   ├── utils/                # Utilidades
│   │   └── slugify.ts
│   ├── app.ts                # Configuración principal de Express
│   └── server.ts             # Punto de entrada, bootstrap y shutdown
├── scripts/                  # Scripts de utilidad (Node.js)
│   ├── test-attendance.js
│   ├── run-migration-012.js
│   ├── run-migration-011.js
│   └── check-db.js
├── uploads/                  # Directorio de archivos subidos (imágenes)
├── tests/                    # Tests adicionales (si existen)
├── jest.config.js            # Configuración de Jest
├── tsconfig.json             # Configuración de TypeScript
├── Dockerfile                # Imagen Docker del backend
├── docker-compose.kafka.yml  # Compose adicional para Kafka
├── .env.example              # Variables de entorno de ejemplo
├── .gitignore
└── package.json
```

### 3.3. Patrón Arquitectónico del Backend

El backend sigue una **Arquitectura en Capas (Layered Architecture)**:

1. **Capa de Presentación (Routes + Controllers):** Recibe peticiones HTTP, extrae parámetros y delega a los servicios.
2. **Capa de Aplicación (Services):** Contiene la lógica de negocio, orquesta repositorios y utilidades.
3. **Capa de Datos (Repositories):** Realiza consultas directas a PostgreSQL usando el pool de `pg`.
4. **Capa de Infraestructura (Config + Kafka + Redis):** Conexiones a bases de datos, caché, mensajería y logging.

Se utilizan los siguientes **Patrones de Diseño**:
- **Repository Pattern:** Aislamiento de la lógica de acceso a datos.
- **Service Layer:** Centralización de la lógica de negocio.
- **Middleware Chain:** Autenticación, autorización, validación, rate limiting y logging.
- **DTO/Schema Validation:** Validación estricta con Zod antes de llegar a los servicios.

---

## 4. Frontend (`/frontend`)

### 4.1. Tecnologías y Dependencias Principales

| Tecnología                  | Versión   | Propósito                                    |
| --------------------------- | --------- | -------------------------------------------- |
| Next.js                     | ^16.2.4   | Framework React (App Router)               |
| React                       | 19.2.4    | Librería UI                                  |
| React DOM                   | 19.2.4    | Renderizado del DOM                          |
| TypeScript                  | ^5        | Tipado estático                              |
| Tailwind CSS                | ^4        | Framework de utilidades CSS                  |
| Tailwind PostCSS            | ^4        | Plugin de PostCSS para Tailwind               |
| Axios                       | ^1.15.2   | Cliente HTTP                                 |
| React Hook Form             | ^7.74.0   | Manejo de formularios                        |
| Zod                         | ^4.3.6    | Validación de esquemas                       |
| @hookform/resolvers         | ^5.2.2    | Integración Zod + React Hook Form            |
| Lucide React                | ^1.14.0   | Iconos SVG                                   |
| MapLibre GL                 | ^5.24.0   | Mapas interactivos (OpenStreetMap)           |
| Recharts                    | ^3.8.1    | Gráficos y visualización de datos            |
| jsPDF / jsPDF-AutoTable    | ^4.2.1    | Generación de PDFs en el cliente             |
| shadcn/ui                   | ^4.7.0    | Componentes de UI base (implícito)           |
| class-variance-authority    | ^0.7.1    | Variantes de componentes                     |
| tailwind-merge              | ^3.6.0    | Merge de clases Tailwind                     |
| tw-animate-css              | ^1.4.0    | Animaciones CSS con Tailwind                 |
| ESLint (Next.js config)     | ^9        | Linting                                      |

### 4.2. Estructura de Carpetas del Frontend

```
frontend/
├── app/                              # App Router de Next.js
│   ├── (rutas raíz)
│   │   ├── page.tsx                  # Página de inicio (Landing)
│   │   ├── layout.tsx                # Layout raíz (AuthProvider, OrderProvider)
│   │   └── favicon.ico
│   ├── auth/
│   │   └── register/
│   │       └── page.tsx              # Registro de usuarios
│   ├── usuario/
│   │   └── page.tsx                  # Perfil de usuario
│   ├── admin/
│   │   ├── page.tsx                  # Dashboard administrativo
│   │   ├── usuarios/
│   │   │   └── page.tsx              # Gestión de usuarios
│   │   ├── asistencia/
│   │   │   └── page.tsx              # Control de asistencia
│   │   ├── productos/
│   │   │   └── page.tsx              # Gestión de productos
│   │   ├── pedidos/
│   │   │   └── page.tsx              # Gestión de pedidos
│   │   ├── productores/
│   │   │   └── page.tsx              # Gestión de productores
│   │   ├── mingas/
│   │   │   └── page.tsx              # Gestión de mingas
│   │   ├── configuracion/
│   │   │   └── page.tsx              # Configuración del sistema
│   │   ├── anuncios/
│   │   │   └── page.tsx              # Gestión de anuncios
│   │   ├── eventos/
│   │   │   └── page.tsx              # Gestión de eventos
│   │   ├── reportes/
│   │   │   └── page.tsx              # Reportes y estadísticas
│   │   └── reportes-productores/
│   │       └── page.tsx              # Reportes por productor
│   ├── pages/                        # Componentes de página reutilizables
│   │   ├── landing/
│   │   │   └── LandingPage.tsx
│   │   ├── products/
│   │   │   └── ProductsPage.tsx
│   │   ├── product/
│   │   │   └── ProductDetailPage.tsx
│   │   ├── user/
│   │   │   └── UserPage.tsx
│   │   ├── notifications/
│   │   │   └── NotificationsPage.tsx
│   │   ├── announcements/
│   │   │   └── AnnouncementsPage.tsx
│   │   ├── admin/
│   │   │   └── AdminPage.tsx
│   │   └── legal/
│   │       └── LegalPageLayout.tsx
│   ├── components/                   # Componentes React reutilizables
│   │   ├── Header.tsx
│   │   ├── Footer.tsx
│   │   ├── UserAvatar.tsx
│   │   ├── ProductCard.tsx
│   │   ├── ProductoForm.tsx
│   │   ├── SearchBar.tsx
│   │   ├── ProfileEditForm.tsx
│   │   ├── SessionModal.tsx
│   │   ├── Toast.tsx
│   │   ├── EventCard.tsx
│   │   ├── AnnouncementCard.tsx
│   │   ├── MingaStrip.tsx
│   │   ├── MingaMap.tsx
│   │   ├── MingaMapPlaceholder.tsx
│   │   ├── AdminUserEditForm.tsx
│   │   └── AdminMingaForm.tsx
│   ├── controllers/                  # Lógica de control para las vistas
│   │   ├── landing.controller.ts
│   │   ├── products.controller.ts
│   │   ├── product-detail.controller.ts
│   │   ├── producer.controller.ts
│   │   ├── notification.controller.ts
│   │   ├── minga.controller.ts
│   │   ├── admin.controller.ts
│   │   └── user.controller.ts
│   ├── repositories/                 # Acceso a datos del frontend (API client)
│   │   ├── user.repository.ts
│   │   ├── product.repository.ts
│   │   ├── producer.repository.ts
│   │   ├── order.repository.ts
│   │   ├── notification.repository.ts
│   │   ├── minga.repository.ts
│   │   ├── event.repository.ts
│   │   ├── announcement.repository.ts
│   │   ├── admin.repository.ts
│   │   └── unit-type.repository.ts
│   ├── models/                       # Interfaces/Types del frontend
│   │   ├── user.model.ts
│   │   ├── product.model.ts
│   │   ├── order.model.ts
│   │   ├── notification.model.ts
│   │   ├── minga.model.ts
│   │   ├── event.model.ts
│   │   ├── announcement.model.ts
│   │   └── admin.model.ts
│   ├── context/                      # Contextos de React
│   │   ├── AuthContext.tsx           # Estado global de autenticación
│   │   └── OrderContext.tsx          # Estado global de pedidos
│   ├── hooks/                        # Custom Hooks
│   │   ├── useNotifications.ts
│   │   ├── useEventWindow.ts
│   │   └── useClickOutside.ts
│   ├── lib/                          # Utilidades
│   │   ├── slugify.ts
│   │   └── api.ts                    # Configuración base de Axios
│   ├── ... (más rutas de páginas)
│   ├── pedido/
│   │   └── page.tsx                  # Detalle de pedido
│   ├── mis-pedidos/
│   │   ├── page.tsx                  # Listado de pedidos
│   │   └── [id]/
│   │       └── page.tsx              # Detalle de un pedido específico
│   ├── mingas/
│   │   ├── page.tsx                  # Listado de mingas
│   │   └── [slug]/
│   │       └── page.tsx              # Detalle de una minga
│   ├── gestion-productos/
│   │   └── page.tsx                  # Gestión de productos (productor)
│   ├── ofertar-productos/
│   │   └── page.tsx                  # Oferta de productos
│   ├── solicitar-producto/
│   │   └── page.tsx                  # Solicitud de productos
│   ├── anuncios/
│   │   └── page.tsx                  # Listado de anuncios
│   ├── notifications/
│   │   └── page.tsx                  # Centro de notificaciones
│   ├── terms-and-conditions/
│   │   └── page.tsx                  # Términos y condiciones
│   └── privacy-policy/
│       └── page.tsx                  # Política de privacidad
├── components/
│   └── ui/                           # Componentes de UI base (shadcn/ui)
│       ├── button.tsx
│       └── map.tsx
├── styles/                           # Estilos globales y tokens
│   ├── globals.css
│   ├── tokens.css
│   └── utilities.css
├── public/                           # Assets estáticos
│   ├── images/                       # Logos y fotos de organizaciones
│   ├── window.svg
│   ├── vercel.svg
│   ├── next.svg
│   ├── file.svg
│   └── globe.svg
├── lib/
│   └── utils.ts                      # Utilidades (cn, etc.)
├── next.config.ts                    # Configuración de Next.js
├── tsconfig.json                     # Configuración de TypeScript
├── postcss.config.mjs                # Configuración de PostCSS
├── eslint.config.mjs                 # Configuración de ESLint
├── components.json                   # Configuración de shadcn/ui
├── Dockerfile                        # Imagen Docker del frontend
├── .dockerignore
├── .gitignore
├── README.md
├── CLAUDE.md
├── AGENTS.md
└── package.json
```

### 4.3. Patrón Arquitectónico del Frontend

El frontend utiliza el **App Router de Next.js 16**, adoptando una arquitectura híbrida:

- **Server Components:** Para la carga inicial de datos y SEO (páginas de Next.js por defecto).
- **Client Components:** Para interactividad (formularios, modales, mapas, gráficos), marcados con `"use client"`.

Se siguen los siguientes patrones:
- **Repository Pattern (Frontend):** Aislamiento de llamadas HTTP en la carpeta `repositories/`.
- **Controller Pattern:** Separación de la lógica de vista de los componentes React (`controllers/`).
- **Context API:** Manejo de estado global para autenticación (`AuthContext`) y pedidos (`OrderContext`).
- **Component-based Architecture:** Componentes reutilizables en `components/` y `components/ui/`.

---

## 5. Base de Datos (`/database`)

### 5.1. Tecnología

- **Motor:** PostgreSQL 17 (Alpine)
- **Inicialización:** Script `01-init.sql` ejecutado automáticamente al crear el contenedor.
- **Extensiones:** `pgcrypto`, `uuid-ossp`

### 5.2. Esquema de Tablas (Inferido)

A partir del código del backend y las migraciones, las tablas principales incluyen:

| Tabla                        | Descripción                                      |
| ---------------------------- | ------------------------------------------------ |
| `users`                      | Usuarios del sistema (productores, admins, etc.)|
| `producers`                  | Perfiles de productores                          |
| `products`                   | Catálogo de productos                            |
| `producer_products`          | Relación productor-producto (ofertas)            |
| `orders`                     | Pedidos realizados                               |
| `order_items`                | Items dentro de un pedido                        |
| `order_periods`              | Períodos de tiempo para realizar pedidos         |
| `notifications`              | Notificaciones del sistema                       |
| `events`                     | Eventos (mingas, ferias, etc.)                   |
| `event_attendance`           | Registro de asistencia a eventos                 |
| `event_external_attendees`   | Asistentes externos a eventos                    |
| `mingas`                     | Organizaciones/Mingas de productores             |
| `announcements`              | Anuncios públicos                                |
| `product_requests`           | Solicitudes de productos nuevos                  |
| `unit_types`                 | Tipos de unidad de medida                        |
| `product_price_history`      | Historial de precios de productos                |
| `live_purchases`             | Compras en vivo / ferias                         |
| `attendance_lists`           | Listas de asistencia                             |
| `invoices`                   | Facturas                                         |
| `system_logs`                | Logs de auditoría del sistema                    |
| `statistics`                 | Datos estadísticos agregados                     |

---

## 6. Infraestructura y DevOps

### 6.1. Docker Compose

El archivo `docker-compose.yml` define los siguientes servicios:

| Servicio   | Imagen              | Puerto  | Dependencias               |
| ---------- | ------------------- | ------- | -------------------------- |
| `database` | postgres:17-alpine  | 5432    | —                          |
| `redis`    | redis:7-alpine      | 6379    | —                          |
| `backend`  | Dockerfile (backend)| 3001    | database, redis            |
| `frontend` | Dockerfile (frontend)| 3000   | backend                    |
| `nginx`    | nginx:alpine        | 80/443 | frontend, backend (opt)    |

### 6.2. Nginx (Reverse Proxy)

Configurado para:
- Servir el frontend en `/`
- Proxy de API en `/api` al backend
- Servir archivos estáticos subidos en `/uploads`
- Soporte para WebSockets en `/ws`
- Caché de assets estáticos y archivos de imagen
- Headers de seguridad (X-Frame-Options, X-Content-Type-Options, X-XSS-Protection)

### 6.3. Kafka (Opcional)

- Archivo adicional: `docker-compose.kafka.yml`
- Usado para la generación asíncrona de notificaciones y eventos del sistema.
- Puede deshabilitarse con la variable `KAFKA_ENABLED=false`.

---

## 7. Flujo de Datos y Comunicación

```
┌─────────────┐
│   Cliente   │
│  (Navegador)│
└──────┬──────┘
       │ HTTPS/HTTP
       ▼
┌─────────────┐
│    Nginx    │  (Reverse Proxy / Load Balancer)
│   (Puerto 80/443)
└──────┬──────┘
       │ Proxy Pass
   ┌───┴───┐
   ▼       ▼
┌──────┐ ┌────────┐
│Front │ │Backend │
│:3000 │ │:3001   │
└──┬───┘ └───┬────┘
   │         │
   │    ┌────┴────┐
   │    ▼         ▼
   │ ┌──────┐  ┌──────┐
   │ │Postgre│  │Redis │
   │ │SQL    │  │Cache │
   │ └──────┘  └──────┘
   │
   ▼
┌──────┐
│Public│  (Assets Estáticos / Imágenes)
└──────┘
```

### 7.1. Flujo de una Petición Típica

1. El cliente solicita una página o recurso a Nginx.
2. Si es una ruta de frontend, Nginx proxy-pass al servicio Next.js.
3. Next.js puede renderizar Server Components que hacen fetch al backend.
4. Si es una llamada a `/api/*`, Nginx redirige al backend Express.
5. El backend ejecuta middlewares (CORS, Rate Limit, Auth, Correlation ID, Logger).
6. El controlador recibe la petición y delega al servicio correspondiente.
7. El servicio utiliza el repositorio para consultar/actualizar PostgreSQL.
8. Opcionalmente, el servicio puede publicar un evento a Kafka o interactuar con Redis.
9. La respuesta fluye de vuelta al cliente.

---

## 8. Seguridad

| Capa           | Implementación                                           |
| -------------- | -------------------------------------------------------- |
| Transporte     | HTTPS (Nginx), headers de seguridad (HSTS, CSP, etc.)  |
| Autenticación  | JWT (JSON Web Tokens) con secret de 64+ caracteres     |
| Autorización   | Middleware de roles (`role.middleware.ts`)               |
| Validación     | Zod Schemas en body, query y params                      |
| Rate Limiting  | Express Rate Limit + Redis (distribuido)                 |
| Headers        | Helmet.js (CSP, X-Frame-Options, etc.)                   |
| Auditoría      | Middleware de audit log y logger de Winston              |
| Subida Archivos| Multer + validación de tipo y tamaño                     |
| CORS           | Whitelist de orígenes permitidos                         |

---

## 9. Reporte de Estructura Utilizada (Análisis de Calidad)

### 9.1. Fortalezas

1. **Separación de Responsabilidades:** Clara separación entre frontend, backend y base de datos. Dentro del backend, el patrón Repository + Service mantiene la lógica de negocio desacoplada del acceso a datos.
2. **TypeScript en Todo el Stack:** Tipado estático tanto en frontend como backend, reduciendo errores en tiempo de ejecución.
3. **Dockerización Completa:** Todos los servicios están containerizados, facilitando el despliegue y la replicación de entornos.
4. **Middlewares de Seguridad Robustos:** Helmet, CORS restringido, Rate Limiting distribuido con Redis, validación Zod y JWT fuerte.
5. **Logging y Trazabilidad:** Uso de Winston con rotación diaria y IDs de correlación para trazabilidad de peticiones.
6. **Migraciones de Base de Datos:** Scripts versionados (001-017) para control de cambios en el esquema.
7. **Arquitectura Escalable:** Redis para caché/sesiones, Kafka para eventos asíncronos, Nginx como reverse proxy.
8. **App Router de Next.js:** Aprovecha Server Components para mejor rendimiento y SEO.

### 9.2. Áreas de Mejora / Observaciones

1. **Duplicación de Código (Frontend/Backend):**
   - Existe una duplicación de interfaces (`models/`) y lógica de acceso a datos (`repositories/`, `controllers/`) tanto en el frontend como en el backend. Considerar un **monorepo con paquetes compartidos** (por ejemplo, usando pnpm workspaces o Nx) para compartir tipos y schemas Zod.

2. **Consistencia en la Nomenclatura:**
   - Algunas rutas en el frontend usan guiones (`gestion-productos`) y otras no (`usuario`). Estandarizar a `kebab-case` para todas las rutas.
   - En el backend, algunos archivos usan `camelCase` (`errorHandler.middleware.ts`) y otros `kebab-case` (`rate-limit.middleware.ts`).

3. **Tests:**
   - Aunque existe `jest.config.js` y una carpeta `__tests__/`, el coverage parece limitado a un solo archivo. Expandir las suites de prueba para cubrir servicios y repositorios críticos.

4. **Base de Datos:**
   - El script `01-init.sql` tiene 1580+ líneas. Idealmente, se debería dividir en archivos más pequeños (uno por tabla o dominio) para facilitar el mantenimiento.
   - No se observa un ORM (TypeORM, Prisma, Sequelize). El uso de `pg` directamente con queries SQL brinda flexibilidad pero aumenta el riesgo de inyección SQL si no se sanitizan bien los inputs (aunque el patrón Repository y el uso de parámetros de `pg` mitigan esto).

5. **Frontend - Mezcla de Patrones:**
   - La carpeta `app/controllers/` en el frontend es inusual para una aplicación Next.js moderna. Normalmente, la lógica de fetch se maneja dentro de Server Components o Custom Hooks. Revisar si esta capa es necesaria o si puede simplificarse con Server Actions de Next.js 16.
   - Los `repositories` del frontend son wrappers de Axios. Considerar usar **React Query (TanStack Query)** o **SWR** para manejo de estado de servidor, caché, revalidación y manejo de errores.

6. **Manejo de Estado Global:**
   - Se usa React Context para Auth y Orders. Para aplicaciones grandes, considerar **Zustand** o **Redux Toolkit** si la complejidad del estado global crece.

7. **Variables de Entorno:**
   - En `docker-compose.yml`, la contraseña de la base de datos y el JWT_SECRET están hardcodeados/visibles. Asegurar que en producción se inyecten mediante secretos de Docker o un vault (HashiCorp Vault, AWS Secrets Manager, etc.).

8. **Frontend Styling:**
   - Existe una mezcla de **CSS Modules** (`*.module.css`) y **Tailwind CSS**. Definir una estrategia única (recomendado Tailwind para todo, o CSS Modules para componentes muy específicos) para mantener consistencia.

9. **Monitoreo y Observabilidad:**
   - No se observa integración con herramientas de APM (Application Performance Monitoring) como Datadog, New Relic o Prometheus/Grafana. Agregar health checks detallados y métricas sería beneficioso para producción.

---

## 10. Conclusión

El proyecto **ADC CCC** presenta una arquitectura moderna, bien estructurada y lista para producción. El uso de TypeScript, Docker, capas de seguridad y patrones de diseño establecidos (Repository, Service, Middlewares) demuestra un enfoque profesional. Las principales oportunidades de mejora radican en la **eliminación de duplicación de código entre frontend y backend**, la **adopción de herramientas de manejo de estado de servidor** (React Query) y la **expansión de la cobertura de tests**.
