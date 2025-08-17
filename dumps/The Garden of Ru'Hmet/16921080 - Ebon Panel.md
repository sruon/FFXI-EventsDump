# 16921080 - Ebon Panel

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | The Garden of Ru'Hmet (ID: 35) |
| Block Size       | 728 bytes                      |
| Total Events     | 3                              |
| References Count | 13                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [121](#event-121)     | 0x0001       |    344 |             52 |
| [301](#event-301)     | 0x0159       |    300 |             42 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x02C4      |         708 |
|       1 | 0x1DDF      |        7647 |
|       2 | 0x1DE1      |        7649 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C8      |         200 |
|       6 | 0x003C      |          60 |
|       7 | 0x0013      |          19 |
|       8 | 0x005E      |          94 |
|       9 | 0x0078      |         120 |
|      10 | 0x00B4      |         180 |
|      11 | 0x00C9      |         201 |
|      12 | 0x00F0      |         240 |

## String References

- **7647**: The $3 is humming in response to the device...
- **7649**: Hold up the $3? [Yes./No.]

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

### Event 121

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 344 bytes |
| Instructions | 52        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 02 10 00 80  48 01 80 23 24 02 80 03    ......H..#$...
0010: 80 04 80 25 02 00 10 04  80 00 45 01 43 00 43 01  ...%......E.C.C.
0020: 46 01 42 45 05 80 F0 FF  FF 7F F0 FF FF 7F 66 64  F.BE..........fd
0030: 6F 31 04 80 1C 06 80 38  07 80 45 08 80 F0 FF FF  o1.....8..E.....
0040: 7F F0 FF FF 7F 74 6F 77  33 04 80 29 01 F7 31 02  .....tow3..)..1.
0050: 01 01 29 01 F0 FF FF 7F  07 1C 09 80 45 05 80 F0  ..).........E...
0060: FF FF 7F F0 FF FF 7F 66  64 69 31 04 80 1C 09 80  .......fdi1.....
0070: 2D F8 FF FF 7F F8 FF FF  7F 73 31 35 37 2D F8 FF  -........s157-..
0080: FF 7F F8 FF FF 7F 31 63  6F 6E 1C 0A 80 27 01 F5  ......1con...'..
0090: 31 02 01 0B 1C 0A 80 2D  F8 FF FF 7F F8 FF FF 7F  1......-........
00A0: 33 6D 69 7A 1C 09 80 27  01 F6 31 02 01 0B 1C 0A  3miz...'..1.....
00B0: 80 52 08 80 F0 FF FF 7F  F0 FF FF 7F 74 6F 77 33  .R..........tow3
00C0: 45 05 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 04  E..........ovl1.
00D0: 80 45 08 80 F0 FF FF 7F  F0 FF FF 7F 74 6F 77 34  .E..........tow4
00E0: 04 80 29 01 F7 31 02 01  02 1C 0A 80 45 0B 80 F0  ..)..1......E...
00F0: FF FF 7F F0 FF FF 7F 77  68 6F 31 04 80 1C 06 80  .......who1.....
0100: 27 01 F6 31 02 01 0C 1C  0C 80 52 08 80 F0 FF FF  '..1......R.....
0110: 7F F0 FF FF 7F 74 6F 77  34 03 01 10 03 80 27 01  .....tow4.....'.
0120: F5 31 02 01 0C 27 01 F7  31 02 01 03 46 00 1C 09  .1...'..1...F...
0130: 80 45 0B 80 F0 FF FF 7F  F0 FF FF 7F 77 68 69 31  .E..........whi1
0140: 04 80 01 55 01 02 00 10  03 80 00 55 01 03 01 10  ...U.......U....
0150: 04 80 01 55 01 20 00 21  00                       ...U. .!.       
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] Work_Zone[2] = 708*
  2: 0x0008 [0x48] [System] [7647*]:
    → "The $3 is humming in response to the device..."
  3: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000C [0x24] CREATE_DIALOG(message_id=7649*, default_option=1*, option_flags=0*)
    → "Hold up the $3? [Yes./No.]"
  5: 0x0013 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0014 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0145
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0020 [0x46] CAMERA_CONTROL: Disable user control
 10: 0x0022 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 11: 0x0023 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x0034 [0x1C] WAIT(60* ticks)
 13: 0x0037 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 14: 0x003A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "tow3" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 15: 0x004B [0x29] REQ_SET_WAIT(priority=0x01, entity_id=??? (ID: 16921079/0x010231F7), tag_num=0x01)
 16: 0x0052 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x07)
 17: 0x0059 [0x1C] WAIT(120* ticks)
 18: 0x005C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x006D [0x1C] WAIT(120* ticks)
 20: 0x0070 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s157" with entities [EventEntity, EventEntity]
 21: 0x007D [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1con" with entities [EventEntity, EventEntity]
 22: 0x008A [0x1C] WAIT(180* ticks)
 23: 0x008D [0x27] REQ_SET(priority=0x01, entity_id=Ebon Panel (ID: 16921077/0x010231F5), tag_num=0x0B)
 24: 0x0094 [0x1C] WAIT(180* ticks)
 25: 0x0097 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "3miz" with entities [EventEntity, EventEntity]
 26: 0x00A4 [0x1C] WAIT(120* ticks)
 27: 0x00A7 [0x27] REQ_SET(priority=0x01, entity_id=4F_N_BOX (ID: 16921078/0x010231F6), tag_num=0x0B)
 28: 0x00AE [0x1C] WAIT(180* ticks)
 29: 0x00B1 [0x52] END_LOAD_SCHEDULER: End scheduler "tow3" with entities [LocalPlayer, LocalPlayer], work=94*
 30: 0x00C0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x00D1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "tow4" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 32: 0x00E2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=??? (ID: 16921079/0x010231F7), tag_num=0x02)
 33: 0x00E9 [0x1C] WAIT(180* ticks)
 34: 0x00EC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 35: 0x00FD [0x1C] WAIT(60* ticks)
 36: 0x0100 [0x27] REQ_SET(priority=0x01, entity_id=4F_N_BOX (ID: 16921078/0x010231F6), tag_num=0x0C)
 37: 0x0107 [0x1C] WAIT(240* ticks)
 38: 0x010A [0x52] END_LOAD_SCHEDULER: End scheduler "tow4" with entities [LocalPlayer, LocalPlayer], work=94*
 39: 0x0119 [0x03] Work_Zone[1] = 1*
 40: 0x011E [0x27] REQ_SET(priority=0x01, entity_id=Ebon Panel (ID: 16921077/0x010231F5), tag_num=0x0C)
 41: 0x0125 [0x27] REQ_SET(priority=0x01, entity_id=??? (ID: 16921079/0x010231F7), tag_num=0x03)
 42: 0x012C [0x46] CAMERA_CONTROL: Restore default settings
 43: 0x012E [0x1C] WAIT(120* ticks)
 44: 0x0131 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 45: 0x0142 [0x01] GOTO 0x0155
 46: 0x0145 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0155
 47: 0x014D [0x03] Work_Zone[1] = 0*
 48: 0x0152 [0x01] GOTO 0x0155

