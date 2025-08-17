# 17830105 - Risen Hackles

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 440 bytes                 |
| Total Events     | 7                         |
| References Count | 28                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [528](#event-528)        | 0x0001       |     47 |             11 |
| [2550](#event-2550)      | 0x0030       |     72 |             24 |
| [2551](#event-2551)      | 0x0078       |     43 |              9 |
| [2552](#event-2552)      | 0x00A3       |     93 |             27 |
| [90](#event-90)          | 0x0100       |      1 |              1 |
| [65535.1](#event-655351) | 0x0101       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0041      |          65 |
|       1 | 0x28E0      |       10464 |
|       2 | 0x28E1      |       10465 |
|       3 | 0x1F06      |        7942 |
|       4 | 0x1F07      |        7943 |
|       5 | 0x1F08      |        7944 |
|       6 | 0x1F09      |        7945 |
|       7 | 0x1F0A      |        7946 |
|       8 | 0x1F0B      |        7947 |
|       9 | 0x1F0C      |        7948 |
|      10 | 0x1F0D      |        7949 |
|      11 | 0x1F0E      |        7950 |
|      12 | 0x1F0F      |        7951 |
|      13 | 0x1F10      |        7952 |
|      14 | 0x1F11      |        7953 |
|      15 | 0x1F12      |        7954 |
|      16 | 0x1F13      |        7955 |
|      17 | 0x1F14      |        7956 |
|      18 | 0x1F15      |        7957 |
|      19 | 0x1F16      |        7958 |
|      20 | 0x1F17      |        7959 |
|      21 | 0x00C9      |         201 |
|      22 | 0x0000      |           0 |
|      23 | 0x0028      |          40 |
|      24 | 0xFFFEC3A1  |  4294886305 |
|      25 | 0x209A      |        8346 |
|      26 | 0xFFFEC049  |  4294885449 |
|      27 | 0x1031      |        4145 |

## String References

- **7942**: You must be one of those pioneers I keep hearing about.
- **7943**: You heard of the Rala Waterways, located beneath the areas surrounding the castle?
- **7944**: It's like a goddamn maze down there. Good luck finding a reliable way in.
- **7945**: There are gates located throughout, but which ones are open changes depending on the day.
- **7946**: Don't think you can learn one way in and be set for life. It's not that easy.
- **7947**: I want you to check the gates' operations and help keep the area safe.
- **7948**: Go speak to the soldier located near the holy battlegrounds, an area of the Waterways located beneath locales leading to Big Bridge.
- **7949**: If you can do this simple task, then I'll recognize you as a [man/woman] of mettle.
- **7950**: Forgot how to get there already? You're looking for a soldier located in the holy battlegrounds area of the Waterways, located in areas beneath Big Bridge.
- **7951**: How are you progressing?
- **7952**: Everything checks out, then?
- **7953**: If you managed to get that far, then you've succeeded in navigating that area without getting lost. Good work.
- **7954**: With all the foul creatures sprouting like weeds down there, we've had trouble ensuring the gates are functioning properly of late.
- **7955**: Any help you can give in keeping the area safe would be most welcome.
- **7956**: I'll share a secret with you. The Waterways also serve as an emergency exit of sorts.
- **7957**: I find it quite helpful that more pioneers are beginning to learn about the area. If anything happens, the lot of you can assist us in case of evacuation.
- **7958**: There can never be too many people willing to lend us a hand.
- **7959**: Leave your pride at the door and strive to be the best pioneer you can. Adoulin is counting on you.
- **10464**: There's a large system of tunnels under this city called the Rala Waterways.
- **10465**: Almost everyone who's been down there talks about hearing grotesque howls deep within. Some have even seen monsters, they say. Maybe they slip through secret holes to get around the magic barrier...I don't know.

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

### Event 528

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 62 30 1D  01 80 23 1D 02 80 23 66  ...tlb0...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 31 21 00  ..........tlb1!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10464*)
    → "There's a large system of tunnels under this city called the Rala Waterways."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=10465*)
    → "Almost everyone who's been down there talks about hearing grotesque howls deep within. Some have even seen monsters, they say. Maybe they slip through secret holes to get around the magic barrier...I don't know."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 2550

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 72 bytes |
| Instructions | 24       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 42 6F 70  66 00 80 F8 FF FF 7F F8  .....Bopf.......
0040: FF FF 7F 74 6C 62 30 1D  03 80 23 1D 04 80 23 1D  ...tlb0...#...#.
0050: 05 80 23 1D 06 80 23 1D  07 80 23 1D 08 80 23 1D  ..#...#...#...#.
0060: 09 80 23 1D 0A 80 23 66  00 80 F8 FF FF 7F F8 FF  ..#...#f........
0070: FF 7F 74 6C 62 31 21 00                           ..tlb1!.        
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0036 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0037 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  5: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=7942*)
    → "You must be one of those pioneers I keep hearing about."
  6: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=7943*)
    → "You heard of the Rala Waterways, located beneath the areas surrounding the castle?"
  8: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=7944*)
    → "It's like a goddamn maze down there. Good luck finding a reliable way in."
 10: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=7945*)
    → "There are gates located throughout, but which ones are open changes depending on the day."
 12: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0057 [0x1D] PRINT_EVENT_MESSAGE(message_id=7946*)
    → "Don't think you can learn one way in and be set for life. It's not that easy."
 14: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x005B [0x1D] PRINT_EVENT_MESSAGE(message_id=7947*)
    → "I want you to check the gates' operations and help keep the area safe."
 16: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=7948*)
    → "Go speak to the soldier located near the holy battlegrounds, an area of the Waterways located beneath locales leading to Big Bridge."
 18: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0063 [0x1D] PRINT_EVENT_MESSAGE(message_id=7949*)
    → "If you can do this simple task, then I'll recognize you as a [man/woman] of mettle."
 20: 0x0066 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0067 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
 22: 0x0076 [0x21] END_EVENT
 23: 0x0077 [0x00] END_REQSTACK()
