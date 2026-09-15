# 02-node-web

## 🌐 Idiomas / Languages / Idiomas

| 🇪🇸 Español | 🇬🇧 English | 🇧🇷 Português |
|------------|-------------|---------------|
| [Leer en español](#español) | [Read in English](#english) | [Ler em português](#português) |

---

## Español

Servidor Express.js containerizado con Docker.

## Estructura

├── server.js        # Servidor Express
├── package.json     # Dependencias
├── Dockerfile       # Configuración Docker
├── .dockerignore    # Archivos excluidos del build
└── README.md        # Este archivo

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Mensaje con hostname y timestamp |
| GET | `/health` | Health check |

## Variables de entorno

| Variable | Por defecto | Descripción |
|----------|-------------|-------------|
| `PORT` | `3000` | Puerto del servidor |
| `SALUDO` | `¡Hola desde Node.js dentro de Docker!` | Mensaje personalizado |
| `HOSTNAME` | *(automático en Docker)* | ID del contenedor |

## Ejecutar

### Local
```bash
npm install
npm start
```

### Docker
```bash
docker build -t node-web-2 .
docker run -d -p 3001:3001 -e PORT=3001 --name puerto-3001 node-web-2
```

### Docker con variables
```bash
docker run -d -p 3012:3012 \
  -e SALUDO="Hola Napoleon" \
  -e HOSTNAME="nar" \
  -e PORT=3012 \
  --name puerto12 \
  node-web-2
```

## Probar

```bash
curl http://localhost:3001
curl http://localhost:3001/health
```

## Dockerfile

```dockerfile
FROM node:26.5.0-alpine
WORKDIR /app
COPY package.json .
RUN npm install
COPY server.js .
EXPOSE 3000
USER node
CMD ["node", "server.js"]
```

---

## PostgreSQL con Docker

### Contenedor básico

```bash
docker run -d \
  --name postgres-container \
  -e POSTGRES_PASSWORD=secreto \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=mydb \
  -v datos-db:/var/lib/postgresql/data \
  -p 5432:5432 \
  --restart unless-stopped \
  postgres:16
```

| Parámetro | Descripción |
|-----------|-------------|
| `-d` | Ejecuta en segundo plano (detach) |
| `--name` | Nombre del contenedor |
| `-e POSTGRES_PASSWORD` | Contraseña del superusuario |
| `-e POSTGRES_USER` | Usuario personalizado (evitar `postgres`) |
| `-e POSTGRES_DB` | Base de datos a crear automáticamente |
| `-v datos-db:/var/lib/postgresql/data` | Volumen para persistir datos |
| `-p 5432:5432` | Mapeo de puertos (host:container) |
| `--restart unless-stopped` | Reinicio automático |

### Conectar al contenedor

```bash
# Shell dentro del contenedor
docker exec -it postgres-container psql -U admin -d mydb

# Ejecutar comando directo
docker exec -it postgres-container psql -U admin -d mydb -c "SELECT * FROM usuarios;"
```

### Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `role "postgres" does not exist` | Usuario incorrecto | Usar `-U admin` (el configurado) |
| `column "nar" does not exist` | Falta comillas en string | Usar `'nar'` (comillas simples) |
| `syntax error near unexpected token '('` | Bash interpreta paréntesis | Usar comillas simples en SQL |

### PostgreSQL con pgAdmin (GUI)

#### Red Docker personalizada

```bash
# Crear red para comunicación entre contenedores
docker network create pg-network

# Conectar contenedor existente a la red
docker network connect pg-network postgres-container
```

#### Ejecutar pgAdmin

```bash
docker run -d \
  --name pgadmin \
  --network pg-network \
  -e PGADMIN_DEFAULT_EMAIL=admin@admin.com \
  -e PGADMIN_DEFAULT_PASSWORD=admin \
  -p 5050:80 \
  dpage/pgadmin4
```

#### Conexión en pgAdmin

| Campo | Valor |
|-------|-------|
| Host | `postgres-container` (nombre del contenedor) |
| Port | `5432` |
| User | `admin` |
| Password | `secreto` |
| Database | `mydb` |

> **Nota:** Usar nombre del contenedor Docker como Host (no `localhost`) porque están en la misma red Docker.

### Múltiples contenedores PostgreSQL

```bash
# Contenedor 1 - Puerto 5432
docker run -d \
  --name postgres-container \
  -e POSTGRES_PASSWORD=secreto \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=mydb \
  -v datos-db:/var/lib/postgresql/data \
  -p 5432:5432 \
  --restart unless-stopped \
  --network pg-network \
  postgres:16

# Contenedor 2 - Puerto 5433
docker run -d \
  --name postgres-new \
  -e POSTGRES_PASSWORD=secreto \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=mydb \
  -v datos-new:/var/lib/postgresql/data \
  -p 5433:5432 \
  --restart unless-stopped \
  --network pg-network \
  postgres:16

# Contenedor 3 - Puerto 5434
docker run -d \
  --name postgres-otro \
  -e POSTGRES_PASSWORD=secreto \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=mydb \
  -v datos-otro:/var/lib/postgresql/data \
  -p 5434:5432 \
  --restart unless-stopped \
  --network pg-network \
  postgres:16
```

| Contenedor | Puerto Host | Acceso externo |
|------------|-------------|----------------|
| postgres-container | 5432 | `localhost:5432` |
| postgres-new | 5433 | `localhost:5433` |
| postgres-otro | 5434 | `localhost:5434` |

#### Conexión en pgAdmin (múltiples servidores)

| Servidor | Host | Port | User | Password |
|----------|------|------|------|----------|
| server-1 | `postgres-container` | 5432 | admin | secreto |
| server-2 | `postgres-new` | 5432 | admin | secreto |
| server-3 | `postgres-otro` | 5432 | admin | secreto |

### Limpiar Docker

```bash
# Verificar espacio en uso
docker system df

# Eliminar contenedores detenidos
docker container prune -f

# Eliminar volúmenes no usados
docker volume prune -f

# Eliminar cache de build
docker builder prune -f

# Limpieza profunda (cuidado: elimina imágenes)
docker system prune -a --volumes -f
```

| Comando | Qué elimina |
|---------|-------------|
| `docker container prune -f` | Contenedores detenidos |
| `docker volume prune -f` | Volúmenes sin usar |
| `docker builder prune -f` | Cache de build |
| `docker system prune -a` | Todo lo no usado (incluye imágenes) |

---

## English

Express.js server containerized with Docker.

### Structure

├── server.js        # Express server
├── package.json     # Dependencies
├── Dockerfile       # Docker configuration
├── .dockerignore    # Files excluded from build
└── README.md        # This file

### Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Message with hostname and timestamp |
| GET | `/health` | Health check |

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `3000` | Server port |
| `SALUDO` | `¡Hola desde Node.js dentro de Docker!` | Custom message |
| `HOSTNAME` | *(automatic in Docker)* | Container ID |

### Run

#### Local
```bash
npm install
npm start
```

#### Docker
```bash
docker build -t node-web-2 .
docker run -d -p 3001:3001 -e PORT=3001 --name puerto-3001 node-web-2
```

#### Docker with variables
```bash
docker run -d -p 3012:3012 \
  -e SALUDO="Hola Napoleon" \
  -e HOSTNAME="nar" \
  -e PORT=3012 \
  --name puerto12 \
  node-web-2
```

### Test

```bash
curl http://localhost:3001
curl http://localhost:3001/health
```

### Dockerfile

```dockerfile
FROM node:26.5.0-alpine
WORKDIR /app
COPY package.json .
RUN npm install
COPY server.js .
EXPOSE 3000
USER node
CMD ["node", "server.js"]
```

### PostgreSQL with Docker

#### Basic container

```bash
docker run -d \
  --name postgres-container \
  -e POSTGRES_PASSWORD=secreto \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=mydb \
  -v datos-db:/var/lib/postgresql/data \
  -p 5432:5432 \
  --restart unless-stopped \
  postgres:16
```

| Parameter | Description |
|-----------|-------------|
| `-d` | Run in background (detach) |
| `--name` | Container name |
| `-e POSTGRES_PASSWORD` | Superuser password |
| `-e POSTGRES_USER` | Custom user (avoid `postgres`) |
| `-e POSTGRES_DB` | Database to create automatically |
| `-v datos-db:/var/lib/postgresql/data` | Volume for data persistence |
| `-p 5432:5432` | Port mapping (host:container) |
| `--restart unless-stopped` | Auto restart |

#### Connect to container

```bash
# Shell inside container
docker exec -it postgres-container psql -U admin -d mydb

# Run command directly
docker exec -it postgres-container psql -U admin -d mydb -c "SELECT * FROM usuarios;"
```

#### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `role "postgres" does not exist` | Wrong user | Use `-U admin` (configured one) |
| `column "nar" does not exist` | Missing quotes in string | Use `'nar'` (single quotes) |
| `syntax error near unexpected token '('` | Bash interprets parentheses | Use single quotes in SQL |

#### PostgreSQL with pgAdmin (GUI)

```bash
# Create network for container communication
docker network create pg-network

# Connect existing container to network
docker network connect pg-network postgres-container

# Run pgAdmin
docker run -d \
  --name pgadmin \
  --network pg-network \
  -e PGADMIN_DEFAULT_EMAIL=admin@admin.com \
  -e PGADMIN_DEFAULT_PASSWORD=admin \
  -p 5050:80 \
  dpage/pgadmin4
```

| Field | Value |
|-------|-------|
| Host | `postgres-container` (container name) |
| Port | `5432` |
| User | `admin` |
| Password | `secreto` |
| Database | `mydb` |

> **Note:** Use Docker container name as Host (not `localhost`) because they are on the same Docker network.

#### Multiple PostgreSQL Containers

| Container | Host Port | External Access |
|-----------|-----------|-----------------|
| postgres-container | 5432 | `localhost:5432` |
| postgres-new | 5433 | `localhost:5433` |
| postgres-otro | 5434 | `localhost:5434` |

#### Clean Docker

```bash
# Check disk usage
docker system df

# Remove stopped containers
docker container prune -f

# Remove unused volumes
docker volume prune -f

# Remove build cache
docker builder prune -f

# Deep clean (careful: removes images)
docker system prune -a --volumes -f
```

| Command | What it removes |
|---------|-----------------|
| `docker container prune -f` | Stopped containers |
| `docker volume prune -f` | Unused volumes |
| `docker builder prune -f` | Build cache |
| `docker system prune -a` | Everything unused (including images) |

---

## Português

Servidor Express.js containerizado com Docker.

### Estrutura

├── server.js        # Servidor Express
├── package.json     # Dependências
├── Dockerfile       # Configuração Docker
├── .dockerignore    # Arquivos excluídos do build
└── README.md        # Este arquivo

### Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Mensagem com hostname e timestamp |
| GET | `/health` | Health check |

### Variáveis de Ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `PORT` | `3000` | Porta do servidor |
| `SALUDO` | `¡Hola desde Node.js dentro de Docker!` | Mensagem personalizada |
| `HOSTNAME` | *(automático no Docker)* | ID do contêiner |

### Executar

#### Local
```bash
npm install
npm start
```

#### Docker
```bash
docker build -t node-web-2 .
docker run -d -p 3001:3001 -e PORT=3001 --name puerto-3001 node-web-2
```

#### Docker com variáveis
```bash
docker run -d -p 3012:3012 \
  -e SALUDO="Hola Napoleon" \
  -e HOSTNAME="nar" \
  -e PORT=3012 \
  --name puerto12 \
  node-web-2
```

### Testar

```bash
curl http://localhost:3001
curl http://localhost:3001/health
```

### Dockerfile

```dockerfile
FROM node:26.5.0-alpine
WORKDIR /app
COPY package.json .
RUN npm install
COPY server.js .
EXPOSE 3000
USER node
CMD ["node", "server.js"]
```

### PostgreSQL com Docker

#### Contêiner básico

```bash
docker run -d \
  --name postgres-container \
  -e POSTGRES_PASSWORD=secreto \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=mydb \
  -v dados-db:/var/lib/postgresql/data \
  -p 5432:5432 \
  --restart unless-stopped \
  postgres:16
```

| Parâmetro | Descrição |
|-----------|-----------|
| `-d` | Executa em segundo plano (detach) |
| `--name` | Nome do contêiner |
| `-e POSTGRES_PASSWORD` | Senha do superusuário |
| `-e POSTGRES_USER` | Usuário personalizado (evitar `postgres`) |
| `-e POSTGRES_DB` | Banco de dados a criar automaticamente |
| `-v dados-db:/var/lib/postgresql/data` | Volume para persistir dados |
| `-p 5432:5432` | Mapeamento de portas (host:container) |
| `--restart unless-stopped` | Reinício automático |

#### Conectar ao contêiner

```bash
# Shell dentro do contêiner
docker exec -it postgres-container psql -U admin -d mydb

# Executar comando diretamente
docker exec -it postgres-container psql -U admin -d mydb -c "SELECT * FROM usuarios;"
```

#### Erros Comuns

| Erro | Causa | Solução |
|------|-------|---------|
| `role "postgres" does not exist` | Usuário incorreto | Usar `-U admin` (o configurado) |
| `column "nar" does not exist` | Faltam aspas na string | Usar `'nar'` (aspas simples) |
| `syntax error near unexpected token '('` | Bash interpreta parênteses | Usar aspas simples no SQL |

#### PostgreSQL com pgAdmin (GUI)

```bash
# Criar rede para comunicação entre contêineres
docker network create pg-network

# Conectar contêiner existente à rede
docker network connect pg-network postgres-container

# Executar pgAdmin
docker run -d \
  --name pgadmin \
  --network pg-network \
  -e PGADMIN_DEFAULT_EMAIL=admin@admin.com \
  -e PGADMIN_DEFAULT_PASSWORD=admin \
  -p 5050:80 \
  dpage/pgadmin4
```

| Campo | Valor |
|-------|-------|
| Host | `postgres-container` (nome do contêiner) |
| Port | `5432` |
| User | `admin` |
| Password | `secreto` |
| Database | `mydb` |

> **Nota:** Usar o nome do contêiner Docker como Host (não `localhost`) porque estão na mesma rede Docker.

#### Múltiplos Contêineres PostgreSQL

| Contêiner | Porta Host | Acesso Externo |
|-----------|------------|----------------|
| postgres-container | 5432 | `localhost:5432` |
| postgres-new | 5433 | `localhost:5433` |
| postgres-otro | 5434 | `localhost:5434` |

#### Limpar Docker

```bash
# Verificar uso de disco
docker system df

# Remover contêineres parados
docker container prune -f

# Remover volumes não usados
docker volume prune -f

# Remover cache de build
docker builder prune -f

# Limpeza profunda (cuidado: remove imagens)
docker system prune -a --volumes -f
```

| Comando | O que remove |
|---------|--------------|
| `docker container prune -f` | Contêineres parados |
| `docker volume prune -f` | Volumes não usados |
| `docker builder prune -f` | Cache de build |
| `docker system prune -a` | Tudo não usado (incluindo imagens) |
