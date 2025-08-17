# 17175374 - Nzha Abaleenah

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Meriphataud Mountains [S] (ID: 97) |
| Block Size       | 324 bytes                          |
| Total Events     | 17                                 |
| References Count | 18                                 |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [3](#event-3)              | 0x0001       |      1 |              1 |
| [4](#event-4)              | 0x0002       |      1 |              1 |
| [5](#event-5)              | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |     14 |              4 |
| [65535.2](#event-655352)   | 0x0012       |     16 |              4 |
| [65535.3](#event-655353)   | 0x0022       |     13 |              3 |
| [65535.4](#event-655354)   | 0x002F       |     24 |              6 |
| [65535.5](#event-655355)   | 0x0047       |     14 |              4 |
| [65535.6](#event-655356)   | 0x0055       |     13 |              3 |
| [65535.7](#event-655357)   | 0x0062       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0063       |     18 |              4 |
| [65535.9](#event-655359)   | 0x0075       |     10 |              2 |
| [65535.10](#event-6553510) | 0x007F       |      9 |              3 |
| [65535.11](#event-6553511) | 0x0088       |      9 |              3 |
| [65535.12](#event-6553512) | 0x0091       |     10 |              2 |
| [65535.13](#event-6553513) | 0x009B       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x612F8     |      398072 |
|       2 | 0x10495     |       66709 |
|       3 | 0xFFFFC24C  |  4294951500 |
|       4 | 0x001E      |          30 |
|       5 | 0x000C      |          12 |
|       6 | 0x0024      |          36 |
|       7 | 0x0028      |          40 |
|       8 | 0xA4D90     |      675216 |
|       9 | 0x73DA      |       29658 |
|      10 | 0xFFFFA254  |  4294943316 |
|      11 | 0xA7A22     |      686626 |
|      12 | 0x20DE      |        8414 |
|      13 | 0xFFFFA2A6  |  4294943398 |
|      14 | 0x0015      |          21 |
|      15 | 0x0000      |           0 |
|      16 | 0x0001      |           1 |
|      17 | 0x0080      |         128 |

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 1F  00 01 80 02 80 03 80 1F      2...........
0010: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=398.072*, Z=66.709*, Y=-15.796*
  2: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       1C 04 80 6E F8 FF  FF 7F 05 80 99 F8 FF FF    ...n..........
0020: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0012 [0x1C] WAIT(30* ticks)
  1: 0x0015 [0x6E] EventEntity uses emote 12*
  2: 0x001C [0x99] Wait for EventEntity animation to complete
  3: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       6E F8 FF FF 7F 06  80 99 F8 FF FF 7F 00       n............ 
```

#### Opcodes

```
  0: 0x0022 [0x6E] EventEntity uses emote 36*
  1: 0x0029 [0x99] Wait for EventEntity animation to complete
  2: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               32                 2
0030: 07 80 1F 00 08 80 09 80  0A 80 1F 01 1F 00 0B 80  ................
0040: 0C 80 0D 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x002F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=675.216*, Z=29.658*, Y=-23.980*
  2: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=686.626*, Z=8.414*, Y=-23.898*
  4: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      32  07 80 1F 00 0B 80 0C 80         2........
0050: 0D 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0047 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x004A [0x1F] MOVE_ENTITY: EventEntity moves to X=686.626*, Z=8.414*, Y=-23.898*
  2: 0x0052 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                6E F8 FF  FF 7F 0E 80 99 F8 FF FF       n..........
0060: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0055 [0x6E] EventEntity uses emote 21*
  1: 0x005C [0x99] Wait for EventEntity animation to complete
  2: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0062  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       00                                            .             
```

#### Opcodes

```
  0: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          22 00 2F 00 F8  FF FF 7F 6C F8 FF FF 7F     "./.....l....
0070: 0F 80 10 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0063 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0065 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x006B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                6C F8 FF  FF 7F 11 80 10 80 00          l......... 
```

#### Opcodes

```
  0: 0x0075 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007F  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               22                 "
0080: 00 2F 00 F8 FF FF 7F 00                           ./......        
```

#### Opcodes

```
  0: 0x007F [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0081 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0087 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0088  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          22 01 2F 01 F8 FF FF 7F          "./.....
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0088 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x008A [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    6C F8 FF FF 7F 0F 80  10 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0091 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   6C F8 FF FF 7F             l....
00A0: 11 80 10 80 00                                    .....           
```

#### Opcodes

```
  0: 0x009B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00A4 [0x00] END_REQSTACK()
```