```

### Event 2551

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          1E F0 FF FF 7F 6F 70 66          .....opf
0080: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 30 1D 0B  ..........tlb0..
0090: 80 23 66 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 62  .#f..........tlb
00A0: 31 21 00                                          1!.             
```

#### Opcodes

```
  0: 0x0078 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x007D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x007E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x007F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  4: 0x008E [0x1D] PRINT_EVENT_MESSAGE(message_id=7950*)
    → "Forgot how to get there already? You're looking for a soldier located in the holy battlegrounds area of the Waterways, located in areas beneath Big Bridge."
  5: 0x0091 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0092 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
  7: 0x00A1 [0x21] END_EVENT
  8: 0x00A2 [0x00] END_REQSTACK()
```

### Event 2552

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 93 bytes |
| Instructions | 27       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          1E F0 FF FF 7F  42 6F 70 66 00 80 F8 FF     .....Bopf....
00B0: FF 7F F8 FF FF 7F 74 6C  62 30 1D 0C 80 23 1D 0D  ......tlb0...#..
00C0: 80 23 1D 0E 80 23 1D 0F  80 23 1D 10 80 23 1D 11  .#...#...#...#..
00D0: 80 23 1D 12 80 23 1D 13  80 23 1D 14 80 23 45 15  .#...#...#...#E.
00E0: 80 F8 FF FF 7F F8 FF FF  7F 71 73 74 63 16 80 66  .........qstc..f
00F0: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 62 31 21 00  ..........tlb1!.
```

#### Opcodes

```
  0: 0x00A3 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00A9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00AA [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00AB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=65*
  5: 0x00BA [0x1D] PRINT_EVENT_MESSAGE(message_id=7951*)
    → "How are you progressing?"
  6: 0x00BD [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00BE [0x1D] PRINT_EVENT_MESSAGE(message_id=7952*)
    → "Everything checks out, then?"
  8: 0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7953*)
    → "If you managed to get that far, then you've succeeded in navigating that area without getting lost. Good work."
 10: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00C6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7954*)
    → "With all the foul creatures sprouting like weeds down there, we've had trouble ensuring the gates are functioning properly of late."
 12: 0x00C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00CA [0x1D] PRINT_EVENT_MESSAGE(message_id=7955*)
    → "Any help you can give in keeping the area safe would be most welcome."
 14: 0x00CD [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00CE [0x1D] PRINT_EVENT_MESSAGE(message_id=7956*)
    → "I'll share a secret with you. The Waterways also serve as an emergency exit of sorts."
 16: 0x00D1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x00D2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7957*)
    → "I find it quite helpful that more pioneers are beginning to learn about the area. If anything happens, the lot of you can assist us in case of evacuation."
 18: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x00D6 [0x1D] PRINT_EVENT_MESSAGE(message_id=7958*)
    → "There can never be too many people willing to lend us a hand."
 20: 0x00D9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x00DA [0x1D] PRINT_EVENT_MESSAGE(message_id=7959*)
    → "Leave your pride at the door and strive to be the best pioneer you can. Adoulin is counting on you."
 22: 0x00DD [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x00DE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 24: 0x00EF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=65*
 25: 0x00FE [0x21] END_EVENT
 26: 0x00FF [0x00] END_REQSTACK()
```

### Event 90

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0100  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    32 17 80 1F 00 18 80  19 80 16 80 1F 01 1F 00   2..............
0110: 1A 80 1B 80 16 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x0101 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0104 [0x1F] MOVE_ENTITY: EventEntity moves to X=-80.991*, Z=8.346*, Y=0.000*
  2: 0x010C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x010E [0x1F] MOVE_ENTITY: EventEntity moves to X=-81.847*, Z=4.145*, Y=0.000*
  4: 0x0116 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0118 [0x00] END_REQSTACK()
```
