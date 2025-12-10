# 17195780 - Garmatur the Merciless

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 464 bytes                   |
| Total Events     | 18                          |
| References Count | 22                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [225](#event-225)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351)   | 0x0008       |     65 |             11 |
| [65535.2](#event-655352)   | 0x0049       |      6 |              2 |
| [226](#event-226)          | 0x004F       |      7 |              2 |
| [227](#event-227)          | 0x0056       |      7 |              2 |
| [65535.3](#event-655353)   | 0x005D       |      7 |              3 |
| [65535.4](#event-655354)   | 0x0064       |      7 |              3 |
| [65535.5](#event-655355)   | 0x006B       |     16 |              2 |
| [65535.6](#event-655356)   | 0x007B       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0089       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0099       |     14 |              2 |
| [65535.9](#event-655359)   | 0x00A7       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00B7       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00C5       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00D5       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00E3       |     15 |              5 |
| [65535.14](#event-6553514) | 0x00F2       |     44 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x000A      |          10 |
|       2 | 0x006E      |         110 |
|       3 | 0x0001      |           1 |
|       4 | 0x0337      |         823 |
|       5 | 0x0336      |         822 |
|       6 | 0x000D      |          13 |
|       7 | 0x39EBF     |      237247 |
|       8 | 0xFFFA9A43  |  4294613571 |
|       9 | 0x4E38      |       20024 |
|      10 | 0x39D76     |      236918 |
|      11 | 0xFFFAA298  |  4294615704 |
|      12 | 0x4F63      |       20323 |
|      13 | 0x39C42     |      236610 |
|      14 | 0xFFFAB004  |  4294619140 |
|      15 | 0x5119      |       20761 |
|      16 | 0x39EB7     |      237239 |
|      17 | 0xFFFAC9D6  |  4294625750 |
|      18 | 0x51BE      |       20926 |
|      19 | 0x3A2BF     |      238271 |
|      20 | 0xFFFB0397  |  4294640535 |
|      21 | 0x4E1F      |       19999 |

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

### Event 225

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 65 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          03 00 00 00 80 02 00 00          ........
0010: 00 80 00 48 00 1C 01 80  C4 01 00 80 F8 FF FF 7F  ...H............
0020: FD 62 06 01 1C 02 80 C4  01 00 80 F8 FF FF 7F FD  .b..............
0030: 62 06 01 1C 02 80 C4 01  00 80 F8 FF FF 7F FD 62  b..............b
0040: 06 01 1C 02 80 01 0D 00  00                       .........       
```

#### Opcodes

```
  0: 0x0008 [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x000D [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0048
  2: 0x0015 [0x1C] WAIT(10* ticks)
  3: 0x0018 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=17): EventEntity casts magic 0* on Kupofried (ID: 17195773/0x010662FD)
  4: 0x0024 [0x1C] WAIT(110* ticks)
  5: 0x0027 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=17): EventEntity casts magic 0* on Kupofried (ID: 17195773/0x010662FD)
  6: 0x0033 [0x1C] WAIT(110* ticks)
  7: 0x0036 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=17): EventEntity casts magic 0* on Kupofried (ID: 17195773/0x010662FD)
  8: 0x0042 [0x1C] WAIT(110* ticks)
  9: 0x0045 [0x01] GOTO 0x000D
 10: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0049  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             03 00 00 03 80 00              ...... 
```

#### Opcodes

```
  0: 0x0049 [0x03] ExtData[1]->WorkLocal[0] = 1*
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 226

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               92                 .
0050: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x004F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 227

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0056  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0056 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005D  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         AB 03 AC               ...
0060: 01 03 80 00                                       ....            
```

#### Opcodes

```
  0: 0x005D [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x005F [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             AC 01 00 80  AB 04 00                     .......     
```

#### Opcodes

```
  0: 0x0064 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x0068 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   5B 04 80 F8 FF             [....
0070: FF 7F F8 FF FF 7F 77 61  72 30 00                 ......war0.     
```

#### Opcodes

```
  0: 0x006B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "war0" with entities [EventEntity, EventEntity], work=823*
  1: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   53 F8 FF FF 7F             S....
0080: F8 FF FF 7F 77 61 72 30  00                       ....war0.       
```

#### Opcodes

```
  0: 0x007B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "war0" with entities [EventEntity, EventEntity]
  1: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             5B 04 80 F8 FF FF 7F           [......
0090: F8 FF FF 7F 65 73 63 30  00                       ....esc0.       
```

#### Opcodes

```
  0: 0x0089 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "esc0" with entities [EventEntity, EventEntity], work=823*
  1: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             53 F8 FF FF 7F F8 FF           S......
00A0: FF 7F 65 73 63 30 00                              ..esc0.         
```

#### Opcodes

```
  0: 0x0099 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "esc0" with entities [EventEntity, EventEntity]
  1: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      5B  05 80 F8 FF FF 7F F8 FF         [........
00B0: FF 7F 74 6C 6B 30 00                              ..tlk0.         
```

#### Opcodes

```
  0: 0x00A7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=822*
  1: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00C0: 74 6C 6B 30 00                                    tlk0.           
```

#### Opcodes

```
  0: 0x00B7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                5B 05 80  F8 FF FF 7F F8 FF FF 7F       [..........
00D0: 74 6C 6B 31 00                                    tlk1.           
```

#### Opcodes

```
  0: 0x00C5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=822*
  1: 0x00D4 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                53 F8 FF  FF 7F F8 FF FF 7F 74 6C       S........tl
00E0: 6B 31 00                                          k1.             
```

#### Opcodes

```
  0: 0x00D5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          32 06 80 1F 00  07 80 08 80 09 80 1F 01     2............
00F0: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x00E3 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00E6 [0x1F] MOVE_ENTITY: EventEntity moves to X=237.247*, Z=-353.725*, Y=20.024*
  2: 0x00EE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00F1 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F2   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:       32 06 80 5A 00 0A  80 0B 80 0C 80 5A 01 5A    2..Z.......Z.Z
0100: 00 0D 80 0E 80 0F 80 5A  01 5A 00 10 80 11 80 12  .......Z.Z......
0110: 80 5A 01 5A 00 13 80 14  80 15 80 5A 01 00        .Z.Z.......Z..  
```

#### Opcodes

```
  0: 0x00F2 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00F5 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=236.918*, Z=-351.592*, Y=20.323*
  2: 0x00FD [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x00FF [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=236.610*, Z=-348.156*, Y=20.761*
  4: 0x0107 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  5: 0x0109 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=237.239*, Z=-341.546*, Y=20.926*
  6: 0x0111 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  7: 0x0113 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=238.271*, Z=-326.761*, Y=19.999*
  8: 0x011B [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  9: 0x011D [0x00] END_REQSTACK()
```
