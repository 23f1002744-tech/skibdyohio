from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 229.05,
    "uptime_pct": 98.531,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 130.17,
    "uptime_pct": 97.327,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 156.47,
    "uptime_pct": 98.806,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 120.66,
    "uptime_pct": 97.627,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 196.31,
    "uptime_pct": 98.807,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 130.82,
    "uptime_pct": 97.44,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 192.09,
    "uptime_pct": 97.852,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 159.69,
    "uptime_pct": 98.212,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 170.75,
    "uptime_pct": 98.066,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 160.06,
    "uptime_pct": 97.416,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 145.96,
    "uptime_pct": 97.741,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 198.57,
    "uptime_pct": 97.433,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 185.04,
    "uptime_pct": 98.912,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 215.22,
    "uptime_pct": 98.022,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 221.02,
    "uptime_pct": 99.166,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 233.8,
    "uptime_pct": 98.865,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 182.94,
    "uptime_pct": 98.734,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 208.62,
    "uptime_pct": 97.104,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 230.46,
    "uptime_pct": 97.122,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 189.34,
    "uptime_pct": 99.42,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 177.49,
    "uptime_pct": 97.736,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 157.66,
    "uptime_pct": 98.954,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 179.3,
    "uptime_pct": 99.264,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 160.27,
    "uptime_pct": 97.612,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 136.87,
    "uptime_pct": 98.978,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 189.06,
    "uptime_pct": 99.087,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 213.81,
    "uptime_pct": 99.471,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 129.98,
    "uptime_pct": 99.479,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 104.76,
    "uptime_pct": 98.939,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 157.54,
    "uptime_pct": 97.288,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 127.8,
    "uptime_pct": 97.687,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 189.79,
    "uptime_pct": 97.65,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 197.67,
    "uptime_pct": 97.785,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 158.81,
    "uptime_pct": 98.074,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 128.34,
    "uptime_pct": 97.51,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 137.69,
    "uptime_pct": 98.568,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
