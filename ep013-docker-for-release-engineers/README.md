# EP013 — Docker for Release Engineers

From Deploy or Die Episode 13: "Docker in 15 Minutes: The Only Guide a Release Engineer Needs"

## Files

| File | What it shows |
|------|---------------|
| `Dockerfile.simple` | Basic single-stage Dockerfile (Python) |
| `Dockerfile.multistage` | Multi-stage build (Node.js) — 10x smaller images |
| `docker-compose.yml` | App + Postgres + Redis local dev stack |
| `.dockerignore` | Keep your images lean |

## Quick Reference

### Build and run
```bash
docker build -t myapp:1.0.0 .
docker run -p 3000:3000 myapp:1.0.0
```

### Local dev with Compose
```bash
docker compose up        # start everything
docker compose down      # stop and remove containers
docker compose logs -f   # follow logs
```

### Registry workflow
```bash
docker tag myapp:1.0.0 ghcr.io/yourname/myapp:1.0.0
docker push ghcr.io/yourname/myapp:1.0.0
docker pull ghcr.io/yourname/myapp:1.0.0
```

### Debug a failing container
```bash
docker run -it myapp:1.0.0 bash   # interactive shell
docker logs <container_id>         # view logs
docker inspect <container_id>      # full config
```

## The 3 Failures (and fixes)

**Container exits immediately** → CMD is wrong. Run `docker run -it myapp bash` to debug.

**Can't connect to database** → Use service name as hostname (`postgres`), not `localhost`.

**Image is enormous** → Add `.dockerignore`. Include `node_modules`, `.git`, `.env`.

## Links
- Newsletter: https://deployordie.io
- EP004 (GitHub Actions): https://github.com/mttaylor/deployordiecontent/tree/main/ep004-github-actions-release
