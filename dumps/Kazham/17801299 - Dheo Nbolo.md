# 17801299 - Dheo Nbolo

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 528 bytes        |
| Total Events     | 13               |
| References Count | 20               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [91](#event-91)          | 0x001A       |     33 |             12 |
| [181](#event-181)        | 0x003B       |     33 |             12 |
| [217](#event-217)        | 0x005C       |      1 |              1 |
| [65535.3](#event-655353) | 0x005D       |     70 |              6 |
| [65535.4](#event-655354) | 0x00A3       |    126 |             12 |
| [65535.5](#event-655355) | 0x0121       |     17 |              5 |
| [65535.6](#event-655356) | 0x0132       |      5 |              3 |
| [218](#event-218)        | 0x0137       |     33 |             12 |
| [240](#event-240)        | 0x0158       |     33 |             12 |
| [239](#event-239)        | 0x0179       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x272C      |       10028 |
|       3 | 0x272D      |       10029 |
|       4 | 0x287C      |       10364 |
|       5 | 0x287D      |       10365 |
|       6 | 0x0096      |         150 |
|       7 | 0x0000      |           0 |
|       8 | 0x0078      |         120 |
|       9 | 0x00C8      |         200 |
|      10 | 0x0082      |         130 |
|      11 | 0x0005      |           5 |
|      12 | 0x0006      |           6 |
|      13 | 0x0009      |           9 |
|      14 | 0x28B2      |       10418 |
|      15 | 0x28B4      |       10420 |
|      16 | 0x28B8      |       10424 |
|      17 | 0x28B9      |       10425 |
|      18 | 0x28C8      |       10440 |
|      19 | 0x28C9      |       10441 |

## String References

- **10028**: Wow! You say you got here by airship? Prrretty good for an adventurer!
- **10029**: Someday I'd like to trrravel around Vana'diel on one of those flying ships. Thanks to the chieftainness, it's easier to travel outside of Kazham these days.
- **10364**: I'm only telling you this because I like you--you should rrreally get on the next airship and never show your face in this village again.
- **10365**: I don't mean to be rude, but you smell worse than my Mithran Gaiterrrs.
- **10418**: Hey! Vuih! Quit your gabbing and finish what you starrrted!
- **10420**: Thanks, Vuih. There isn't a Mithra nicer than you...now, if we could just do something about that smell.
- **10424**: That Vuih lives alone in the Yuhtunga Jungle. Well, not really alone. She's got hundrrreds of wild "friends."
- **10425**: After that accident with the Rafflesia flower, she hasn't been able to rrremove that odor from her body. If you don't do something about that stench on you, you'll end up just like her!
- **10440**: There are ten Opo-opos living in this village.
- **10441**: Vuih Stecoppah brrrought all them to Kazham when they were still babies. That's why they are so friendly around people.

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
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 91

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 29 08 53 A0 0F 01 01  1D 02 80 23 1D 03 80 23  p).S.......#...#
0030: 29 08 53 A0 0F 01 02 20  00 21 00                 ).S.... .!.     
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dheo Nbolo (ID: 17801299/0x010FA053), tag_num=0x01)
  4: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=10028*)
    → "Wow! You say you got here by airship? Prrretty good for an adventurer!"
  5: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=10029*)
    → "Someday I'd like to trrravel around Vana'diel on one of those flying ships. Thanks to the chieftainness, it's easier to travel outside of Kazham these days."
  7: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0030 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dheo Nbolo (ID: 17801299/0x010FA053), tag_num=0x02)
  9: 0x0037 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0039 [0x21] END_EVENT
 11: 0x003A [0x00] END_REQSTACK()
```

### Event 181

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   1E F0 FF FF 7F             .....
0040: 6F 70 29 08 53 A0 0F 01  01 1D 04 80 23 1D 05 80  op).S.......#...
0050: 23 29 08 53 A0 0F 01 02  20 00 21 00              #).S.... .!.    
```

#### Opcodes

```
  0: 0x003B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0041 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0042 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dheo Nbolo (ID: 17801299/0x010FA053), tag_num=0x01)
  4: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=10364*)
    → "I'm only telling you this because I like you--you should rrreally get on the next airship and never show your face in this village again."
  5: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=10365*)
    → "I don't mean to be rude, but you smell worse than my Mithran Gaiterrrs."
  7: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0051 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dheo Nbolo (ID: 17801299/0x010FA053), tag_num=0x02)
  9: 0x0058 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x005A [0x21] END_EVENT
 11: 0x005B [0x00] END_REQSTACK()
```

### Event 217

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      00                       .   
```

#### Opcodes

```
  0: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 70 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         45 06 80               E..
0060: F0 FF FF 7F F0 FF FF 7F  73 30 36 30 07 80 1C 08  ........s060....
0070: 80 52 06 80 F0 FF FF 7F  F0 FF FF 7F 73 30 36 30  .R..........s060
0080: 45 09 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 07  E..........ovl1.
0090: 80 45 06 80 F0 FF FF 7F  F0 FF FF 7F 73 30 36 31  .E..........s061
00A0: 07 80 00                                          ...             
```

#### Opcodes

```
  0: 0x005D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s060" with entities [LocalPlayer, LocalPlayer], work=[150*, 0*]
  1: 0x006E [0x1C] WAIT(120* ticks)
  2: 0x0071 [0x52] END_LOAD_SCHEDULER: End scheduler "s060" with entities [LocalPlayer, LocalPlayer], work=150*
  3: 0x0080 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0091 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s061" with entities [LocalPlayer, LocalPlayer], work=[150*, 0*]
  5: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00A3    |
| Data Size    | 126 bytes |
| Instructions | 12        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          45 06 80 F0 FF  FF 7F F0 FF FF 7F 73 30     E..........s0
00B0: 36 39 07 80 1C 0A 80 52  06 80 F0 FF FF 7F F0 FF  69.....R........
00C0: FF 7F 73 30 36 39 45 09  80 F0 FF FF 7F F0 FF FF  ..s069E.........
00D0: 7F 6F 76 6C 31 07 80 02  09 10 0B 80 00 F3 00 45  .ovl1..........E
00E0: 06 80 F0 FF FF 7F F0 FF  FF 7F 73 30 38 34 07 80  ..........s084..
00F0: 01 20 01 02 09 10 0C 80  00 0F 01 45 06 80 F0 FF  . .........E....
0100: FF 7F F0 FF FF 7F 73 30  38 34 07 80 01 20 01 45  ......s084... .E
0110: 06 80 F0 FF FF 7F F0 FF  FF 7F 73 30 37 31 07 80  ..........s071..
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x00A3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s069" with entities [LocalPlayer, LocalPlayer], work=[150*, 0*]
  1: 0x00B4 [0x1C] WAIT(130* ticks)
  2: 0x00B7 [0x52] END_LOAD_SCHEDULER: End scheduler "s069" with entities [LocalPlayer, LocalPlayer], work=150*
  3: 0x00C6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x00D7 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x00F3
  5: 0x00DF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s084" with entities [LocalPlayer, LocalPlayer], work=[150*, 0*]
  6: 0x00F0 [0x01] GOTO 0x0120
  7: 0x00F3 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x010F
  8: 0x00FB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s084" with entities [LocalPlayer, LocalPlayer], work=[150*, 0*]
  9: 0x010C [0x01] GOTO 0x0120
 10: 0x010F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s071" with entities [LocalPlayer, LocalPlayer], work=[150*, 0*]

SUBROUTINE_0120:
 11: 0x0120 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0121   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:    6E F8 FF FF 7F 0D 80  99 F8 FF FF 7F 1D 0E 80   n..............
0130: 23 00                                             #.              
```

#### Opcodes

```
  0: 0x0121 [0x6E] EventEntity uses emote 9*
  1: 0x0128 [0x99] Wait for EventEntity animation to complete
  2: 0x012D [0x1D] PRINT_EVENT_MESSAGE(message_id=10418*)
    → "Hey! Vuih! Quit your gabbing and finish what you starrrted!"
  3: 0x0130 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0131 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0132  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:       1D 0F 80 23 00                                ...#.         
```

#### Opcodes

```
  0: 0x0132 [0x1D] PRINT_EVENT_MESSAGE(message_id=10420*)
    → "Thanks, Vuih. There isn't a Mithra nicer than you...now, if we could just do something about that smell."
  1: 0x0135 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0136 [0x00] END_REQSTACK()
```

### Event 218

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0137   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                      1E  F0 FF FF 7F 6F 70 29 08         .....op).
0140: 53 A0 0F 01 01 1D 10 80  23 1D 11 80 23 29 08 53  S.......#...#).S
0150: A0 0F 01 02 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0137 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x013C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x013D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x013E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dheo Nbolo (ID: 17801299/0x010FA053), tag_num=0x01)
  4: 0x0145 [0x1D] PRINT_EVENT_MESSAGE(message_id=10424*)
    → "That Vuih lives alone in the Yuhtunga Jungle. Well, not really alone. She's got hundrrreds of wild "friends.""
  5: 0x0148 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0149 [0x1D] PRINT_EVENT_MESSAGE(message_id=10425*)
    → "After that accident with the Rafflesia flower, she hasn't been able to rrremove that odor from her body. If you don't do something about that stench on you, you'll end up just like her!"
  7: 0x014C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x014D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dheo Nbolo (ID: 17801299/0x010FA053), tag_num=0x02)
  9: 0x0154 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0156 [0x21] END_EVENT
 11: 0x0157 [0x00] END_REQSTACK()
```

### Event 240

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0158   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                          1E F0 FF FF 7F 6F 70 29          .....op)
0160: 08 53 A0 0F 01 01 1D 12  80 23 1D 13 80 23 29 08  .S.......#...#).
0170: 53 A0 0F 01 02 20 00 21  00                       S.... .!.       
```

#### Opcodes

```
  0: 0x0158 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x015D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x015E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x015F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dheo Nbolo (ID: 17801299/0x010FA053), tag_num=0x01)
  4: 0x0166 [0x1D] PRINT_EVENT_MESSAGE(message_id=10440*)
    → "There are ten Opo-opos living in this village."
  5: 0x0169 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x016A [0x1D] PRINT_EVENT_MESSAGE(message_id=10441*)
    → "Vuih Stecoppah brrrought all them to Kazham when they were still babies. That's why they are so friendly around people."
  7: 0x016D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x016E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dheo Nbolo (ID: 17801299/0x010FA053), tag_num=0x02)
  9: 0x0175 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0177 [0x21] END_EVENT
 11: 0x0178 [0x00] END_REQSTACK()
```

### Event 239

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0179  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                             00                             .      
```

#### Opcodes

```
  0: 0x0179 [0x00] END_REQSTACK()
```
