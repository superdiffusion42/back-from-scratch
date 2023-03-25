# Back from scratch

## Setup from scratch

### 1. Create a virtual env
```
virtualenv back_env
source back_env/bin/activate
```

### 2. Install dependencies 
```
pip install sanic
```

### 3. Start server
```
sanic server.server
```

### 4. Check route
```
curl http://127.0.0.1:8000/health
```
