# 16994358 - Kyokyoroon

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 356 bytes        |
| Total Events     | 13               |
| References Count | 26               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [263](#event-263)        | 0x0001       |     59 |             15 |
| [305](#event-305)        | 0x003C       |      1 |              1 |
| [65535.1](#event-655351) | 0x003D       |     10 |              2 |
| [65535.2](#event-655352) | 0x0047       |     20 |              4 |
| [65535.3](#event-655353) | 0x005B       |     20 |              4 |
| [311](#event-311)        | 0x006F       |      1 |              1 |
| [312](#event-312)        | 0x0070       |      1 |              1 |
| [65535.4](#event-655354) | 0x0071       |     15 |              5 |
| [65535.5](#event-655355) | 0x0080       |     15 |              5 |
| [65535.6](#event-655356) | 0x008F       |     15 |              5 |
| [316](#event-316)        | 0x009E       |     15 |              7 |
| [317](#event-317)        | 0x00AD       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2939      |       10553 |
|       1 | 0x034B      |         843 |
|       2 | 0x001E      |          30 |
|       3 | 0x293A      |       10554 |
|       4 | 0x293B      |       10555 |
|       5 | 0x293C      |       10556 |
|       6 | 0xFFFFB8CC  |  4294949068 |
|       7 | 0xFFFF5874  |  4294924404 |
|       8 | 0x0000      |           0 |
|       9 | 0x096E      |        2414 |
|      10 | 0xFFFFB6F5  |  4294948597 |
|      11 | 0xFFFF5532  |  4294923570 |
|      12 | 0xFFFFC2B7  |  4294951607 |
|      13 | 0xFFFF71C9  |  4294930889 |
|      14 | 0x0028      |          40 |
|      15 | 0x16BB      |        5819 |
|      16 | 0x418A      |       16778 |
|      17 | 0x000D      |          13 |
|      18 | 0x0A6B      |        2667 |
|      19 | 0x15F4      |        5620 |
|      20 | 0x000B      |          11 |
|      21 | 0x06D3      |        1747 |
|      22 | 0xFFFF6AF5  |  4294929141 |
|      23 | 0x2D55      |       11605 |
|      24 | 0x2D56      |       11606 |
|      25 | 0x2D6A      |       11626 |

## String References

- **10553**: Hohoho? Yooo come from Al Zaaahbi? Hohoho? Kyokyoroon tell you goood seeecret!
- **10554**: Seeecret about "alzadal"? Yooo know about alzadal?
- **10555**: An alzadal float hiiigh in sky and shiiine like pretty stone.
- **10556**: High in sky? Shine? Maybe a staaar? Romantic, no? Hohoho?
- **11605**: Kyokyoroon have must hurry to boat dock place!
- **11606**: Kyokyoroon seee if perfect plan work, ya?
- **11626**: Tarooo babeee really gone...

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

### Event 263

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 59 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 5B 01 80 F8 FF FF   ........#[.....
0010: 7F F8 FF FF 7F 74 6C 62  30 1C 02 80 1D 03 80 23  .....tlb0......#
0020: 1D 04 80 23 1D 05 80 23  5B 01 80 F8 FF FF 7F F8  ...#...#[.......
0030: FF FF 7F 74 6C 62 31 1C  02 80 21 00              ...tlb1...!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=10553*)
    → "Hohoho? Yooo come from Al Zaaahbi? Hohoho? Kyokyoroon tell you goood seeecret!"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=843*
  4: 0x0019 [0x1C] WAIT(30* ticks)
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=10554*)
    → "Seeecret about "alzadal"? Yooo know about alzadal?"
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=10555*)
    → "An alzadal float hiiigh in sky and shiiine like pretty stone."
  8: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=10556*)
    → "High in sky? Shine? Maybe a staaar? Romantic, no? Hohoho?"
 10: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0028 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=843*
 12: 0x0037 [0x1C] WAIT(30* ticks)
 13: 0x003A [0x21] END_EVENT
 14: 0x003B [0x00] END_REQSTACK()
```

### Event 305

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      00                       .   
```

#### Opcodes

```
  0: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         37 06 80               7..
0040: 07 80 08 80 09 80 00                              .......         
```

#### Opcodes

```
  0: 0x003D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-18.228*, z=-42.892*, y=0.000*, direction=212.2°*
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 20 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      1F  00 0A 80 0B 80 08 80 1F         .........
0050: 01 4A 36 50 03 01 F0 FF  FF 7F 00                 .J6P.......     
```

#### Opcodes

```
  0: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=-18.699*, Z=-43.726*, Y=0.000*
  1: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0051 [0x4A] Kyokyoroon (ID: 16994358/0x01035036) looks at LocalPlayer
  3: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 20 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   1F 00 0C 80 0D             .....
0060: 80 08 80 1F 01 4A 36 50  03 01 78 50 03 01 00     .....J6P..xP... 
```

#### Opcodes

```
  0: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=-15.689*, Z=-36.407*, Y=0.000*
  1: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0065 [0x4A] Kyokyoroon (ID: 16994358/0x01035036) looks at Galiwao (ID: 16994424/0x01035078)
  3: 0x006E [0x00] END_REQSTACK()
```

### Event 311

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               00                 .
```

#### Opcodes

```
  0: 0x006F [0x00] END_REQSTACK()
```

### Event 312

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0070  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    32 0E 80 1F 00 0F 80  10 80 08 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0071 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0074 [0x1F] MOVE_ENTITY: EventEntity moves to X=5.819*, Z=16.778*, Y=0.000*
  2: 0x007C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 32 11 80 1F 00 12 80 13  80 08 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0080 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0083 [0x1F] MOVE_ENTITY: EventEntity moves to X=2.667*, Z=5.620*, Y=0.000*
  2: 0x008B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                               32                 2
0090: 14 80 1F 00 15 80 16 80  08 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x008F [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0092 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.747*, Z=-38.155*, Y=0.000*
  2: 0x009A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x009D [0x00] END_REQSTACK()
```

### Event 316

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            1E F0                ..
00A0: FF FF 7F 1D 17 80 23 1D  18 80 23 21 00           ......#...#!.   
```

#### Opcodes

```
  0: 0x009E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=11605*)
    → "Kyokyoroon have must hurry to boat dock place!"
  2: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00A7 [0x1D] PRINT_EVENT_MESSAGE(message_id=11606*)
    → "Kyokyoroon seee if perfect plan work, ya?"
  4: 0x00AA [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00AB [0x21] END_EVENT
  6: 0x00AC [0x00] END_REQSTACK()
```

### Event 317

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         1E F0 FF               ...
00B0: FF 7F 1D 19 80 23 21 00                           .....#!.        
```

#### Opcodes

```
  0: 0x00AD [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B2 [0x1D] PRINT_EVENT_MESSAGE(message_id=11626*)
    → "Tarooo babeee really gone..."
  2: 0x00B5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B6 [0x21] END_EVENT
  4: 0x00B7 [0x00] END_REQSTACK()
```
