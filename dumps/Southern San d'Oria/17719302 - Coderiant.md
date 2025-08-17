# 17719302 - Coderiant

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 432 bytes                     |
| Total Events     | 2                             |
| References Count | 19                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [583](#event-583)     | 0x0001       |    330 |             68 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0008      |           8 |
|       1 | 0x0014      |          20 |
|       2 | 0x2011      |        8209 |
|       3 | 0x2012      |        8210 |
|       4 | 0x0000      |           0 |
|       5 | 0x0623      |        1571 |
|       6 | 0x2013      |        8211 |
|       7 | 0x001E      |          30 |
|       8 | 0x0001      |           1 |
|       9 | 0x0EAC      |        3756 |
|      10 | 0x2014      |        8212 |
|      11 | 0x2ECA      |       11978 |
|      12 | 0x0002      |           2 |
|      13 | 0x2EDD      |       11997 |
|      14 | 0x0015      |          21 |
|      15 | 0x2EDE      |       11998 |
|      16 | 0x2EDF      |       11999 |
|      17 | 0x2EF5      |       12021 |
|      18 | 0x2EF6      |       12022 |

## String References

- **8209**: Are you lost? I know this neighborhood well.
- **8210**: Which way are you going? [Left./Right.]
- **8211**: There on Pikeman's Way you can find a grocer, sundries and the Tanners' Guild. At the end lies the mansion of Count Caffaule.
- **8212**: Go up those stairs for Watchdog Alley. Homes of townsfolk line the street.
- **11978**: Ask if this person is the chick's owner? [Yes./No.]
- **11997**: You have my chocobo?
- **11998**: My family was opposed to having a chocobo as a pet, so I raised her in secret. But one day, they found her... I...I had to let her go...
- **11999**: There must be a way for chocobos and people to live together in peace! Here, let me teach you a story I often tell my chocobo...
- **12021**: You say you have my chocobo?
- **12022**: Although I have always granted my chocobo a measure of independence, I do give her proper care. You must be mistaken.

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

### Event 583

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 330 bytes |
| Instructions | 68        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    38 00 80 1E F0 FF FF  7F 6F 70 66 01 80 F8 FF   8.......opf....
0010: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 02 80 23 5E 69  ......tlk0...#^i
0020: 64 6C 30 24 03 80 04 80  04 80 25 02 00 10 04 80  dl0$......%.....
0030: 00 6D 00 39 05 80 6F 70  66 01 80 F8 FF FF 7F F8  .m.9..opf.......
0040: FF FF 7F 70 6F 69 31 1D  06 80 23 66 01 80 F8 FF  ...poi1...#f....
0050: FF 7F F8 FF FF 7F 70 6F  69 32 53 F8 FF FF 7F F8  ......poi2S.....
0060: FF FF 7F 70 6F 69 32 1C  07 80 01 AF 00 02 00 10  ...poi2.........
0070: 08 80 00 AF 00 39 09 80  6F 70 66 01 80 F8 FF FF  .....9..opf.....
0080: 7F F8 FF FF 7F 70 6F 69  31 1D 0A 80 23 66 01 80  .....poi1...#f..
0090: F8 FF FF 7F F8 FF FF 7F  70 6F 69 32 53 F8 FF FF  ........poi2S...
00A0: 7F F8 FF FF 7F 70 6F 69  32 1C 07 80 01 AF 00 03  .....poi2.......
00B0: 01 10 08 80 43 00 43 01  02 03 10 04 80 00 C8 00  ....C.C.........
00C0: 03 01 10 04 80 01 49 01  42 24 0B 80 08 80 04 80  ......I.B$......
00D0: 25 02 00 10 04 80 00 39  01 1E F0 FF FF 7F 1C 07  %......9........
00E0: 80 03 01 10 0C 80 43 00  43 01 02 03 10 08 80 00  ......C.C.......
00F0: 1F 01 1D 0D 80 23 66 0E  80 F8 FF FF 7F F8 FF FF  .....#f.........
0100: 7F 64 69 73 30 1D 0F 80  23 66 01 80 F8 FF FF 7F  .dis0...#f......
0110: F8 FF FF 7F 74 6C 6B 30  1D 10 80 23 01 36 01 1D  ....tlk0...#.6..
0120: 11 80 23 66 01 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0130: 6B 30 1D 12 80 23 01 49  01 02 00 10 08 80 00 49  k0...#.I.......I
0140: 01 03 01 10 04 80 01 49  01 21 00                 .......I.!.     
```

#### Opcodes

```
  0: 0x0001 [0x38] SET_CLIENT_EVENT_MODE(mode=8*)
  1: 0x0004 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0009 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=8209*)
    → "Are you lost? I know this neighborhood well."
  6: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  8: 0x0023 [0x24] CREATE_DIALOG(message_id=8210*, default_option=0*, option_flags=0*)
    → "Which way are you going? [Left./Right.]"
  9: 0x002A [0x25] WAIT_DIALOG_SELECT()
 10: 0x002B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x006D
 11: 0x0033 [0x39] SET_ENTITY_DIRECTION(direction=8.6°*)
 12: 0x0036 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 13: 0x0037 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 14: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=20*
 15: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=8211*)
    → "There on Pikeman's Way you can find a grocer, sundries and the Tanners' Guild. At the end lies the mansion of Count Caffaule."
 16: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x004B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi2" with entities [EventEntity, EventEntity], work=20*
 18: 0x005A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi2" with entities [EventEntity, EventEntity]
 19: 0x0067 [0x1C] WAIT(30* ticks)
 20: 0x006A [0x01] GOTO 0x00AF
 21: 0x006D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00AF
 22: 0x0075 [0x39] SET_ENTITY_DIRECTION(direction=20.6°*)
 23: 0x0078 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 24: 0x0079 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 25: 0x007A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=20*
 26: 0x0089 [0x1D] PRINT_EVENT_MESSAGE(message_id=8212*)
    → "Go up those stairs for Watchdog Alley. Homes of townsfolk line the street."
 27: 0x008C [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x008D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi2" with entities [EventEntity, EventEntity], work=20*
 29: 0x009C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi2" with entities [EventEntity, EventEntity]
 30: 0x00A9 [0x1C] WAIT(30* ticks)
 31: 0x00AC [0x01] GOTO 0x00AF

SUBROUTINE_00AF:
 32: 0x00AF [0x03] Work_Zone[1] = 1*
 33: 0x00B4 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 34: 0x00B6 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 35: 0x00B8 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x00C8
 36: 0x00C0 [0x03] Work_Zone[1] = 0*
 37: 0x00C5 [0x01] GOTO 0x0149
 38: 0x00C8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 39: 0x00C9 [0x24] CREATE_DIALOG(message_id=11978*, default_option=1*, option_flags=0*)
    → "Ask if this person is the chick's owner? [Yes./No.]"
 40: 0x00D0 [0x25] WAIT_DIALOG_SELECT()
 41: 0x00D1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0139
 42: 0x00D9 [0x1E] EventEntity looks at LocalPlayer and starts talking
 43: 0x00DE [0x1C] WAIT(30* ticks)
 44: 0x00E1 [0x03] Work_Zone[1] = 2*
 45: 0x00E6 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 46: 0x00E8 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 47: 0x00EA [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x011F
 48: 0x00F2 [0x1D] PRINT_EVENT_MESSAGE(message_id=11997*)
    → "You have my chocobo?"
 49: 0x00F5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x00F6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=21*
 51: 0x0105 [0x1D] PRINT_EVENT_MESSAGE(message_id=11998*)
    → "My family was opposed to having a chocobo as a pet, so I raised her in secret. But one day, they found her... I...I had to let her go..."
 52: 0x0108 [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x0109 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 54: 0x0118 [0x1D] PRINT_EVENT_MESSAGE(message_id=11999*)
    → "There must be a way for chocobos and people to live together in peace! Here, let me teach you a story I often tell my chocobo..."
 55: 0x011B [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x011C [0x01] GOTO 0x0136
 57: 0x011F [0x1D] PRINT_EVENT_MESSAGE(message_id=12021*)
    → "You say you have my chocobo?"
 58: 0x0122 [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x0123 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 60: 0x0132 [0x1D] PRINT_EVENT_MESSAGE(message_id=12022*)
    → "Although I have always granted my chocobo a measure of independence, I do give her proper care. You must be mistaken."
 61: 0x0135 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0136:
 62: 0x0136 [0x01] GOTO 0x0149
 63: 0x0139 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0149
 64: 0x0141 [0x03] Work_Zone[1] = 0*
 65: 0x0146 [0x01] GOTO 0x0149

SUBROUTINE_0149:
 66: 0x0149 [0x21] END_EVENT
 67: 0x014A [0x00] END_REQSTACK()
```
