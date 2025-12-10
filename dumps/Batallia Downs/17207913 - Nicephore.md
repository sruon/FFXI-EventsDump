# 17207913 - Nicephore

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Batallia Downs (ID: 105) |
| Block Size       | 424 bytes                |
| Total Events     | 21                       |
| References Count | 26                       |

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
| [504](#event-504)          | 0x0044       |      1 |              1 |
| [505](#event-505)          | 0x0045       |      1 |              1 |
| [506](#event-506)          | 0x0046       |      1 |              1 |
| [507](#event-507)          | 0x0047       |      1 |              1 |
| [508](#event-508)          | 0x0048       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0049       |     13 |              3 |
| [65535.9](#event-655359)   | 0x0056       |     13 |              3 |
| [65535.10](#event-6553510) | 0x0063       |     14 |              4 |
| [65535.11](#event-6553511) | 0x0071       |     14 |              4 |
| [65535.12](#event-6553512) | 0x007F       |     21 |              2 |
| [65535.13](#event-6553513) | 0x0094       |     21 |              2 |
| [65535.14](#event-6553514) | 0x00A9       |     33 |              5 |
| [65535.15](#event-6553515) | 0x00CA       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x052B      |        1323 |
|       4 | 0x0002      |           2 |
|       5 | 0x000D      |          13 |
|       6 | 0x512CA     |      332490 |
|       7 | 0xFFFCB86A  |  4294752362 |
|       8 | 0x1B8D      |        7053 |
|       9 | 0x0050      |          80 |
|      10 | 0x575C6     |      357830 |
|      11 | 0xFFFCD141  |  4294758721 |
|      12 | 0x1C48      |        7240 |
|      13 | 0x0003      |           3 |
|      14 | 0x000A      |          10 |
|      15 | 0x0038      |          56 |
|      16 | 0x000C      |          12 |
|      17 | 0x010E      |         270 |
|      18 | 0x001B      |          27 |
|      19 | 0x0004      |           4 |
|      20 | 0x00D2      |         210 |
|      21 | 0x001D      |          29 |
|      22 | 0x003C      |          60 |
|      23 | 0x157A4     |       87972 |
|      24 | 0xFFFF7AC0  |  4294933184 |
|      25 | 0x07CF      |        1999 |

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

### Event 504

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

### Event 505

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

### Event 506

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

### Event 507

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      00                                  .        
```

#### Opcodes

```
  0: 0x0047 [0x00] END_REQSTACK()
```

### Event 508

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          00                               .       
```

#### Opcodes

```
  0: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             6E F8 FF FF 7F 03 80           n......
0050: 99 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0049 [0x6E] EventEntity uses emote 1323*
  1: 0x0050 [0x99] Wait for EventEntity animation to complete
  2: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   6E F8  FF FF 7F 04 80 99 F8 FF        n.........
0060: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x0056 [0x6E] EventEntity uses emote 2*
  1: 0x005D [0x99] Wait for EventEntity animation to complete
  2: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          32 05 80 1F 00  06 80 07 80 08 80 1F 01     2............
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0063 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0066 [0x1F] MOVE_ENTITY: EventEntity moves to X=332.490*, Z=-214.934*, Y=7.053*
  2: 0x006E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    32 09 80 1F 00 0A 80  0B 80 0C 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0071 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  1: 0x0074 [0x1F] MOVE_ENTITY: EventEntity moves to X=357.830*, Z=-208.575*, Y=7.240*
  2: 0x007C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               B6                 .
0080: 0B 0D 80 0E 80 0F 80 10  80 10 80 10 80 10 80 11  ................
0090: 80 12 80 00                                       ....            
```

#### Opcodes

```
  0: 0x007F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=10*, head=56*, body=12*, hands=12*, legs=12*, feet=12*, main=270*, sub=27*)
  1: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             B6 0B 0D 80  13 80 10 80 10 80 10 80      ............
00A0: 10 80 10 80 14 80 00 80  00                       .........       
```

#### Opcodes

```
  0: 0x0094 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=4*, head=12*, body=12*, hands=12*, legs=12*, feet=12*, main=210*, sub=0*)
  1: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 33 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             66 15 80 69 92 06 01           f..i...
00B0: 69 92 06 01 73 69 74 31  1C 16 80 4A 69 92 06 01  i...sit1...Ji...
00C0: 5C 92 06 01 7B 69 92 06  01 00                    \...{i....      
```

#### Opcodes

```
  0: 0x00A9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sit1" with entities [Nicephore (ID: 17207913/0x01069269), Nicephore (ID: 17207913/0x01069269)], work=29*
  1: 0x00B8 [0x1C] WAIT(60* ticks)
  2: 0x00BB [0x4A] Nicephore (ID: 17207913/0x01069269) looks at Excenmille (ID: 17207900/0x0106925C)
  3: 0x00C4 [0x7B] Nicephore (ID: 17207913/0x01069269) stops talking
  4: 0x00C9 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                32 05 80 1F 00 17            2.....
00D0: 80 18 80 19 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x00CA [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00CD [0x1F] MOVE_ENTITY: EventEntity moves to X=87.972*, Z=-34.112*, Y=1.999*
  2: 0x00D5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00D8 [0x00] END_REQSTACK()
```
