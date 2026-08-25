## Arquitectura

Capas, desde fuera hacia adentro, cada una solo conoce lo que está por debajo:

```
app/api/v1/endpoints/*.py   → routers FastAPI: validan con pydantic y llaman al service. Sin lógica.
app/services/*.py           → lógica de negocio. Punto de extensión: aquí van las reglas futuras.
app/repositories/*.py       → acceso a datos vía SQLAlchemy async.
app/models/*.py             → un archivo por tabla, ORM declarativo 2.0 (Mapped/mapped_column).
app/schemas/*.py            → Create/Update/Read por entidad, Pydantic v2 (ConfigDict(from_attributes=True)).
app/core/                   → config.py (Settings), database.py (engine/sesión async), security.py (jwt/bcrypt).
```

**CRUD genérico por fábrica** (`app/api/v1/endpoints/crud_factory.py`): las 11 tablas con clave primaria simple (`categories`, `customers`, `employees`, `orders`, `products`, `region`, `shippers`, `suppliers`, `territories`, `us_states`, `customer_demographics`) no tienen un router propio — `build_crud_router()` genera `list`, `get`, `create`, `update` y `delete` a partir del modelo y sus esquemas, y `app/api/v1/router.py` los registra en un bucle. Para añadir una tabla nueva con PK simple: `modelo + esquemas + una entrada en _simple_crud_entities`, nada más.

Las 3 tablas puente con **clave primaria compuesta** (`order_details`, `employee_territories`, `customer_customer_demo`) no encajan en el genérico (necesitan dos parámetros de ruta) y tienen cada una su propio router en `app/api/v1/endpoints/`, reutilizando igualmente `BaseRepository`/`BaseService` genéricos.

`BaseRepository`/`BaseService` (`app/repositories/base.py`, `app/services/base.py`) usan sintaxis de genéricos PEP 695 (`class BaseRepository[ModelType: Base]`). Para añadir una regla de negocio a una entidad concreta, subclasificar `BaseService` (ver `app/services/auth.py` como ejemplo) en vez de tocar el router.

**Auth**: `POST /api/v1/auth/register` y `/auth/login` (`OAuth2PasswordRequestForm`, no JSON) en `app/api/v1/endpoints/auth.py` + `app/services/auth.py`. Lectura (`GET`) pública en todas las entidades; escritura (`POST`/`PUT`/`DELETE`) exige `Authorization: Bearer <jwt>`, resuelto en `app/api/deps.py::get_current_user`.



# Estructura del proyecto

```
nortwind/
├── app/
│   ├── main.py               punto de entrada: instancia FastAPI, monta el router /api/v1 y expone /health
│   ├── core/                 configuración transversal, sin lógica de negocio
│   │   ├── config.py         Settings (pydantic-settings): lee .env, sin defaults sensibles
│   │   ├── database.py       engine y sesiones async de SQLAlchemy, dependencia get_db()
│   │   └── security.py       hashing de contraseñas (bcrypt) y jwt (crear/decodificar)
│   ├── models/               ORM declarativo 2.0 (Mapped/mapped_column), un archivo por tabla
│   │   ├── base.py           DeclarativeBase común
│   │   ├── user.py           tabla users (auth, no forma parte del esquema Northwind original)
│   │   └── ...               reflejan 1:1 las 14 tablas de northwind
│   ├── schemas/              esquemas Pydantic v2 (entrada/salida de la api), uno por entidad
│   │   ├── token.py          Token (respuesta del login)
│   │   ├── user.py           UserBase/UserCreate/UserRead
│   │   └── ...               <entidad>Base/<entidad>Create/<entidad>Update/<entidad>Read por cada tabla, en paralelo a models/
│   ├── repositories/         acceso a datos vía SQLAlchemy async, sin reglas de negocio
│   │   ├── base.py           BaseRepository[ModelType] genérico: list/get/create/update/delete, soporta clave primaria simple o compuesta
│   │   └── user.py           añade get_by_username(), usado en el login
│   ├── services/             lógica de negocio; único lugar donde deberían añadirse validaciones
│   │   ├── base.py           BaseService[ModelType] genérico, envuelve un repository
│   │   └── auth.py           registro, validación de credenciales y emisión de jwt
│   └── api/
│       ├── deps.py           dependencias fastapi comunes: get_current_user (valida el jwt)
│       └── v1/
│           ├── router.py                       agrega todos los endpoints bajo /api/v1
│           └── endpoints/
│               ├── auth.py                     POST /auth/register, /auth/login
│               ├── crud_factory.py             build_crud_router(): genera list/get/create/update/delete para una entidad con pk simple
│               ├── order_details.py            router propio (pk compuesta: order_id+product_id)
│               ├── employee_territories.py     router propio (pk compuesta: employee_id+territory_id)
│               └── customer_customer_demo.py   router propio (pk compuesta: customer_id+customer_type_id)
│
├── alembic/
│   ├── env.py                           configuración async de alembic, apunta a Base.metadata
│   ├── script.py.mako                   plantilla usada al generar nuevas migraciones
│   └── versions/
│       └── 0001_create_users_table.py   única migración: crea `users` (las 14 tablas de northwind ya existían en la bd)
│
├── tests/
│   └── test_health.py        smoke test de /health (asyncio_mode=auto en pyproject.toml)
│
├── pyproject.toml            dependencias, config de ruff (lint/format) y pytest
├── alembic.ini               configuración de alembic (script_location, logging)
├── .env.example              plantilla de variables de entorno — copiar como .env
├── .gitignore                archivos ignorados por git
└── README.md                 instrucciones de instalación, migración y arranque
```



## Material de referencia

`northwind_psql/` contiene el esquema y datos de Northwind en SQL puro. Se debe crear la base de datos `northwind` y ejecutar el script de creación para generar y poblar las tablas.



## Cómo fluye una petición

```
request → api/v1/endpoints/*.py  (valida con schemas, sin lógica)
        → services/*.py          (reglas de negocio; punto de extensión)
        → repositories/*.py      (query SQLAlchemy)
        → models/*.py            (tabla real en PostgreSQL)
```

Las vistas (routers) nunca acceden a `repositories` ni a la sesión de bd directamente: siempre pasan por un `service`. Para añadir una tabla nueva con clave primaria simple no hace falta escribir un router: basta con su modelo, sus esquemas y una entrada en `_simple_crud_entities` (`app/api/v1/router.py`), que usa `crud_factory.build_crud_router()`. Solo las 3 tablas puente con clave primaria compuesta tienen un router propio, porque necesitan dos parámetros de ruta.
