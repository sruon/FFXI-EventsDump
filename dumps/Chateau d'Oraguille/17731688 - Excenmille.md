# 17731688 - Excenmille

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 644 bytes                     |
| Total Events     | 30                            |
| References Count | 18                            |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     16 |              2 |
| [65535.6](#event-655356)   | 0x004D       |     14 |              2 |
| [65535.7](#event-655357)   | 0x005B       |     16 |              2 |
| [65535.8](#event-655358)   | 0x006B       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0079       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0089       |     14 |              2 |
| [65535.11](#event-6553511) | 0x0097       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00A7       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00B5       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00C5       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00D3       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00E3       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00F1       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0101       |     14 |              2 |
| [65535.19](#event-6553519) | 0x010F       |     16 |              2 |
| [65535.20](#event-6553520) | 0x011F       |     14 |              2 |
| [65535.21](#event-6553521) | 0x012D       |      7 |              3 |
| [65535.22](#event-6553522) | 0x0134       |      7 |              3 |
| [598](#event-598)          | 0x013B       |      7 |              2 |
| [65535.23](#event-6553523) | 0x0142       |     25 |              7 |
| [65535.24](#event-6553524) | 0x015B       |     22 |              8 |
| [65535.25](#event-6553525) | 0x0171       |     28 |              9 |
| [604](#event-604)          | 0x018D       |      7 |              2 |
| [65535.26](#event-6553526) | 0x0194       |     15 |              5 |
| [65535.27](#event-6553527) | 0x01A3       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001D      |          29 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFFFA898  |  4294944920 |
|       5 | 0xFFFFF027  |  4294963239 |
|       6 | 0xFFFFA81F  |  4294944799 |
|       7 | 0xFFFFFEA6  |  4294966950 |
|       8 | 0xFFFFA935  |  4294945077 |
|       9 | 0xFFFFF5C9  |  4294964681 |
|      10 | 0xFFFFB0F4  |  4294947060 |
|      11 | 0xFFFFEF97  |  4294963095 |
|      12 | 0xFFFF6F3D  |  4294930237 |
|      13 | 0x1509A     |       86170 |
|      14 | 0xFFFFF15A  |  4294963546 |
|      15 | 0x3BDC2     |      245186 |
|      16 | 0x3B7D3     |      243667 |
|      17 | 0x003A      |          58 |

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
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31   f..........thk1
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 00      S........thk1. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               66                 f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00     ..........thk2. 
```

#### Opcodes

```
  0: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 00           ........thk2.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         66 00 80               f..
0040: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 00           ........tlk0.   
```

#### Opcodes

```
  0: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         53 F8 FF               S..
0050: FF 7F F8 FF FF 7F 74 6C  6B 30 00                 ......tlk0.     
```

#### Opcodes

```
  0: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   66 00 80 F8 FF             f....
0060: FF 7F F8 FF FF 7F 74 6C  6B 31 00                 ......tlk1.     
```

#### Opcodes

```
  0: 0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   53 F8 FF FF 7F             S....
0070: F8 FF FF 7F 74 6C 6B 31  00                       ....tlk1.       
```

#### Opcodes

```
  0: 0x006B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             66 00 80 F8 FF FF 7F           f......
0080: F8 FF FF 7F 74 77 61 30  00                       ....twa0.       
```

#### Opcodes

```
  0: 0x0079 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             53 F8 FF FF 7F F8 FF           S......
0090: FF 7F 74 77 61 30 00                              ..twa0.         
```

#### Opcodes

```
  0: 0x0089 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "twa0" with entities [EventEntity, EventEntity]
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      66  00 80 F8 FF FF 7F F8 FF         f........
00A0: FF 7F 74 77 61 31 00                              ..twa1.         
```

#### Opcodes

```
  0: 0x0097 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa1" with entities [EventEntity, EventEntity], work=29*
  1: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00B0: 74 77 61 31 00                                    twa1.           
```

#### Opcodes

```
  0: 0x00A7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "twa1" with entities [EventEntity, EventEntity]
  1: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
00C0: 74 77 62 30 00                                    twb0.           
```

#### Opcodes

```
  0: 0x00B5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twb0" with entities [EventEntity, EventEntity], work=29*
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                53 F8 FF  FF 7F F8 FF FF 7F 74 77       S........tw
00D0: 62 30 00                                          b0.             
```

#### Opcodes

```
  0: 0x00C5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "twb0" with entities [EventEntity, EventEntity]
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 77     f..........tw
00E0: 62 31 00                                          b1.             
```

#### Opcodes

```
  0: 0x00D3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twb1" with entities [EventEntity, EventEntity], work=29*
  1: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          53 F8 FF FF 7F  F8 FF FF 7F 74 77 62 31     S........twb1
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "twb1" with entities [EventEntity, EventEntity]
  1: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 73 68 61 30   f..........sha0
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00F1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    53 F8 FF FF 7F F8 FF  FF 7F 73 68 61 30 00      S........sha0. 
```

#### Opcodes

```
  0: 0x0101 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  1: 0x010E [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               66                 f
0110: 00 80 F8 FF FF 7F F8 FF  FF 7F 73 68 61 31 00     ..........sha1. 
```

#### Opcodes

```
  0: 0x010F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=29*
  1: 0x011E [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                               53                 S
0120: F8 FF FF 7F F8 FF FF 7F  73 68 61 31 00           ........sha1.   
```

#### Opcodes

```
  0: 0x011F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  1: 0x012C [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x012D  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                         AB 03 AC               ...
0130: 01 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x012D [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x012F [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0133 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0134  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:             AC 01 02 80  AB 04 00                     .......     
```

#### Opcodes

```
  0: 0x0134 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x0138 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x013A [0x00] END_REQSTACK()
```

### Event 598

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                   92 01 F8 FF FF             .....
0140: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x013B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0141 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0142   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:       32 03 80 1F 00 04  80 05 80 02 80 1F 01 1F    2.............
0150: 00 06 80 07 80 02 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x0142 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0145 [0x1F] MOVE_ENTITY: EventEntity moves to X=-22.376*, Z=-4.057*, Y=0.000*
  2: 0x014D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x014F [0x1F] MOVE_ENTITY: EventEntity moves to X=-22.497*, Z=-0.346*, Y=0.000*
  4: 0x0157 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0159 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x015A [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015B   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                   32 03 80 1F 00             2....
0160: 06 80 07 80 02 80 1F 01  6F 1E 66 90 0E 01 6F 70  ........o.f...op
0170: 00                                                .               
```

#### Opcodes

```
  0: 0x015B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x015E [0x1F] MOVE_ENTITY: EventEntity moves to X=-22.497*, Z=-0.346*, Y=0.000*
  2: 0x0166 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0168 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0169 [0x1E] EventEntity looks at Trion (ID: 17731686/0x010E9066) and starts talking
  5: 0x016E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x016F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0170 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0171   |
| Data Size    | 28 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:    32 03 80 1F 00 08 80  09 80 02 80 1F 01 6F 1F   2............o.
0180: 00 0A 80 0B 80 02 80 1F  01 6F 22 01 00           .........o"..   
```

#### Opcodes

```
  0: 0x0171 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0174 [0x1F] MOVE_ENTITY: EventEntity moves to X=-22.219*, Z=-2.615*, Y=0.000*
  2: 0x017C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x017E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x017F [0x1F] MOVE_ENTITY: EventEntity moves to X=-20.236*, Z=-4.201*, Y=0.000*
  5: 0x0187 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0189 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x018A [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  8: 0x018C [0x00] END_REQSTACK()
```

### Event 604

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x018D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                         92 01 F8               ...
0190: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x018D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0193 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0194   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:             32 03 80 1F  00 0C 80 0D 80 0E 80 1F      2...........
01A0: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0194 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0197 [0x1F] MOVE_ENTITY: EventEntity moves to X=-37.059*, Z=86.170*, Y=-3.750*
  2: 0x019F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01A1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01A2 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A3   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:          32 03 80 1F 00  0F 80 10 80 11 80 1F 01     2............
01B0: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x01A3 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01A6 [0x1F] MOVE_ENTITY: EventEntity moves to X=245.186*, Z=243.667*, Y=0.058*
  2: 0x01AE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01B0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01B1 [0x00] END_REQSTACK()
```
