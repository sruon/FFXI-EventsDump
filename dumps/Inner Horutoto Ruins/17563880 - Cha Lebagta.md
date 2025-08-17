# 17563880 - Cha Lebagta

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Inner Horutoto Ruins (ID: 192) |
| Block Size       | 360 bytes                      |
| Total Events     | 15                             |
| References Count | 15                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |      9 |              3 |
| [65535.3](#event-655353)   | 0x001A       |     22 |              3 |
| [65535.4](#event-655354)   | 0x0030       |     20 |              3 |
| [65535.5](#event-655355)   | 0x0044       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0054       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0062       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0072       |     14 |              2 |
| [46](#event-46)            | 0x0080       |      7 |              2 |
| [65535.9](#event-655359)   | 0x0087       |     10 |              2 |
| [65535.10](#event-6553510) | 0x0091       |     35 |              8 |
| [65535.11](#event-6553511) | 0x00B4       |     19 |              5 |
| [65535.12](#event-6553512) | 0x00C7       |     19 |              5 |
| [65535.13](#event-6553513) | 0x00DA       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0167      |         359 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFFCF70  |  4294954864 |
|       3 | 0x5022      |       20514 |
|       4 | 0x0000      |           0 |
|       5 | 0x0775      |        1909 |
|       6 | 0x000D      |          13 |
|       7 | 0xFFFFB800  |  4294948864 |
|       8 | 0xFFFFA9AD  |  4294945197 |
|       9 | 0x50E3      |       20707 |
|      10 | 0xFFFFA107  |  4294942983 |
|      11 | 0x5069      |       20585 |
|      12 | 0xFFFFFFEB  |  4294967275 |
|      13 | 0x1C78      |        7288 |
|      14 | 0x1C7E      |        7294 |

## String References

- **7288**: Hah! Perrrhaps you should consider this as your tuition fee? You see, we intended to use that book as bait...to lurrre unsuspecting do-gooders like yourself into our little trap.
- **7294**: Grrr... This is bad!

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
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=359*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                81 00 F8 FF FF 7F            ......
0020: 5B 00 80 F8 FF FF 7F F8  FF FF 7F 73 69 73 30 00  [..........sis0.
```

#### Opcodes

```
  0: 0x001A [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0020 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sis0" with entities [EventEntity, EventEntity], work=359*
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 53 F8 FF FF 7F F8 FF FF  7F 73 69 73 30 81 01 F8  S........sis0...
0040: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0030 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sis0" with entities [EventEntity, EventEntity]
  1: 0x003D [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             5B 00 80 F8  FF FF 7F F8 FF FF 7F 67      [..........g
0050: 65 65 30 00                                       ee0.            
```

#### Opcodes

```
  0: 0x0044 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gee0" with entities [EventEntity, EventEntity], work=359*
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             53 F8 FF FF  7F F8 FF FF 7F 67 65 65      S........gee
0060: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0054 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gee0" with entities [EventEntity, EventEntity]
  1: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       5B 00 80 F8 FF FF  7F F8 FF FF 7F 67 65 65    [..........gee
0070: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0062 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gee1" with entities [EventEntity, EventEntity], work=359*
  1: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       53 F8 FF FF 7F F8  FF FF 7F 67 65 65 31 00    S........gee1.
```

#### Opcodes

```
  0: 0x0072 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gee1" with entities [EventEntity, EventEntity]
  1: 0x007F [0x00] END_REQSTACK()
```

### Event 46

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0080  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 4E 01 E8 00 0C 01 00                              N......         
```

#### Opcodes

```
  0: 0x0080 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Cha Lebagta (ID: 17563880/0x010C00E8)
  1: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      37  02 80 03 80 04 80 05 80         7........
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0087 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-12.432*, z=20.514*, y=0.000*, direction=167.8°*
  1: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 35 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    4E 00 E8 00 0C 01 32  06 80 1F 00 07 80 03 80   N.....2........
00A0: 04 80 1F 01 1F 00 08 80  09 80 04 80 1F 01 1E F0  ................
00B0: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0091 [0x4E] SET_ENTITY_HIDE_FLAG: Show Cha Lebagta (ID: 17563880/0x010C00E8)
  1: 0x0097 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x009A [0x1F] MOVE_ENTITY: EventEntity moves to X=-18.432*, Z=20.514*, Y=0.000*
  3: 0x00A2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00A4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-22.099*, Z=20.707*, Y=0.000*
  5: 0x00AC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x00AE [0x1E] EventEntity looks at LocalPlayer and starts talking
  7: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             32 06 80 1F  00 0A 80 0B 80 0C 80 1F      2...........
00C0: 01 1E F0 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x00B4 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B7 [0x1F] MOVE_ENTITY: EventEntity moves to X=-24.313*, Z=20.585*, Y=-0.021*
  2: 0x00BF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C1 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00C6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C7   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                      29  08 E8 00 0C 01 03 1D 0D         )........
00D0: 80 23 29 08 E8 00 0C 01  04 00                    .#).......      
```

#### Opcodes

```
  0: 0x00C7 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cha Lebagta (ID: 17563880/0x010C00E8), tag_num=0x03)
  1: 0x00CE [0x1D] PRINT_EVENT_MESSAGE(message_id=7288*)
    → "Hah! Perrrhaps you should consider this as your tuition fee? You see, we intended to use that book as bait...to lurrre unsuspecting do-gooders like yourself into our little trap."
  2: 0x00D1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00D2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Cha Lebagta (ID: 17563880/0x010C00E8), tag_num=0x04)
  4: 0x00D9 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DA  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                1D 0E 80 23 00               ...#. 
```

#### Opcodes

```
  0: 0x00DA [0x1D] PRINT_EVENT_MESSAGE(message_id=7294*)
    → "Grrr... This is bad!"
  1: 0x00DD [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00DE [0x00] END_REQSTACK()
```
