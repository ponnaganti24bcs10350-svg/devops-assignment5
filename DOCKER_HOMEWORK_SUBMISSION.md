# Docker Homework Tasks: Hello World Applications

**Name:** Srividya Ponnaganti  

---

## Folder Structure
```text
.
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
- **Code:** `server.js` using Node HTTP server.
- **Port:** 3000
- **Build & Run:**
```bash
cd nodejs-app
docker build -t nodejs-app .
docker run -d -p 3000:3000 --name my-nodejs-app nodejs-app
```
- **Access in browser:** `http://localhost:3000`

---

## 2. Python Application (`python-app`)
- **Code:** `app.py` standard library HTTP server in Python 3.11.
- **Port:** 5000
- **Build & Run:**
```bash
cd python-app
docker build -t python-app .
docker run -d -p 5000:5000 --name my-python-app python-app
```
- **Access in browser:** `http://localhost:5000`

---

## 3. Java Application (`java-app`)
- **Code:** `App.java` built with JDK 17 and running on lightweight JRE.
- **Port:** 8080
- **Build & Run:**
```bash
cd java-app
docker build -t java-app .
docker run -d -p 8080:8080 --name my-java-app java-app
```
- **Access in browser:** `http://localhost:8080`

---

## 4. Apache Web Server (`Apache-app`)
- **Code:** `index.html` served using `httpd:alpine`.
- **Port:** 80
- **Build & Run:**
```bash
cd Apache-app
docker build -t apache-app .
docker run -d -p 80:80 --name my-apache-app apache-app
```
- **Access in browser:** `http://localhost:80`

---

## 5. React Application (`React-app`)
- **Code:** `index.html` React 18 component served with Nginx.
- **Port:** 80
- **Build & Run:**
```bash
cd React-app
docker build -t react-app .
docker run -d -p 80:80 --name my-react-app react-app
```
- **Access in browser:** `http://localhost:80`

---

## 6. Nginx Application (`nginx-app`)
- **Code:** `index.html` served using `nginx:alpine`.
- **Port:** 80
- **Build & Run:**
```bash
cd nginx-app
docker build -t nginx-app .
docker run -d -p 80:80 --name my-nginx-app nginx-app
```
- **Access in browser:** `http://localhost:80`

---

## Verification
All 6 containers build cleanly and serve a responsive "Hello World!" web page on their respective ports.
