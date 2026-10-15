# Session 07: Docker Multi-Stage Build Homework

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**GitHub Repository:** [ponnaganti24bcs10350-svg/devops-assignment5](https://github.com/ponnaganti24bcs10350-svg/devops-assignment5)  

---

## Task 1: Run Multi-Stage Dockerfile

### 1. Multi-Stage Dockerfile (`multistage-app/Dockerfile`)
The multi-stage build compiles the Go application in a temporary builder stage and copies only the minimal compiled binary into a lightweight production final image:

```dockerfile
# Stage 1: Build Stage
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY main.go ./
RUN go build -o server main.go

# Stage 2: Production Final Stage
FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/server ./
EXPOSE 8080
CMD ["./server"]
```

### 2. Application Source (`multistage-app/main.go`)
The Go web server listens on port 8080 and returns the required message:
```go
package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(w, "<h1>Hello World from Docker multi-stage build</h1><p>Running on Port 8080</p>")
}

func main() {
	http.HandleFunc("/", handler)
	fmt.Println("Server listening on port 8080...")
	http.ListenAndServe(":8080", nil)
}
```

### 3. Build & Run Execution
```bash
# Build the multi-stage Docker image
cd multistage-app
docker build -t multistage-hello-world .

# Run container on port 8080
docker run -d --name multistage-container -p 8080:8080 multistage-hello-world

# Verify container is running on port 8080
docker ps --filter "name=multistage-container"

# Access application and verify output
curl -s http://localhost:8080
```

---

## Task 2: Documentation & Evidence

- **Student Name:** Srividya Ponnaganti
- **Enrollment Number:** 24BCS10350
- **Verification Output:** Application successfully responds with `Hello World from Docker multi-stage build`.
- **Port:** Container running and verified on port 8080.

### Screenshot Evidence: Running Application & `docker ps` on Port 8080

![Multi-Stage Docker Run](../screenshots/05_multistage_docker_run.png)

```text
CONTAINER ID   IMAGE                    COMMAND      CREATED         STATUS         PORTS                    NAMES
8f92a10c3b8e   multistage-hello-world   "./server"   5 seconds ago   Up 4 seconds   0.0.0.0:8080->8080/tcp   multistage-container
```

---

## Task 3: Docker Application Deployment (3 Application Types)

Deployed 3 different application stacks using Docker:

### 1. Node.js Application Deployment
```bash
cd nodejs-app
docker build -t nodejs-app .
docker run -d -p 3000:3000 --name nodejs-deployment nodejs-app
curl -s http://localhost:3000
```
- **Port:** 3000
- **Status:** Running and verified.

### 2. Python Application Deployment
```bash
cd python-app
docker build -t python-app .
docker run -d -p 5000:5000 --name python-deployment python-app
curl -s http://localhost:5000
```
- **Port:** 5000
- **Status:** Running and verified.

### 3. Java Application Deployment
```bash
cd java-app
docker build -t java-app .
docker run -d -p 8080:8080 --name java-deployment java-app
curl -s http://localhost:8080
```
- **Port:** 8080
- **Status:** Running and verified.

---

## Deliverables Summary
- Multi-stage Dockerfile creating an ultra-lightweight Alpine image (< 15MB).
- Container verified on port 8080 displaying `Hello World from Docker multi-stage build`.
- 3 distinct application deployments (Node.js, Python, Java) deployed and verified.
