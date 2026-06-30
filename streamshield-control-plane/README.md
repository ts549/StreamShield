# undox-control-plane

Local RTMP server (MediaMTX) for the undox pipeline.

## Run

```powershell
.\start.ps1
```

First run downloads `mediamtx.exe` (~15 MB) next to this README. Subsequent runs reuse it.

Listens on `rtmp://localhost:1935/` — accepts any path.

## Pipeline wiring

- OBS publishes to: `rtmp://localhost/live` with stream key `test`
- `undox-security-server/main.py` ingests:  `rtmp://localhost/live/test`
- `undox-security-server/main.py` republishes: `rtmp://localhost/live/blurred`
- Play blurred output (low latency): `ffplay rtmp://localhost/live/blurred`
- Play blurred output in browser (HLS, ~5–10 s extra latency): http://localhost:8888/live/blurred

Start order: this server → `python main.py` → OBS Start Streaming → open the blurred URL in a player.
