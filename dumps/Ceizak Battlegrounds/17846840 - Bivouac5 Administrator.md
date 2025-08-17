# 17846840 - Bivouac5 Administrator

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Ceizak Battlegrounds (ID: 261) |
| Block Size       | 288 bytes                      |
| Total Events     | 2                              |
| References Count | 14                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [3006](#event-3006)   | 0x0001       |    205 |             49 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0004      |           4 |
|       1 | 0x08A6      |        2214 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x1D8E      |        7566 |
|       5 | 0x1DA5      |        7589 |
|       6 | 0x40000000  |  1073741824 |
|       7 | 0x0007      |           7 |
|       8 | 0x1D8F      |        7567 |
|       9 | 0x0002      |           2 |
|      10 | 0x0006      |           6 |
|      11 | 0x1D90      |        7568 |
|      12 | 0x0003      |           3 |
|      13 | 0x1D91      |        7569 |

## String References

- **7566**: Good day to you. This is [the future site of /]frontier bivouac [#1/#2/#3/#4/#5].
- **7567**: Thank you for the $3. We greatly appreciate your efforts to [help set up/provision] frontier bivouac [#1/#2/#3/#4/#5]. Please speak with the manager in charge of this assignment to collect your reward.
- **7568**: I'm terribly sorry, but we can't use broken $5. Could you please return to the coalition assignment desk and procure us another?
- **7569**: How nice it is to see another face out here! As much as I'd like for you to help us set up frontier bivouac [#1/#2/#3/#4/#5], we won't be able to do anything until we've established a base of operations with a frontier station.
- **7589**: [Construction on /]Frontier Bivouac #[1/2/3/4/5] is[/ currently at] $2 percent [complete/durability]. We are in need of [materials with which to set up camp/provisions], so would it be possible for you to undertake a coalition assignment and assist us in [building this thing/keeping this place running]?

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

### Event 3006

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 205 bytes |
| Instructions | 49        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 03 00 00 80 03 00  00 02 10 03 01 00 03 10   ...............
0010: 03 04 00 04 10 03 02 00  01 80 1E F0 FF FF 7F 6F  ...............o
0020: 70 02 00 00 02 80 80 54  00 03 02 10 01 00 03 03  p......T........
0030: 10 03 00 03 04 10 04 00  6E F8 FF FF 7F 03 80 99  ........n.......
0040: F8 FF FF 7F 1D 04 80 23  1D 05 80 23 03 01 10 06  .......#...#....
0050: 80 01 CC 00 02 00 00 03  80 80 84 00 42 03 02 10  ............B...
0060: 02 00 03 03 10 01 00 03  04 10 03 00 6E F8 FF FF  ............n...
0070: 7F 07 80 99 F8 FF FF 7F  1D 08 80 23 03 01 10 03  ...........#....
0080: 80 01 CC 00 02 00 00 09  80 80 B3 00 03 02 10 02  ................
0090: 00 03 03 10 01 00 03 04  10 03 00 6E F8 FF FF 7F  ...........n....
00A0: 0A 80 99 F8 FF FF 7F 1D  0B 80 23 03 01 10 06 80  ..........#.....
00B0: 01 CC 00 02 00 00 0C 80  80 CC 00 03 02 10 03 00  ................
00C0: 1D 0D 80 23 03 01 10 06  80 01 CC 00 21 00        ...#........!.  
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[3] = 4*
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  2: 0x000B [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  3: 0x0010 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[4]
  4: 0x0015 [0x03] ExtData[1]->WorkLocal[2] = 2214*
  5: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x0021 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0054
  9: 0x0029 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 10: 0x002E [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[3]
 11: 0x0033 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[4]
 12: 0x0038 [0x6E] EventEntity uses emote 1*
 13: 0x003F [0x99] Wait for EventEntity animation to complete
 14: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=7566*)
    → "Good day to you. This is [the future site of /]frontier bivouac [#1/#2/#3/#4/#5]."
 15: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=7589*)
    → "[Construction on /]Frontier Bivouac #[1/2/3/4/5] is[/ currently at] $2 percent [complete/durability]. We are in need of [materials with which to set up camp/provisions], so would it be possible for you to undertake a coalition assignment and assist us in [building this thing/keeping this place running]?"
 17: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x004C [0x03] Work_Zone[1] = 1073741824*
 19: 0x0051 [0x01] GOTO 0x00CC
 20: 0x0054 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0084
 21: 0x005C [0x42] SET_CLI_EVENT_CANCEL_DATA()
 22: 0x005D [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
 23: 0x0062 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[1]
 24: 0x0067 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 25: 0x006C [0x6E] EventEntity uses emote 7*
 26: 0x0073 [0x99] Wait for EventEntity animation to complete
 27: 0x0078 [0x1D] PRINT_EVENT_MESSAGE(message_id=7567*)
    → "Thank you for the $3. We greatly appreciate your efforts to [help set up/provision] frontier bivouac [#1/#2/#3/#4/#5]. Please speak with the manager in charge of this assignment to collect your reward."
 28: 0x007B [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x007C [0x03] Work_Zone[1] = 1*
 30: 0x0081 [0x01] GOTO 0x00CC
 31: 0x0084 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x00B3
 32: 0x008C [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
 33: 0x0091 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[1]
 34: 0x0096 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 35: 0x009B [0x6E] EventEntity uses emote 6*
 36: 0x00A2 [0x99] Wait for EventEntity animation to complete
 37: 0x00A7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7568*)
    → "I'm terribly sorry, but we can't use broken $5. Could you please return to the coalition assignment desk and procure us another?"
 38: 0x00AA [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x00AB [0x03] Work_Zone[1] = 1073741824*
 40: 0x00B0 [0x01] GOTO 0x00CC
 41: 0x00B3 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x00CC
 42: 0x00BB [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[3]
 43: 0x00C0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7569*)
    → "How nice it is to see another face out here! As much as I'd like for you to help us set up frontier bivouac [#1/#2/#3/#4/#5], we won't be able to do anything until we've established a base of operations with a frontier station."
 44: 0x00C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x00C4 [0x03] Work_Zone[1] = 1073741824*
 46: 0x00C9 [0x01] GOTO 0x00CC

SUBROUTINE_00CC:
 47: 0x00CC [0x21] END_EVENT
 48: 0x00CD [0x00] END_REQSTACK()
```
