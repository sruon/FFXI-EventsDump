# 17449504 - Routandeault

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Garlaige Citadel [S] (ID: 164) |
| Block Size       | 428 bytes                      |
| Total Events     | 12                             |
| References Count | 23                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [20](#event-20)          | 0x0001       |     45 |             11 |
| [65535.1](#event-655351) | 0x002E       |     35 |              9 |
| [65535.2](#event-655352) | 0x0051       |     35 |              9 |
| [33](#event-33)          | 0x0074       |      1 |              1 |
| [65535.3](#event-655353) | 0x0075       |     21 |              2 |
| [65535.4](#event-655354) | 0x008A       |     21 |              2 |
| [65535.5](#event-655355) | 0x009F       |     21 |              2 |
| [65535.6](#event-655356) | 0x00B4       |     13 |              3 |
| [65535.7](#event-655357) | 0x00C1       |     13 |              3 |
| [65535.8](#event-655358) | 0x00CE       |     15 |              5 |
| [65535.9](#event-655359) | 0x00DD       |     50 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0005      |           5 |
|       1 | 0x1E0A      |        7690 |
|       2 | 0x001E      |          30 |
|       3 | 0x0014      |          20 |
|       4 | 0x1E0B      |        7691 |
|       5 | 0x0028      |          40 |
|       6 | 0x000D      |          13 |
|       7 | 0x0003      |           3 |
|       8 | 0x0006      |           6 |
|       9 | 0x000C      |          12 |
|      10 | 0x00FB      |         251 |
|      11 | 0x001B      |          27 |
|      12 | 0x007C      |         124 |
|      13 | 0x0015      |          21 |
|      14 | 0x0000      |           0 |
|      15 | 0x0038      |          56 |
|      16 | 0x010E      |         270 |
|      17 | 0x002B      |          43 |
|      18 | 0x0002      |           2 |
|      19 | 0xFFFFD9FF  |  4294957567 |
|      20 | 0xFFFBB904  |  4294686980 |
|      21 | 0x019E      |         414 |
|      22 | 0x0516      |        1302 |

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

### Event 20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 45 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    6E 21 42 0A 01 00 80  99 21 42 0A 01 2B 21 42   n!B.....!B..+!B
0010: 0A 01 01 80 23 1C 02 80  6E 20 42 0A 01 03 80 99  ....#...n B.....
0020: 20 42 0A 01 2B 20 42 0A  01 04 80 23 21 00         B..+ B....#!.  
```

#### Opcodes

```
  0: 0x0001 [0x6E] Laurimaux (ID: 17449505/0x010A4221) uses emote 5*
  1: 0x0008 [0x99] Wait for Laurimaux (ID: 17449505/0x010A4221) animation to complete
  2: 0x000D [0x2B] Laurimaux (ID: 17449505/0x010A4221) [7690*]:
    → "Beastman Confederate or not, if they are going to attack, I wish they would just hurry up and get it over with! I'm sick of being afraid and waiting... I just want it all to be over!"
  3: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0015 [0x1C] WAIT(30* ticks)
  5: 0x0018 [0x6E] Routandeault (ID: 17449504/0x010A4220) uses emote 20*
  6: 0x001F [0x99] Wait for Routandeault (ID: 17449504/0x010A4220) animation to complete
  7: 0x0024 [0x2B] Routandeault (ID: 17449504/0x010A4220) [7691*]:
    → "Pull yourself together, man! You think you're the only one who's scared? I'm terrified! But if we give in to that fear and run now, we'll have no place left to go!"
  8: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002C [0x21] END_EVENT
 10: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            03 00                ..
0030: 00 25 10 03 02 00 27 10  03 01 00 26 10 03 03 00  .%....'....&....
0040: 28 10 32 05 80 1F 00 00  00 02 00 01 00 1F 01 6F  (.2............o
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x002E [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0033 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x0038 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x003D [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0042 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x004F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    03 00 00 25 10 03 02  00 27 10 03 01 00 26 10   ...%....'....&.
0060: 03 03 00 28 10 32 06 80  1F 00 00 00 02 00 01 00  ...(.2..........
0070: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0051 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0056 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x005B [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0060 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0065 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x0068 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0070 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0072 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0073 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0074  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             00                                        .           
```

#### Opcodes

```
  0: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                B6 0B 07  80 08 80 09 80 09 80 09       ...........
0080: 80 09 80 09 80 0A 80 0B  80 00                    ..........      
```

#### Opcodes

```
  0: 0x0075 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=6*, head=12*, body=12*, hands=12*, legs=12*, feet=12*, main=251*, sub=27*)
  1: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                B6 0B 07 80 08 80            ......
0090: 0C 80 0C 80 0D 80 0D 80  0D 80 0E 80 0E 80 00     ............... 
```

#### Opcodes

```
  0: 0x008A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=6*, head=124*, body=124*, hands=21*, legs=21*, feet=21*, main=0*, sub=0*)
  1: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               B6                 .
00A0: 0B 07 80 08 80 0F 80 09  80 09 80 09 80 09 80 10  ................
00B0: 80 0B 80 00                                       ....            
```

#### Opcodes

```
  0: 0x009F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=6*, head=56*, body=12*, hands=12*, legs=12*, feet=12*, main=270*, sub=27*)
  1: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             6E F8 FF FF  7F 11 80 99 F8 FF FF 7F      n...........
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00B4 [0x6E] EventEntity uses emote 43*
  1: 0x00BB [0x99] Wait for EventEntity animation to complete
  2: 0x00C0 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C1   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    6E F8 FF FF 7F 12 80  99 F8 FF FF 7F 00         n............  
```

#### Opcodes

```
  0: 0x00C1 [0x6E] EventEntity uses emote 2*
  1: 0x00C8 [0x99] Wait for EventEntity animation to complete
  2: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            32 05                2.
00D0: 80 1F 00 13 80 14 80 15  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x00CE [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00D1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-9.729*, Z=-280.316*, Y=0.414*
  2: 0x00D9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00DB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00DC [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 50 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         32 05 80               2..
00E0: 1F 00 13 80 14 80 15 80  1F 01 6F 4A 20 42 0A 01  ..........oJ B..
00F0: 45 42 0A 01 7B 20 42 0A  01 6F 76 20 42 0A 01 5B  EB..{ B..ov B..[
0100: 16 80 20 42 0A 01 20 42  0A 01 6C 62 74 30 00     .. B.. B..lbt0. 
```

#### Opcodes

```
  0: 0x00DD [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00E0 [0x1F] MOVE_ENTITY: EventEntity moves to X=-9.729*, Z=-280.316*, Y=0.414*
  2: 0x00E8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00EA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00EB [0x4A] Routandeault (ID: 17449504/0x010A4220) looks at D (ID: 17449541/0x010A4245)
  5: 0x00F4 [0x7B] Routandeault (ID: 17449504/0x010A4220) stops talking
  6: 0x00F9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00FA [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Routandeault (ID: 17449504/0x010A4220) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x00FF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "lbt0" with entities [Routandeault (ID: 17449504/0x010A4220), Routandeault (ID: 17449504/0x010A4220)], work=1302*
  9: 0x010E [0x00] END_REQSTACK()
```
