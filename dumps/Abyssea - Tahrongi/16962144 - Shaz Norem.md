# 16962144 - Shaz Norem

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 376 bytes                   |
| Total Events     | 4                           |
| References Count | 17                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |    201 |             47 |
| [404](#event-404)     | 0x00C9       |     20 |             10 |
| [405](#event-405)     | 0x00DD       |     28 |              8 |
| [406](#event-406)     | 0x00F9       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00FE      |         254 |
|       1 | 0x0001      |           1 |
|       2 | 0x1FDF      |        8159 |
|       3 | 0x0000      |           0 |
|       4 | 0x0007      |           7 |
|       5 | 0x1FE0      |        8160 |
|       6 | 0x0008      |           8 |
|       7 | 0x1FE1      |        8161 |
|       8 | 0x0002      |           2 |
|       9 | 0x0009      |           9 |
|      10 | 0x1FE2      |        8162 |
|      11 | 0x1FC1      |        8129 |
|      12 | 0x1FC5      |        8133 |
|      13 | 0x1FC2      |        8130 |
|      14 | 0x1FC3      |        8131 |
|      15 | 0x00C9      |         201 |
|      16 | 0x1FC4      |        8132 |

## String References

- **8129**: I am Shaz Norem, and I have been following your career with grrreat interest. If you would hear an objective evaluation of your efforts, then listen well...
- **8130**: Your accomplishments have not gone unnoticed.
- **8131**: This is but a small token, but with it comes the gratitude of a nation's people.
- **8132**: Thank you, friend. You have been as a torrrch to a people who were groping in darkness.
- **8133**: This land is still frrraught with danger. Be safe in your travels.
- **8159**: Current progress: [Ancient abyssite obtained: $0/$1/Atma obtained: $2/$3/Quests completed: $4/$5/Return.]
- **8160**: [Requirement/Objective completed]: Obtain all ancient abyssite found in this area.
- **8161**: [Requirement/Objective completed]: Obtain all atma found in this area.
- **8162**: [Requirement/Objective completed]: Complete all quests issued in this area.

## Events

### Event 65535

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0000    |
| Data Size    | 201 bytes |
| Instructions | 47        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 03 01 10 00 80 43 00 43  01 03 00 00 02 10 03 01  .....C.C........
0010: 00 03 10 03 02 00 04 10  03 03 00 05 10 03 04 00  ................
0020: 06 10 03 05 00 07 10 03  06 00 08 10 02 01 80 01  ................
0030: 80 00 C7 00 24 02 80 03  80 03 80 25 02 00 10 03  ....$......%....
0040: 80 00 5F 00 3E 06 00 04  80 53 00 03 02 10 01 80  .._.>....S......
0050: 01 58 00 03 02 10 03 80  48 05 80 23 01 A6 00 02  .X......H..#....
0060: 00 10 01 80 00 82 00 3E  06 00 06 80 76 00 03 02  .......>....v...
0070: 10 01 80 01 7B 00 03 02  10 03 80 48 07 80 23 01  ....{......H..#.
0080: A6 00 02 00 10 08 80 00  A5 00 3E 06 00 09 80 99  ..........>.....
0090: 00 03 02 10 01 80 01 9E  00 03 02 10 03 80 48 0A  ..............H.
00A0: 80 23 01 A6 00 1B 03 02  10 00 00 03 03 10 01 00  .#..............
00B0: 03 04 10 02 00 03 05 10  03 00 03 06 10 04 00 03  ................
00C0: 07 10 05 00 01 2C 00 1B  00                       .....,...       
```

#### Opcodes

```
  0: 0x0000 [0x03] Work_Zone[1] = 254*
  1: 0x0005 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  2: 0x0007 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  3: 0x0009 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  4: 0x000E [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  5: 0x0013 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  6: 0x0018 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  7: 0x001D [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[6]
  8: 0x0022 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[7]
  9: 0x0027 [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[8]
 10: 0x002C [0x02] IF !(1* == 1*) GOTO 0x00C7
 11: 0x0034 [0x24] CREATE_DIALOG(message_id=8159*, default_option=0*, option_flags=0*)
    → "Current progress: [Ancient abyssite obtained: $0/$1/Atma obtained: $2/$3/Quests completed: $4/$5/Return.]"
 12: 0x003B [0x25] WAIT_DIALOG_SELECT()
 13: 0x003C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x005F
 14: 0x0044 [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 7*) GOTO 0x0053
 15: 0x004B [0x03] Work_Zone[2] = 1*
 16: 0x0050 [0x01] GOTO 0x0058
 17: 0x0053 [0x03] Work_Zone[2] = 0*

SUBROUTINE_0058:
 18: 0x0058 [0x48] [System] [8160*]:
    → "[Requirement/Objective completed]: Obtain all ancient abyssite found in this area."
 19: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x005C [0x01] GOTO 0x00A6
 21: 0x005F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0082
 22: 0x0067 [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 8*) GOTO 0x0076
 23: 0x006E [0x03] Work_Zone[2] = 1*
 24: 0x0073 [0x01] GOTO 0x007B
 25: 0x0076 [0x03] Work_Zone[2] = 0*

SUBROUTINE_007B:
 26: 0x007B [0x48] [System] [8161*]:
    → "[Requirement/Objective completed]: Obtain all atma found in this area."
 27: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x007F [0x01] GOTO 0x00A6
 29: 0x0082 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00A5
 30: 0x008A [0x3E] IF !(ExtData[1]->WorkLocal[6] bit 9*) GOTO 0x0099
 31: 0x0091 [0x03] Work_Zone[2] = 1*
 32: 0x0096 [0x01] GOTO 0x009E
 33: 0x0099 [0x03] Work_Zone[2] = 0*

SUBROUTINE_009E:
 34: 0x009E [0x48] [System] [8162*]:
    → "[Requirement/Objective completed]: Complete all quests issued in this area."
 35: 0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x00A2 [0x01] GOTO 0x00A6
 37: 0x00A5 [0x1B] RETURN

SUBROUTINE_00A6:
 38: 0x00A6 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[0]
 39: 0x00AB [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[1]
 40: 0x00B0 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[2]
 41: 0x00B5 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[3]
 42: 0x00BA [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[4]
 43: 0x00BF [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[5]
 44: 0x00C4 [0x01] GOTO 0x002C
 45: 0x00C7 [0x1B] RETURN
 46: 0x00C8 [0x00] END_REQSTACK()
```

### Event 404

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 20 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             1E F0 FF FF 7F 6F 70           .....op
00D0: 1D 0B 80 23 1A 00 00 1D  0C 80 23 21 00           ...#......#!.   
```

#### Opcodes

```
  0: 0x00C9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00CF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00D0 [0x1D] PRINT_EVENT_MESSAGE(message_id=8129*)
    → "I am Shaz Norem, and I have been following your career with grrreat interest. If you would hear an objective evaluation of your efforts, then listen well..."
  4: 0x00D3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00D4 [0x1A] CALL_SUBROUTINE(address=0x0000)
  6: 0x00D7 [0x1D] PRINT_EVENT_MESSAGE(message_id=8133*)
    → "This land is still frrraught with danger. Be safe in your travels."
  7: 0x00DA [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00DB [0x21] END_EVENT
  9: 0x00DC [0x00] END_REQSTACK()
```

### Event 405

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         42 1D 0D               B..
00E0: 80 23 1D 0E 80 23 45 0F  80 F0 FF FF 7F F0 FF FF  .#...#E.........
00F0: 7F 71 73 74 63 03 80 21  00                       .qstc..!.       
```

#### Opcodes

```
  0: 0x00DD [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00DE [0x1D] PRINT_EVENT_MESSAGE(message_id=8130*)
    → "Your accomplishments have not gone unnoticed."
  2: 0x00E1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00E2 [0x1D] PRINT_EVENT_MESSAGE(message_id=8131*)
    → "This is but a small token, but with it comes the gratitude of a nation's people."
  4: 0x00E5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00E6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  6: 0x00F7 [0x21] END_EVENT
  7: 0x00F8 [0x00] END_REQSTACK()
```

### Event 406

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F9   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                             42 1D 10 80 23 45 0F           B...#E.
0100: 80 F0 FF FF 7F F0 FF FF  7F 71 73 74 63 03 80 21  .........qstc..!
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x00F9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00FA [0x1D] PRINT_EVENT_MESSAGE(message_id=8132*)
    → "Thank you, friend. You have been as a torrrch to a people who were groping in darkness."
  2: 0x00FD [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  4: 0x010F [0x21] END_EVENT
  5: 0x0110 [0x00] END_REQSTACK()
```
