# 17105431 - Phillieulais S Dieuffon

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 332 bytes                        |
| Total Events     | 16                               |
| References Count | 12                               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [55](#event-55)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     27 |              9 |
| [65535.2](#event-655352)   | 0x001D       |     20 |              6 |
| [65535.3](#event-655353)   | 0x0031       |     14 |              4 |
| [60](#event-60)            | 0x003F       |      1 |              1 |
| [65535.4](#event-655354)   | 0x0040       |     35 |              9 |
| [65535.5](#event-655355)   | 0x0063       |     35 |              9 |
| [631](#event-631)          | 0x0086       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0087       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0088       |     18 |              4 |
| [65535.8](#event-655358)   | 0x009A       |     10 |              2 |
| [65535.9](#event-655359)   | 0x00A4       |      9 |              3 |
| [65535.10](#event-6553510) | 0x00AD       |      9 |              3 |
| [65535.11](#event-6553511) | 0x00B6       |     10 |              2 |
| [65535.12](#event-6553512) | 0x00C0       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x0524      |        1316 |
|       2 | 0xA6D4      |       42708 |
|       3 | 0xFFFFF830  |  4294965296 |
|       4 | 0x0466      |        1126 |
|       5 | 0xAB7D      |       43901 |
|       6 | 0x05DC      |        1500 |
|       7 | 0x4E7D      |       20093 |
|       8 | 0x0000      |           0 |
|       9 | 0x0028      |          40 |
|      10 | 0x0001      |           1 |
|      11 | 0x0080      |         128 |

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

### Event 55

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
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 1E EF 01 05 01 7B 0E 02  05 01 6F 70 00           .....{....op.   
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.316*, Z=42.708*, Y=-2.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x1E] EventEntity looks at Raustigne (ID: 17105391/0x010501EF) and starts talking
  5: 0x0015 [0x7B] Altennia (ID: 17105422/0x0105020E) stops talking
  6: 0x001A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x001B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         32 00 80               2..
0020: 1F 00 04 80 05 80 03 80  1F 01 6F 1E 18 02 05 01  ..........o.....
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x001D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0020 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.126*, Z=43.901*, Y=-2.000*
  2: 0x0028 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002B [0x1E] EventEntity looks at Halver M Borel (ID: 17105432/0x01050218) and starts talking
  5: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    32 00 80 1F 00 06 80  07 80 08 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0031 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0034 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.500*, Z=20.093*, Y=0.000*
  2: 0x003C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003E [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               00                 .
```

#### Opcodes

```
  0: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 03 00 00 25 10 03 02 00  27 10 03 01 00 26 10 03  ...%....'....&..
0050: 03 00 28 10 32 09 80 1F  00 00 00 02 00 01 00 1F  ..(.2...........
0060: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0040 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0045 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x004A [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x004F [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0054 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          03 00 00 25 10  03 02 00 27 10 03 01 00     ...%....'....
0070: 26 10 03 03 00 28 10 32  00 80 1F 00 00 00 02 00  &....(.2........
0080: 01 00 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0063 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0068 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x006D [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0072 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0077 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0084 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0085 [0x00] END_REQSTACK()
```

### Event 631

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0086  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   00                                    .         
```

#### Opcodes

```
  0: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0087  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      00                                  .        
```

#### Opcodes

```
  0: 0x0087 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          22 00 2F 00 F8 FF FF 7F          "./.....
0090: 6C F8 FF FF 7F 08 80 0A  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0088 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x008A [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0090 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                6C F8 FF FF 7F 0B            l.....
00A0: 80 0A 80 00                                       ....            
```

#### Opcodes

```
  0: 0x009A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A4  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             22 00 2F 00  F8 FF FF 7F 00               "./......   
```

#### Opcodes

```
  0: 0x00A4 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00A6 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AD  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         22 01 2F               "./
00B0: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x00AD [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00AF [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x00B5 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B6   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   6C F8  FF FF 7F 08 80 0A 80 00        l.........
```

#### Opcodes

```
  0: 0x00B6 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x00BF [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C0   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 6C F8 FF FF 7F 0B 80 0A  80 00                    l.........      
```

#### Opcodes

```
  0: 0x00C0 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00C9 [0x00] END_REQSTACK()
```