SUBROUTINE_0155:
 49: 0x0155 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 50: 0x0157 [0x21] END_EVENT
 51: 0x0158 [0x00] END_REQSTACK()
```

### Event 301

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0159    |
| Data Size    | 300 bytes |
| Instructions | 42        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                             20 01 43 00 43 01 46            .C.C.F
0160: 01 42 45 05 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  .BE..........fdo
0170: 31 04 80 1C 06 80 38 07  80 45 08 80 F0 FF FF 7F  1.....8..E......
0180: F0 FF FF 7F 74 6F 77 33  04 80 29 01 F7 31 02 01  ....tow3..)..1..
0190: 01 29 01 F0 FF FF 7F 07  1C 09 80 45 05 80 F0 FF  .).........E....
01A0: FF 7F F0 FF FF 7F 66 64  69 31 04 80 1C 09 80 2D  ......fdi1.....-
01B0: F8 FF FF 7F F8 FF FF 7F  73 31 35 37 2D F8 FF FF  ........s157-...
01C0: 7F F8 FF FF 7F 31 63 6F  6E 1C 0A 80 27 01 F5 31  .....1con...'..1
01D0: 02 01 0B 1C 0A 80 2D F8  FF FF 7F F8 FF FF 7F 33  ......-........3
01E0: 6D 69 7A 1C 09 80 27 01  F6 31 02 01 0B 1C 0A 80  miz...'..1......
01F0: 52 08 80 F0 FF FF 7F F0  FF FF 7F 74 6F 77 33 45  R..........tow3E
0200: 05 80 F0 FF FF 7F F0 FF  FF 7F 6F 76 6C 31 04 80  ..........ovl1..
0210: 45 08 80 F0 FF FF 7F F0  FF FF 7F 74 6F 77 34 04  E..........tow4.
0220: 80 29 01 F7 31 02 01 02  1C 0A 80 45 0B 80 F0 FF  .)..1......E....
0230: FF 7F F0 FF FF 7F 77 68  6F 31 04 80 1C 06 80 27  ......who1.....'
0240: 01 F6 31 02 01 0C 1C 0C  80 52 08 80 F0 FF FF 7F  ..1......R......
0250: F0 FF FF 7F 74 6F 77 34  03 01 10 03 80 27 01 F5  ....tow4.....'..
0260: 31 02 01 0C 27 01 F7 31  02 01 03 46 00 1C 09 80  1...'..1...F....
0270: 45 0B 80 F0 FF FF 7F F0  FF FF 7F 77 68 69 31 04  E..........whi1.
0280: 80 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0159 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x015B [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  2: 0x015D [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  3: 0x015F [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0161 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0162 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x0173 [0x1C] WAIT(60* ticks)
  7: 0x0176 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x0179 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "tow3" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  9: 0x018A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=??? (ID: 16921079/0x010231F7), tag_num=0x01)
 10: 0x0191 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x07)
 11: 0x0198 [0x1C] WAIT(120* ticks)
 12: 0x019B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x01AC [0x1C] WAIT(120* ticks)
 14: 0x01AF [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s157" with entities [EventEntity, EventEntity]
 15: 0x01BC [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1con" with entities [EventEntity, EventEntity]
 16: 0x01C9 [0x1C] WAIT(180* ticks)
 17: 0x01CC [0x27] REQ_SET(priority=0x01, entity_id=Ebon Panel (ID: 16921077/0x010231F5), tag_num=0x0B)
 18: 0x01D3 [0x1C] WAIT(180* ticks)
 19: 0x01D6 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "3miz" with entities [EventEntity, EventEntity]
 20: 0x01E3 [0x1C] WAIT(120* ticks)
 21: 0x01E6 [0x27] REQ_SET(priority=0x01, entity_id=4F_N_BOX (ID: 16921078/0x010231F6), tag_num=0x0B)
 22: 0x01ED [0x1C] WAIT(180* ticks)
 23: 0x01F0 [0x52] END_LOAD_SCHEDULER: End scheduler "tow3" with entities [LocalPlayer, LocalPlayer], work=94*
 24: 0x01FF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x0210 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "tow4" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 26: 0x0221 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=??? (ID: 16921079/0x010231F7), tag_num=0x02)
 27: 0x0228 [0x1C] WAIT(180* ticks)
 28: 0x022B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 29: 0x023C [0x1C] WAIT(60* ticks)
 30: 0x023F [0x27] REQ_SET(priority=0x01, entity_id=4F_N_BOX (ID: 16921078/0x010231F6), tag_num=0x0C)
 31: 0x0246 [0x1C] WAIT(240* ticks)
 32: 0x0249 [0x52] END_LOAD_SCHEDULER: End scheduler "tow4" with entities [LocalPlayer, LocalPlayer], work=94*
 33: 0x0258 [0x03] Work_Zone[1] = 1*
 34: 0x025D [0x27] REQ_SET(priority=0x01, entity_id=Ebon Panel (ID: 16921077/0x010231F5), tag_num=0x0C)
 35: 0x0264 [0x27] REQ_SET(priority=0x01, entity_id=??? (ID: 16921079/0x010231F7), tag_num=0x03)
 36: 0x026B [0x46] CAMERA_CONTROL: Restore default settings
 37: 0x026D [0x1C] WAIT(120* ticks)
 38: 0x0270 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 39: 0x0281 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 40: 0x0283 [0x21] END_EVENT
 41: 0x0284 [0x00] END_REQSTACK()
```
