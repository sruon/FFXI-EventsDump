# 16974321 - Shihu-Danhu

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al Zahbi (ID: 48) |
| Block Size       | 508 bytes         |
| Total Events     | 4                 |
| References Count | 20                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [103](#event-103)     | 0x0001       |    279 |             43 |
| [207](#event-207)     | 0x0118       |     52 |             13 |
| [104](#event-104)     | 0x014C       |     64 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x1F28      |        7976 |
|       2 | 0x1F29      |        7977 |
|       3 | 0x1F2A      |        7978 |
|       4 | 0x1F2B      |        7979 |
|       5 | 0x0001      |           1 |
|       6 | 0x0000      |           0 |
|       7 | 0x1F2D      |        7981 |
|       8 | 0x1F2E      |        7982 |
|       9 | 0x002B      |          43 |
|      10 | 0x012C      |         300 |
|      11 | 0x010A      |         266 |
|      12 | 0x002A      |          42 |
|      13 | 0x1F2F      |        7983 |
|      14 | 0x00C8      |         200 |
|      15 | 0x003C      |          60 |
|      16 | 0x1F2C      |        7980 |
|      17 | 0x0022      |          34 |
|      18 | 0x1DF3      |        7667 |
|      19 | 0x1F30      |        7984 |

## String References

- **7667**: You saved me earlier! Thank you very much! You can have this...for free!
- **7976**: Hello... Y-you see, I... I'm t-training in the art of magic...
- **7977**: I-I've been practicing a s-spell that will tele...trans...send people to the faraway land of Jeuno...
- **7978**: W-would you like to be one of my t-test subjects?
- **7979**: Be a test subject? [Sounds like fun./Are you crazy?]
- **7980**: W-well, I don't b-blame you... I w-wish I was as s-skilled as my brother...
- **7981**: R-really!? Y-you're very b-brave!
- **7982**: P-probably best if you c-close your eyes...
- **7983**: Oops...
- **7984**: I-I'm terribly s-sorry... I s-seem to be out of m-magic. M-maybe you can h-help me out another t-time...?

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

### Event 103

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 279 bytes |
| Instructions | 43        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 20 01 79 00 F8 FF  FF 7F F0 FF FF 7F 66 00   B .y.........f.
0010: 80 F8 FF FF 7F F8 FF FF  7F 6D 6F 6A 30 1D 01 80  .........moj0...
0020: 23 1D 02 80 23 1D 03 80  23 24 04 80 05 80 06 80  #...#...#$......
0030: 25 02 00 10 06 80 00 CB  00 43 00 43 01 66 00 80  %........C.C.f..
0040: F8 FF FF 7F F8 FF FF 7F  77 61 69 30 1D 07 80 53  ........wai0...S
0050: F8 FF FF 7F F8 FF FF 7F  77 61 69 30 1D 08 80 66  ........wai0...f
0060: 09 80 F8 FF FF 7F F8 FF  FF 7F 63 61 62 6B 1C 0A  ..........cabk..
0070: 80 03 01 10 05 80 73 0B  80 F1 01 03 01 F0 FF FF  ......s.........
0080: 7F 66 09 80 F8 FF FF 7F  F8 FF FF 7F 73 70 65 66  .f..........spef
0090: 1C 0A 80 66 0C 80 F8 FF  FF 7F F8 FF FF 7F 62 69  ...f..........bi
00A0: 6B 30 1D 0D 80 53 F8 FF  FF 7F F8 FF FF 7F 62 69  k0...S........bi
00B0: 6B 30 45 0E 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  k0E..........fdo
00C0: 31 06 80 1C 0F 80 46 00  01 05 01 02 00 10 05 80  1.....F.........
00D0: 00 05 01 66 00 80 F8 FF  FF 7F F8 FF FF 7F 67 6B  ...f..........gk
00E0: 72 30 53 F8 FF FF 7F F8  FF FF 7F 67 6B 72 30 1D  r0S........gkr0.
00F0: 10 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 67 6B  ..#f..........gk
0100: 72 31 01 05 01 66 11 80  F8 FF FF 7F F8 FF FF 7F  r1...f..........
0110: 74 6C 62 31 20 00 21 00                           tlb1 .!.        
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0004 [0x79] EventEntity looks at LocalPlayer (Basic look)
  3: 0x000E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "moj0" with entities [EventEntity, EventEntity], work=40*
  4: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=7976*)
    → "Hello... Y-you see, I... I'm t-training in the art of magic..."
  5: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=7977*)
    → "I-I've been practicing a s-spell that will tele...trans...send people to the faraway land of Jeuno..."
  7: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7978*)
    → "W-would you like to be one of my t-test subjects?"
  9: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0029 [0x24] CREATE_DIALOG(message_id=7979*, default_option=1*, option_flags=0*)
    → "Be a test subject? [Sounds like fun./Are you crazy?]"
 11: 0x0030 [0x25] WAIT_DIALOG_SELECT()
 12: 0x0031 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00CB
 13: 0x0039 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 14: 0x003B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 15: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wai0" with entities [EventEntity, EventEntity], work=40*
 16: 0x004C [0x1D] PRINT_EVENT_MESSAGE(message_id=7981*)
    → "R-really!? Y-you're very b-brave!"
 17: 0x004F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wai0" with entities [EventEntity, EventEntity]
 18: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=7982*)
    → "P-probably best if you c-close your eyes..."
 19: 0x005F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "cabk" with entities [EventEntity, EventEntity], work=43*
 20: 0x006E [0x1C] WAIT(300* ticks)
 21: 0x0071 [0x03] Work_Zone[1] = 1*
 22: 0x0076 [0x73] Shihu-Danhu (ID: 16974321/0x010301F1) casts magic 266* on LocalPlayer
 23: 0x0081 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "spef" with entities [EventEntity, EventEntity], work=43*
 24: 0x0090 [0x1C] WAIT(300* ticks)
 25: 0x0093 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=42*
 26: 0x00A2 [0x1D] PRINT_EVENT_MESSAGE(message_id=7983*)
    → "Oops..."
 27: 0x00A5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [EventEntity, EventEntity]
 28: 0x00B2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 29: 0x00C3 [0x1C] WAIT(60* ticks)
 30: 0x00C6 [0x46] CAMERA_CONTROL: Restore default settings
 31: 0x00C8 [0x01] GOTO 0x0105
 32: 0x00CB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0105
 33: 0x00D3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr0" with entities [EventEntity, EventEntity], work=40*
 34: 0x00E2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gkr0" with entities [EventEntity, EventEntity]
 35: 0x00EF [0x1D] PRINT_EVENT_MESSAGE(message_id=7980*)
    → "W-well, I don't b-blame you... I w-wish I was as s-skilled as my brother..."
 36: 0x00F2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x00F3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr1" with entities [EventEntity, EventEntity], work=40*
 38: 0x0102 [0x01] GOTO 0x0105

