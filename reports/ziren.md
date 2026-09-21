# 📊 Ziren (v2.0)

How to read this report:
- Table rows correspond to security regimes
- Table columns correspond to proof system components
- Cells show bits of security per component
- Proof size estimates are indicative (1 KiB = 1024 bytes)

## zkVM Overview

| Metric | Value | Relevant circuit | Notes |
| --- | --- | --- | --- |
| Final bits of security | **94 bits** | [core](#core) | Regime: UDR |
| Final proof size (worst case) | **963 KiB** | [wrap](#wrap) | |

## Circuits

- [core](#core)
- [compress](#compress)
- [wrap](#wrap)

## core

**Parameters:**
- Proof system: Jagged over WHIR
- Trace length: 4194304
- Trace width: 35330
- Hash size (bits): 248
- Field: KoalaBear⁴
- Iterations (M): 3
- Folding factors (k_i): [3, 6, 6]
- Constraint degree: 3
- Batch size: 256
- Batching: Powers
- Queries per iteration: [124, 88, 85]
- OOD samples per iteration: [2, 2]
- Total grinding overhead log2: 17.59
- Lookup (logup): logup-gkr

**Proof Size:** 1225 KiB (expected) / 1292 KiB (worst case)

| regime | total | logup-gkr | OOD(i=1) | OOD(i=2) | Shift(i=1) | Shift(i=2) | batching | fin | fold(i=0,s=1) | fold(i=0,s=2) | fold(i=0,s=3) | fold(i=1,s=1) | fold(i=1,s=2) | fold(i=1,s=3) | fold(i=1,s=4) | fold(i=1,s=5) | fold(i=1,s=6) | fold(i=2,s=1) | fold(i=2,s=2) | fold(i=2,s=3) | fold(i=2,s=4) | fold(i=2,s=5) | fold(i=2,s=6) | reduce to dense PCS | zerocheck |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UDR | 94 | 100 | 213 | 225 | 100 | 100 | 94 | 100 | 103 | 104 | 105 | 103 | 104 | 105 | 106 | 107 | 108 | 105 | 106 | 107 | 108 | 109 | 110 | 116 | 109 |


## compress

**Parameters:**
- Proof system: Jagged over WHIR
- Trace length: 1048576
- Trace width: 406
- Hash size (bits): 248
- Field: KoalaBear⁴
- Iterations (M): 3
- Folding factors (k_i): [3, 6, 6]
- Constraint degree: 3
- Batch size: 64
- Batching: Powers
- Queries per iteration: [124, 88, 85]
- OOD samples per iteration: [2, 2]
- Total grinding overhead log2: 17.59
- Lookup (logup): logup-gkr

**Proof Size:** 504 KiB (expected) / 570 KiB (worst case)

| regime | total | logup-gkr | OOD(i=1) | OOD(i=2) | Shift(i=1) | Shift(i=2) | batching | fin | fold(i=0,s=1) | fold(i=0,s=2) | fold(i=0,s=3) | fold(i=1,s=1) | fold(i=1,s=2) | fold(i=1,s=3) | fold(i=1,s=4) | fold(i=1,s=5) | fold(i=1,s=6) | fold(i=2,s=1) | fold(i=2,s=2) | fold(i=2,s=3) | fold(i=2,s=4) | fold(i=2,s=5) | fold(i=2,s=6) | reduce to dense PCS | zerocheck |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UDR | 96 | 112 | 213 | 225 | 100 | 100 | 96 | 100 | 103 | 104 | 105 | 103 | 104 | 105 | 106 | 107 | 108 | 105 | 106 | 107 | 108 | 109 | 110 | 116 | 114 |


## wrap

**Parameters:**
- Proof system: Jagged
- PCS: FRI
- Hash size (bits): 254
- Number of queries: 94
- Grinding query phase (bits): 22
- Field: KoalaBear⁴
- Rate (ρ): 0.125
- Dense trace length: $2^{21}$
- Trace length: 1048576
- Trace width: 254
- FRI rounds: 21
- FRI folding factors: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
- FRI early stop degree: 8
- Dense batch size: 24
- Batching: Affine
- Lookup (logup): logup-gkr

**Proof Size:** 534 KiB (expected) / 963 KiB (worst case)

| regime | total | logup-gkr | batching | commit round 1 | commit round 10 | commit round 11 | commit round 12 | commit round 13 | commit round 14 | commit round 15 | commit round 16 | commit round 17 | commit round 18 | commit round 19 | commit round 2 | commit round 20 | commit round 21 | commit round 3 | commit round 4 | commit round 5 | commit round 6 | commit round 7 | commit round 8 | commit round 9 | query phase | reduce to dense PCS | zerocheck |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UDR | 100 | 112 | 114 | 102 | 111 | 112 | 113 | 114 | 115 | 116 | 117 | 118 | 119 | 120 | 103 | 120 | 121 | 104 | 105 | 106 | 107 | 108 | 109 | 110 | 100 | 116 | 115 |

