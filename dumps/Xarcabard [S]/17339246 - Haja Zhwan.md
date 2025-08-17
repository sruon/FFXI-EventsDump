# 17339246 - Haja Zhwan

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 584 bytes               |
| Total Events     | 19                      |
| References Count | 40                      |

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
| [65535.8](#event-655358)   | 0x0044       |     20 |              5 |
| [65535.9](#event-655359)   | 0x0058       |     13 |              3 |
| [65535.10](#event-6553510) | 0x0065       |     45 |             10 |
| [65535.11](#event-6553511) | 0x0092       |     52 |              9 |
| [65535.12](#event-6553512) | 0x00C6       |     20 |              5 |
| [65535.13](#event-6553513) | 0x00DA       |     81 |             18 |
| [21](#event-21)            | 0x012B       |      1 |              1 |
| [22](#event-22)            | 0x012C       |      1 |              1 |
| [41](#event-41)            | 0x012D       |     10 |              3 |
| [65535.14](#event-6553514) | 0x0137       |     14 |              4 |
| [65535.15](#event-6553515) | 0x0145       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0010      |          16 |
|       4 | 0xE918      |       59672 |
|       5 | 0xFFFCB221  |  4294750753 |
|       6 | 0xFFFFA24A  |  4294943306 |
|       7 | 0x001A      |          26 |
|       8 | 0xDE1B      |       56859 |
|       9 | 0xFFFCB39F  |  4294751135 |
|      10 | 0xFFFFA2C9  |  4294943433 |
|      11 | 0xD49B      |       54427 |
|      12 | 0xFFFCB36D  |  4294751085 |
|      13 | 0xFFFFA34A  |  4294943562 |
|      14 | 0x052B      |        1323 |
|      15 | 0x000D      |          13 |
|      16 | 0xD078      |       53368 |
|      17 | 0xFFFCAF75  |  4294750069 |
|      18 | 0xFFFFA3C7  |  4294943687 |
|      19 | 0x05FA      |        1530 |
|      20 | 0xE1CD      |       57805 |
|      21 | 0xFFFCB3B0  |  4294751152 |
|      22 | 0xFFFFA29C  |  4294943388 |
|      23 | 0x0028      |          40 |
|      24 | 0xCA44      |       51780 |
|      25 | 0xFFFCA538  |  4294747448 |
|      26 | 0xFFFFA49A  |  4294943898 |
|      27 | 0xD440      |       54336 |
|      28 | 0xFFFC90F6  |  4294742262 |
|      29 | 0xFFFFA423  |  4294943779 |
|      30 | 0xE883      |       59523 |
|      31 | 0xFFFC8578  |  4294739320 |
|      32 | 0xFFFFA3CA  |  4294943690 |
|      33 | 0x003C      |          60 |
|      34 | 0xFAF5      |       64245 |
|      35 | 0xFFFCA416  |  4294747158 |
|      36 | 0xFFFFA233  |  4294943283 |
|      37 | 0xFFFDD556  |  4294825302 |
|      38 | 0xFFFFF5DA  |  4294964698 |
|      39 | 0xFFFFC504  |  4294952196 |

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

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             59 04 F8 FF  FF 7F 03 80 1F 00 04 80      Y...........
0050: 05 80 06 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0044 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 16* * 0.1
  1: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=59.672*, Z=-216.543*, Y=-23.990*
  2: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          6E F8 FF FF 7F 07 80 99          n.......
0060: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0058 [0x6E] EventEntity uses emote 26*
  1: 0x005F [0x99] Wait for EventEntity animation to complete
  2: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 45 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                59 04 F8  FF FF 7F 03 80 1F 00 08       Y..........
0070: 80 09 80 0A 80 1F 01 1F  00 0B 80 0C 80 0D 80 1F  ................
0080: 01 6F 4A F8 FF FF 7F 6A  93 08 01 6F 76 F8 FF FF  .oJ....j...ov...
0090: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0065 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 16* * 0.1
  1: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=56.859*, Z=-216.161*, Y=-23.863*
  2: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0077 [0x1F] MOVE_ENTITY: EventEntity moves to X=54.427*, Z=-216.211*, Y=-23.734*
  4: 0x007F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0081 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0082 [0x4A] EventEntity looks at Kayeel-Payeel (ID: 17339242/0x0108936A)
  7: 0x008B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x008C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  9: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 52 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       6E F8 FF FF 7F 0E  80 99 F8 FF FF 7F 7B F8    n...........{.
00A0: FF FF 7F 59 04 F8 FF FF  7F 0F 80 1F 00 10 80 11  ...Y............
00B0: 80 12 80 1F 01 6F 5B 13  80 F8 FF FF 7F F8 FF FF  .....o[.........
00C0: 7F 6B 65 6E 30 00                                 .ken0.          
```

#### Opcodes

```
  0: 0x0092 [0x6E] EventEntity uses emote 1323*
  1: 0x0099 [0x99] Wait for EventEntity animation to complete
  2: 0x009E [0x7B] EventEntity stops talking
  3: 0x00A3 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  4: 0x00AB [0x1F] MOVE_ENTITY: EventEntity moves to X=53.368*, Z=-217.227*, Y=-23.609*
  5: 0x00B3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x00B5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00B6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ken0" with entities [EventEntity, EventEntity], work=1530*
  8: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   59 04  F8 FF FF 7F 0F 80 1F 00        Y.........
00D0: 14 80 15 80 16 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x00C6 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x00CE [0x1F] MOVE_ENTITY: EventEntity moves to X=57.805*, Z=-216.144*, Y=-23.908*
  2: 0x00D6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00D9 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DA   |
| Data Size    | 81 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                59 04 F8 FF FF 7F            Y.....
00E0: 17 80 1F 00 18 80 19 80  1A 80 1F 01 1F 00 1B 80  ................
00F0: 1C 80 1D 80 1F 01 1F 00  1E 80 1F 80 20 80 1F 01  ............ ...
0100: 6F 1C 21 80 4A F8 FF FF  7F 56 93 08 01 6F 76 F8  o.!.J....V...ov.
0110: FF FF 7F 1C 21 80 1F 00  22 80 23 80 24 80 1F 01  ....!...".#.$...
0120: 6F 4A F8 FF FF 7F 56 93  08 01 00                 oJ....V....     
```

#### Opcodes

```
  0: 0x00DA [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 40* * 0.1
  1: 0x00E2 [0x1F] MOVE_ENTITY: EventEntity moves to X=51.780*, Z=-219.848*, Y=-23.398*
  2: 0x00EA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00EC [0x1F] MOVE_ENTITY: EventEntity moves to X=54.336*, Z=-225.034*, Y=-23.517*
  4: 0x00F4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00F6 [0x1F] MOVE_ENTITY: EventEntity moves to X=59.523*, Z=-227.976*, Y=-23.606*
  6: 0x00FE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0100 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0101 [0x1C] WAIT(60* ticks)
  9: 0x0104 [0x4A] EventEntity looks at Lilisette (ID: 17339222/0x01089356)
 10: 0x010D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x010E [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
 12: 0x0113 [0x1C] WAIT(60* ticks)
 13: 0x0116 [0x1F] MOVE_ENTITY: EventEntity moves to X=64.245*, Z=-220.138*, Y=-24.013*
 14: 0x011E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 15: 0x0120 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 16: 0x0121 [0x4A] EventEntity looks at Lilisette (ID: 17339222/0x01089356)
 17: 0x012A [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x012B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   00                         .    
```

#### Opcodes

```
  0: 0x012B [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x012C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                      00                       .   
```

#### Opcodes

```
  0: 0x012C [0x00] END_REQSTACK()
```

### Event 41

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012D   |
| Data Size    | 10 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                         92 01 F8               ...
0130: FF FF 7F C0 01 80 00                              .......         
```

#### Opcodes

```
  0: 0x012D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0133 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0136 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0137   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                      32  17 80 1F 00 25 80 26 80         2....%.&.
0140: 27 80 1F 01 00                                    '....           
```

#### Opcodes

```
  0: 0x0137 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x013A [0x1F] MOVE_ENTITY: EventEntity moves to X=-141.994*, Z=-2.598*, Y=-15.100*
  2: 0x0142 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0144 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0145  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                C0 00 80  00                            ....       
```

#### Opcodes

```
  0: 0x0145 [0xC0] EventEntity->Render.Flags3 &= ~0x1000 // Clear bit 12 (from 0*)
  1: 0x0148 [0x00] END_REQSTACK()
```
