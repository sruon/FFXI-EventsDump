# 17830071 - Corpo-Vorpo

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 496 bytes                 |
| Total Events     | 4                         |
| References Count | 20                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [5017](#event-5017)   | 0x0001       |     33 |              9 |
| [5015](#event-5015)   | 0x0022       |    317 |             38 |
| [5016](#event-5016)   | 0x015F       |     33 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0031      |          49 |
|       2 | 0x270D      |        9997 |
|       3 | 0x270E      |        9998 |
|       4 | 0x00C8      |         200 |
|       5 | 0x0000      |           0 |
|       6 | 0x0013      |          19 |
|       7 | 0x024D      |         589 |
|       8 | 0xFFFE5BF4  |  4294859764 |
|       9 | 0x4C69      |       19561 |
|      10 | 0xFFFFFD77  |  4294966647 |
|      11 | 0x0AB7      |        2743 |
|      12 | 0x026D      |         621 |
|      13 | 0x000F      |          15 |
|      14 | 0x2707      |        9991 |
|      15 | 0x2708      |        9992 |
|      16 | 0x2709      |        9993 |
|      17 | 0x270A      |        9994 |
|      18 | 0x270B      |        9995 |
|      19 | 0x270C      |        9996 |

## String References

- **9991**: Can I help you? ...I see. Information on the leafkin-weafkin, is it?
- **9992**: You know, I saw something resembling a leafkin when I stopped at a frontier station in the Morimar Basaltaru Fields.
- **9993**: Let me take out my mappy-wap. See if that jogs my memory... ...There we go. Right here, around K-10.
- **9994**: 'Course, it was nightaru out, so I can't be sure...but I'd lay money that it was one of them creatures you're looking for.
- **9995**: Forgotaru already? That's OK. I'm not the sharpest tool in the shed, either. I saw a leafkin-like creature in the Morimar Basalt Fields, somewhere in the K-10 vicinity.
- **9996**: It was a moonless night, so my eyes could have been playing tricky-wicks on me. Best go see for yourself.
- **9997**: All you adventarus from the Middle Lands are keeping the coalition busy. I'm earning my paycheck, I tell you.
- **9998**: We'd better beef up our patrols if we hope to keep everyone safe from the trouble you lotaru are stirring up.

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

### Event 5017

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  1D 02 80 23 1D 03 80 23  ....tlk0...#...#
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=9997*)
    → "All you adventarus from the Middle Lands are keeping the coalition busy. I'm earning my paycheck, I tell you."
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=9998*)
    → "We'd better beef up our patrols if we hope to keep everyone safe from the trouble you lotaru are stirring up."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x21] END_EVENT
  8: 0x0021 [0x00] END_REQSTACK()
```

### Event 5015

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0022    |
| Data Size    | 317 bytes |
| Instructions | 38        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       42 45 04 80 F0 FF  FF 7F F0 FF FF 7F 66 64    BE..........fd
0030: 6F 31 05 80 55 04 80 F0  FF FF 7F F0 FF FF 7F 66  o1..U..........f
0040: 64 6F 31 46 01 38 06 80  75 00 07 80 75 01 92 01  do1F.8..u...u...
0050: F8 FF FF 7F BA F0 FF FF  7F 08 80 09 80 0A 80 0B  ................
0060: 80 80 F0 FF FF 7F 80 F8  FF FF 7F 4A F0 FF FF 7F  ...........J....
0070: F8 FF FF 7F 1E F0 FF FF  7F 45 0C 80 F0 FF FF 7F  .........E......
0080: F0 FF FF 7F 73 30 30 36  05 80 1C 0D 80 45 04 80  ....s006.....E..
0090: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 05 80 66 01  ........fdi1..f.
00A0: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 1D 0E 80  .........thk1...
00B0: 23 52 0C 80 F0 FF FF 7F  F0 FF FF 7F 73 30 30 36  #R..........s006
00C0: 45 0C 80 F0 FF FF 7F F0  FF FF 7F 73 30 30 37 05  E..........s007.
00D0: 80 66 01 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32  .f..........thk2
00E0: 1D 0F 80 23 66 01 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
00F0: 6C 6B 30 1D 10 80 23 52  0C 80 F0 FF FF 7F F0 FF  lk0...#R........
0100: FF 7F 73 30 30 37 45 0C  80 F0 FF FF 7F F0 FF FF  ..s007E.........
0110: 7F 73 30 30 38 05 80 1D  11 80 23 45 04 80 F0 FF  .s008.....#E....
0120: FF 7F F0 FF FF 7F 66 64  6F 31 05 80 55 04 80 F0  ......fdo1..U...
0130: FF FF 7F F0 FF FF 7F 66  64 6F 31 52 0C 80 F0 FF  .......fdo1R....
0140: FF 7F F0 FF FF 7F 73 30  30 38 46 00 45 04 80 F0  ......s008F.E...
0150: FF FF 7F F0 FF FF 7F 66  64 69 32 05 80 21 00     .......fdi2..!. 
```

