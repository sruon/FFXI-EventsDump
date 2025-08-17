# 17167261 - Karaha-Baruha

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 372 bytes                      |
| Total Events     | 16                             |
| References Count | 25                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [105](#event-105)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     18 |              6 |
| [65535.2](#event-655352)   | 0x0014       |     11 |              3 |
| [65535.3](#event-655353)   | 0x001F       |     14 |              4 |
| [65535.4](#event-655354)   | 0x002D       |      3 |              2 |
| [107](#event-107)          | 0x0030       |      1 |              1 |
| [112](#event-112)          | 0x0031       |      1 |              1 |
| [65535.5](#event-655355)   | 0x0032       |     73 |             16 |
| [65535.6](#event-655356)   | 0x007B       |      1 |              1 |
| [65535.7](#event-655357)   | 0x007C       |     18 |              4 |
| [65535.8](#event-655358)   | 0x008E       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0098       |      9 |              3 |
| [65535.10](#event-6553510) | 0x00A1       |      9 |              3 |
| [65535.11](#event-6553511) | 0x00AA       |     10 |              2 |
| [65535.12](#event-6553512) | 0x00B4       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000C      |          12 |
|       1 | 0x2140      |        8512 |
|       2 | 0x0C14      |        3092 |
|       3 | 0xFFFF9C64  |  4294941796 |
|       4 | 0x000A      |          10 |
|       5 | 0x16E2      |        5858 |
|       6 | 0x1AEA      |        6890 |
|       7 | 0x1334      |        4916 |
|       8 | 0x1E4C      |        7756 |
|       9 | 0x000B      |          11 |
|      10 | 0x4FE4F     |      327247 |
|      11 | 0xFFFF88A3  |  4294936739 |
|      12 | 0xFFFFBBA4  |  4294949796 |
|      13 | 0x50011     |      327697 |
|      14 | 0xFFFF8C1C  |  4294937628 |
|      15 | 0x5022A     |      328234 |
|      16 | 0xFFFF8DEB  |  4294938091 |
|      17 | 0x50683     |      329347 |
|      18 | 0xFFFF8F80  |  4294938496 |
|      19 | 0x001E      |          30 |
|      20 | 0x0032      |          50 |
|      21 | 0x0C00      |        3072 |
|      22 | 0x0000      |           0 |
|      23 | 0x0001      |           1 |
|      24 | 0x0080      |         128 |

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

### Event 105

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
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 1C 04 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=8.512*, Z=3.092*, Y=-25.500*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x1C] WAIT(10* ticks)
  5: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             1F 00 05 80  06 80 03 80 1F 01 00         ........... 
```

#### Opcodes

```
  0: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=5.858*, Z=6.890*, Y=-25.500*
  1: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 04 80 1F 00 07 80 08 80  03 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=4.916*, Z=7.756*, Y=-25.500*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         A4 01 00               ...
```

#### Opcodes

```
  0: 0x002D [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x002F [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0031  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    00                                              .              
```

#### Opcodes

```
  0: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 73 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       32 09 80 5A 00 0A  80 0B 80 0C 80 5A 01 5A    2..Z.......Z.Z
0040: 00 0D 80 0E 80 0C 80 5A  01 5A 00 0F 80 10 80 0C  .......Z.Z......
0050: 80 5A 01 5A 00 11 80 12  80 0C 80 5A 01 5E 69 64  .Z.Z.......Z.^id
0060: 6C 30 1C 13 80 59 01 F8  FF FF 7F 14 80 4B F8 FF  l0...Y.......K..
0070: FF 7F 15 80 6F 76 F8 FF  FF 7F 00                 ....ov.....     
```

#### Opcodes

```
  0: 0x0032 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0035 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=327.247*, Z=-30.557*, Y=-17.500*
  2: 0x003D [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x003F [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=327.697*, Z=-29.668*, Y=-17.500*
  4: 0x0047 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  5: 0x0049 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=328.234*, Z=-29.205*, Y=-17.500*
  6: 0x0051 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  7: 0x0053 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=329.347*, Z=-28.800*, Y=-17.500*
  8: 0x005B [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  9: 0x005D [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 10: 0x0062 [0x1C] WAIT(30* ticks)
 11: 0x0065 [0x59] UPDATE_ENTITY_DATA: Set EventEntity turn speed = 50*
 12: 0x006D [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=16.9°*)
 13: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 14: 0x0075 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
 15: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   00                         .    
```

#### Opcodes

```
  0: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      22 00 2F 00              "./.
0080: F8 FF FF 7F 6C F8 FF FF  7F 16 80 17 80 00        ....l.........  
```

#### Opcodes

```
  0: 0x007C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x007E [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0084 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            6C F8                l.
0090: FF FF 7F 18 80 17 80 00                           ........        
```

#### Opcodes

```
  0: 0x008E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0098  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          22 00 2F 00 F8 FF FF 7F          "./.....
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0098 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x009A [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00A0 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A1  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    22 01 2F 01 F8 FF FF  7F 00                     "./......      
```

#### Opcodes

```
  0: 0x00A1 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00A3 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                6C F8 FF FF 7F 16            l.....
00B0: 80 17 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00AA [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             6C F8 FF FF  7F 18 80 17 80 00            l.........  
```

#### Opcodes

```
  0: 0x00B4 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00BD [0x00] END_REQSTACK()
```
