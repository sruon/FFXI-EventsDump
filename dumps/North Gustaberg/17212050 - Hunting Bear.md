# 17212050 - Hunting Bear

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | North Gustaberg (ID: 106) |
| Block Size       | 564 bytes                 |
| Total Events     | 5                         |
| References Count | 18                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [20](#event-20)       | 0x0001       |     11 |              5 |
| [21](#event-21)       | 0x000C       |     11 |              5 |
| [22](#event-22)       | 0x0017       |    422 |             51 |
| [23](#event-23)       | 0x01BD       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D2F      |        7471 |
|       1 | 0x1D30      |        7472 |
|       2 | 0x00C8      |         200 |
|       3 | 0x0000      |           0 |
|       4 | 0x0005      |           5 |
|       5 | 0x0413      |        1043 |
|       6 | 0x0006      |           6 |
|       7 | 0x1D31      |        7473 |
|       8 | 0x003C      |          60 |
|       9 | 0x00F0      |         240 |
|      10 | 0x1D32      |        7474 |
|      11 | 0x1D33      |        7475 |
|      12 | 0x1D34      |        7476 |
|      13 | 0x0001      |           1 |
|      14 | 0x1D35      |        7477 |
|      15 | 0x1D36      |        7478 |
|      16 | 0x00C9      |         201 |
|      17 | 0x1D37      |        7479 |

## String References

- **7471**: What am I doing here? Oh, just business. Nothing you should worry about.
- **7472**: You've talked to my partner, I assume? Ah, but you don't meet the requirements. You must come here with a party of two or more members level fifteen and below.
- **7473**: You've talked to my partner, I assume? Stand in a line--let me see you all.
- **7474**: Okay, you check out. So, how was your trip here? Was it fun, or was it rough?
- **7475**: How was your trip here? [Fun!/Rough.]
- **7476**: I see...that means people would not care to pay money to come here, then.
- **7477**: I see...so that means no one would want to come here, however good the sights may be.
- **7478**: Well, some details have to be smoothed out--something my partner isn't too good at--but it isn't a bad business idea. Here, take this, and thanks for coming.
- **7479**: There must be some money to be made with the sights here. It really isn't a bad idea...

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
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7471*)
    → "What am I doing here? Oh, just business. Nothing you should worry about."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 1D 01 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7472*)
    → "You've talked to my partner, I assume? Ah, but you don't meet the requirements. You must come here with a party of two or more members level fifteen and below."
  2: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0015 [0x21] END_EVENT
  4: 0x0016 [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0017    |
| Data Size    | 422 bytes |
| Instructions | 51        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      42  46 01 45 02 80 F8 FF FF         BF.E.....
0020: 7F F8 FF FF 7F 66 64 6F  30 03 80 55 02 80 F8 FF  .....fdo0..U....
0030: FF 7F F8 FF FF 7F 66 64  6F 30 27 64 F0 FF FF 7F  ......fdo0'd....
0040: 02 27 64 F1 FF FF 7F 02  27 64 F2 FF FF 7F 02 27  .'d.....'d.....'
0050: 64 F3 FF FF 7F 02 27 64  F4 FF FF 7F 02 27 64 F5  d.....'d.....'d.
0060: FF FF 7F 02 1C 04 80 38  05 80 45 02 80 F8 FF FF  .......8..E.....
0070: 7F F8 FF FF 7F 66 64 69  30 03 80 79 00 F8 FF FF  .....fdi0..y....
0080: 7F F0 FF FF 7F 45 06 80  F8 FF FF 7F F8 FF FF 7F  .....E..........
0090: 73 30 30 30 03 80 1D 07  80 23 45 02 80 F8 FF FF  s000.....#E.....
00A0: 7F F8 FF FF 7F 66 64 6F  30 03 80 55 02 80 F8 FF  .....fdo0..U....
00B0: FF 7F F8 FF FF 7F 66 64  6F 30 45 02 80 F8 FF FF  ......fdo0E.....
00C0: 7F F8 FF FF 7F 66 64 69  31 03 80 45 06 80 F8 FF  .....fdi1..E....
00D0: FF 7F F8 FF FF 7F 73 30  30 31 03 80 66 08 80 F8  ......s001..f...
00E0: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1C 09 80 1D 0A  .......tlk0.....
00F0: 80 23 5E 69 64 6C 30 24  0B 80 03 80 03 80 25 02  .#^idl0$......%.
0100: 00 10 03 80 00 1D 01 66  08 80 F8 FF FF 7F F8 FF  .......f........
0110: FF 7F 74 68 6B 31 1D 0C  80 23 01 3B 01 02 00 10  ..thk1...#.;....
0120: 0D 80 00 3B 01 66 08 80  F8 FF FF 7F F8 FF FF 7F  ...;.f..........
0130: 74 68 6B 31 1D 0E 80 23  01 3B 01 66 08 80 F8 FF  thk1...#.;.f....
0140: FF 7F F8 FF FF 7F 74 68  6B 32 53 F8 FF FF 7F F8  ......thk2S.....
0150: FF FF 7F 74 68 6B 32 66  08 80 F8 FF FF 7F F8 FF  ...thk2f........
0160: FF 7F 70 61 73 30 1D 0F  80 23 45 02 80 F8 FF FF  ..pas0...#E.....
0170: 7F F8 FF FF 7F 66 64 6F  31 03 80 55 02 80 F8 FF  .....fdo1..U....
0180: FF 7F F8 FF FF 7F 66 64  6F 31 46 00 45 10 80 F8  ......fdo1F.E...
0190: FF FF 7F F8 FF FF 7F 71  73 74 63 03 80 53 F8 FF  .......qstc..S..
01A0: FF 7F F8 FF FF 7F 70 61  73 30 45 02 80 F8 FF FF  ......pas0E.....
01B0: 7F F8 FF FF 7F 66 64 69  31 03 80 21 00           .....fdi1..!.   
```

#### Opcodes

```
  0: 0x0017 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0018 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x001A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
  3: 0x002B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [EventEntity, EventEntity], work=200*
  4: 0x003A [0x27] REQ_SET(priority=0x64, entity_id=LocalPlayer, tag_num=0x02)
  5: 0x0041 [0x27] REQ_SET(priority=0x64, entity_id=Unknown NPC (ID: 2147483633/0x7FFFFFF1), tag_num=0x02)
  6: 0x0048 [0x27] REQ_SET(priority=0x64, entity_id=Unknown NPC (ID: 2147483634/0x7FFFFFF2), tag_num=0x02)
  7: 0x004F [0x27] REQ_SET(priority=0x64, entity_id=Unknown NPC (ID: 2147483635/0x7FFFFFF3), tag_num=0x02)
  8: 0x0056 [0x27] REQ_SET(priority=0x64, entity_id=Unknown NPC (ID: 2147483636/0x7FFFFFF4), tag_num=0x02)
  9: 0x005D [0x27] REQ_SET(priority=0x64, entity_id=Unknown NPC (ID: 2147483637/0x7FFFFFF5), tag_num=0x02)
 10: 0x0064 [0x1C] WAIT(5* ticks)
 11: 0x0067 [0x38] SET_CLIENT_EVENT_MODE(mode=1043*)
 12: 0x006A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 13: 0x007B [0x79] EventEntity looks at LocalPlayer (Basic look)
 14: 0x0085 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [EventEntity, EventEntity], work=[6*, 0*]
 15: 0x0096 [0x1D] PRINT_EVENT_MESSAGE(message_id=7473*)
    → "You've talked to my partner, I assume? Stand in a line--let me see you all."
 16: 0x0099 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x009A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [EventEntity, EventEntity], work=[200*, 0*]
 18: 0x00AB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [EventEntity, EventEntity], work=200*
 19: 0x00BA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 20: 0x00CB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s001" with entities [EventEntity, EventEntity], work=[6*, 0*]
 21: 0x00DC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
 22: 0x00EB [0x1C] WAIT(240* ticks)
 23: 0x00EE [0x1D] PRINT_EVENT_MESSAGE(message_id=7474*)
    → "Okay, you check out. So, how was your trip here? Was it fun, or was it rough?"
 24: 0x00F1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x00F2 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 26: 0x00F7 [0x24] CREATE_DIALOG(message_id=7475*, default_option=0*, option_flags=0*)
    → "How was your trip here? [Fun!/Rough.]"
 27: 0x00FE [0x25] WAIT_DIALOG_SELECT()
 28: 0x00FF [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x011D
 29: 0x0107 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=60*
 30: 0x0116 [0x1D] PRINT_EVENT_MESSAGE(message_id=7476*)
    → "I see...that means people would not care to pay money to come here, then."
 31: 0x0119 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x011A [0x01] GOTO 0x013B
 33: 0x011D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x013B
 34: 0x0125 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=60*
 35: 0x0134 [0x1D] PRINT_EVENT_MESSAGE(message_id=7477*)
    → "I see...so that means no one would want to come here, however good the sights may be."
 36: 0x0137 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x0138 [0x01] GOTO 0x013B

SUBROUTINE_013B:
 38: 0x013B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=60*
 39: 0x014A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
 40: 0x0157 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=60*
 41: 0x0166 [0x1D] PRINT_EVENT_MESSAGE(message_id=7478*)
    → "Well, some details have to be smoothed out--something my partner isn't too good at--but it isn't a bad business idea. Here, take this, and thanks for coming."
 42: 0x0169 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x016A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 44: 0x017B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 45: 0x018A [0x46] CAMERA_CONTROL: Restore default settings
 46: 0x018C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 47: 0x019D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 48: 0x01AA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 49: 0x01BB [0x21] END_EVENT
 50: 0x01BC [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BD   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                         1E F0 FF               ...
01C0: FF 7F 1D 11 80 23 21 00                           .....#!.        
```

#### Opcodes

```
  0: 0x01BD [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x01C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7479*)
    → "There must be some money to be made with the sights here. It really isn't a bad idea..."
  2: 0x01C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01C6 [0x21] END_EVENT
  4: 0x01C7 [0x00] END_REQSTACK()
```
