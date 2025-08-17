# 16879935 - Spatial Displacement

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Misareaux Coast (ID: 25) |
| Block Size       | 508 bytes                |
| Total Events     | 3                        |
| References Count | 10                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [550](#event-550)     | 0x0001       |    152 |             25 |
| [551](#event-551)     | 0x0099       |    284 |             43 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1BA0      |        7072 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x00A0      |         160 |
|       5 | 0x003C      |          60 |
|       6 | 0x0064      |         100 |
|       7 | 0x00F0      |         240 |
|       8 | 0x1BA5      |        7077 |
|       9 | 0x0002      |           2 |

## String References

- **7072**: Proceed onward? [Yes./No.]
- **7077**: Proceed to which area? [Riverne - Site #A01./Riverne - Site #B01./Turn back.]

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

### Event 550

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 152 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  02 80 25 02 00 10 02 80    .$......%.....
0010: 00 8A 00 42 43 00 43 01  45 03 80 F0 FF FF 7F F0  ...BC.C.E.......
0020: FF FF 7F 6F 76 6C 31 02  80 45 04 80 F0 FF FF 7F  ...ovl1..E......
0030: F0 FF FF 7F 62 61 68 31  02 80 03 01 10 01 80 1C  ....bah1........
0040: 05 80 29 01 F0 FF FF 7F  07 1C 06 80 45 03 80 F0  ..).........E...
0050: FF FF 7F F0 FF FF 7F 6F  76 6C 31 02 80 45 04 80  .......ovl1..E..
0060: F0 FF FF 7F F0 FF FF 7F  62 61 68 32 02 80 1C 07  ........bah2....
0070: 80 45 03 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
0080: 02 80 1C 05 80 46 00 01  95 00 02 00 10 01 80 00  .....F..........
0090: 95 00 01 95 00 20 00 21  00                       ..... .!.       
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7072*, default_option=1*, option_flags=0*)
    → "Proceed onward? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x008A
  4: 0x0013 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0014 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0016 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0018 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0029 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "bah1" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
  9: 0x003A [0x03] Work_Zone[1] = 1*
 10: 0x003F [0x1C] WAIT(60* ticks)
 11: 0x0042 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x07)
 12: 0x0049 [0x1C] WAIT(100* ticks)
 13: 0x004C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x005D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "bah2" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
 15: 0x006E [0x1C] WAIT(240* ticks)
 16: 0x0071 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x0082 [0x1C] WAIT(60* ticks)
 18: 0x0085 [0x46] CAMERA_CONTROL: Restore default settings
 19: 0x0087 [0x01] GOTO 0x0095
 20: 0x008A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0095
 21: 0x0092 [0x01] GOTO 0x0095

SUBROUTINE_0095:
 22: 0x0095 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 23: 0x0097 [0x21] END_EVENT
 24: 0x0098 [0x00] END_REQSTACK()
```

### Event 551

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0099    |
| Data Size    | 284 bytes |
| Instructions | 43        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             20 01 24 08 80 09 80            .$....
00A0: 02 80 25 02 00 10 02 80  00 22 01 42 43 00 43 01  ..%......".BC.C.
00B0: 45 03 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 02  E..........ovl1.
00C0: 80 45 04 80 F0 FF FF 7F  F0 FF FF 7F 62 61 68 31  .E..........bah1
00D0: 02 80 03 01 10 01 80 1C  05 80 29 01 F0 FF FF 7F  ..........).....
00E0: 07 1C 06 80 45 03 80 F0  FF FF 7F F0 FF FF 7F 6F  ....E..........o
00F0: 76 6C 31 02 80 45 04 80  F0 FF FF 7F F0 FF FF 7F  vl1..E..........
0100: 62 61 68 32 02 80 1C 07  80 45 03 80 F0 FF FF 7F  bah2.....E......
0110: F0 FF FF 7F 66 64 6F 31  02 80 1C 05 80 46 00 01  ....fdo1.....F..
0120: B1 01 02 00 10 01 80 00  A1 01 42 43 00 43 01 45  ..........BC.C.E
0130: 03 80 F0 FF FF 7F F0 FF  FF 7F 6F 76 6C 31 02 80  ..........ovl1..
0140: 45 04 80 F0 FF FF 7F F0  FF FF 7F 62 61 68 31 02  E..........bah1.
0150: 80 03 01 10 09 80 1C 05  80 29 01 F0 FF FF 7F 07  .........)......
0160: 1C 06 80 45 03 80 F0 FF  FF 7F F0 FF FF 7F 6F 76  ...E..........ov
0170: 6C 31 02 80 45 04 80 F0  FF FF 7F F0 FF FF 7F 62  l1..E..........b
0180: 61 68 32 02 80 1C 07 80  45 03 80 F0 FF FF 7F F0  ah2.....E.......
0190: FF FF 7F 66 64 6F 31 02  80 1C 05 80 46 00 01 B1  ...fdo1.....F...
01A0: 01 02 00 10 09 80 00 B1  01 03 01 10 02 80 01 B1  ................
01B0: 01 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0099 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x009B [0x24] CREATE_DIALOG(message_id=7077*, default_option=2*, option_flags=0*)
    → "Proceed to which area? [Riverne - Site #A01./Riverne - Site #B01./Turn back.]"
  2: 0x00A2 [0x25] WAIT_DIALOG_SELECT()
  3: 0x00A3 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0122
  4: 0x00AB [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x00AC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x00AE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x00B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x00C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "bah1" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
  9: 0x00D2 [0x03] Work_Zone[1] = 1*
 10: 0x00D7 [0x1C] WAIT(60* ticks)
 11: 0x00DA [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x07)
 12: 0x00E1 [0x1C] WAIT(100* ticks)
 13: 0x00E4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x00F5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "bah2" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
 15: 0x0106 [0x1C] WAIT(240* ticks)
 16: 0x0109 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x011A [0x1C] WAIT(60* ticks)
 18: 0x011D [0x46] CAMERA_CONTROL: Restore default settings
 19: 0x011F [0x01] GOTO 0x01B1
 20: 0x0122 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01A1
 21: 0x012A [0x42] SET_CLI_EVENT_CANCEL_DATA()
 22: 0x012B [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 23: 0x012D [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 24: 0x012F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x0140 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "bah1" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
 26: 0x0151 [0x03] Work_Zone[1] = 2*
 27: 0x0156 [0x1C] WAIT(60* ticks)
 28: 0x0159 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x07)
 29: 0x0160 [0x1C] WAIT(100* ticks)
 30: 0x0163 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x0174 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "bah2" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
 32: 0x0185 [0x1C] WAIT(240* ticks)
 33: 0x0188 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 34: 0x0199 [0x1C] WAIT(60* ticks)
 35: 0x019C [0x46] CAMERA_CONTROL: Restore default settings
 36: 0x019E [0x01] GOTO 0x01B1
 37: 0x01A1 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x01B1
 38: 0x01A9 [0x03] Work_Zone[1] = 0*
 39: 0x01AE [0x01] GOTO 0x01B1

SUBROUTINE_01B1:
 40: 0x01B1 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 41: 0x01B3 [0x21] END_EVENT
 42: 0x01B4 [0x00] END_REQSTACK()
```