#### Opcodes

```
  0: 0x0022 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0023 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x0034 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  3: 0x0043 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0045 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x0048 [0x75] LOAD_ROOM(Load indoor room, room=589*)
  6: 0x004C [0x75] LOAD_ROOM(No action)
  7: 0x004E [0x92] EventEntity->Render.Flags3 ^= 0x01
  8: 0x0054 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-107.532*, pos_z=19.561*, pos_y=-0.649*, direction=241.1°*)
  9: 0x0061 [0x80] LOAD_WAIT(entity=LocalPlayer)
 10: 0x0066 [0x80] LOAD_WAIT(entity=EventEntity)
 11: 0x006B [0x4A] LocalPlayer looks at EventEntity
 12: 0x0074 [0x1E] EventEntity looks at LocalPlayer and starts talking
 13: 0x0079 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s006" with entities [LocalPlayer, LocalPlayer], work=[621*, 0*]
 14: 0x008A [0x1C] WAIT(15* ticks)
 15: 0x008D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x009E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=49*
 17: 0x00AD [0x1D] PRINT_EVENT_MESSAGE(message_id=9991*)
    → "Can I help you? ...I see. Information on the leafkin-weafkin, is it?"
 18: 0x00B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x00B1 [0x52] END_LOAD_SCHEDULER: End scheduler "s006" with entities [LocalPlayer, LocalPlayer], work=621*
 20: 0x00C0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=[621*, 0*]
 21: 0x00D1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=49*
 22: 0x00E0 [0x1D] PRINT_EVENT_MESSAGE(message_id=9992*)
    → "You know, I saw something resembling a leafkin when I stopped at a frontier station in the Morimar Basaltaru Fields."
 23: 0x00E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x00E4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
 25: 0x00F3 [0x1D] PRINT_EVENT_MESSAGE(message_id=9993*)
    → "Let me take out my mappy-wap. See if that jogs my memory... ...There we go. Right here, around K-10."
 26: 0x00F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x00F7 [0x52] END_LOAD_SCHEDULER: End scheduler "s007" with entities [LocalPlayer, LocalPlayer], work=621*
 28: 0x0106 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s008" with entities [LocalPlayer, LocalPlayer], work=[621*, 0*]
 29: 0x0117 [0x1D] PRINT_EVENT_MESSAGE(message_id=9994*)
    → "'Course, it was nightaru out, so I can't be sure...but I'd lay money that it was one of them creatures you're looking for."
 30: 0x011A [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x011B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 32: 0x012C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 33: 0x013B [0x52] END_LOAD_SCHEDULER: End scheduler "s008" with entities [LocalPlayer, LocalPlayer], work=621*
 34: 0x014A [0x46] CAMERA_CONTROL: Restore default settings
 35: 0x014C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 36: 0x015D [0x21] END_EVENT
 37: 0x015E [0x00] END_REQSTACK()
```

### Event 5016

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015F   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                               1E                 .
0160: F0 FF FF 7F 1C 00 80 66  01 80 F8 FF FF 7F F8 FF  .......f........
0170: FF 7F 74 6C 6B 30 1D 12  80 23 1D 13 80 23 21 00  ..tlk0...#...#!.
```

#### Opcodes

```
  0: 0x015F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0164 [0x1C] WAIT(30* ticks)
  2: 0x0167 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  3: 0x0176 [0x1D] PRINT_EVENT_MESSAGE(message_id=9995*)
    → "Forgotaru already? That's OK. I'm not the sharpest tool in the shed, either. I saw a leafkin-like creature in the Morimar Basalt Fields, somewhere in the K-10 vicinity."
  4: 0x0179 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x017A [0x1D] PRINT_EVENT_MESSAGE(message_id=9996*)
    → "It was a moonless night, so my eyes could have been playing tricky-wicks on me. Best go see for yourself."
  6: 0x017D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x017E [0x21] END_EVENT
  8: 0x017F [0x00] END_REQSTACK()
```
