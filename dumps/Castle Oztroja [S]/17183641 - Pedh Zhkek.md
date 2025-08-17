# 17183641 - Pedh Zhkek

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Castle Oztroja [S] (ID: 99) |
| Block Size       | 392 bytes                   |
| Total Events     | 15                          |
| References Count | 27                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [105](#event-105)          | 0x0044       |      1 |              1 |
| [107](#event-107)          | 0x0045       |      1 |              1 |
| [108](#event-108)          | 0x0046       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0047       |     13 |              3 |
| [65535.9](#event-655359)   | 0x0054       |     13 |              3 |
| [65535.10](#event-6553510) | 0x0061       |     39 |              8 |
| [65535.11](#event-6553511) | 0x0088       |     71 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0007      |           7 |
|       4 | 0x000C      |          12 |
|       5 | 0xB3A2      |       45986 |
|       6 | 0xFFFE9593  |  4294874515 |
|       7 | 0xFFFFC183  |  4294951299 |
|       8 | 0xB1A9      |       45481 |
|       9 | 0xFFFE9420  |  4294874144 |
|      10 | 0xCF44      |       53060 |
|      11 | 0xFFFE9762  |  4294874978 |
|      12 | 0xFFFFC180  |  4294951296 |
|      13 | 0xE4D5      |       58581 |
|      14 | 0xFFFE9152  |  4294873426 |
|      15 | 0xFFFFC182  |  4294951298 |
|      16 | 0x108DE     |       67806 |
|      17 | 0xFFFE8FC3  |  4294873027 |
|      18 | 0x164C8     |       91336 |
|      19 | 0xFFFE9791  |  4294875025 |
|      20 | 0xFFFFC091  |  4294951057 |
|      21 | 0x1740E     |       95246 |
|      22 | 0xFFFE8B41  |  4294871873 |
|      23 | 0xFFFFC0DA  |  4294951130 |
|      24 | 0x19AB9     |      105145 |
|      25 | 0xFFFE904E  |  4294873166 |
|      26 | 0xFFFFC04B  |  4294950987 |

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 108

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0046  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   00                                    .         
```

#### Opcodes

```
  0: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      6E  F8 FF FF 7F 03 80 99 F8         n........
0050: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0047 [0x6E] EventEntity uses emote 7*
  1: 0x004E [0x99] Wait for EventEntity animation to complete
  2: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             6E F8 FF FF  7F 01 80 99 F8 FF FF 7F      n...........
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0054 [0x6E] EventEntity uses emote 1*
  1: 0x005B [0x99] Wait for EventEntity animation to complete
  2: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 39 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    59 04 F8 FF FF 7F 04  80 1F 00 05 80 06 80 07   Y..............
0070: 80 1F 01 1F 00 08 80 09  80 07 80 1F 01 6F 4A F8  .............oJ.
0080: FF FF 7F 70 33 06 01 00                           ...p3...        
```

#### Opcodes

```
  0: 0x0061 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 12* * 0.1
  1: 0x0069 [0x1F] MOVE_ENTITY: EventEntity moves to X=45.986*, Z=-92.781*, Y=-15.997*
  2: 0x0071 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0073 [0x1F] MOVE_ENTITY: EventEntity moves to X=45.481*, Z=-93.152*, Y=-15.997*
  4: 0x007B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x007D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x007E [0x4A] EventEntity looks at Lehko Habhoka (ID: 17183600/0x01063370)
  7: 0x0087 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 71 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          59 04 F8 FF FF 7F 04 80          Y.......
0090: 1F 00 0A 80 0B 80 0C 80  1F 01 1F 00 0D 80 0E 80  ................
00A0: 0F 80 1F 01 1F 00 10 80  11 80 0C 80 1F 01 6F 1F  ..............o.
00B0: 00 12 80 13 80 14 80 1F  01 1F 00 15 80 16 80 17  ................
00C0: 80 1F 01 1F 00 18 80 19  80 1A 80 1F 01 6F 00     .............o. 
```

#### Opcodes

```
  0: 0x0088 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 12* * 0.1
  1: 0x0090 [0x1F] MOVE_ENTITY: EventEntity moves to X=53.060*, Z=-92.318*, Y=-16.000*
  2: 0x0098 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009A [0x1F] MOVE_ENTITY: EventEntity moves to X=58.581*, Z=-93.870*, Y=-15.998*
  4: 0x00A2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00A4 [0x1F] MOVE_ENTITY: EventEntity moves to X=67.806*, Z=-94.269*, Y=-16.000*
  6: 0x00AC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00AE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00AF [0x1F] MOVE_ENTITY: EventEntity moves to X=91.336*, Z=-92.271*, Y=-16.239*
  9: 0x00B7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 10: 0x00B9 [0x1F] MOVE_ENTITY: EventEntity moves to X=95.246*, Z=-95.423*, Y=-16.166*
 11: 0x00C1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 12: 0x00C3 [0x1F] MOVE_ENTITY: EventEntity moves to X=105.145*, Z=-94.130*, Y=-16.309*
 13: 0x00CB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 14: 0x00CD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 15: 0x00CE [0x00] END_REQSTACK()
```
