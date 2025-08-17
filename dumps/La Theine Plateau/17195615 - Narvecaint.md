# 17195615 - Narvecaint

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 580 bytes                   |
| Total Events     | 23                          |
| References Count | 41                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [6](#event-6)              | 0x0001       |     13 |              7 |
| [7](#event-7)              | 0x000E       |     13 |              7 |
| [8](#event-8)              | 0x001B       |     13 |              7 |
| [107](#event-107)          | 0x0028       |     36 |             10 |
| [106](#event-106)          | 0x004C       |      1 |              1 |
| [65535.1](#event-655351)   | 0x004D       |      5 |              3 |
| [65535.2](#event-655352)   | 0x0052       |     52 |             12 |
| [0](#event-0)              | 0x0086       |      7 |              2 |
| [65535.3](#event-655353)   | 0x008D       |      6 |              2 |
| [65535.4](#event-655354)   | 0x0093       |      6 |              2 |
| [65535.5](#event-655355)   | 0x0099       |      6 |              2 |
| [65535.6](#event-655356)   | 0x009F       |     14 |              4 |
| [65535.7](#event-655357)   | 0x00AD       |     10 |              2 |
| [1](#event-1)              | 0x00B7       |      7 |              2 |
| [65535.8](#event-655358)   | 0x00BE       |     16 |              5 |
| [65535.9](#event-655359)   | 0x00CE       |      3 |              2 |
| [65535.10](#event-6553510) | 0x00D1       |     10 |              2 |
| [65535.11](#event-6553511) | 0x00DB       |     14 |              4 |
| [65535.12](#event-6553512) | 0x00E9       |     14 |              4 |
| [65535.13](#event-6553513) | 0x00F7       |     29 |              3 |
| [65535.14](#event-6553514) | 0x0114       |     16 |              2 |
| [65535.15](#event-6553515) | 0x0124       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E3B      |        7739 |
|       1 | 0x1E3C      |        7740 |
|       2 | 0x1E3D      |        7741 |
|       3 | 0x0014      |          20 |
|       4 | 0x1CF9      |        7417 |
|       5 | 0x001E      |          30 |
|       6 | 0x1CF7      |        7415 |
|       7 | 0x004B      |          75 |
|       8 | 0xFFFBF727  |  4294702887 |
|       9 | 0x207B2     |      133042 |
|      10 | 0x550E      |       21774 |
|      11 | 0x08B6      |        2230 |
|      12 | 0x003C      |          60 |
|      13 | 0x1CF8      |        7416 |
|      14 | 0xFFFC00D0  |  4294705360 |
|      15 | 0x1F27A     |      127610 |
|      16 | 0x5A68      |       23144 |
|      17 | 0x000D      |          13 |
|      18 | 0xFFFC0345  |  4294705989 |
|      19 | 0x1F8B0     |      129200 |
|      20 | 0x5873      |       22643 |
|      21 | 0xFFFA6E2F  |  4294602287 |
|      22 | 0x38CF8     |      232696 |
|      23 | 0x5558      |       21848 |
|      24 | 0x02D5      |         725 |
|      25 | 0x0028      |          40 |
|      26 | 0xFFFBE1AE  |  4294697390 |
|      27 | 0x2182A     |      137258 |
|      28 | 0x5874      |       22644 |
|      29 | 0xFFFBF719  |  4294702873 |
|      30 | 0x185D7     |       99799 |
|      31 | 0x56C0      |       22208 |
|      32 | 0x075D      |        1885 |
|      33 | 0xFFFBBD7A  |  4294688122 |
|      34 | 0x18438     |       99384 |
|      35 | 0x5DC0      |       24000 |
|      36 | 0xFFFBAFA8  |  4294684584 |
|      37 | 0x17C10     |       97296 |
|      38 | 0x5D5E      |       23902 |
|      39 | 0x0015      |          21 |
|      40 | 0x001B      |          27 |

## String References

- **7415**: Hey!
- **7416**: Hey! Come take a look at this! Quickly!
- **7417**: Look, a cave! Maybe he went in there!
- **7739**: Sir Elmemague has taken the suspect to the chateau for questioning. It's back to regular training drills for us.
- **7740**: We have received a report from Sir Elmemague that the suspect we apprehended wasn't the criminal after all. We must be ready to send word to the chateau if any other suspicious characters are sighted.
- **7741**: Thanks to our effective training drills, we were able to capture the new suspect with little trouble. Although I do wonder where that other knight disappeared to...

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

### Event 6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 21 00         .....op...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7739*)
    → "Sir Elmemague has taken the suspect to the chateau for questioning. It's back to regular training drills for us."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            1E F0                ..
0010: FF FF 7F 6F 70 1D 01 80  23 21 00                 ...op...#!.     
```

#### Opcodes

```
  0: 0x000E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0013 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0014 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=7740*)
    → "We have received a report from Sir Elmemague that the suspect we apprehended wasn't the criminal after all. We must be ready to send word to the chateau if any other suspicious characters are sighted."
  4: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0019 [0x21] END_EVENT
  6: 0x001A [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1E F0 FF FF 7F             .....
0020: 6F 70 1D 02 80 23 21 00                           op...#!.        
```

#### Opcodes

```
  0: 0x001B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0020 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0021 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7741*)
    → "Thanks to our effective training drills, we were able to capture the new suspect with little trouble. Although I do wonder where that other knight disappeared to..."
  4: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0026 [0x21] END_EVENT
  6: 0x0027 [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          1E F0 FF FF 7F 6F 70 66          .....opf
0030: 03 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 04  ..........tlk0..
0040: 80 23 5E 69 64 6C 30 1C  05 80 21 00              .#^idl0...!.    
```

#### Opcodes

```
  0: 0x0028 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x002E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=7417*)
    → "Look, a cave! Maybe he went in there!"
  5: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0042 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0047 [0x1C] WAIT(30* ticks)
  8: 0x004A [0x21] END_EVENT
  9: 0x004B [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      00                       .   
```

#### Opcodes

```
  0: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         1D 06 80               ...
0050: 23 00                                             #.              
```

#### Opcodes

```
  0: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=7415*)
    → "Hey!"
  1: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       32 07 80 1F 00 08  80 09 80 0A 80 1F 01 39    2............9
0060: 0B 80 1C 0C 80 66 03 80  F8 FF FF 7F F8 FF FF 7F  .....f..........
0070: 74 6C 6B 30 1D 0D 80 23  1C 05 80 1F 00 0E 80 0F  tlk0...#........
0080: 80 10 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0052 [0x32] ExtData[1]->MainSpeed = 75* * 0.1
  1: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=-264.409*, Z=133.042*, Y=21.774*
  2: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005F [0x39] SET_ENTITY_DIRECTION(direction=12.2°*)
  4: 0x0062 [0x1C] WAIT(60* ticks)
  5: 0x0065 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  6: 0x0074 [0x1D] PRINT_EVENT_MESSAGE(message_id=7416*)
    → "Hey! Come take a look at this! Quickly!"
  7: 0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0078 [0x1C] WAIT(30* ticks)
  9: 0x007B [0x1F] MOVE_ENTITY: EventEntity moves to X=-261.936*, Z=127.610*, Y=23.144*
 10: 0x0083 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x0085 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0086  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   94 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0086 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008D  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         1E F0 FF               ...
0090: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x008D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0092 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0093  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          1E 80 62 06 01  00                          ..b...       
```

#### Opcodes

```
  0: 0x0093 [0x1E] EventEntity looks at Elmemague (ID: 17195648/0x01066280) and starts talking
  1: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0099  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             1E 81 62 06 01 00              ..b... 
```

#### Opcodes

```
  0: 0x0099 [0x1E] EventEntity looks at Vijartal (ID: 17195649/0x01066281) and starts talking
  1: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               32                 2
00A0: 11 80 1F 00 12 80 13 80  14 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x009F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-261.307*, Z=129.200*, Y=22.643*
  2: 0x00AA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         37 15 80               7..
00B0: 16 80 17 80 18 80 00                              .......         
```

#### Opcodes

```
  0: 0x00AD [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-365.009*, z=232.696*, y=21.848*, direction=63.7°*
  1: 0x00B6 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B7  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      94  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x00B7 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00BD [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BE   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            32 19                2.
00C0: 80 1F 00 1A 80 1B 80 1C  80 1F 01 22 01 00        ..........."..  
```

#### Opcodes

```
  0: 0x00BE [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00C1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-269.906*, Z=137.258*, Y=22.644*
  2: 0x00C9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00CB [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CE  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            22 01                ".
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00CE [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    37 1D 80 1E 80 1F 80  20 80 00                  7...... ..     
```

#### Opcodes

```
  0: 0x00D1 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-264.423*, z=99.799*, y=22.208*, direction=165.7°*
  1: 0x00DA [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DB   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   32 19 80 1F 00             2....
00E0: 21 80 22 80 23 80 1F 01  00                       !.".#....       
```

#### Opcodes

```
  0: 0x00DB [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00DE [0x1F] MOVE_ENTITY: EventEntity moves to X=-279.174*, Z=99.384*, Y=24.000*
  2: 0x00E6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E8 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E9   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                             32 19 80 1F 00 24 80           2....$.
00F0: 25 80 26 80 1F 01 00                              %.&....         
```

#### Opcodes

```
  0: 0x00E9 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00EC [0x1F] MOVE_ENTITY: EventEntity moves to X=-282.712*, Z=97.296*, Y=23.902*
  2: 0x00F4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F6 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F7   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      66  27 80 F8 FF FF 7F F8 FF         f'.......
0100: FF 7F 73 6C 30 30 53 F8  FF FF 7F F8 FF FF 7F 73  ..sl00S........s
0110: 6C 30 30 00                                       l00.            
```

#### Opcodes

```
  0: 0x00F7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sl00" with entities [EventEntity, EventEntity], work=21*
  1: 0x0106 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sl00" with entities [EventEntity, EventEntity]
  2: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             66 28 80 F8  FF FF 7F F8 FF FF 7F 74      f(.........t
0120: 6C 62 30 00                                       lb0.            
```

#### Opcodes

```
  0: 0x0114 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=27*
  1: 0x0123 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0124   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:             66 28 80 F8  FF FF 7F F8 FF FF 7F 74      f(.........t
0130: 6C 62 31 00                                       lb1.            
```

#### Opcodes

```
  0: 0x0124 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=27*
  1: 0x0133 [0x00] END_REQSTACK()
```
