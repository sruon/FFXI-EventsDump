# 17105444 - Phillieulais

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 264 bytes                        |
| Total Events     | 13                               |
| References Count | 8                                |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     35 |              9 |
| [65535.2](#event-655352)   | 0x0024       |     35 |              9 |
| [113](#event-113)          | 0x0047       |      1 |              1 |
| [114](#event-114)          | 0x0048       |      1 |              1 |
| [65535.3](#event-655353)   | 0x0049       |     21 |              5 |
| [65535.4](#event-655354)   | 0x005E       |      1 |              1 |
| [65535.5](#event-655355)   | 0x005F       |     18 |              4 |
| [65535.6](#event-655356)   | 0x0071       |     10 |              2 |
| [65535.7](#event-655357)   | 0x007B       |      9 |              3 |
| [65535.8](#event-655358)   | 0x0084       |      9 |              3 |
| [65535.9](#event-655359)   | 0x008D       |     10 |              2 |
| [65535.10](#event-6553510) | 0x0097       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x000D      |          13 |
|       2 | 0xFFFFFBCD  |  4294966221 |
|       3 | 0xFFFEAD17  |  4294880535 |
|       4 | 0x07CF      |        1999 |
|       5 | 0x0000      |           0 |
|       6 | 0x0001      |           1 |
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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 25 10 03 02  00 27 10 03 01 00 26 10   ...%....'....&.
0010: 03 03 00 28 10 32 00 80  1F 00 00 00 02 00 01 00  ...(.2..........
0020: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x000B [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0010 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0015 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             03 00 00 25  10 03 02 00 27 10 03 01      ...%....'...
0030: 00 26 10 03 03 00 28 10  32 01 80 1F 00 00 00 02  .&....(.2.......
0040: 00 01 00 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0024 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0029 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x002E [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0033 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0038 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0045 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0046 [0x00] END_REQSTACK()
```

### Event 113

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      00                                  .        
```

#### Opcodes

```
  0: 0x0047 [0x00] END_REQSTACK()
```

### Event 114

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          00                               .       
```

#### Opcodes

```
  0: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             1F 00 02 80 03 80 04           .......
0050: 80 1F 01 6F 4A 24 02 05  01 EB 02 05 01 00        ...oJ$........  
```

#### Opcodes

```
  0: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.075*, Z=-86.761*, Y=1.999*
  1: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0054 [0x4A] Phillieulais (ID: 17105444/0x01050224) looks at Gissenne (ID: 17105643/0x010502EB)
  4: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            00                   . 
```

#### Opcodes

```
  0: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               22                 "
0060: 00 2F 00 F8 FF FF 7F 6C  F8 FF FF 7F 05 80 06 80  ./.....l........
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x005F [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0061 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0067 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    6C F8 FF FF 7F 07 80  06 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0071 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   22 00 2F 00 F8             "./..
0080: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x007B [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x007D [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0084  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             22 01 2F 01  F8 FF FF 7F 00               "./......   
```

#### Opcodes

```
  0: 0x0084 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0086 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         6C F8 FF               l..
0090: FF 7F 05 80 06 80 00                              .......         
```

#### Opcodes

```
  0: 0x008D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      6C  F8 FF FF 7F 07 80 06 80         l........
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0097 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00A0 [0x00] END_REQSTACK()
```
