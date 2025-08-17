# 17363390 - Incensed Pineapple

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Palborough Mines (ID: 143) |
| Block Size       | 88 bytes                   |
| Total Events     | 5                          |
| References Count | 5                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [127](#event-127)        | 0x0001       |      1 |              1 |
| [128](#event-128)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     18 |              6 |
| [65535.2](#event-655352) | 0x0015       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x4ECA      |       20170 |
|       1 | 0x13CC2     |       81090 |
|       2 | 0xFFFF83D2  |  4294935506 |
|       3 | 0x0000      |           0 |
|       4 | 0x00B4      |         180 |

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

### Event 127

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 128

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          1F 00 00 80 01  80 02 80 1F 01 1E F0 FF     .............
0010: FF 7F 6F 70 00                                    ..op.           
```

#### Opcodes

```
  0: 0x0003 [0x1F] MOVE_ENTITY: EventEntity moves to X=20.170*, Z=81.090*, Y=-31.790*
  1: 0x000B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0012 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0013 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                6C BC F1  08 01 03 80 04 80 00          l......... 
```

#### Opcodes

```
  0: 0x0015 [0x6C] FADE_ENTITY_COLOR(entity_id=Sirius (ID: 17363388/0x0108F1BC), end_alpha=0*, fade_time=180*)
  1: 0x001E [0x00] END_REQSTACK()
```
