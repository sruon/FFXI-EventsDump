# 16883727 - Ondieulix

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 476 bytes                   |
| Total Events     | 13                          |
| References Count | 27                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [101](#event-101)        | 0x0001       |     28 |              5 |
| [107](#event-107)        | 0x001D       |      7 |              2 |
| [65535.1](#event-655351) | 0x0024       |     22 |              4 |
| [285](#event-285)        | 0x003A       |     49 |             11 |
| [286](#event-286)        | 0x006B       |     30 |              8 |
| [287](#event-287)        | 0x0089       |     30 |              8 |
| [288](#event-288)        | 0x00A7       |     49 |             11 |
| [514](#event-514)        | 0x00D8       |      1 |              1 |
| [65535.2](#event-655352) | 0x00D9       |     19 |              5 |
| [65535.3](#event-655353) | 0x00EC       |     11 |              2 |
| [516](#event-516)        | 0x00F7       |      1 |              1 |
| [559](#event-559)        | 0x00F8       |     50 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFBF40  |  4294950720 |
|       1 | 0x1DA23     |      121379 |
|       2 | 0xFFFF981C  |  4294940700 |
|       3 | 0x0EA4      |        3748 |
|       4 | 0x0D2E      |        3374 |
|       5 | 0x06CA      |        1738 |
|       6 | 0xFFFFDCE0  |  4294958304 |
|       7 | 0x049F      |        1183 |
|       8 | 0x2AF7      |       10999 |
|       9 | 0x0014      |          20 |
|      10 | 0x2AF8      |       11000 |
|      11 | 0x2AF9      |       11001 |
|      12 | 0x2AFA      |       11002 |
|      13 | 0x2AFB      |       11003 |
|      14 | 0x2AFC      |       11004 |
|      15 | 0x2AFD      |       11005 |
|      16 | 0x2AFE      |       11006 |
|      17 | 0x2AFF      |       11007 |
|      18 | 0x2B00      |       11008 |
|      19 | 0x000D      |          13 |
|      20 | 0x0568      |        1384 |
|      21 | 0x107BF     |       67519 |
|      22 | 0xFFFF9F3A  |  4294942522 |
|      23 | 0x2E14      |       11796 |
|      24 | 0x001B      |          27 |
|      25 | 0x003C      |          60 |
|      26 | 0x2E15      |       11797 |

## String References

- **10999**: You probably wonder why we have chosen to live our lives under the ground in these caves.
- **11000**: The roads leading to the old Marquisate capital have sunk to the bottom of the seas, and the surrounding meadows crawl with terrible beasts and remnants of the beastman armies.
- **11001**: It is amazing that our tiny patrol is even able to maintain the peace in this small corner of the island...
- **11002**: The sudden influx of visitors from Jeuno has left many of the safehold residents scared and confused. However, I welcome their presence as a blessing.
- **11003**: I do not wish to be tied to this cursed place for the rest of my life...
- **11004**: So you plan to wage a war against the Wyrmking and his minions? I apologize, but I fear the Tavnazian Patrol does not possess the manpower to assist you this time.
- **11005**: However, in your absence we shall ensure the safety of the remaining safehold residents. Good luck, <Player>.
- **11006**: Welcome home! We are all relieved to see you made it back unharmed.
- **11007**: How was your ride on the airship? I had heard stories of the flying machines, but I never thought I would have the opportunity to see one up close.
- **11008**: Perhaps some day I will be blessed with the opportunity to ride one as well...
- **11796**: I heard of your deeds from Tressia. Here is your reward.
- **11797**: We may need your help again someday. Thank you, <Player>.

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

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 22  01 37 00 80 01 80 02 80   ......".7......
0010: 03 80 79 00 F8 FF FF 7F  F0 FF FF 7F 00           ..y..........   
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  2: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-16.576*, z=121.379*, y=-26.596*, direction=329.4°*
  3: 0x0012 [0x79] EventEntity looks at LocalPlayer (Basic look)
  4: 0x001C [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         92 01 F8               ...
0020: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x001D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             22 00 79 00  0F A0 01 01 04 A0 01 01      ".y.........
0030: 37 04 80 05 80 06 80 07  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0024 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0026 [0x79] Ondieulix (ID: 16883727/0x0101A00F) looks at Prishe (ID: 16883716/0x0101A004) (Basic look)
  2: 0x0030 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=3.374*, z=1.738*, y=-8.992*, direction=104.0°*
  3: 0x0039 [0x00] END_REQSTACK()
```

### Event 285

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 49 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                1E F0 FF FF 7F 1D            ......
0040: 08 80 23 66 09 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0050: 6B 30 1D 0A 80 23 66 09  80 F8 FF FF 7F F8 FF FF  k0...#f.........
0060: 7F 74 6C 6B 31 1D 0B 80  23 21 00                 .tlk1...#!.     
```

#### Opcodes

```
  0: 0x003A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=10999*)
    → "You probably wonder why we have chosen to live our lives under the ground in these caves."
  2: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0043 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=11000*)
    → "The roads leading to the old Marquisate capital have sunk to the bottom of the seas, and the surrounding meadows crawl with terrible beasts and remnants of the beastman armies."
  5: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0056 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  7: 0x0065 [0x1D] PRINT_EVENT_MESSAGE(message_id=11001*)
    → "It is amazing that our tiny patrol is even able to maintain the peace in this small corner of the island..."
  8: 0x0068 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0069 [0x21] END_EVENT
 10: 0x006A [0x00] END_REQSTACK()
```

### Event 286

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   1E F0 FF FF 7F             .....
0070: 1D 0C 80 23 66 09 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
0080: 6C 6B 30 1D 0D 80 23 21  00                       lk0...#!.       
```

#### Opcodes

```
  0: 0x006B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=11002*)
    → "The sudden influx of visitors from Jeuno has left many of the safehold residents scared and confused. However, I welcome their presence as a blessing."
  2: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0074 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0083 [0x1D] PRINT_EVENT_MESSAGE(message_id=11003*)
    → "I do not wish to be tied to this cursed place for the rest of my life..."
  5: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0087 [0x21] END_EVENT
  7: 0x0088 [0x00] END_REQSTACK()
```

### Event 287

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             1E F0 FF FF 7F 1D 0E           .......
0090: 80 23 66 09 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#f..........tlk
00A0: 30 1D 0F 80 23 21 00                              0...#!.         
```

#### Opcodes

```
  0: 0x0089 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x008E [0x1D] PRINT_EVENT_MESSAGE(message_id=11004*)
    → "So you plan to wage a war against the Wyrmking and his minions? I apologize, but I fear the Tavnazian Patrol does not possess the manpower to assist you this time."
  2: 0x0091 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0092 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x00A1 [0x1D] PRINT_EVENT_MESSAGE(message_id=11005*)
    → "However, in your absence we shall ensure the safety of the remaining safehold residents. Good luck, <Player>."
  5: 0x00A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A5 [0x21] END_EVENT
  7: 0x00A6 [0x00] END_REQSTACK()
```

### Event 288

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 49 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      1E  F0 FF FF 7F 1D 10 80 23         ........#
00B0: 66 09 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
00C0: 11 80 23 66 09 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
00D0: 6B 31 1D 12 80 23 21 00                           k1...#!.        
```

#### Opcodes

```
  0: 0x00A7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00AC [0x1D] PRINT_EVENT_MESSAGE(message_id=11006*)
    → "Welcome home! We are all relieved to see you made it back unharmed."
  2: 0x00AF [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x00BF [0x1D] PRINT_EVENT_MESSAGE(message_id=11007*)
    → "How was your ride on the airship? I had heard stories of the flying machines, but I never thought I would have the opportunity to see one up close."
  5: 0x00C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00C3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  7: 0x00D2 [0x1D] PRINT_EVENT_MESSAGE(message_id=11008*)
    → "Perhaps some day I will be blessed with the opportunity to ride one as well..."
  8: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00D6 [0x21] END_EVENT
 10: 0x00D7 [0x00] END_REQSTACK()
```

### Event 514

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                          00                               .       
```

#### Opcodes

```
  0: 0x00D8 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D9   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                             32 13 80 1F 00 14 80           2......
00E0: 15 80 16 80 1F 01 1E 0E  A0 01 01 00              ............    
```

#### Opcodes

```
  0: 0x00D9 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00DC [0x1F] MOVE_ENTITY: EventEntity moves to X=1.384*, Z=67.519*, Y=-24.774*
  2: 0x00E4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E6 [0x1E] EventEntity looks at Parelbriaux (ID: 16883726/0x0101A00E) and starts talking
  4: 0x00EB [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EC   |
| Data Size    | 11 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      79 00 0F A0              y...
00F0: 01 01 0E A0 01 01 00                              .......         
```

#### Opcodes

```
  0: 0x00EC [0x79] Ondieulix (ID: 16883727/0x0101A00F) looks at Parelbriaux (ID: 16883726/0x0101A00E) (Basic look)
  1: 0x00F6 [0x00] END_REQSTACK()
```

### Event 516

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F7  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      00                                  .        
```

#### Opcodes

```
  0: 0x00F7 [0x00] END_REQSTACK()
```

### Event 559

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F8   |
| Data Size    | 50 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                          1E F0 FF FF 7F 6F 70 1D          .....op.
0100: 17 80 23 66 18 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0110: 62 30 1C 19 80 1D 1A 80  23 66 18 80 F8 FF FF 7F  b0......#f......
0120: F8 FF FF 7F 74 6C 62 31  21 00                    ....tlb1!.      
```

#### Opcodes

```
  0: 0x00F8 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00FD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00FE [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00FF [0x1D] PRINT_EVENT_MESSAGE(message_id=11796*)
    → "I heard of your deeds from Tressia. Here is your reward."
  4: 0x0102 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0103 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=27*
  6: 0x0112 [0x1C] WAIT(60* ticks)
  7: 0x0115 [0x1D] PRINT_EVENT_MESSAGE(message_id=11797*)
    → "We may need your help again someday. Thank you, <Player>."
  8: 0x0118 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0119 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=27*
 10: 0x0128 [0x21] END_EVENT
 11: 0x0129 [0x00] END_REQSTACK()
```
