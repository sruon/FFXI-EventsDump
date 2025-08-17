# 17175372 - Shikaree G

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Meriphataud Mountains [S] (ID: 97) |
| Block Size       | 364 bytes                          |
| Total Events     | 13                                 |
| References Count | 30                                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [4](#event-4)              | 0x0001       |      1 |              1 |
| [5](#event-5)              | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0004       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0016       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0020       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0029       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0032       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003C       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0046       |     14 |              4 |
| [65535.9](#event-655359)   | 0x0054       |     18 |              6 |
| [65535.10](#event-6553510) | 0x0066       |     74 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000A      |          10 |
|       4 | 0x68842     |      428098 |
|       5 | 0x2443C     |      148540 |
|       6 | 0xFFFFAC9E  |  4294945950 |
|       7 | 0x68E36     |      429622 |
|       8 | 0x25170     |      151920 |
|       9 | 0xFFFFAA2F  |  4294945327 |
|      10 | 0x001E      |          30 |
|      11 | 0x000D      |          13 |
|      12 | 0x6E9C6     |      453062 |
|      13 | 0x2C9AB     |      182699 |
|      14 | 0xFFFFA0BB  |  4294942907 |
|      15 | 0x6ED8C     |      454028 |
|      16 | 0x2CE95     |      183957 |
|      17 | 0xFFFFA07E  |  4294942846 |
|      18 | 0x6F14E     |      454990 |
|      19 | 0x2D380     |      185216 |
|      20 | 0xFFFFA096  |  4294942870 |
|      21 | 0x702E5     |      459493 |
|      22 | 0x2EA7E     |      191102 |
|      23 | 0xFFFFA45E  |  4294943838 |
|      24 | 0x71098     |      463000 |
|      25 | 0x2FC9B     |      195739 |
|      26 | 0xFFFFA3F1  |  4294943729 |
|      27 | 0x71C68     |      466024 |
|      28 | 0x30BF6     |      199670 |
|      29 | 0xFFFFA464  |  4294943844 |

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

### Event 4

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

### Event 5

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             22 00 2F 00  F8 FF FF 7F 6C F8 FF FF      "./.....l...
0010: 7F 00 80 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0004 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0006 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   6C F8  FF FF 7F 02 80 01 80 00        l.........
```

#### Opcodes

```
  0: 0x0016 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0020  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 22 00 2F 00 F8 FF FF 7F  00                       "./......       
```

#### Opcodes

```
  0: 0x0020 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0022 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             22 01 2F 01 F8 FF FF           "./....
0030: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0029 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x002B [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       6C F8 FF FF 7F 00  80 01 80 00                l.........    
```

#### Opcodes

```
  0: 0x0032 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      6C F8 FF FF              l...
0040: 7F 02 80 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x003C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   32 03  80 1F 00 04 80 05 80 06        2.........
0050: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=428.098*, Z=148.540*, Y=-21.346*
  2: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             32 03 80 1F  00 07 80 08 80 09 80 1F      2...........
0060: 01 6F 1C 0A 80 00                                 .o....          
```

#### Opcodes

```
  0: 0x0054 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=429.622*, Z=151.920*, Y=-21.969*
  2: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0062 [0x1C] WAIT(30* ticks)
  5: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 74 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   32 0B  80 1F 00 0C 80 0D 80 0E        2.........
0070: 80 1F 01 1F 00 0F 80 10  80 11 80 1F 01 1F 00 12  ................
0080: 80 13 80 14 80 1F 01 1F  00 12 80 13 80 14 80 1F  ................
0090: 01 1F 00 15 80 16 80 17  80 1F 01 1F 00 18 80 19  ................
00A0: 80 1A 80 1F 01 1F 00 1B  80 1C 80 1D 80 1F 01 00  ................
```

#### Opcodes

```
  0: 0x0066 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0069 [0x1F] MOVE_ENTITY: EventEntity moves to X=453.062*, Z=182.699*, Y=-24.389*
  2: 0x0071 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0073 [0x1F] MOVE_ENTITY: EventEntity moves to X=454.028*, Z=183.957*, Y=-24.450*
  4: 0x007B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x007D [0x1F] MOVE_ENTITY: EventEntity moves to X=454.990*, Z=185.216*, Y=-24.426*
  6: 0x0085 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0087 [0x1F] MOVE_ENTITY: EventEntity moves to X=454.990*, Z=185.216*, Y=-24.426*
  8: 0x008F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0091 [0x1F] MOVE_ENTITY: EventEntity moves to X=459.493*, Z=191.102*, Y=-23.458*
 10: 0x0099 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x009B [0x1F] MOVE_ENTITY: EventEntity moves to X=463.000*, Z=195.739*, Y=-23.567*
 12: 0x00A3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 13: 0x00A5 [0x1F] MOVE_ENTITY: EventEntity moves to X=466.024*, Z=199.670*, Y=-23.452*
 14: 0x00AD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 15: 0x00AF [0x00] END_REQSTACK()
```
