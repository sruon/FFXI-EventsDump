# 17031691 - Decorative Bronze Gate

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Halvung (ID: 62) |
| Block Size       | 264 bytes        |
| Total Events     | 2                |
| References Count | 11               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [206](#event-206)     | 0x0001       |    192 |             37 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0321      |         801 |
|       1 | 0x1CDE      |        7390 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0x1CE2      |        7394 |
|       5 | 0x00B4      |         180 |
|       6 | 0x00C8      |         200 |
|       7 | 0x003C      |          60 |
|       8 | 0x0013      |          19 |
|       9 | 0x00D9      |         217 |
|      10 | 0x00F0      |         240 |

## String References

- **7390**: Use the $3? [Yes./No.]
- **7394**: You rap on the gate using the same pattern you saw in the pictographs. You hear the creaking sound of a bar lifting on the other side of the gate.

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

### Event 206

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 192 bytes |
| Instructions | 37        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 20 01 03 02 10  00 80 24 01 80 02 80 03    . ......$.....
0010: 80 25 02 00 10 03 80 00  AD 00 43 00 43 01 46 01  .%........C.C.F.
0020: 42 48 04 80 1C 05 80 45  06 80 F0 FF FF 7F F0 FF  BH.....E........
0030: FF 7F 66 64 6F 31 03 80  1C 07 80 38 08 80 45 09  ..fdo1.....8..E.
0040: 80 F0 FF FF 7F F0 FF FF  7F 7A 36 32 61 03 80 29  .........z62a..)
0050: 01 F0 FF FF 7F 07 29 01  F0 FF FF 7F 05 45 06 80  ......)......E..
0060: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 03 80 1C 07  ........fdi1....
0070: 80 4C 1C 07 80 27 01 F0  FF FF 7F 06 1C 05 80 45  .L...'.........E
0080: 06 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 03 80  ..........fdo1..
0090: 1C 07 80 4D 46 00 1C 0A  80 45 06 80 F0 FF FF 7F  ...MF....E......
00A0: F0 FF FF 7F 66 64 69 31  03 80 01 BD 00 02 00 10  ....fdi1........
00B0: 02 80 00 BD 00 03 01 10  03 80 01 BD 00 20 00 21  ............. .!
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0005 [0x03] Work_Zone[2] = 801*
  3: 0x000A [0x24] CREATE_DIALOG(message_id=7390*, default_option=1*, option_flags=0*)
    → "Use the $3? [Yes./No.]"
  4: 0x0011 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0012 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00AD
  6: 0x001A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x001E [0x46] CAMERA_CONTROL: Disable user control
  9: 0x0020 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0021 [0x48] [System] [7394*]:
    → "You rap on the gate using the same pattern you saw in the pictographs. You hear the creaking sound of a bar lifting on the other side of the gate."
 11: 0x0024 [0x1C] WAIT(180* ticks)
 12: 0x0027 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0038 [0x1C] WAIT(60* ticks)
 14: 0x003B [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 15: 0x003E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z62a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 16: 0x004F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x07)
 17: 0x0056 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 18: 0x005D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x006E [0x1C] WAIT(60* ticks)
 20: 0x0071 [0x4C] EventEntity->StatusEvent = 8 // Open door
 21: 0x0072 [0x1C] WAIT(60* ticks)
 22: 0x0075 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x06)
 23: 0x007C [0x1C] WAIT(180* ticks)
 24: 0x007F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x0090 [0x1C] WAIT(60* ticks)
 26: 0x0093 [0x4D] EventEntity->StatusEvent = 9 // Close door
 27: 0x0094 [0x46] CAMERA_CONTROL: Restore default settings
 28: 0x0096 [0x1C] WAIT(240* ticks)
 29: 0x0099 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 30: 0x00AA [0x01] GOTO 0x00BD
 31: 0x00AD [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00BD
 32: 0x00B5 [0x03] Work_Zone[1] = 0*
 33: 0x00BA [0x01] GOTO 0x00BD

SUBROUTINE_00BD:
 34: 0x00BD [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 35: 0x00BF [0x21] END_EVENT
 36: 0x00C0 [0x00] END_REQSTACK()
```
