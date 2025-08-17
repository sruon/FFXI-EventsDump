# 17760334 - DoorDepartures Exit

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 328 bytes               |
| Total Events     | 4                       |
| References Count | 10                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [181](#event-181)     | 0x0001       |    163 |             31 |
| [183](#event-183)     | 0x00A4       |     21 |              6 |
| [184](#event-184)     | 0x00B9       |     71 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0DEA      |        3562 |
|       2 | 0x0DEB      |        3563 |
|       3 | 0x0000      |           0 |
|       4 | 0x0DE9      |        3561 |
|       5 | 0x00C8      |         200 |
|       6 | 0x003C      |          60 |
|       7 | 0x0DEF      |        3567 |
|       8 | 0x0DE8      |        3560 |
|       9 | 0x0DEC      |        3564 |

## String References

- **3563**: Board an airship? [Board./Catch the next one.]

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

### Event 181

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 163 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    29 0B F0 FF FF 7F 0B  02 07 10 00 80 00 80 00   )..............
0010: 4A 4C 00 0F 01 F0 FF FF  7F 2B 4C 00 0F 01 01 80  JL.......+L.....
0020: 23 24 02 80 00 80 03 80  25 02 00 10 03 80 00 7D  #$......%......}
0030: 00 42 46 01 4C 2B 4C 00  0F 01 04 80 23 29 0B F0  .BF.L+L.....#)..
0040: FF FF 7F 27 45 05 80 F8  FF FF 7F F8 FF FF 7F 66  ...'E..........f
0050: 64 6F 31 03 80 29 0B F0  FF FF 7F 28 4D 1C 06 80  do1..).....(M...
0060: 29 0B F0 FF FF 7F 25 45  05 80 F8 FF FF 7F F8 FF  ).....%E........
0070: FF 7F 66 64 69 31 03 80  46 00 01 7D 00 01 A0 00  ..fdi1..F..}....
0080: 29 0B F0 FF FF 7F 0D 02  08 10 00 80 00 A0 00 4A  )..............J
0090: 4D 00 0F 01 F0 FF FF 7F  2B 4D 00 0F 01 07 80 23  M.......+M.....#
00A0: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0001 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0B)
  1: 0x0008 [0x02] IF !(Work_Zone[7] == 1*) GOTO 0x0080
  2: 0x0010 [0x4A] Honorio (ID: 17760332/0x010F004C) looks at LocalPlayer
  3: 0x0019 [0x2B] Honorio (ID: 17760332/0x010F004C) [3562*]:
    → "You appear to have the necessary $3, but to board the next airship bound for Jeuno, we require a payment of $7 gil."
  4: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0021 [0x24] CREATE_DIALOG(message_id=3563*, default_option=1*, option_flags=0*)
    → "Board an airship? [Board./Catch the next one.]"
  6: 0x0028 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0029 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x007D
  8: 0x0031 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0032 [0x46] CAMERA_CONTROL: Disable user control
 10: 0x0034 [0x4C] EventEntity->StatusEvent = 8 // Open door
 11: 0x0035 [0x2B] Honorio (ID: 17760332/0x010F004C) [3561*]:
    → "Please proceed through this doorway."
 12: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x003D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x27)
 14: 0x0044 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 15: 0x0055 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x28)
 16: 0x005C [0x4D] EventEntity->StatusEvent = 9 // Close door
 17: 0x005D [0x1C] WAIT(60* ticks)
 18: 0x0060 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x25)
 19: 0x0067 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 20: 0x0078 [0x46] CAMERA_CONTROL: Restore default settings
 21: 0x007A [0x01] GOTO 0x007D

SUBROUTINE_007D:
 22: 0x007D [0x01] GOTO 0x00A0
 23: 0x0080 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0D)
 24: 0x0087 [0x02] IF !(Work_Zone[8] == 1*) GOTO 0x00A0
 25: 0x008F [0x4A] Breanainn (ID: 17760333/0x010F004D) looks at LocalPlayer
 26: 0x0098 [0x2B] Breanainn (ID: 17760333/0x010F004D) [3567*]:
    → "That door is for departures only. Arrivals to Windurst should pass through this door here."
 27: 0x009F [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00A0:
 28: 0x00A0 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x00A2 [0x21] END_EVENT
 30: 0x00A3 [0x00] END_REQSTACK()
```

### Event 183

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 21 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             4A 4C 00 0F  01 F0 FF FF 7F 2B 4C 00      JL.......+L.
00B0: 0F 01 08 80 23 20 00 21  00                       ....# .!.       
```

#### Opcodes

```
  0: 0x00A4 [0x4A] Honorio (ID: 17760332/0x010F004C) looks at LocalPlayer
  1: 0x00AD [0x2B] Honorio (ID: 17760332/0x010F004C) [3560*]:
    → "You cannot pass beyond these doors unless you have $6."
  2: 0x00B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B5 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  4: 0x00B7 [0x21] END_EVENT
  5: 0x00B8 [0x00] END_REQSTACK()
```

### Event 184

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 71 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             29 0B F0 FF FF 7F 0B           )......
00C0: 02 07 10 00 80 00 DC 00  4A 4C 00 0F 01 F0 FF FF  ........JL......
00D0: 7F 2B 4C 00 0F 01 09 80  23 01 FC 00 29 0B F0 FF  .+L.....#...)...
00E0: FF 7F 0D 02 08 10 00 80  00 FC 00 4A 4D 00 0F 01  ...........JM...
00F0: F0 FF FF 7F 2B 4D 00 0F  01 07 80 23 20 00 21 00  ....+M.....# .!.
```

#### Opcodes

```
  0: 0x00B9 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0B)
  1: 0x00C0 [0x02] IF !(Work_Zone[7] == 1*) GOTO 0x00DC
  2: 0x00C8 [0x4A] Honorio (ID: 17760332/0x010F004C) looks at LocalPlayer
  3: 0x00D1 [0x2B] Honorio (ID: 17760332/0x010F004C) [3564*]:
    → "Before you can ride on an airship, we require a payment of $7 gil from you."
  4: 0x00D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00D9 [0x01] GOTO 0x00FC
  6: 0x00DC [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0D)
  7: 0x00E3 [0x02] IF !(Work_Zone[8] == 1*) GOTO 0x00FC
  8: 0x00EB [0x4A] Breanainn (ID: 17760333/0x010F004D) looks at LocalPlayer
  9: 0x00F4 [0x2B] Breanainn (ID: 17760333/0x010F004D) [3567*]:
    → "That door is for departures only. Arrivals to Windurst should pass through this door here."
 10: 0x00FB [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00FC:
 11: 0x00FC [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x00FE [0x21] END_EVENT
 13: 0x00FF [0x00] END_REQSTACK()
```
