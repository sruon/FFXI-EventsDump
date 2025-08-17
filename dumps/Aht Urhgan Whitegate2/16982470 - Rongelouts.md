# 16982470 - Rongelouts

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Aht Urhgan Whitegate2 (ID: 50) |
| Block Size       | 140 bytes                      |
| Total Events     | 10                             |
| References Count | 7                              |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [5080](#event-5080)       | 0x0001       |      1 |              1 |
| [5081](#event-5081)       | 0x0002       |      1 |              1 |
| [5083](#event-5083)       | 0x0003       |      1 |              1 |
| [5084](#event-5084)       | 0x0004       |      1 |              1 |
| [5085](#event-5085)       | 0x0005       |      1 |              1 |
| [5086](#event-5086)       | 0x0006       |      1 |              1 |
| [65535.1](#event-65535-1) | 0x0007       |     10 |              2 |
| [65535.2](#event-65535-2) | 0x0011       |     10 |              2 |
| [65535.3](#event-65535-3) | 0x001B       |     26 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x003C      |          60 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFF759F0  |  4294400496 |
|       5 | 0xA1F7      |       41463 |
|       6 | 0x07CF      |        1999 |

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

### Event 5080

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

### Event 5081

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

### Event 5083

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 5084

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 5085

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                00                                      .          
```

#### Opcodes

```
  0: 0x0005 [0x00] END_REQSTACK()
```

### Event 5086

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   00                                    .         
```

#### Opcodes

```
  0: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      6C  F8 FF FF 7F 00 80 01 80         l........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0007 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=60*)
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    6C F8 FF FF 7F 02 80  01 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0011 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=60*)
  1: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   32 03 80 1F 00             2....
0020: 04 80 05 80 06 80 1F 01  6F 4A C6 21 03 01 C8 21  ........oJ.!...!
0030: 03 01 6F 70 00                                    ..op.           
```

#### Opcodes

```
  0: 0x001B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=-566.800*, Z=41.463*, Y=1.999*
  2: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0029 [0x4A] Rongelouts (ID: 16982470/0x010321C6) looks at Koja Salaheem (ID: 16982472/0x010321C8)
  5: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0033 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0034 [0x00] END_REQSTACK()
```
