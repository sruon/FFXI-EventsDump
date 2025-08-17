# 17428937 - Stone Picture Frame

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 908 bytes                     |
| Total Events     | 5                             |
| References Count | 15                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [50](#event-50)       | 0x0001       |    204 |             36 |
| [51](#event-51)       | 0x00CD       |    204 |             36 |
| [52](#event-52)       | 0x0199       |    200 |             34 |
| [53](#event-53)       | 0x0261       |    200 |             34 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CD8      |        7384 |
|       1 | 0x0000      |           0 |
|       2 | 0x00C8      |         200 |
|       3 | 0x003C      |          60 |
|       4 | 0x0013      |          19 |
|       5 | 0x1CD9      |        7385 |
|       6 | 0x0064      |         100 |
|       7 | 0x00EA      |         234 |
|       8 | 0x0014      |          20 |
|       9 | 0x0078      |         120 |
|      10 | 0x1CD6      |        7382 |
|      11 | 0x1CD7      |        7383 |
|      12 | 0x00C9      |         201 |
|      13 | 0x0001      |           1 |
|      14 | 0x1CD5      |        7381 |

## String References

- **7381**: You take one last, long look at the painting.
- **7382**: A hideous voice rings in your ears...
- **7383**: (That abomination has no place in my gallery!)
- **7384**: Hang $3 on the wall? [Yes./Not yet.]
- **7385**: You place $3 in the frame.

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

### Event 50

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 204 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 24 00 80 01  80 01 80 25 02 00 10 01    .B$......%....
0010: 80 00 BE 00 43 00 43 01  46 01 45 02 80 F0 FF FF  ....C.C.F.E.....
0020: 7F F0 FF FF 7F 66 64 6F  31 01 80 1C 03 80 4E 01  .....fdo1.....N.
0030: F0 FF FF 7F 38 04 80 48  05 80 1C 06 80 45 07 80  ....8..H.....E..
0040: F0 FF FF 7F F0 FF FF 7F  61 72 74 30 01 80 1C 08  ........art0....
0050: 80 2D F8 FF FF 7F F8 FF  FF 7F 73 30 30 30 45 02  .-........s000E.
0060: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 01 80 1C  .........fdi1...
0070: 09 80 48 0A 80 1C 03 80  48 0B 80 23 45 0C 80 F0  ..H.....H..#E...
0080: FF FF 7F F0 FF FF 7F 77  68 6F 31 01 80 1C 03 80  .......who1.....
0090: 2D F8 FF FF 7F F8 FF FF  7F 6B 69 6C 6C 46 00 4E  -........killF.N
00A0: 00 F0 FF FF 7F 45 0C 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
00B0: 77 68 69 31 01 80 03 01  10 0D 80 01 C9 00 02 00  whi1............
00C0: 10 0D 80 00 C9 00 01 C9  00 20 00 21 00           ......... .!.   
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x24] CREATE_DIALOG(message_id=7384*, default_option=0*, option_flags=0*)
    → "Hang $3 on the wall? [Yes./Not yet.]"
  3: 0x000B [0x25] WAIT_DIALOG_SELECT()
  4: 0x000C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00BE
  5: 0x0014 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0016 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0018 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x001A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x002B [0x1C] WAIT(60* ticks)
 10: 0x002E [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
 11: 0x0034 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0037 [0x48] [System] [7385*]:
    → "You place $3 in the frame."
 13: 0x003A [0x1C] WAIT(100* ticks)
 14: 0x003D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "art0" with entities [LocalPlayer, LocalPlayer], work=[234*, 0*]
 15: 0x004E [0x1C] WAIT(20* ticks)
 16: 0x0051 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s000" with entities [EventEntity, EventEntity]
 17: 0x005E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x006F [0x1C] WAIT(120* ticks)
 19: 0x0072 [0x48] [System] [7382*]:
    → "A hideous voice rings in your ears..."
 20: 0x0075 [0x1C] WAIT(60* ticks)
 21: 0x0078 [0x48] [System] [7383*]:
    → "(That abomination has no place in my gallery!)"
 22: 0x007B [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x007C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 24: 0x008D [0x1C] WAIT(60* ticks)
 25: 0x0090 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kill" with entities [EventEntity, EventEntity]
 26: 0x009D [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x009F [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 28: 0x00A5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 29: 0x00B6 [0x03] Work_Zone[1] = 1*
 30: 0x00BB [0x01] GOTO 0x00C9
 31: 0x00BE [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00C9
 32: 0x00C6 [0x01] GOTO 0x00C9

SUBROUTINE_00C9:
 33: 0x00C9 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 34: 0x00CB [0x21] END_EVENT
 35: 0x00CC [0x00] END_REQSTACK()
```

### Event 51

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00CD    |
| Data Size    | 204 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         20 01 42                .B
00D0: 24 00 80 01 80 01 80 25  02 00 10 01 80 00 8A 01  $......%........
00E0: 43 00 43 01 46 01 45 02  80 F0 FF FF 7F F0 FF FF  C.C.F.E.........
00F0: 7F 66 64 6F 31 01 80 1C  03 80 4E 01 F0 FF FF 7F  .fdo1.....N.....
0100: 38 04 80 48 05 80 1C 06  80 45 07 80 F0 FF FF 7F  8..H.....E......
0110: F0 FF FF 7F 61 72 74 30  01 80 1C 08 80 2D F8 FF  ....art0.....-..
0120: FF 7F F8 FF FF 7F 73 30  30 30 45 02 80 F0 FF FF  ......s000E.....
0130: 7F F0 FF FF 7F 66 64 69  31 01 80 1C 09 80 48 0A  .....fdi1.....H.
0140: 80 1C 03 80 48 0B 80 23  45 0C 80 F0 FF FF 7F F0  ....H..#E.......
0150: FF FF 7F 77 68 6F 31 01  80 1C 03 80 2D F8 FF FF  ...who1.....-...
0160: 7F F8 FF FF 7F 6B 69 6C  6C 46 00 4E 00 F0 FF FF  .....killF.N....
0170: 7F 45 0C 80 F0 FF FF 7F  F0 FF FF 7F 77 68 69 31  .E..........whi1
0180: 01 80 03 01 10 0D 80 01  95 01 02 00 10 0D 80 00  ................
0190: 95 01 01 95 01 20 00 21  00                       ..... .!.       
```

#### Opcodes

```
  0: 0x00CD [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00CF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00D0 [0x24] CREATE_DIALOG(message_id=7384*, default_option=0*, option_flags=0*)
    → "Hang $3 on the wall? [Yes./Not yet.]"
  3: 0x00D7 [0x25] WAIT_DIALOG_SELECT()
  4: 0x00D8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x018A
  5: 0x00E0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x00E2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x00E4 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x00E6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x00F7 [0x1C] WAIT(60* ticks)
 10: 0x00FA [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
 11: 0x0100 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0103 [0x48] [System] [7385*]:
    → "You place $3 in the frame."
 13: 0x0106 [0x1C] WAIT(100* ticks)
 14: 0x0109 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "art0" with entities [LocalPlayer, LocalPlayer], work=[234*, 0*]
 15: 0x011A [0x1C] WAIT(20* ticks)
 16: 0x011D [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s000" with entities [EventEntity, EventEntity]
 17: 0x012A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x013B [0x1C] WAIT(120* ticks)
 19: 0x013E [0x48] [System] [7382*]:
    → "A hideous voice rings in your ears..."
 20: 0x0141 [0x1C] WAIT(60* ticks)
 21: 0x0144 [0x48] [System] [7383*]:
    → "(That abomination has no place in my gallery!)"
 22: 0x0147 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x0148 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 24: 0x0159 [0x1C] WAIT(60* ticks)
 25: 0x015C [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kill" with entities [EventEntity, EventEntity]
 26: 0x0169 [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x016B [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 28: 0x0171 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 29: 0x0182 [0x03] Work_Zone[1] = 1*
 30: 0x0187 [0x01] GOTO 0x0195
 31: 0x018A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0195
 32: 0x0192 [0x01] GOTO 0x0195

SUBROUTINE_0195:
 33: 0x0195 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 34: 0x0197 [0x21] END_EVENT
 35: 0x0198 [0x00] END_REQSTACK()
```

### Event 52

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0199    |
| Data Size    | 200 bytes |
| Instructions | 34        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                             20 01 42 24 00 80 01            .B$...
01A0: 80 01 80 25 02 00 10 01  80 00 52 02 43 00 43 01  ...%......R.C.C.
01B0: 46 01 45 02 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  F.E..........fdo
01C0: 31 01 80 1C 03 80 4E 01  F0 FF FF 7F 38 04 80 48  1.....N.....8..H
01D0: 05 80 1C 06 80 45 07 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
01E0: 61 72 74 30 01 80 1C 08  80 2D F8 FF FF 7F F8 FF  art0.....-......
01F0: FF 7F 73 30 30 30 45 02  80 F0 FF FF 7F F0 FF FF  ..s000E.........
0200: 7F 66 64 69 31 01 80 1C  09 80 48 0E 80 1C 09 80  .fdi1.....H.....
0210: 45 02 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 01  E..........fdo1.
0220: 80 1C 03 80 2D F8 FF FF  7F F8 FF FF 7F 6B 69 6C  ....-........kil
0230: 6C 46 00 4E 00 F0 FF FF  7F 45 02 80 F0 FF FF 7F  lF.N.....E......
0240: F0 FF FF 7F 66 64 69 31  01 80 03 01 10 0D 80 01  ....fdi1........
0250: 5D 02 02 00 10 0D 80 00  5D 02 01 5D 02 20 00 21  ].......]..]. .!
0260: 00                                                .               
```

#### Opcodes

```
  0: 0x0199 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x019B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x019C [0x24] CREATE_DIALOG(message_id=7384*, default_option=0*, option_flags=0*)
    → "Hang $3 on the wall? [Yes./Not yet.]"
  3: 0x01A3 [0x25] WAIT_DIALOG_SELECT()
  4: 0x01A4 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0252
  5: 0x01AC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x01AE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x01B0 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x01B2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x01C3 [0x1C] WAIT(60* ticks)
 10: 0x01C6 [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
 11: 0x01CC [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x01CF [0x48] [System] [7385*]:
    → "You place $3 in the frame."
 13: 0x01D2 [0x1C] WAIT(100* ticks)
 14: 0x01D5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "art0" with entities [LocalPlayer, LocalPlayer], work=[234*, 0*]
 15: 0x01E6 [0x1C] WAIT(20* ticks)
 16: 0x01E9 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s000" with entities [EventEntity, EventEntity]
 17: 0x01F6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0207 [0x1C] WAIT(120* ticks)
 19: 0x020A [0x48] [System] [7381*]:
    → "You take one last, long look at the painting."
 20: 0x020D [0x1C] WAIT(120* ticks)
 21: 0x0210 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0221 [0x1C] WAIT(60* ticks)
 23: 0x0224 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kill" with entities [EventEntity, EventEntity]
 24: 0x0231 [0x46] CAMERA_CONTROL: Restore default settings
 25: 0x0233 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 26: 0x0239 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x024A [0x03] Work_Zone[1] = 1*
 28: 0x024F [0x01] GOTO 0x025D
 29: 0x0252 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x025D
 30: 0x025A [0x01] GOTO 0x025D

SUBROUTINE_025D:
 31: 0x025D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 32: 0x025F [0x21] END_EVENT
 33: 0x0260 [0x00] END_REQSTACK()
```

### Event 53

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0261    |
| Data Size    | 200 bytes |
| Instructions | 34        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:    20 01 42 24 00 80 01  80 01 80 25 02 00 10 01    .B$......%....
0270: 80 00 1A 03 43 00 43 01  46 01 45 02 80 F0 FF FF  ....C.C.F.E.....
0280: 7F F0 FF FF 7F 66 64 6F  31 01 80 1C 03 80 4E 01  .....fdo1.....N.
0290: F0 FF FF 7F 38 04 80 48  05 80 1C 06 80 45 07 80  ....8..H.....E..
02A0: F0 FF FF 7F F0 FF FF 7F  61 72 74 30 01 80 1C 08  ........art0....
02B0: 80 2D F8 FF FF 7F F8 FF  FF 7F 73 30 30 30 45 02  .-........s000E.
02C0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 01 80 1C  .........fdi1...
02D0: 09 80 48 0E 80 1C 09 80  45 02 80 F0 FF FF 7F F0  ..H.....E.......
02E0: FF FF 7F 66 64 6F 31 01  80 1C 03 80 2D F8 FF FF  ...fdo1.....-...
02F0: 7F F8 FF FF 7F 6B 69 6C  6C 46 00 4E 00 F0 FF FF  .....killF.N....
0300: 7F 45 02 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
0310: 01 80 03 01 10 0D 80 01  25 03 02 00 10 0D 80 00  ........%.......
0320: 25 03 01 25 03 20 00 21  00                       %..%. .!.       
```

#### Opcodes

```
  0: 0x0261 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0263 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0264 [0x24] CREATE_DIALOG(message_id=7384*, default_option=0*, option_flags=0*)
    → "Hang $3 on the wall? [Yes./Not yet.]"
  3: 0x026B [0x25] WAIT_DIALOG_SELECT()
  4: 0x026C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x031A
  5: 0x0274 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0276 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0278 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x027A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x028B [0x1C] WAIT(60* ticks)
 10: 0x028E [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
 11: 0x0294 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x0297 [0x48] [System] [7385*]:
    → "You place $3 in the frame."
 13: 0x029A [0x1C] WAIT(100* ticks)
 14: 0x029D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "art0" with entities [LocalPlayer, LocalPlayer], work=[234*, 0*]
 15: 0x02AE [0x1C] WAIT(20* ticks)
 16: 0x02B1 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s000" with entities [EventEntity, EventEntity]
 17: 0x02BE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x02CF [0x1C] WAIT(120* ticks)
 19: 0x02D2 [0x48] [System] [7381*]:
    → "You take one last, long look at the painting."
 20: 0x02D5 [0x1C] WAIT(120* ticks)
 21: 0x02D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x02E9 [0x1C] WAIT(60* ticks)
 23: 0x02EC [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kill" with entities [EventEntity, EventEntity]
 24: 0x02F9 [0x46] CAMERA_CONTROL: Restore default settings
 25: 0x02FB [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 26: 0x0301 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x0312 [0x03] Work_Zone[1] = 1*
 28: 0x0317 [0x01] GOTO 0x0325
 29: 0x031A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0325
 30: 0x0322 [0x01] GOTO 0x0325

SUBROUTINE_0325:
 31: 0x0325 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 32: 0x0327 [0x21] END_EVENT
 33: 0x0328 [0x00] END_REQSTACK()
```
