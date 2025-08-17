# 17531157 - Cermet Door

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 720 bytes                        |
| Total Events     | 5                                |
| References Count | 9                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [6](#event-6)         | 0x0001       |      5 |              3 |
| [7](#event-7)         | 0x0006       |      5 |              3 |
| [10](#event-10)       | 0x000B       |    218 |             34 |
| [16](#event-16)       | 0x00E5       |    417 |             61 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x55730     |      350000 |
|       2 | 0x00B9      |         185 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C8      |         200 |
|       6 | 0x0013      |          19 |
|       7 | 0x005E      |          94 |
|       8 | 0x009F      |         159 |

## String References

- **159**: The door is firmly shut. You might be able to open it if you had the key.
- **185**: Open the door? [Yes./No.]

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

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4C 1C 00 80 00                                  L....          
```

#### Opcodes

```
  0: 0x0001 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0002 [0x1C] WAIT(60* ticks)
  2: 0x0005 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   4D 1C  00 80 00                       M....     
```

#### Opcodes

```
  0: 0x0006 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0007 [0x1C] WAIT(60* ticks)
  2: 0x000A [0x00] END_REQSTACK()
```

### Event 10

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000B    |
| Data Size    | 218 bytes |
| Instructions | 34        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   3B F0 FF FF 7F             ;....
0010: 00 00 01 00 02 00 02 00  00 01 80 02 DD 00 24 02  ..............$.
0020: 80 03 80 04 80 25 02 00  10 04 80 00 CF 00 43 00  .....%........C.
0030: 43 01 46 01 42 45 05 80  F0 FF FF 7F F0 FF FF 7F  C.F.BE..........
0040: 66 64 6F 31 04 80 1C 00  80 38 06 80 29 01 F0 FF  fdo1.....8..)...
0050: FF 7F 1D 45 07 80 F0 FF  FF 7F F0 FF FF 7F 66 65  ...E..........fe
0060: 30 31 04 80 29 01 F0 FF  FF 7F 1E 45 05 80 F0 FF  01..)......E....
0070: FF 7F F0 FF FF 7F 66 64  69 31 04 80 1C 00 80 29  ......fdi1.....)
0080: 01 15 81 0B 01 01 45 07  80 F0 FF FF 7F F0 FF FF  ......E.........
0090: 7F 66 65 30 32 04 80 29  01 F0 FF FF 7F 1F 27 01  .fe02..)......'.
00A0: 15 81 0B 01 02 45 05 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
00B0: 66 64 6F 31 04 80 1C 00  80 45 05 80 F0 FF FF 7F  fdo1.....E......
00C0: F0 FF FF 7F 66 64 69 31  04 80 46 00 01 DA 00 02  ....fdi1..F.....
00D0: 00 10 03 80 00 DA 00 01  DA 00 01 E1 00 48 08 80  .............H..
00E0: 23 20 00 21 00                                    # .!.           
```

#### Opcodes

```
  0: 0x000B [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x0016 [0x02] IF !(ExtData[1]->WorkLocal[0] <= 350000*) GOTO 0x00DD
  2: 0x001E [0x24] CREATE_DIALOG(message_id=185*, default_option=1*, option_flags=0*)
    → "Open the door? [Yes./No.]"
  3: 0x0025 [0x25] WAIT_DIALOG_SELECT()
  4: 0x0026 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00CF
  5: 0x002E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0030 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0032 [0x46] CAMERA_CONTROL: Disable user control
  8: 0x0034 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0035 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0046 [0x1C] WAIT(60* ticks)
 11: 0x0049 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 12: 0x004C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x1D)
 13: 0x0053 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fe01" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 14: 0x0064 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x1E)
 15: 0x006B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x007C [0x1C] WAIT(60* ticks)
 17: 0x007F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Cermet Door (ID: 17531157/0x010B8115), tag_num=0x01)
 18: 0x0086 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fe02" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 19: 0x0097 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x1F)
 20: 0x009E [0x27] REQ_SET(priority=0x01, entity_id=Cermet Door (ID: 17531157/0x010B8115), tag_num=0x02)
 21: 0x00A5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x00B6 [0x1C] WAIT(60* ticks)
 23: 0x00B9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x00CA [0x46] CAMERA_CONTROL: Restore default settings
 25: 0x00CC [0x01] GOTO 0x00DA
 26: 0x00CF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00DA
 27: 0x00D7 [0x01] GOTO 0x00DA

SUBROUTINE_00DA:
 28: 0x00DA [0x01] GOTO 0x00E1
 29: 0x00DD [0x48] [System] [159*]:
    → "The door is firmly shut. You might be able to open it if you had the key."
 30: 0x00E0 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00E1:
 31: 0x00E1 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 32: 0x00E3 [0x21] END_EVENT
 33: 0x00E4 [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00E5    |
| Data Size    | 417 bytes |
| Instructions | 61        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                03 01 10  04 80 3B F0 FF FF 7F 00       .....;.....
00F0: 00 01 00 02 00 02 00 00  01 80 03 C1 01 24 02 80  .............$..
0100: 03 80 04 80 25 02 00 10  04 80 00 B3 01 43 00 43  ....%........C.C
0110: 01 46 01 42 45 05 80 F0  FF FF 7F F0 FF FF 7F 66  .F.BE..........f
0120: 64 6F 31 04 80 1C 00 80  38 06 80 29 01 F0 FF FF  do1.....8..)....
0130: 7F 21 45 07 80 F0 FF FF  7F F0 FF FF 7F 66 65 30  .!E..........fe0
0140: 32 04 80 29 01 F0 FF FF  7F 22 45 05 80 F0 FF FF  2..)....."E.....
0150: 7F F0 FF FF 7F 66 64 69  31 04 80 1C 00 80 29 01  .....fdi1.....).
0160: 15 81 0B 01 01 45 07 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0170: 66 65 30 31 04 80 29 01  F0 FF FF 7F 23 27 01 15  fe01..).....#'..
0180: 81 0B 01 02 45 05 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0190: 64 6F 31 04 80 1C 00 80  45 05 80 F0 FF FF 7F F0  do1.....E.......
01A0: FF FF 7F 66 64 69 31 04  80 46 00 03 01 10 03 80  ...fdi1..F......
01B0: 01 BE 01 02 00 10 03 80  00 BE 01 01 BE 01 01 82  ................
01C0: 02 24 02 80 03 80 04 80  25 02 00 10 04 80 00 77  .$......%......w
01D0: 02 43 00 43 01 46 01 42  45 05 80 F0 FF FF 7F F0  .C.C.F.BE.......
01E0: FF FF 7F 66 64 6F 31 04  80 1C 00 80 38 06 80 29  ...fdo1.....8..)
01F0: 01 F0 FF FF 7F 1D 45 07  80 F0 FF FF 7F F0 FF FF  ......E.........
0200: 7F 66 65 30 31 04 80 29  01 F0 FF FF 7F 1E 45 05  .fe01..)......E.
0210: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 04 80 1C  .........fdi1...
0220: 00 80 29 01 15 81 0B 01  01 45 07 80 F0 FF FF 7F  ..)......E......
0230: F0 FF FF 7F 66 65 30 32  04 80 29 01 F0 FF FF 7F  ....fe02..).....
0240: 1F 27 01 15 81 0B 01 02  45 05 80 F0 FF FF 7F F0  .'......E.......
0250: FF FF 7F 66 64 6F 31 04  80 1C 00 80 45 05 80 F0  ...fdo1.....E...
0260: FF FF 7F F0 FF FF 7F 66  64 69 31 04 80 46 00 03  .......fdi1..F..
0270: 01 10 03 80 01 82 02 02  00 10 03 80 00 82 02 01  ................
0280: 82 02 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x00E5 [0x03] Work_Zone[1] = 0*
  1: 0x00EA [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  2: 0x00F5 [0x02] IF !(ExtData[1]->WorkLocal[0] >= 350000*) GOTO 0x01C1
  3: 0x00FD [0x24] CREATE_DIALOG(message_id=185*, default_option=1*, option_flags=0*)
    → "Open the door? [Yes./No.]"
  4: 0x0104 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0105 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01B3
  6: 0x010D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x010F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x0111 [0x46] CAMERA_CONTROL: Disable user control
  9: 0x0113 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0114 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x0125 [0x1C] WAIT(60* ticks)
 12: 0x0128 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 13: 0x012B [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x21)
 14: 0x0132 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fe02" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 15: 0x0143 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x22)
 16: 0x014A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x015B [0x1C] WAIT(60* ticks)
 18: 0x015E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Cermet Door (ID: 17531157/0x010B8115), tag_num=0x01)
 19: 0x0165 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fe01" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 20: 0x0176 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x23)
 21: 0x017D [0x27] REQ_SET(priority=0x01, entity_id=Cermet Door (ID: 17531157/0x010B8115), tag_num=0x02)
 22: 0x0184 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x0195 [0x1C] WAIT(60* ticks)
 24: 0x0198 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x01A9 [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x01AB [0x03] Work_Zone[1] = 1*
 27: 0x01B0 [0x01] GOTO 0x01BE
 28: 0x01B3 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01BE
 29: 0x01BB [0x01] GOTO 0x01BE

SUBROUTINE_01BE:
 30: 0x01BE [0x01] GOTO 0x0282
 31: 0x01C1 [0x24] CREATE_DIALOG(message_id=185*, default_option=1*, option_flags=0*)
    → "Open the door? [Yes./No.]"
 32: 0x01C8 [0x25] WAIT_DIALOG_SELECT()
 33: 0x01C9 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0277
 34: 0x01D1 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x01D3 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x01D5 [0x46] CAMERA_CONTROL: Disable user control
 37: 0x01D7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 38: 0x01D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x01E9 [0x1C] WAIT(60* ticks)
 40: 0x01EC [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 41: 0x01EF [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x1D)
 42: 0x01F6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fe01" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 43: 0x0207 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x1E)
 44: 0x020E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 45: 0x021F [0x1C] WAIT(60* ticks)
 46: 0x0222 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=Cermet Door (ID: 17531157/0x010B8115), tag_num=0x01)
 47: 0x0229 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fe02" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 48: 0x023A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x1F)
 49: 0x0241 [0x27] REQ_SET(priority=0x01, entity_id=Cermet Door (ID: 17531157/0x010B8115), tag_num=0x02)
 50: 0x0248 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 51: 0x0259 [0x1C] WAIT(60* ticks)
 52: 0x025C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 53: 0x026D [0x46] CAMERA_CONTROL: Restore default settings
 54: 0x026F [0x03] Work_Zone[1] = 1*
 55: 0x0274 [0x01] GOTO 0x0282
 56: 0x0277 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0282
 57: 0x027F [0x01] GOTO 0x0282

SUBROUTINE_0282:
 58: 0x0282 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 59: 0x0284 [0x21] END_EVENT
 60: 0x0285 [0x00] END_REQSTACK()
```
