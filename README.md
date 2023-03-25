# Back from scratch

## Setup from scratch

### 1. Create a virtual env
```
virtualenv back_env
source back_env/bin/activate
```

### 2. Install dependencies 
```
pip install -r requirements.txt
```

#### 2.1 Setup environment variables
- Copy / Rename '.env.sample' to '.env'
- Set up the required values if missing

### 3. Start server
```
sanic server.api
```

### 4. Check health route
In another terminal
```
curl http://127.0.0.1:8000/health
```

### 5. Call /generate route with payload
```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"prompt": "a bucket in a field of grass"}' \
  http://127.0.0.1:8000/generate
```

