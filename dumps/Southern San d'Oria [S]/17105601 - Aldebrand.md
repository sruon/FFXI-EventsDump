# 17105601 - Aldebrand

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 268 bytes                        |
| Total Events     | 13                               |
| References Count | 13                               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [172](#event-172)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     26 |              8 |
| [65535.2](#event-655352)   | 0x001C       |     13 |              3 |
| [65535.3](#event-655353)   | 0x0029       |     16 |              4 |
| [65535.4](#event-655354)   | 0x0039       |     24 |              6 |
| [65535.5](#event-655355)   | 0x0051       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0052       |     18 |              4 |
| [65535.7](#event-655357)   | 0x0064       |     10 |              2 |
| [65535.8](#event-655358)   | 0x006E       |      9 |              3 |
| [65535.9](#event-655359)   | 0x0077       |      9 |              3 |
| [65535.10](#event-6553510) | 0x0080       |     10 |              2 |
| [65535.11](#event-6553511) | 0x008A       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFFCDDE  |  4294954462 |
|       2 | 0xFFFF9A70  |  4294941296 |
|       3 | 0x07CF      |        1999 |
|       4 | 0x0015      |          21 |
|       5 | 0x0002      |           2 |
|       6 | 0x00A0      |         160 |
|       7 | 0x0028      |          40 |
|       8 | 0xFFFFE111  |  4294959377 |
|       9 | 0xFFFFC8C2  |  4294953154 |
|      10 | 0x0000      |           0 |
|      11 | 0x0001      |           1 |
|      12 | 0x0080      |         128 |

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

### Event 172

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 1E 83 02 05 01 6F 76 F8  FF FF 7F 00              .....ov.....    
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.834*, Z=-26.000*, Y=1.999*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x1E] EventEntity looks at Lilisette (ID: 17105539/0x01050283) and starts talking
  5: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0016 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      6E F8 FF FF              n...
0020: 7F 04 80 99 F8 FF FF 7F  00                       .........       
```

#### Opcodes

```
  0: 0x001C [0x6E] EventEntity uses emote 21*
  1: 0x0023 [0x99] Wait for EventEntity animation to complete
  2: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             6E F8 FF FF 7F 05 80           n......
0030: 99 F8 FF FF 7F 1C 06 80  00                       .........       
```

#### Opcodes

```
  0: 0x0029 [0x6E] EventEntity uses emote 2*
  1: 0x0030 [0x99] Wait for EventEntity animation to complete
  2: 0x0035 [0x1C] WAIT(160* ticks)
  3: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 07 80 1F 00 08 80           2......
0040: 09 80 03 80 1F 01 6F 6C  F8 FF FF 7F 0A 80 0B 80  ......ol........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.919*, Z=-14.142*, Y=1.999*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0047 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  5: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    00                                              .              
```

#### Opcodes

```
  0: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 0A    "./.....l.....
0060: 80 0B 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0052 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0054 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x005A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             6C F8 FF FF  7F 0C 80 0B 80 00            l.........  
```

#### Opcodes

```
  0: 0x0064 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x006D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            22 00                ".
0070: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x006E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0070 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0077  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0077 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0079 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 6C F8 FF FF 7F 0A 80 0B  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0080 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                6C F8 FF FF 7F 0C            l.....
0090: 80 0B 80 00                                       ....            
```

#### Opcodes

```
  0: 0x008A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0093 [0x00] END_REQSTACK()
```
