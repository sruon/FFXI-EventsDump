# 17248929 - Gomada-Vulmada

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 340 bytes                   |
| Total Events     | 9                           |
| References Count | 28                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [919](#event-919)        | 0x0001       |      7 |              2 |
| [920](#event-920)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     24 |              8 |
| [65535.2](#event-655352) | 0x0027       |     24 |              8 |
| [65535.3](#event-655353) | 0x003F       |     26 |              8 |
| [65535.4](#event-655354) | 0x0059       |     14 |              4 |
| [65535.5](#event-655355) | 0x0067       |     39 |              9 |
| [65535.6](#event-655356) | 0x008E       |     34 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0015      |          21 |
|       1 | 0x3FD0E     |      261390 |
|       2 | 0x0442      |        1090 |
|       3 | 0xFFFFEBD4  |  4294962132 |
|       4 | 0x000A      |          10 |
|       5 | 0x3E30D     |      254733 |
|       6 | 0x0A46      |        2630 |
|       7 | 0xFFFFED10  |  4294962448 |
|       8 | 0x3AAB2     |      240306 |
|       9 | 0x25F7      |        9719 |
|      10 | 0xFFFFEF3E  |  4294963006 |
|      11 | 0x0D1B      |        3355 |
|      12 | 0x30D69     |      200041 |
|      13 | 0xFFFFEBDF  |  4294962143 |
|      14 | 0xFFFFF017  |  4294963223 |
|      15 | 0x39F95     |      237461 |
|      16 | 0x1C82      |        7298 |
|      17 | 0xFFFFEFF9  |  4294963193 |
|      18 | 0x0055      |          85 |
|      19 | 0x39BA8     |      236456 |
|      20 | 0x1DB4      |        7604 |
|      21 | 0xFFFFEFEF  |  4294963183 |
|      22 | 0x3944A     |      234570 |
|      23 | 0x1D89      |        7561 |
|      24 | 0xFFFFEF67  |  4294963047 |
|      25 | 0x34825     |      215077 |
|      26 | 0x1432      |        5170 |
|      27 | 0xFFFFED2C  |  4294962476 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 919

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 920

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 24 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               32                 2
0010: 00 80 1F 00 01 80 02 80  03 80 1F 01 1C 04 80 1E  ................
0020: F0 FF FF 7F 6F 70 00                              ....op.         
```

#### Opcodes

```
  0: 0x000F [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=261.390*, Z=1.090*, Y=-5.164*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x1C] WAIT(10* ticks)
  4: 0x001F [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0024 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0025 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 24 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  00 80 1F 00 05 80 06 80         2........
0030: 07 80 1F 01 1C 04 80 1E  A6 32 07 01 6F 70 00     .........2..op. 
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=254.733*, Z=2.630*, Y=-4.848*
  2: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0034 [0x1C] WAIT(10* ticks)
  4: 0x0037 [0x1E] EventEntity looks at Honoi-Gomoi (ID: 17248934/0x010732A6) and starts talking
  5: 0x003C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x003D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               32                 2
0040: 00 80 1F 00 08 80 09 80  0A 80 1F 01 1C 04 80 4B  ...............K
0050: F8 FF FF 7F 0B 80 6F 70  00                       ......op.       
```

#### Opcodes

```
  0: 0x003F [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x0042 [0x1F] MOVE_ENTITY: EventEntity moves to X=240.306*, Z=9.719*, Y=-4.290*
  2: 0x004A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004C [0x1C] WAIT(10* ticks)
  4: 0x004F [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=18.4°*)
  5: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0057 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             32 00 80 1F 00 0C 80           2......
0060: 0D 80 0E 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0059 [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=200.041*, Z=-5.153*, Y=-4.073*
  2: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 39 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      32  00 80 1F 00 0F 80 10 80         2........
0070: 11 80 1F 01 1C 04 80 1E  A8 32 07 01 6F 70 5B 12  .........2..op[.
0080: 80 F8 FF FF 7F F8 FF FF  7F 61 6E 67 30 00        .........ang0.  
```

#### Opcodes

```
  0: 0x0067 [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x006A [0x1F] MOVE_ENTITY: EventEntity moves to X=237.461*, Z=7.298*, Y=-4.103*
  2: 0x0072 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0074 [0x1C] WAIT(10* ticks)
  4: 0x0077 [0x1E] EventEntity looks at Chepelle (ID: 17248936/0x010732A8) and starts talking
  5: 0x007C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x007D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x007E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=85*
  8: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            32 00                2.
0090: 80 1F 00 13 80 14 80 15  80 1F 01 1F 00 16 80 17  ................
00A0: 80 18 80 1F 01 1F 00 19  80 1A 80 1B 80 1F 01 00  ................
```

#### Opcodes

```
  0: 0x008E [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x0091 [0x1F] MOVE_ENTITY: EventEntity moves to X=236.456*, Z=7.604*, Y=-4.113*
  2: 0x0099 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009B [0x1F] MOVE_ENTITY: EventEntity moves to X=234.570*, Z=7.561*, Y=-4.249*
  4: 0x00A3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00A5 [0x1F] MOVE_ENTITY: EventEntity moves to X=215.077*, Z=5.170*, Y=-4.820*
  6: 0x00AD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00AF [0x00] END_REQSTACK()
```