SUBROUTINE_0105:
 39: 0x0105 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=34*
 40: 0x0114 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 41: 0x0116 [0x21] END_EVENT
 42: 0x0117 [0x00] END_REQSTACK()
```

### Event 207

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0118   |
| Data Size    | 52 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                          43 00 43 01 20 01 42 03          C.C. .B.
0120: 01 10 05 80 1E F0 FF FF  7F 6F 70 1D 12 80 66 00  .........op...f.
0130: 80 F8 FF FF 7F F8 FF FF  7F 70 61 73 30 53 F8 FF  .........pas0S..
0140: FF 7F F8 FF FF 7F 70 61  73 30 21 00              ......pas0!.    
```

#### Opcodes

```
  0: 0x0118 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  1: 0x011A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  2: 0x011C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x011E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x011F [0x03] Work_Zone[1] = 1*
  5: 0x0124 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x0129 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x012A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x012B [0x1D] PRINT_EVENT_MESSAGE(message_id=7667*)
    → "You saved me earlier! Thank you very much! You can have this...for free!"
  9: 0x012E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=40*
 10: 0x013D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 11: 0x014A [0x21] END_EVENT
 12: 0x014B [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014C   |
| Data Size    | 64 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                      42 20 01 79              B .y
0150: 00 F8 FF FF 7F F0 FF FF  7F 66 00 80 F8 FF FF 7F  .........f......
0160: F8 FF FF 7F 67 6B 72 30  53 F8 FF FF 7F F8 FF FF  ....gkr0S.......
0170: 7F 67 6B 72 30 1D 13 80  23 66 00 80 F8 FF FF 7F  .gkr0...#f......
0180: F8 FF FF 7F 67 6B 72 31  20 00 21 00              ....gkr1 .!.    
```

#### Opcodes

```
  0: 0x014C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x014D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x014F [0x79] EventEntity looks at LocalPlayer (Basic look)
  3: 0x0159 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0168 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gkr0" with entities [EventEntity, EventEntity]
  5: 0x0175 [0x1D] PRINT_EVENT_MESSAGE(message_id=7984*)
    → "I-I'm terribly s-sorry... I s-seem to be out of m-magic. M-maybe you can h-help me out another t-time...?"
  6: 0x0178 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0179 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr1" with entities [EventEntity, EventEntity], work=40*
  8: 0x0188 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x018A [0x21] END_EVENT
 10: 0x018B [0x00] END_REQSTACK()
```
