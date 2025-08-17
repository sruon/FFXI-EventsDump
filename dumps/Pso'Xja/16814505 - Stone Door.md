# 16814505 - Stone Door

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Pso'Xja (ID: 9) |
| Block Size       | 280 bytes       |
| Total Events     | 2               |
| References Count | 12              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [62](#event-62)       | 0x0001       |    206 |             38 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0254      |         596 |
|       1 | 0x1C57      |        7255 |
|       2 | 0x1C6A      |        7274 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C9      |         201 |
|       6 | 0x003C      |          60 |
|       7 | 0x0012      |          18 |
|       8 | 0x00A0      |         160 |
|       9 | 0x0096      |         150 |
|      10 | 0x00B4      |         180 |
|      11 | 0x00C8      |         200 |

## String References

- **7255**: The $3 is responding to the glow from the arch!
- **7274**: Touch the door? [Yes./No.]

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

### Event 62

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 206 bytes |
| Instructions | 38        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 02 10 00 80  48 01 80 23 24 02 80 03    ......H..#$...
0010: 80 04 80 25 02 00 10 04  80 00 C0 00 43 00 43 01  ...%........C.C.
0020: 46 01 42 45 05 80 F0 FF  FF 7F F0 FF FF 7F 77 68  F.BE..........wh
0030: 6F 31 04 80 1C 06 80 03  01 10 03 80 38 07 80 45  o1..........8..E
0040: 08 80 F0 FF FF 7F F0 FF  FF 7F 39 67 72 64 04 80  ..........9grd..
0050: 29 01 F0 FF FF 7F 2E 29  01 F0 FF FF 7F 2D 45 05  )......).....-E.
0060: 80 F0 FF FF 7F F0 FF FF  7F 77 68 69 31 04 80 1C  .........whi1...
0070: 06 80 1C 06 80 4C 1C 09  80 27 01 F0 FF FF 7F 2F  .....L...'...../
0080: 1C 0A 80 4D 1C 09 80 45  0B 80 F0 FF FF 7F F0 FF  ...M...E........
0090: FF 7F 66 64 6F 31 04 80  1C 06 80 52 08 80 F0 FF  ..fdo1.....R....
00A0: FF 7F F0 FF FF 7F 39 67  72 64 45 0B 80 F0 FF FF  ......9grdE.....
00B0: 7F F0 FF FF 7F 66 64 69  31 04 80 46 00 01 CB 00  .....fdi1..F....
00C0: 02 00 10 03 80 00 CB 00  01 CB 00 20 00 21 00     ........... .!. 
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] Work_Zone[2] = 596*
  2: 0x0008 [0x48] [System] [7255*]:
    → "The $3 is responding to the glow from the arch!"
  3: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000C [0x24] CREATE_DIALOG(message_id=7274*, default_option=1*, option_flags=0*)
    → "Touch the door? [Yes./No.]"
  5: 0x0013 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0014 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C0
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0020 [0x46] CAMERA_CONTROL: Disable user control
 10: 0x0022 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 11: 0x0023 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 12: 0x0034 [0x1C] WAIT(60* ticks)
 13: 0x0037 [0x03] Work_Zone[1] = 1*
 14: 0x003C [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
 15: 0x003F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9grd" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
 16: 0x0050 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x2E)
 17: 0x0057 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x2D)
 18: 0x005E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 19: 0x006F [0x1C] WAIT(60* ticks)
 20: 0x0072 [0x1C] WAIT(60* ticks)
 21: 0x0075 [0x4C] EventEntity->StatusEvent = 8 // Open door
 22: 0x0076 [0x1C] WAIT(150* ticks)
 23: 0x0079 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x2F)
 24: 0x0080 [0x1C] WAIT(180* ticks)
 25: 0x0083 [0x4D] EventEntity->StatusEvent = 9 // Close door
 26: 0x0084 [0x1C] WAIT(150* ticks)
 27: 0x0087 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 28: 0x0098 [0x1C] WAIT(60* ticks)
 29: 0x009B [0x52] END_LOAD_SCHEDULER: End scheduler "9grd" with entities [LocalPlayer, LocalPlayer], work=160*
 30: 0x00AA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 31: 0x00BB [0x46] CAMERA_CONTROL: Restore default settings
 32: 0x00BD [0x01] GOTO 0x00CB
 33: 0x00C0 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00CB
 34: 0x00C8 [0x01] GOTO 0x00CB

SUBROUTINE_00CB:
 35: 0x00CB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 36: 0x00CD [0x21] END_EVENT
 37: 0x00CE [0x00] END_REQSTACK()
```
