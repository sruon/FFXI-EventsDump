# 17694725 - Passenger

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Bastok-Jeuno Airship (ID: 224) |
| Block Size       | 384 bytes                      |
| Total Events     | 3                              |
| References Count | 18                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [102](#event-102)     | 0x0001       |      5 |              3 |
| [112](#event-112)     | 0x0006       |    275 |             75 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C43      |        7235 |
|       1 | 0x1C42      |        7234 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0x1C46      |        7238 |
|       5 | 0x0003      |           3 |
|       6 | 0x0005      |           5 |
|       7 | 0x0008      |           8 |
|       8 | 0x1C47      |        7239 |
|       9 | 0x1C48      |        7240 |
|      10 | 0x00C9      |         201 |
|      11 | 0x1C44      |        7236 |
|      12 | 0x1C45      |        7237 |
|      13 | 0x1C49      |        7241 |
|      14 | 0x1C4A      |        7242 |
|      15 | 0x0002      |           2 |
|      16 | 0x1C4B      |        7243 |
|      17 | 0x1C4C      |        7244 |

## String References

- **7234**: Return the dropped item? [Yes./No.]
- **7235**: Can I help you?
- **7236**: Oh, thanks... I'm not sure that this belongs to me, though...
- **7237**: Wow, thanks... I don't really remember dropping anything, though...
- **7238**: Thank you! I've been looking all over the place for this!
- **7239**: Thank you! I don't know what I would've done if I had lost this!
- **7240**: Please take this as a token of my gratitude.
- **7241**: I wonder if I could see my house from up here...
- **7242**: There seem to be a lot of disreputable characters riding the airships these days...
- **7243**: It's hard to tell people apart these days, don't you agree? For some reason, that thought occurs to me whenever I ride an airship...
- **7244**: These flights to Jeuno are always so crowded, aren't they?

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

### Event 102

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1A 0B 00 21 00                                  ...!.          
```

#### Opcodes

```
  0: 0x0001 [0x1A] CALL_SUBROUTINE(address=0x000B)
  1: 0x0004 [0x21] END_EVENT
  2: 0x0005 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0006    |
| Data Size    | 275 bytes |
| Instructions | 22        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   1A D2  00 21 00 1E F0 FF FF 7F        ...!......
0010: 1D 00 80 23 24 01 80 02  80 03 80 25 02 00 10 03  ...#$......%....
0020: 80 00 D1 00 42 43 00 43  01 02 02 10 03 80 00 89  ....BC.C........
0030: 00 02 03 10 02 80 80 40  00 1D 04 80 23 01 71 00  .......@....#.q.
0040: 02 03 10 05 80 80 4F 00  1D 04 80 23 01 71 00 02  ......O....#.q..
0050: 03 10 06 80 80 5E 00 1D  04 80 23 01 71 00 02 03  .....^....#.q...
0060: 10 07 80 80 6D 00 1D 04  80 23 01 71 00 1D 08 80  ....m....#.q....
0070: 23 1D 09 80 23 45 0A 80  F8 FF FF 7F F8 FF FF 7F  #...#E..........
0080: 71 73 74 63 03 80 01 C9  00 02 03 10 02 80 80 98  qstc............
0090: 00 1D 0B 80 23 01 C9 00  02 03 10 05 80 80 A7 00  ....#...........
00A0: 1D 0B 80 23 01 C9 00 02  03 10 06 80 80 B6 00 1D  ...#............
00B0: 0B 80 23 01 C9 00 02 03  10 07 80 80 C5 00 1D 0B  ..#.............
00C0: 80 23 01 C9 00 1D 0C 80  23 03 01 10 02 80 01 D1  .#......#.......
00D0: 00 1B 1E F0 FF FF 7F 13  00 00 05 80 02 00 00 03  ................
00E0: 80 80 EB 00 1D 0D 80 23  01 18 01 02 00 00 02 80  .......#........
00F0: 80 FA 00 1D 0E 80 23 01  18 01 02 00 00 0F 80 80  ......#.........
0100: 09 01 1D 10 80 23 01 18  01 02 00 00 05 80 80 18  .....#..........
0110: 01 1D 11 80 23 01 18 01  1B                       ....#....       
```

#### Opcodes

```
  0: 0x0006 [0x1A] CALL_SUBROUTINE(address=0x00D2)
  1: 0x0009 [0x21] END_EVENT
  2: 0x000A [0x00] END_REQSTACK()

SUBROUTINE_00D2:
  3: 0x00D2 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00D7 [0x13] ExtData[1]->WorkLocal[0] = rand() % 3*
  5: 0x00DC [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x00EB
  6: 0x00E4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7241*)
    → "I wonder if I could see my house from up here..."
  7: 0x00E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00E8 [0x01] GOTO 0x0118
  9: 0x00EB [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x00FA
 10: 0x00F3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7242*)
    → "There seem to be a lot of disreputable characters riding the airships these days..."
 11: 0x00F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x00F7 [0x01] GOTO 0x0118
 13: 0x00FA [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x0109
 14: 0x0102 [0x1D] PRINT_EVENT_MESSAGE(message_id=7243*)
    → "It's hard to tell people apart these days, don't you agree? For some reason, that thought occurs to me whenever I ride an airship..."
 15: 0x0105 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0106 [0x01] GOTO 0x0118
 17: 0x0109 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x0118
 18: 0x0111 [0x1D] PRINT_EVENT_MESSAGE(message_id=7244*)
    → "These flights to Jeuno are always so crowded, aren't they?"
 19: 0x0114 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0115 [0x01] GOTO 0x0118

SUBROUTINE_0118:
 21: 0x0118 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x000B [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=7235*)
    → "Can I help you?"
     0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0014 [0x24] CREATE_DIALOG(message_id=7234*, default_option=1*, option_flags=0*)
    → "Return the dropped item? [Yes./No.]"
     0x001B [0x25] WAIT_DIALOG_SELECT()
     0x001C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00D1
     0x0024 [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x0025 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0027 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x0029 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0089
     0x0031 [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x0040
     0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=7238*)
    → "Thank you! I've been looking all over the place for this!"
     0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x003D [0x01] GOTO 0x0071
     0x0040 [0x02] IF !(Work_Zone[3] == 3*) GOTO 0x004F
     0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=7238*)
    → "Thank you! I've been looking all over the place for this!"
     0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x004C [0x01] GOTO 0x0071
     0x004F [0x02] IF !(Work_Zone[3] == 5*) GOTO 0x005E
     0x0057 [0x1D] PRINT_EVENT_MESSAGE(message_id=7238*)
    → "Thank you! I've been looking all over the place for this!"
     0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x005B [0x01] GOTO 0x0071
     0x005E [0x02] IF !(Work_Zone[3] == 8*) GOTO 0x006D
     0x0066 [0x1D] PRINT_EVENT_MESSAGE(message_id=7238*)
    → "Thank you! I've been looking all over the place for this!"
     0x0069 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x006A [0x01] GOTO 0x0071
     0x006D [0x1D] PRINT_EVENT_MESSAGE(message_id=7239*)
    → "Thank you! I don't know what I would've done if I had lost this!"
     0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0071 [0x1D] PRINT_EVENT_MESSAGE(message_id=7240*)
    → "Please take this as a token of my gratitude."
     0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0075 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
     0x0086 [0x01] GOTO 0x00C9
     0x0089 [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x0098
     0x0091 [0x1D] PRINT_EVENT_MESSAGE(message_id=7236*)
    → "Oh, thanks... I'm not sure that this belongs to me, though..."
     0x0094 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0095 [0x01] GOTO 0x00C9
     0x0098 [0x02] IF !(Work_Zone[3] == 3*) GOTO 0x00A7
     0x00A0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7236*)
    → "Oh, thanks... I'm not sure that this belongs to me, though..."
     0x00A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00A4 [0x01] GOTO 0x00C9
     0x00A7 [0x02] IF !(Work_Zone[3] == 5*) GOTO 0x00B6
     0x00AF [0x1D] PRINT_EVENT_MESSAGE(message_id=7236*)
    → "Oh, thanks... I'm not sure that this belongs to me, though..."
     0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00B3 [0x01] GOTO 0x00C9
     0x00B6 [0x02] IF !(Work_Zone[3] == 8*) GOTO 0x00C5
     0x00BE [0x1D] PRINT_EVENT_MESSAGE(message_id=7236*)
    → "Oh, thanks... I'm not sure that this belongs to me, though..."
     0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00C2 [0x01] GOTO 0x00C9
     0x00C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7237*)
    → "Wow, thanks... I don't really remember dropping anything, though..."
     0x00C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00C9 [0x03] Work_Zone[1] = 1*
     0x00CE [0x01] GOTO 0x00D1
     0x00D1 [0x1B] RETURN
```
