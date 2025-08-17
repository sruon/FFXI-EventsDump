# 17224381 - Odyssean Passage

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Pashhow Marshlands (ID: 109) |
| Block Size       | 344 bytes                    |
| Total Events     | 4                            |
| References Count | 9                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [40](#event-40)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |      7 |              2 |
| [43](#event-43)          | 0x000F       |    260 |             40 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x31DC      |       12764 |
|       2 | 0x31DD      |       12765 |
|       3 | 0x00A5      |         165 |
|       4 | 0x0078      |         120 |
|       5 | 0x00C8      |         200 |
|       6 | 0x0001      |           1 |
|       7 | 0x31DE      |       12766 |
|       8 | 0x0002      |           2 |

## String References

- **12764**: Vague images of worlds beyond coalesce and diffuse within.
- **12765**: Enter the light? [Take me now!/Absolutely not!]
- **12766**: Enter the light? [Take me now!/I'll dive in head first!/Absolutely not!]

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

### Event 40

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 43

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000F    |
| Data Size    | 260 bytes |
| Instructions | 40        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               42                 B
0010: 03 01 10 00 80 48 01 80  23 03 00 00 02 10 02 00  .....H..#.......
0020: 00 00 80 00 79 00 24 02  80 00 80 00 80 25 02 00  ....y.$......%..
0030: 10 00 80 00 76 00 43 00  43 01 CD 03 80 F0 FF FF  ....v.C.C.......
0040: 7F F0 FF FF 7F 6D 61 69  6E 00 80 1C 04 80 45 05  .....main.....E.
0050: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 00 80 55  .........fdo1..U
0060: 05 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 03 01  ..........fdo1..
0070: 10 06 80 01 76 00 01 11  01 24 07 80 00 80 00 80  ....v....$......
0080: 25 02 00 10 00 80 00 C9  00 43 00 43 01 CD 03 80  %........C.C....
0090: F0 FF FF 7F F0 FF FF 7F  6D 61 69 6E 00 80 1C 04  ........main....
00A0: 80 45 05 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
00B0: 00 80 55 05 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
00C0: 31 03 01 10 06 80 01 11  01 02 00 10 06 80 00 11  1...............
00D0: 01 43 00 43 01 CD 03 80  F0 FF FF 7F F0 FF FF 7F  .C.C............
00E0: 6D 61 69 6E 00 80 1C 04  80 45 05 80 F0 FF FF 7F  main.....E......
00F0: F0 FF FF 7F 66 64 6F 31  00 80 55 05 80 F0 FF FF  ....fdo1..U.....
0100: 7F F0 FF FF 7F 66 64 6F  31 03 01 10 08 80 01 11  .....fdo1.......
0110: 01 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x000F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0010 [0x03] Work_Zone[1] = 0*
  2: 0x0015 [0x48] [System] [12764*]:
    → "Vague images of worlds beyond coalesce and diffuse within."
  3: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0019 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  5: 0x001E [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0079
  6: 0x0026 [0x24] CREATE_DIALOG(message_id=12765*, default_option=0*, option_flags=0*)
    → "Enter the light? [Take me now!/Absolutely not!]"
  7: 0x002D [0x25] WAIT_DIALOG_SELECT()
  8: 0x002E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0076
  9: 0x0036 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0038 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x003A [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[165*, 0*]
 12: 0x004B [0x1C] WAIT(120* ticks)
 13: 0x004E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x005F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 15: 0x006E [0x03] Work_Zone[1] = 1*
 16: 0x0073 [0x01] GOTO 0x0076

SUBROUTINE_0076:
 17: 0x0076 [0x01] GOTO 0x0111
 18: 0x0079 [0x24] CREATE_DIALOG(message_id=12766*, default_option=0*, option_flags=0*)
    → "Enter the light? [Take me now!/I'll dive in head first!/Absolutely not!]"
 19: 0x0080 [0x25] WAIT_DIALOG_SELECT()
 20: 0x0081 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C9
 21: 0x0089 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 22: 0x008B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 23: 0x008D [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[165*, 0*]
 24: 0x009E [0x1C] WAIT(120* ticks)
 25: 0x00A1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x00B2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 27: 0x00C1 [0x03] Work_Zone[1] = 1*
 28: 0x00C6 [0x01] GOTO 0x0111
 29: 0x00C9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0111
 30: 0x00D1 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 31: 0x00D3 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 32: 0x00D5 [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[165*, 0*]
 33: 0x00E6 [0x1C] WAIT(120* ticks)
 34: 0x00E9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 35: 0x00FA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 36: 0x0109 [0x03] Work_Zone[1] = 2*
 37: 0x010E [0x01] GOTO 0x0111

SUBROUTINE_0111:
 38: 0x0111 [0x21] END_EVENT
 39: 0x0112 [0x00] END_REQSTACK()
```
