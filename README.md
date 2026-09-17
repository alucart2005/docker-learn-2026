# 🐳 Docker Learn 2026

> **Un viaje de aprendizaje con Docker, desde "Hello World" hasta asistentes de IA.**
> **A learning journey with Docker, from "Hello World" to AI assistants.**
> **Uma jornada de aprendizado com Docker, do "Hello World" até assistentes de IA.**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Express.js](https://img.shields.io/badge/Express.js-000000?style=flat&logo=express&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)

---

## [🇪🇸 Español](#español) | [🇬🇧 English](#english) | [🇧🇷 Português](#português)

---

<a id="español"></a>
## 🇪🇸 Español

### Sobre el proyecto

Este repositorio documenta mi viaje de aprendizaje con Docker durante 2026. Cada proyecto se construye sobre el anterior, demostrando cómo fui dominando conceptos progresivamente — desde un simple "Hello World" hasta una aplicación web con inteligencia artificial corriendo en contenedores.

**Lo más importante: me disfruté cada paso del camino.** Aprender Docker no fue solo un requisito técnico, sino una experiencia que disfruté haciendo. Cada `docker build` exitoso, cada contenedor que corría, cada error que resolvía — todo eso fue parte del aprendizaje.

---

### Proyectos

#### 01 - Hello Docker

Un script Node.js que ejecuta dentro de un contenedor y muestra información del sistema: versión de Node, plataforma y arquitectura.

**Tecnologías:** Node.js (Alpine)

**Comandos:**
```bash
# Construir la imagen
docker build -t hello-docker .

# Ejecutar el contenedor
docker run hello-docker
```

**Conceptos aprendidos:**
- `FROM` — imagen base
- `WORKDIR` — directorio de trabajo
- `COPY` — copiar archivos al contenedor
- `CMD` — comando de entrada
- Por qué Alpine es más ligero

---

#### 02 - Express Web Server

Un servidor web Express.js con dos endpoints (`/` y `/health`), variables de entorno, Docker Compose, BuildKit y documentación completa de PostgreSQL + pgAdmin.

**Tecnologías:** Node.js, Express.js, Docker Compose, BuildKit

**Comandos:**
```bash
# Construir y ejecutar con Docker Compose
docker compose up --build

# O por separado
docker build -t web-server .
docker run -p 3000:3000 -e SALUDO="Hola" web-server

# Verificar endpoints
curl http://localhost:3000
curl http://localhost:3000/health
```

**Variables de entorno:**
| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `PORT` | Puerto del servidor | `3000` |
| `SALUDO` | Mensaje de saludo | `Hola Mundo` |
| `HOSTNAME` | Nombre del host | `localhost` |

**Conceptos aprendidos:**
- Multi-stage builds y BuildKit (`--mount=type=cache`)
- Seguridad: `USER node` (ejecutar como usuario no-root)
- Docker Compose para orquestación
- `.dockerignore` eficiente
- PostgreSQL con Docker y pgAdmin
- Dos versiones de Dockerfile (simple vs. producción)

---

#### 03 - AI Assistant

Un asistente de IA basado en Flask que se conecta a un modelo de lenguaje local (Docker Model Runner) para responder preguntas sobre Docker. Incluye una interfaz web con tema cyberpunk.

**Tecnologías:** Python, Flask, OpenAI Client, Docker Model Runner

**Comandos:**
```bash
# Pull del modelo de IA (requerido una vez)
docker model pull ai/smollm2

# Construir y ejecutar
docker build -t ai-assistant .
docker run -p 5000:5000 ai-assistant

# Abrir en navegador
http://localhost:5000
```

**Conceptos aprendidos:**
- Patrones de Dockerfile para Python (`pip install --no-cache-dir`)
- Docker Model Runner para inferencia local
- Integración de IA en contenedores
- Comunicación entre servicios Docker

---

### Progresión de aprendizaje

| Aspecto | 01 - Hello Docker | 02 - Express Web | 03 - AI Assistant |
|---------|-------------------|------------------|-------------------|
| **Lenguaje** | JavaScript | JavaScript + Express | Python + Flask |
| **Complejidad** | Mínima | Intermedia | Alta |
| **Conceptos Docker** | Básicos | Compose, BuildKit, seguridad | Model Runner, multi-servicio |
| **Servicios externos** | Ninguno | PostgreSQL, pgAdmin | Docker Model Runner |
| **Seguridad** | Root | Usuario no-root | Root |

---

### Comandos Docker útiles

```bash
# Construir imagen
docker build -t nombre .

# Ejecutar contenedor
docker run -p puerto_host:puerto_contenedor nombre

# Listar contenedores en ejecución
docker ps

# Ver logs
docker logs nombre_contenedor

# Detener contenedor
docker stop nombre_contenedor

# Docker Compose
docker compose up --build    # Construir y ejecutar
docker compose down          # Detener y eliminar
docker compose logs          # Ver logs

# Limpieza
docker system prune -a       # Eliminar todo lo no utilizado
docker system df             # Ver espacio en disco
docker image prune -a        # Eliminar imágenes no utilizadas
```

---

### Reflexión

> Aprender Docker fue una de las experiencias más gratificantes de mi desarrollo profesional. No se trató solo de memorizar comandos, sino de entender una nueva forma de pensar sobre el software. Cada proyecto en este repositorio representa un momento de "¡Eureka!" — cuando algo que parecía complejo finalmente hacía sentido.
>
> **Mi consejo:** disfruten cada paso. Cada error es una oportunidad de aprender, cada contenedor que funciona es una victoria. El proceso de aprendizaje es tan valioso como el resultado final.

---

<a id="english"></a>
## 🇬🇧 English

### About the project

This repository documents my learning journey with Docker during 2026. Each project builds upon the previous one, showing how I progressively mastered concepts — from a simple "Hello World" to a web application with AI running in containers.

**The most important thing: I enjoyed every step of the way.** Learning Docker wasn't just a technical requirement — it was an experience I genuinely enjoyed. Every successful `docker build`, every container that ran, every error I resolved — it was all part of the learning process.

---

### Projects

#### 01 - Hello Docker

A Node.js script that runs inside a container and displays system information: Node version, platform, and architecture.

**Technologies:** Node.js (Alpine)

**Commands:**
```bash
# Build the image
docker build -t hello-docker .

# Run the container
docker run hello-docker
```

**Concepts learned:**
- `FROM` — base image
- `WORKDIR` — working directory
- `COPY` — copy files into container
- `CMD` — entry command
- Why Alpine is lighter

---

#### 02 - Express Web Server

An Express.js web server with two endpoints (`/` and `/health`), environment variables, Docker Compose, BuildKit, and complete PostgreSQL + pgAdmin documentation.

**Technologies:** Node.js, Express.js, Docker Compose, BuildKit

**Commands:**
```bash
# Build and run with Docker Compose
docker compose up --build

# Or separately
docker build -t web-server .
docker run -p 3000:3000 -e SALUDO="Hello" web-server

# Verify endpoints
curl http://localhost:3000
curl http://localhost:3000/health
```

**Environment variables:**
| Variable | Description | Default value |
|----------|-------------|---------------|
| `PORT` | Server port | `3000` |
| `SALUDO` | Greeting message | `Hello World` |
| `HOSTNAME` | Host name | `localhost` |

**Concepts learned:**
- Multi-stage builds and BuildKit (`--mount=type=cache`)
- Security: `USER node` (run as non-root user)
- Docker Compose for orchestration
- Efficient `.dockerignore`
- PostgreSQL with Docker and pgAdmin
- Two Dockerfile versions (simple vs. production)

---

#### 03 - AI Assistant

An AI assistant built with Flask that connects to a local language model (Docker Model Runner) to answer questions about Docker. Features a cyberpunk-themed web interface.

**Technologies:** Python, Flask, OpenAI Client, Docker Model Runner

**Commands:**
```bash
# Pull the AI model (required once)
docker model pull ai/smollm2

# Build and run
docker build -t ai-assistant .
docker run -p 5000:5000 ai-assistant

# Open in browser
http://localhost:5000
```

**Concepts learned:**
- Dockerfile patterns for Python (`pip install --no-cache-dir`)
- Docker Model Runner for local inference
- AI integration in containers
- Docker service communication

---

### Learning progression

| Aspect | 01 - Hello Docker | 02 - Express Web | 03 - AI Assistant |
|--------|-------------------|------------------|-------------------|
| **Language** | JavaScript | JavaScript + Express | Python + Flask |
| **Complexity** | Minimal | Intermediate | High |
| **Docker concepts** | Basics | Compose, BuildKit, security | Model Runner, multi-service |
| **External services** | None | PostgreSQL, pgAdmin | Docker Model Runner |
| **Security** | Root | Non-root user | Root |

---

### Useful Docker commands

```bash
# Build image
docker build -t name .

# Run container
docker run -p host_port:container_port name

# List running containers
docker ps

# View logs
docker logs container_name

# Stop container
docker stop container_name

# Docker Compose
docker compose up --build    # Build and run
docker compose down          # Stop and remove
docker compose logs          # View logs

# Cleanup
docker system prune -a       # Remove all unused resources
docker system df             # Show disk usage
docker image prune -a        # Remove unused images
```

---

### Reflection

> Learning Docker was one of the most rewarding experiences in my professional development. It wasn't just about memorizing commands — it was about understanding a new way of thinking about software. Each project in this repository represents a "Eureka!" moment — when something that seemed complex finally made sense.
>
> **My advice:** enjoy every step. Every error is an opportunity to learn, every container that works is a victory. The learning process is as valuable as the final result.

---

<a id="português"></a>
## 🇧🇷 Português

### Sobre o projeto

Este repositório documenta minha jornada de aprendizado com Docker durante 2026. Cada projeto se constrói sobre o anterior, mostrando como fui dominando conceitos progressivamente — de um simples "Hello World" até uma aplicação web com inteligência artificial rodando em contêineres.

**O mais importante: eu aproveitei cada passo do caminho.** Aprender Docker não foi apenas um requisito técnico — foi uma experiência que genuinamente aproveitei. Cada `docker build` bem-sucedido, cada contêiner que rodou, cada erro que resolvi — tudo isso fez parte do aprendizado.

---

### Projetos

#### 01 - Hello Docker

Um script Node.js que roda dentro de um contêiner e exibe informações do sistema: versão do Node, plataforma e arquitetura.

**Tecnologias:** Node.js (Alpine)

**Comandos:**
```bash
# Construir a imagem
docker build -t hello-docker .

# Rodar o contêiner
docker run hello-docker
```

**Conceitos aprendidos:**
- `FROM` — imagem base
- `WORKDIR` — diretório de trabalho
- `COPY` — copiar arquivos para o contêiner
- `CMD` — comando de entrada
- Por que Alpine é mais leve

---

#### 02 - Express Web Server

Um servidor web Express.js com dois endpoints (`/` e `/health`), variáveis de ambiente, Docker Compose, BuildKit e documentação completa de PostgreSQL + pgAdmin.

**Tecnologias:** Node.js, Express.js, Docker Compose, BuildKit

**Comandos:**
```bash
# Construir e rodar com Docker Compose
docker compose up --build

# Ou separadamente
docker build -t web-server .
docker run -p 3000:3000 -e SALUDO="Olá" web-server

# Verificar endpoints
curl http://localhost:3000
curl http://localhost:3000/health
```

**Variáveis de ambiente:**
| Variável | Descrição | Valor padrão |
|----------|-----------|--------------|
| `PORT` | Porta do servidor | `3000` |
| `SALUDO` | Mensagem de saudação | `Hello World` |
| `HOSTNAME` | Nome do host | `localhost` |

**Conceitos aprendidos:**
- Multi-stage builds e BuildKit (`--mount=type=cache`)
- Segurança: `USER node` (rodar como usuário não-root)
- Docker Compose para orquestração
- `.dockerignore` eficiente
- PostgreSQL com Docker e pgAdmin
- Duas versões de Dockerfile (simples vs. produção)

---

#### 03 - AI Assistant

Um assistente de IA construído com Flask que se conecta a um modelo de linguagem local (Docker Model Runner) para responder perguntas sobre Docker. Possui uma interface web com tema cyberpunk.

**Tecnologias:** Python, Flask, OpenAI Client, Docker Model Runner

**Comandos:**
```bash
# Baixar o modelo de IA (requerido uma vez)
docker model pull ai/smollm2

# Construir e rodar
docker build -t ai-assistant .
docker run -p 5000:5000 ai-assistant

# Abrir no navegador
http://localhost:5000
```

**Conceitos aprendidos:**
- Padrões de Dockerfile para Python (`pip install --no-cache-dir`)
- Docker Model Runner para inferência local
- Integração de IA em contêineres
- Comunicação entre serviços Docker

---

### Progressão de aprendizado

| Aspecto | 01 - Hello Docker | 02 - Express Web | 03 - AI Assistant |
|---------|-------------------|------------------|-------------------|
| **Linguagem** | JavaScript | JavaScript + Express | Python + Flask |
| **Complexidade** | Mínima | Intermediária | Alta |
| **Conceitos Docker** | Básicos | Compose, BuildKit, segurança | Model Runner, multi-serviço |
| **Serviços externos** | Nenhum | PostgreSQL, pgAdmin | Docker Model Runner |
| **Segurança** | Root | Usuário não-root | Root |

---

### Comandos Docker úteis

```bash
# Construir imagem
docker build -t nome .

# Rodar contêiner
docker run -p porta_host:porta_contêiner nome

# Listar contêineres em execução
docker ps

# Ver logs
docker logs nome_contêiner

# Parar contêiner
docker stop nome_contêiner

# Docker Compose
docker compose up --build    # Construir e rodar
docker compose down          # Parar e remover
docker compose logs          # Ver logs

# Limpeza
docker system prune -a       # Remover tudo não utilizado
docker system df             # Mostrar uso de disco
docker image prune -a        # Remover imagens não utilizadas
```

---

### Reflexão

> Aprender Docker foi uma das experiências mais gratificantes do meu desenvolvimento profissional. Não se tratava apenas de memorizar comandos — era sobre entender uma nova forma de pensar sobre software. Cada projeto neste repositório representa um momento de "Eureka!" — quando algo que parecia complexo finalmente fazia sentido.
>
> **Meu conselho:** aproveitem cada passo. Cada erro é uma oportunidade de aprender, cada contêiner que funciona é uma vitória. O processo de aprendizado é tão valioso quanto o resultado final.

---

## 📄 Licencia

Este projeto es para fines de aprendizaje y portafolio. Siéntete libre de usar como referencia.

This project is for learning and portfolio purposes. Feel free to use as reference.

Este projeto é para fins de aprendizado e portfólio. Sinta-se livre para usar como referência.
