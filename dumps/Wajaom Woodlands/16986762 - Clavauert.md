# 16986762 - Clavauert

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Wajaom Woodlands (ID: 51) |
| Block Size       | 760 bytes                 |
| Total Events     | 24                        |
| References Count | 27                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      9 |              3 |
| [65535.2](#event-655352)   | 0x000A       |     21 |              5 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              4 |
| [65535.4](#event-655354)   | 0x002F       |     16 |              4 |
| [65535.5](#event-655355)   | 0x003F       |     21 |              5 |
| [513](#event-513)          | 0x0054       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0055       |     10 |              2 |
| [65535.7](#event-655357)   | 0x005F       |      8 |              4 |
| [65535.8](#event-655358)   | 0x0067       |     16 |              4 |
| [65535.9](#event-655359)   | 0x0077       |     27 |              5 |
| [65535.10](#event-6553510) | 0x0092       |     62 |             12 |
| [65535.11](#event-6553511) | 0x00D0       |     27 |              3 |
| [65535.12](#event-6553512) | 0x00EB       |     32 |              4 |
| [65535.13](#event-6553513) | 0x010B       |     29 |              3 |
| [65535.14](#event-6553514) | 0x0128       |     16 |              4 |
| [65535.15](#event-6553515) | 0x0138       |     50 |             10 |
| [65535.16](#event-6553516) | 0x016A       |     37 |              7 |
| [65535.17](#event-6553517) | 0x018F       |     16 |              4 |
| [65535.18](#event-6553518) | 0x019F       |     16 |              4 |
| [65535.19](#event-6553519) | 0x01AF       |     29 |              3 |
| [65535.20](#event-6553520) | 0x01CC       |     29 |              3 |
| [65535.21](#event-6553521) | 0x01E9       |     50 |             10 |
| [20](#event-20)            | 0x021B       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0004      |           4 |
|       1 | 0x00B4      |         180 |
|       2 | 0x0024      |          36 |
|       3 | 0x0078      |         120 |
|       4 | 0x0010      |          16 |
|       5 | 0x001A      |          26 |
|       6 | 0x0050      |          80 |
|       7 | 0xA5A82     |      678530 |
|       8 | 0x31FA7     |      204711 |
|       9 | 0xFFFFC1AB  |  4294951339 |
|      10 | 0x0400      |        1024 |
|      11 | 0x000D      |          13 |
|      12 | 0x005A      |          90 |
|      13 | 0x003C      |          60 |
|      14 | 0x0000      |           0 |
|      15 | 0xFFFFFED4  |  4294966996 |
|      16 | 0x00C8      |         200 |
|      17 | 0x05DC      |        1500 |
|      18 | 0x03E8      |        1000 |
|      19 | 0x000A      |          10 |
|      20 | 0x001D      |          29 |
|      21 | 0x0015      |          21 |
|      22 | 0x0600      |        1536 |
|      23 | 0x09C4      |        2500 |
|      24 | 0xFFFFFC00  |  4294966272 |
|      25 | 0x0020      |          32 |
|      26 | 0x0014      |          20 |

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
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 2F 00 F8 FF FF  7F 00                     "./......      
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0009 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000A   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                6E F8 FF FF 7F 00            n.....
0010: 80 99 F8 FF FF 7F 99 F8  FF FF 7F 1C 01 80 00     ............... 
```

#### Opcodes

```
  0: 0x000A [0x6E] EventEntity uses emote 4*
  1: 0x0011 [0x99] Wait for EventEntity animation to complete
  2: 0x0016 [0x99] Wait for EventEntity animation to complete
  3: 0x001B [0x1C] WAIT(180* ticks)
  4: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               6E                 n
0020: F8 FF FF 7F 02 80 99 F8  FF FF 7F 1C 03 80 00     ............... 
```

#### Opcodes

```
  0: 0x001F [0x6E] EventEntity uses emote 36*
  1: 0x0026 [0x99] Wait for EventEntity animation to complete
  2: 0x002B [0x1C] WAIT(120* ticks)
  3: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               6E                 n
0030: F8 FF FF 7F 04 80 99 F8  FF FF 7F 1C 03 80 00     ............... 
```

#### Opcodes

```
  0: 0x002F [0x6E] EventEntity uses emote 16*
  1: 0x0036 [0x99] Wait for EventEntity animation to complete
  2: 0x003B [0x1C] WAIT(120* ticks)
  3: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               6E                 n
0040: F8 FF FF 7F 05 80 99 F8  FF FF 7F 99 F8 FF FF 7F  ................
0050: 1C 06 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003F [0x6E] EventEntity uses emote 26*
  1: 0x0046 [0x99] Wait for EventEntity animation to complete
  2: 0x004B [0x99] Wait for EventEntity animation to complete
  3: 0x0050 [0x1C] WAIT(80* ticks)
  4: 0x0053 [0x00] END_REQSTACK()
```

### Event 513

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0054  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             00                                        .           
```

#### Opcodes

```
  0: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                37 07 80  08 80 09 80 0A 80 00          7......... 
```

#### Opcodes

```
  0: 0x0055 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=678.530*, z=204.711*, y=-15.957*, direction=90.0°*
  1: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005F  |
| Data Size    | 8 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               1E                 .
0060: F0 FF FF 7F 6F 70 00                              ....op.         
```

#### Opcodes

```
  0: 0x005F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0064 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0065 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      6E  F8 FF FF 7F 0B 80 99 F8         n........
0070: FF FF 7F 1C 0C 80 00                              .......         
```

#### Opcodes

```
  0: 0x0067 [0x6E] EventEntity uses emote 13*
  1: 0x006E [0x99] Wait for EventEntity animation to complete
  2: 0x0073 [0x1C] WAIT(90* ticks)
  3: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 27 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      1C  0D 80 79 02 F8 FF FF 7F         ...y.....
0080: 0E 80 0F 80 1C 0C 80 79  02 F8 FF FF 7F 10 80 10  .......y........
0090: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0077 [0x1C] WAIT(60* ticks)
  1: 0x007A [0x79] EventEntity looks at Unknown NPC (ID: 2148499470/0x800F800E) (Direct axis set)
  2: 0x0084 [0x1C] WAIT(90* ticks)
  3: 0x0087 [0x79] EventEntity looks at Unknown NPC (ID: 2148565008/0x80108010) (Direct axis set)
  4: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 62 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       3B F8 FF FF 7F 00  00 01 00 02 00 3A F8 FF    ;..........:..
00A0: FF 7F 03 00 17 04 00 03  00 11 80 16 05 00 03 00  ................
00B0: 11 80 07 00 00 04 00 07  01 00 05 00 08 02 00 12  ................
00C0: 80 32 0B 80 1F 00 00 00  01 00 02 00 1F 01 6F 00  .2............o.
```

#### Opcodes

```
  0: 0x0092 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x009D [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[3])
  2: 0x00A4 [0x17] ExtData[1]->WorkLocal[4] = cos(ExtData[1]->WorkLocal[3]) * 1500*
  3: 0x00AB [0x16] ExtData[1]->WorkLocal[5] = sin(ExtData[1]->WorkLocal[3]) * 1500*
  4: 0x00B2 [0x07] ExtData[1]->WorkLocal[0] += ExtData[1]->WorkLocal[4]
  5: 0x00B7 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
  6: 0x00BC [0x08] ExtData[1]->WorkLocal[2] -= 1000*
  7: 0x00C1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  8: 0x00C4 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2]
  9: 0x00CC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 10: 0x00CE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D0   |
| Data Size    | 27 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 2C F8 FF FF 7F F8 FF FF  7F 63 6F 72 70 53 F8 FF  ,........corpS..
00E0: FF 7F F8 FF FF 7F 63 6F  72 70 00                 ......corp.     
```

#### Opcodes

```
  0: 0x00D0 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [EventEntity, EventEntity]
  1: 0x00DD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "corp" with entities [EventEntity, EventEntity]
  2: 0x00EA [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EB   |
| Data Size    | 32 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                   1C 13 80 66 14             ...f.
00F0: 80 F8 FF FF 7F F8 FF FF  7F 73 68 61 30 53 F8 FF  .........sha0S..
0100: FF 7F F8 FF FF 7F 73 68  61 30 00                 ......sha0.     
```

#### Opcodes

```
  0: 0x00EB [0x1C] WAIT(10* ticks)
  1: 0x00EE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  2: 0x00FD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  3: 0x010A [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010B   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                   66 14 80 F8 FF             f....
0110: FF 7F F8 FF FF 7F 73 68  61 31 53 F8 FF FF 7F F8  ......sha1S.....
0120: FF FF 7F 73 68 61 31 00                           ...sha1.        
```

#### Opcodes

```
  0: 0x010B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=29*
  1: 0x011A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  2: 0x0127 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0128   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                          6E F8 FF FF 7F 15 80 99          n.......
0130: F8 FF FF 7F 1C 0C 80 00                           ........        
```

#### Opcodes

```
  0: 0x0128 [0x6E] EventEntity uses emote 21*
  1: 0x012F [0x99] Wait for EventEntity animation to complete
  2: 0x0134 [0x1C] WAIT(90* ticks)
  3: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0138   |
| Data Size    | 50 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          3B F8 FF FF 7F 00 00 01          ;.......
0140: 00 02 00 17 04 00 16 80  17 80 16 05 00 16 80 17  ................
0150: 80 07 00 00 04 00 07 01  00 05 00 32 0B 80 1F 00  ...........2....
0160: 00 00 01 00 02 00 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0138 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x0143 [0x17] ExtData[1]->WorkLocal[4] = cos(1536*) * 2500*
  2: 0x014A [0x16] ExtData[1]->WorkLocal[5] = sin(1536*) * 2500*
  3: 0x0151 [0x07] ExtData[1]->WorkLocal[0] += ExtData[1]->WorkLocal[4]
  4: 0x0156 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
  5: 0x015B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  6: 0x015E [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2]
  7: 0x0166 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0168 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x0169 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016A   |
| Data Size    | 37 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                79 02 F8 FF FF 7F            y.....
0170: 0E 80 0A 80 1C 0C 80 7B  F8 FF FF 7F 79 02 F8 FF  .......{....y...
0180: FF 7F 0E 80 18 80 1C 0C  80 7B F8 FF FF 7F 00     .........{..... 
```

#### Opcodes

```
  0: 0x016A [0x79] EventEntity looks at Unknown NPC (ID: 2148171790/0x800A800E) (Direct axis set)
  1: 0x0174 [0x1C] WAIT(90* ticks)
  2: 0x0177 [0x7B] EventEntity stops talking
  3: 0x017C [0x79] EventEntity looks at Unknown NPC (ID: 2149089294/0x8018800E) (Direct axis set)
  4: 0x0186 [0x1C] WAIT(90* ticks)
  5: 0x0189 [0x7B] EventEntity stops talking
  6: 0x018E [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018F   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                               6E                 n
0190: F8 FF FF 7F 19 80 99 F8  FF FF 7F 1C 03 80 00     ............... 
```

#### Opcodes

```
  0: 0x018F [0x6E] EventEntity uses emote 32*
  1: 0x0196 [0x99] Wait for EventEntity animation to complete
  2: 0x019B [0x1C] WAIT(120* ticks)
  3: 0x019E [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019F   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                               6E                 n
01A0: F8 FF FF 7F 1A 80 99 F8  FF FF 7F 1C 0C 80 00     ............... 
```

#### Opcodes

```
  0: 0x019F [0x6E] EventEntity uses emote 20*
  1: 0x01A6 [0x99] Wait for EventEntity animation to complete
  2: 0x01AB [0x1C] WAIT(90* ticks)
  3: 0x01AE [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01AF   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                               66                 f
01B0: 14 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 53 F8  ..........tlk0S.
01C0: FF FF 7F F8 FF FF 7F 74  6C 6B 30 00              .......tlk0.    
```

#### Opcodes

```
  0: 0x01AF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x01BE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x01CB [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01CC   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                      66 14 80 F8              f...
01D0: FF FF 7F F8 FF FF 7F 74  6C 6B 31 53 F8 FF FF 7F  .......tlk1S....
01E0: F8 FF FF 7F 74 6C 6B 31  00                       ....tlk1.       
```

#### Opcodes

```
  0: 0x01CC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x01DB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x01E8 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E9   |
| Data Size    | 50 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                             3B F8 FF FF 7F 00 00           ;......
01F0: 01 00 02 00 17 04 00 16  80 17 80 16 05 00 16 80  ................
0200: 17 80 07 00 00 04 00 07  01 00 05 00 32 0B 80 1F  ............2...
0210: 00 00 00 01 00 02 00 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x01E9 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x01F4 [0x17] ExtData[1]->WorkLocal[4] = cos(1536*) * 2500*
  2: 0x01FB [0x16] ExtData[1]->WorkLocal[5] = sin(1536*) * 2500*
  3: 0x0202 [0x07] ExtData[1]->WorkLocal[0] += ExtData[1]->WorkLocal[4]
  4: 0x0207 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
  5: 0x020C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  6: 0x020F [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[1], Y=ExtData[1]->WorkLocal[2]
  7: 0x0217 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0219 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x021A [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x021B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                                   00                         .    
```

#### Opcodes

```
  0: 0x021B [0x00] END_REQSTACK()
```
