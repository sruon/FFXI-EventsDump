# 17183644 - Koh Lenbalalako

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Castle Oztroja [S] (ID: 99) |
| Block Size       | 432 bytes                   |
| Total Events     | 14                          |
| References Count | 33                          |

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
| [106](#event-106)          | 0x0044       |      1 |              1 |
| [107](#event-107)          | 0x0045       |      1 |              1 |
| [108](#event-108)          | 0x0046       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0047       |     35 |              6 |
| [65535.9](#event-655359)   | 0x006A       |     49 |             10 |
| [65535.10](#event-6553510) | 0x009B       |     71 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0xAEA8      |       44712 |
|       5 | 0xFFFE948C  |  4294874252 |
|       6 | 0xFFFFC185  |  4294951301 |
|       7 | 0x0195      |         405 |
|       8 | 0x000B      |          11 |
|       9 | 0xC262      |       49762 |
|      10 | 0xFFFE9674  |  4294874740 |
|      11 | 0xFFFFC180  |  4294951296 |
|      12 | 0xB4EE      |       46318 |
|      13 | 0xFFFE9647  |  4294874695 |
|      14 | 0xFFFFC183  |  4294951299 |
|      15 | 0xB1CF      |       45519 |
|      16 | 0xFFFE9731  |  4294874929 |
|      17 | 0xCF44      |       53060 |
|      18 | 0xFFFE9762  |  4294874978 |
|      19 | 0xE4D5      |       58581 |
|      20 | 0xFFFE9152  |  4294873426 |
|      21 | 0xFFFFC182  |  4294951298 |
|      22 | 0x11721     |       71457 |
|      23 | 0xFFFE8863  |  4294871139 |
|      24 | 0x164C8     |       91336 |
|      25 | 0xFFFE9791  |  4294875025 |
|      26 | 0xFFFFC091  |  4294951057 |
|      27 | 0x1740E     |       95246 |
|      28 | 0xFFFE8B41  |  4294871873 |
|      29 | 0xFFFFC0DA  |  4294951130 |
|      30 | 0x19AB9     |      105145 |
|      31 | 0xFFFE904E  |  4294873166 |
|      32 | 0xFFFFC04B  |  4294950987 |

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

### Event 106

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
| Data Size    | 35 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      59  04 F8 FF FF 7F 03 80 1F         Y........
0050: 00 04 80 05 80 06 80 1F  01 6F 5B 07 80 F8 FF FF  .........o[.....
0060: 7F F8 FF FF 7F 74 6C 63  30 00                    .....tlc0.      
```

#### Opcodes

```
  0: 0x0047 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x004F [0x1F] MOVE_ENTITY: EventEntity moves to X=44.712*, Z=-93.044*, Y=-15.995*
  2: 0x0057 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0059 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=405*
  5: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 49 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                59 04 F8 FF FF 7F            Y.....
0070: 08 80 1F 00 09 80 0A 80  0B 80 1F 01 1F 00 0C 80  ................
0080: 0D 80 0E 80 1F 01 1F 00  0F 80 10 80 06 80 1F 01  ................
0090: 6F 4A F8 FF FF 7F 70 33  06 01 00                 oJ....p3...     
```

#### Opcodes

```
  0: 0x006A [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 11* * 0.1
  1: 0x0072 [0x1F] MOVE_ENTITY: EventEntity moves to X=49.762*, Z=-92.556*, Y=-16.000*
  2: 0x007A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007C [0x1F] MOVE_ENTITY: EventEntity moves to X=46.318*, Z=-92.601*, Y=-15.997*
  4: 0x0084 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0086 [0x1F] MOVE_ENTITY: EventEntity moves to X=45.519*, Z=-92.367*, Y=-15.995*
  6: 0x008E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0090 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0091 [0x4A] EventEntity looks at Lehko Habhoka (ID: 17183600/0x01063370)
  9: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 71 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   59 04 F8 FF FF             Y....
00A0: 7F 03 80 1F 00 11 80 12  80 0B 80 1F 01 1F 00 13  ................
00B0: 80 14 80 15 80 1F 01 1F  00 16 80 17 80 0B 80 1F  ................
00C0: 01 6F 1F 00 18 80 19 80  1A 80 1F 01 1F 00 1B 80  .o..............
00D0: 1C 80 1D 80 1F 01 1F 00  1E 80 1F 80 20 80 1F 01  ............ ...
00E0: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x009B [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x00A3 [0x1F] MOVE_ENTITY: EventEntity moves to X=53.060*, Z=-92.318*, Y=-16.000*
  2: 0x00AB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AD [0x1F] MOVE_ENTITY: EventEntity moves to X=58.581*, Z=-93.870*, Y=-15.998*
  4: 0x00B5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00B7 [0x1F] MOVE_ENTITY: EventEntity moves to X=71.457*, Z=-96.157*, Y=-16.000*
  6: 0x00BF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00C1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00C2 [0x1F] MOVE_ENTITY: EventEntity moves to X=91.336*, Z=-92.271*, Y=-16.239*
  9: 0x00CA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 10: 0x00CC [0x1F] MOVE_ENTITY: EventEntity moves to X=95.246*, Z=-95.423*, Y=-16.166*
 11: 0x00D4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 12: 0x00D6 [0x1F] MOVE_ENTITY: EventEntity moves to X=105.145*, Z=-94.130*, Y=-16.309*
 13: 0x00DE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 14: 0x00E0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 15: 0x00E1 [0x00] END_REQSTACK()
```
