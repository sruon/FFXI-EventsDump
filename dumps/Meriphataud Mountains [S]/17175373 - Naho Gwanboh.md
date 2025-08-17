# 17175373 - Naho Gwanboh

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Meriphataud Mountains [S] (ID: 97) |
| Block Size       | 300 bytes                          |
| Total Events     | 15                                 |
| References Count | 16                                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [3](#event-3)              | 0x0001       |      1 |              1 |
| [4](#event-4)              | 0x0002       |      1 |              1 |
| [5](#event-5)              | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |     19 |              3 |
| [65535.2](#event-655352)   | 0x0017       |     31 |              9 |
| [65535.3](#event-655353)   | 0x0036       |     24 |              6 |
| [65535.4](#event-655354)   | 0x004E       |     14 |              4 |
| [65535.5](#event-655355)   | 0x005C       |      1 |              1 |
| [65535.6](#event-655356)   | 0x005D       |     18 |              4 |
| [65535.7](#event-655357)   | 0x006F       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0079       |      9 |              3 |
| [65535.9](#event-655359)   | 0x0082       |      9 |              3 |
| [65535.10](#event-6553510) | 0x008B       |     10 |              2 |
| [65535.11](#event-6553511) | 0x0095       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x052F      |        1327 |
|       2 | 0x000D      |          13 |
|       3 | 0x669A9     |      420265 |
|       4 | 0x139A8     |       80296 |
|       5 | 0xFFFFC55A  |  4294952282 |
|       6 | 0x0028      |          40 |
|       7 | 0xA5817     |      677911 |
|       8 | 0x6FDA      |       28634 |
|       9 | 0xFFFFA2DB  |  4294943451 |
|      10 | 0xA870A     |      689930 |
|      11 | 0x1A71      |        6769 |
|      12 | 0xFFFFA0AA  |  4294942890 |
|      13 | 0x0000      |           0 |
|      14 | 0x0001      |           1 |
|      15 | 0x0080      |         128 |

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

### Event 3

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

### Event 4

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

### Event 5

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
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             1C 00 80 5B  01 80 F8 FF FF 7F F8 FF      ...[........
0010: FF 7F 73 74 61 30 00                              ..sta0.         
```

#### Opcodes

```
  0: 0x0004 [0x1C] WAIT(20* ticks)
  1: 0x0007 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sta0" with entities [EventEntity, EventEntity], work=1327*
  2: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 31 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      1E  F0 FF FF 7F 6F 76 F8 FF         .....ov..
0020: FF 7F 32 02 80 1F 00 03  80 04 80 05 80 1F 01 6F  ..2............o
0030: 1E 42 13 06 01 00                                 .B....          
```

#### Opcodes

```
  0: 0x0017 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x001D [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x0022 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  4: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=420.265*, Z=80.296*, Y=-15.014*
  5: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0030 [0x1E] EventEntity looks at Lehko Habhoka (ID: 17175362/0x01061342) and starts talking
  8: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   32 06  80 1F 00 07 80 08 80 09        2.........
0040: 80 1F 01 1F 00 0A 80 0B  80 0C 80 1F 01 00        ..............  
```

#### Opcodes

```
  0: 0x0036 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0039 [0x1F] MOVE_ENTITY: EventEntity moves to X=677.911*, Z=28.634*, Y=-23.845*
  2: 0x0041 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0043 [0x1F] MOVE_ENTITY: EventEntity moves to X=689.930*, Z=6.769*, Y=-24.406*
  4: 0x004B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            32 06                2.
0050: 80 1F 00 0A 80 0B 80 0C  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x004E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=689.930*, Z=6.769*, Y=-24.406*
  2: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      00                       .   
```

#### Opcodes

```
  0: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         22 00 2F               "./
0060: 00 F8 FF FF 7F 6C F8 FF  FF 7F 0D 80 0E 80 00     .....l......... 
```

#### Opcodes

```
  0: 0x005D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x005F [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0065 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               6C                 l
0070: F8 FF FF 7F 0F 80 0E 80  00                       .........       
```

#### Opcodes

```
  0: 0x006F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0079  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             22 00 2F 00 F8 FF FF           "./....
0080: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0079 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x007B [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0082  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       22 01 2F 01 F8 FF  FF 7F 00                   "./......     
```

#### Opcodes

```
  0: 0x0082 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0084 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   6C F8 FF FF 7F             l....
0090: 0D 80 0E 80 00                                    .....           
```

#### Opcodes

```
  0: 0x008B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                6C F8 FF  FF 7F 0F 80 0E 80 00          l......... 
```

#### Opcodes

```
  0: 0x0095 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x009E [0x00] END_REQSTACK()
```
