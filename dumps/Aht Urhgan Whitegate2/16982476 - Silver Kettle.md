# 16982476 - Silver Kettle

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Aht Urhgan Whitegate2 (ID: 50) |
| Block Size       | 148 bytes                      |
| Total Events     | 11                             |
| References Count | 8                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [5080](#event-5080)      | 0x0001       |      1 |              1 |
| [5081](#event-5081)      | 0x0002       |      1 |              1 |
| [5082](#event-5082)      | 0x0003       |      1 |              1 |
| [5083](#event-5083)      | 0x0004       |      1 |              1 |
| [5084](#event-5084)      | 0x0005       |      1 |              1 |
| [65535.1](#event-655351) | 0x0006       |     28 |              8 |
| [65535.2](#event-655352) | 0x0022       |     10 |              2 |
| [65535.3](#event-655353) | 0x002C       |     10 |              2 |
| [5085](#event-5085)      | 0x0036       |      1 |              1 |
| [5086](#event-5086)      | 0x0037       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFF758A2  |  4294400162 |
|       2 | 0x9EB4      |       40628 |
|       3 | 0x07CF      |        1999 |
|       4 | 0x07D0      |        2000 |
|       5 | 0x0000      |           0 |
|       6 | 0x003C      |          60 |
|       7 | 0x0080      |         128 |

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

### Event 5082

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

### Event 5083

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

### Event 5084

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   32 00  80 1F 00 01 80 02 80 03        2.........
0010: 80 1F 01 6F 4B CC 21 03  01 04 80 6F 76 CC 21 03  ...oK.!....ov.!.
0020: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0006 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0009 [0x1F] MOVE_ENTITY: EventEntity moves to X=-567.134*, Z=40.628*, Y=1.999*
  2: 0x0011 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0013 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0014 [0x4B] UPDATE_ENTITY_YAW(entity=Silver Kettle (ID: 16982476/0x010321CC), yaw=11.0°*)
  5: 0x001B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x001C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Silver Kettle (ID: 16982476/0x010321CC) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       6C F8 FF FF 7F 05  80 06 80 00                l.........    
```

#### Opcodes

```
  0: 0x0022 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=60*)
  1: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      6C F8 FF FF              l...
0030: 7F 07 80 06 80 00                                 ......          
```

#### Opcodes

```
  0: 0x002C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=60*)
  1: 0x0035 [0x00] END_REQSTACK()
```

### Event 5085

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0036  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   00                                    .         
```

#### Opcodes

```
  0: 0x0036 [0x00] END_REQSTACK()
```

### Event 5086

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0037  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      00                                  .        
```

#### Opcodes

```
  0: 0x0037 [0x00] END_REQSTACK()
```
