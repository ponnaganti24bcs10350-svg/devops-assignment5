# Session 06: Docker Homework Tasks - Hello World Applications

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**GitHub Repository:** [ponnaganti24bcs10350-svg/devops-assignment5](https://github.com/ponnaganti24bcs10350-svg/devops-assignment5)  

---

## Folder Structure
```text
session6-docker-hello-world/
├── nodejs-app/
│   ├── server.js
│   ├── package.json
│   └── Dockerfile
├── python-app/
│   ├── app.py
│   └── Dockerfile
├── java-app/
│   ├── App.java
│   └── Dockerfile
├── Apache-app/
│   ├── index.html
│   └── Dockerfile
├── React-app/
│   ├── index.html
│   └── Dockerfile
└── nginx-app/
    ├── index.html
    └── Dockerfile
```

---

## 1. Node.js Application (`nodejs-app`)
- **Application Code:** `server.js` using Node HTTP module.
- **Port:** 3000
- **Dockerfile:**
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
COPY server.js ./
EXPOSE 3000
CMD ["node", "server.js"]
```
- **Build & Run Commands:**
```bash
cd nodejs-app
docker build -t nodejs-app .
docker run -d -p 3000:3000 --name my-nodejs-app nodejs-app
```
- **Verification:** Access `http://localhost:3000` &rarr; displays "Hello World from Node.js!".

---

## 2. Python Application (`python-app`)
- **Application Code:** `app.py` standard library HTTP server in Python 3.11.
- **Port:** 5000
- **Dockerfile:**
```dockerfile
FROM python:3.11-alpine
WORKDIR /app
COPY app.py ./
EXPOSE 5000
CMD ["python", "app.py"]
```
- **Build & Run Commands:**
```bash
cd python-app
docker build -t python-app .
docker run -d -p 5000:5000 --name my-python-app python-app
```
- **Verification:** Access `http://localhost:5000` &rarr; displays "Hello World from Python!".

---

## 3. Java Application (`java-app`)
- **Application Code:** `App.java` built with JDK 17.
- **Port:** 8080
- **Dockerfile:**
```dockerfile
FROM eclipse-temurin:17-jdk-alpine AS builder
WORKDIR /app
COPY App.java ./
RUN javac App.java

FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=builder /app/App.class ./
EXPOSE 8080
CMD ["java", "App"]
```
- **Build & Run Commands:**
```bash
cd java-app
docker build -t java-app .
docker run -d -p 8080:8080 --name my-java-app java-app
```
- **Verification:** Access `http://localhost:8080` &rarr; displays "Hello World from Java!".

---

## 4. Apache Web Server (`Apache-app`)
- **Application Code:** `index.html` served using `httpd:alpine`.
- **Port:** 80
- **Dockerfile:**
```dockerfile
FROM httpd:alpine
COPY index.html /usr/local/apache2/htdocs/
EXPOSE 80
```
- **Build & Run Commands:**
```bash
cd Apache-app
docker build -t apache-app .
docker run -d -p 8081:80 --name my-apache-app apache-app
```
- **Verification:** Access `http://localhost:8081` &rarr; displays "Hello World from Apache HTTP Server!".

---

## 5. React Application (`React-app`)
- **Application Code:** `index.html` React 18 component served with Nginx.
- **Port:** 80
- **Dockerfile:**
```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
EXPOSE 80
```
- **Build & Run Commands:**
```bash
cd React-app
docker build -t react-app .
docker run -d -p 8082:80 --name my-react-app react-app
```
- **Verification:** Access `http://localhost:8082` &rarr; displays "Hello World from React 18!".

---

## 6. Nginx Application (`nginx-app`)
- **Application Code:** `index.html` served using `nginx:alpine`.
- **Port:** 80
- **Dockerfile:**
```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
EXPOSE 80
```
- **Build & Run Commands:**
```bash
cd nginx-app
docker build -t nginx-app .
docker run -d -p 8083:80 --name my-nginx-app nginx-app
```
- **Verification:** Access `http://localhost:8083` &rarr; displays "Hello World from Nginx!".

---

## Verification Summary
All 6 applications build cleanly, create isolated lightweight Docker containers, and serve "Hello World" responsive web pages on their configured ports.
