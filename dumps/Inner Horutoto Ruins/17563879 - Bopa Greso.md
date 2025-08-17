# 17563879 - Bopa Greso

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Inner Horutoto Ruins (ID: 192) |
| Block Size       | 456 bytes                      |
| Total Events     | 17                             |
| References Count | 22                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     50 |              4 |
| [65535.2](#event-655352)   | 0x0033       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0043       |      9 |              3 |
| [65535.4](#event-655354)   | 0x004C       |     16 |              2 |
| [65535.5](#event-655355)   | 0x005C       |     14 |              2 |
| [65535.6](#event-655356)   | 0x006A       |     16 |              2 |
| [65535.7](#event-655357)   | 0x007A       |     14 |              2 |
| [65535.8](#event-655358)   | 0x0088       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0098       |     14 |              2 |
| [46](#event-46)            | 0x00A6       |      7 |              2 |
| [65535.10](#event-6553510) | 0x00AD       |     10 |              2 |
| [65535.11](#event-6553511) | 0x00B7       |     35 |              8 |
| [65535.12](#event-6553512) | 0x00DA       |     23 |              5 |
| [65535.13](#event-6553513) | 0x00F1       |     17 |              5 |
| [65535.14](#event-6553514) | 0x0102       |     19 |              5 |
| [65535.15](#event-6553515) | 0x0115       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x005C      |          92 |
|       1 | 0x0000      |           0 |
|       2 | 0x0032      |          50 |
|       3 | 0x001E      |          30 |
|       4 | 0x0035      |          53 |
|       5 | 0x0008      |           8 |
|       6 | 0xFFFFC7D8  |  4294952920 |
|       7 | 0x4B69      |       19305 |
|       8 | 0x086B      |        2155 |
|       9 | 0x000D      |          13 |
|      10 | 0xFFFFB748  |  4294948680 |
|      11 | 0xFFFFA8F0  |  4294945008 |
|      12 | 0x4A7E      |       19070 |
|      13 | 0xFFFFA0F5  |  4294942965 |
|      14 | 0x4B25      |       19237 |
|      15 | 0xFFFFFFEC  |  4294967276 |
|      16 | 0xFFFF9E52  |  4294942290 |
|      17 | 0x470C      |       18188 |
|      18 | 0xFFFFFFE6  |  4294967270 |
|      19 | 0x0E9A      |        3738 |
|      20 | 0x1C77      |        7287 |
|      21 | 0x1C7F      |        7295 |

## String References

- **7287**: Heh heh heh... Don't tell us this is yourrr first lesson in the school of hard knocks now, little [girrrl/boy]?
- **7295**: What do we do, Top Cat? We can't take on three Ace Carrrdians and expect to live!

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
| Data Size    | 50 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    45 00 80 F0 FF FF 7F  F0 FF FF 7F 73 30 33 33   E..........s033
0010: 01 80 55 00 80 F0 FF FF  7F F0 FF FF 7F 73 30 33  ..U..........s03
0020: 33 45 00 80 F0 FF FF 7F  F0 FF FF 7F 73 30 35 32  3E..........s052
0030: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s033" with entities [LocalPlayer, LocalPlayer], work=[92*, 0*]
  1: 0x0012 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s033" with entities [LocalPlayer, LocalPlayer], work=92*
  2: 0x0021 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s052" with entities [LocalPlayer, LocalPlayer], work=[92*, 0*]
  3: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          66 02 80 F8 FF  FF 7F F8 FF FF 7F 74 6C     f..........tl
0040: 6B 30 00                                          k0.             
```

#### Opcodes

```
  0: 0x0033 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          5E 69 64 6C 30  1C 03 80 00                 ^idl0....    
```

#### Opcodes

```
  0: 0x0043 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0048 [0x1C] WAIT(30* ticks)
  2: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      66 04 80 F8              f...
0050: FF FF 7F F8 FF FF 7F 74  6C 62 30 00              .......tlb0.    
```

#### Opcodes

```
  0: 0x004C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=53*
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      53 F8 FF FF              S...
0060: 7F F8 FF FF 7F 74 6C 62  30 00                    .....tlb0.      
```

#### Opcodes

```
  0: 0x005C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb0" with entities [EventEntity, EventEntity]
  1: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                66 05 80 F8 FF FF            f.....
0070: 7F F8 FF FF 7F 61 66 72  30 00                    .....afr0.      
```

#### Opcodes

```
  0: 0x006A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "afr0" with entities [EventEntity, EventEntity], work=8*
  1: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                53 F8 FF FF 7F F8            S.....
0080: FF FF 7F 61 66 72 30 00                           ...afr0.        
```

#### Opcodes

```
  0: 0x007A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "afr0" with entities [EventEntity, EventEntity]
  1: 0x0087 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          66 05 80 F8 FF FF 7F F8          f.......
0090: FF FF 7F 61 66 72 31 00                           ...afr1.        
```

#### Opcodes

```
  0: 0x0088 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "afr1" with entities [EventEntity, EventEntity], work=8*
  1: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          53 F8 FF FF 7F F8 FF FF          S.......
00A0: 7F 61 66 72 31 00                                 .afr1.          
```

#### Opcodes

```
  0: 0x0098 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "afr1" with entities [EventEntity, EventEntity]
  1: 0x00A5 [0x00] END_REQSTACK()
```

### Event 46

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A6  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                   4E 01  E7 00 0C 01 00                 N......   
```

#### Opcodes

```
  0: 0x00A6 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Bopa Greso (ID: 17563879/0x010C00E7)
  1: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         37 06 80               7..
00B0: 07 80 01 80 08 80 00                              .......         
```

#### Opcodes

```
  0: 0x00AD [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-14.376*, z=19.305*, y=0.000*, direction=189.4°*
  1: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 35 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      4E  00 E7 00 0C 01 32 09 80         N.....2..
00C0: 1F 00 0A 80 07 80 01 80  1F 01 1F 00 0B 80 0C 80  ................
00D0: 01 80 1F 01 1E F0 FF FF  7F 00                    ..........      
```

#### Opcodes

```
  0: 0x00B7 [0x4E] SET_ENTITY_HIDE_FLAG: Show Bopa Greso (ID: 17563879/0x010C00E7)
  1: 0x00BD [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x00C0 [0x1F] MOVE_ENTITY: EventEntity moves to X=-18.616*, Z=19.305*, Y=0.000*
  3: 0x00C8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00CA [0x1F] MOVE_ENTITY: EventEntity moves to X=-22.288*, Z=19.070*, Y=0.000*
  5: 0x00D2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x00D4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  7: 0x00D9 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DA   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                32 09 80 1F 00 0D            2.....
00E0: 80 0E 80 0F 80 1F 01 4A  E7 00 0C 01 F0 FF FF 7F  .......J........
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00DA [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00DD [0x1F] MOVE_ENTITY: EventEntity moves to X=-24.331*, Z=19.237*, Y=-0.020*
  2: 0x00E5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E7 [0x4A] Bopa Greso (ID: 17563879/0x010C00E7) looks at LocalPlayer
  4: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    32 09 80 1F 00 10 80  11 80 12 80 1F 01 39 13   2............9.
0100: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00F1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00F4 [0x1F] MOVE_ENTITY: EventEntity moves to X=-25.006*, Z=18.188*, Y=-0.026*
  2: 0x00FC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00FE [0x39] SET_ENTITY_DIRECTION(direction=20.5°*)
  4: 0x0101 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0102   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       29 08 E7 00 0C 01  02 1D 14 80 23 29 08 E7    ).........#)..
0110: 00 0C 01 03 00                                    .....           
```

#### Opcodes

```
  0: 0x0102 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bopa Greso (ID: 17563879/0x010C00E7), tag_num=0x02)
  1: 0x0109 [0x1D] PRINT_EVENT_MESSAGE(message_id=7287*)
    → "Heh heh heh... Don't tell us this is yourrr first lesson in the school of hard knocks now, little [girrrl/boy]?"
  2: 0x010C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x010D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bopa Greso (ID: 17563879/0x010C00E7), tag_num=0x03)
  4: 0x0114 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0115  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                1D 15 80  23 00                         ...#.      
```

#### Opcodes

```
  0: 0x0115 [0x1D] PRINT_EVENT_MESSAGE(message_id=7295*)
    → "What do we do, Top Cat? We can't take on three Ace Carrrdians and expect to live!"
  1: 0x0118 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0119 [0x00] END_REQSTACK()
```
