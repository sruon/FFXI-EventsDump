# 17138598 - Lilisette

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | North Gustaberg [S] (ID: 88) |
| Block Size       | 288 bytes                    |
| Total Events     | 15                           |
| References Count | 16                           |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [14](#event-14)            | 0x0001       |      1 |              1 |
| [15](#event-15)            | 0x0002       |      1 |              1 |
| [16](#event-16)            | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |     10 |              2 |
| [65535.2](#event-655352)   | 0x000E       |     10 |              2 |
| [65535.3](#event-655353)   | 0x0018       |     34 |              8 |
| [65535.4](#event-655354)   | 0x003A       |     20 |              6 |
| [65535.5](#event-655355)   | 0x004E       |      1 |              1 |
| [65535.6](#event-655356)   | 0x004F       |     18 |              4 |
| [65535.7](#event-655357)   | 0x0061       |     10 |              2 |
| [65535.8](#event-655358)   | 0x006B       |      9 |              3 |
| [65535.9](#event-655359)   | 0x0074       |      9 |              3 |
| [65535.10](#event-6553510) | 0x007D       |     10 |              2 |
| [65535.11](#event-6553511) | 0x0087       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0028      |          40 |
|       4 | 0xFFF9A2B1  |  4294550193 |
|       5 | 0xFFFE5B7A  |  4294859642 |
|       6 | 0xA179      |       41337 |
|       7 | 0xFFF98117  |  4294541591 |
|       8 | 0xFFFE632A  |  4294861610 |
|       9 | 0xA062      |       41058 |
|      10 | 0xFFF971A4  |  4294537636 |
|      11 | 0xFFFE70CF  |  4294865103 |
|      12 | 0x9C92      |       40082 |
|      13 | 0xFFF821E6  |  4294451686 |
|      14 | 0x8CB40     |      576320 |
|      15 | 0x9999      |       39321 |

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

### Event 14

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

### Event 15

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

### Event 16

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             6C F8 FF FF  7F 00 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0004 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            6C F8                l.
0010: FF FF 7F 02 80 01 80 00                           ........        
```

#### Opcodes

```
  0: 0x000E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          32 03 80 1F 00 04 80 05          2.......
0020: 80 06 80 1F 01 1F 00 07  80 08 80 09 80 1F 01 1F  ................
0030: 00 0A 80 0B 80 0C 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0018 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=-417.103*, Z=-107.654*, Y=41.337*
  2: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=-425.705*, Z=-105.686*, Y=41.058*
  4: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=-429.660*, Z=-102.193*, Y=40.082*
  6: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                32 03 80 1F 00 0D            2.....
0040: 80 0E 80 0F 80 1F 01 6F  1E 28 83 05 01 00        .......o.(....  
```

#### Opcodes

```
  0: 0x003A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=-515.610*, Z=576.320*, Y=39.321*
  2: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0048 [0x1E] EventEntity looks at Unnamed NPC (ID: 17138472/0x01058328) and starts talking
  5: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            00                   . 
```

#### Opcodes

```
  0: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               22                 "
0050: 00 2F 00 F8 FF FF 7F 6C  F8 FF FF 7F 00 80 01 80  ./.....l........
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x004F [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0051 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0057 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    6C F8 FF FF 7F 02 80  01 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0061 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   22 00 2F 00 F8             "./..
0070: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x006B [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x006D [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0074  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             22 01 2F 01  F8 FF FF 7F 00               "./......   
```

#### Opcodes

```
  0: 0x0074 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0076 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         6C F8 FF               l..
0080: FF 7F 00 80 01 80 00                              .......         
```

#### Opcodes

```
  0: 0x007D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      6C  F8 FF FF 7F 02 80 01 80         l........
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0087 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0090 [0x00] END_REQSTACK()
```
