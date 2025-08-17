# 17784917 - DoorDepartures Exit

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Port Jeuno (ID: 246) |
| Block Size       | 368 bytes            |
| Total Events     | 4                    |
| References Count | 16                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [46](#event-46)       | 0x0001       |     54 |             11 |
| [38](#event-38)       | 0x0037       |    154 |             27 |
| [42](#event-42)       | 0x00D1       |     62 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xE1C8      |       57800 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0008      |           8 |
|       3 | 0x1BAF      |        7087 |
|       4 | 0x1BB1      |        7089 |
|       5 | 0x1BB2      |        7090 |
|       6 | 0x0001      |           1 |
|       7 | 0x0000      |           0 |
|       8 | 0x0092      |         146 |
|       9 | 0x003C      |          60 |
|      10 | 0xFFFED2F8  |  4294890232 |
|      11 | 0xE7CD      |       59341 |
|      12 | 0x1F41      |        8001 |
|      13 | 0x0C15      |        3093 |
|      14 | 0x1BC3      |        7107 |
|      15 | 0x1BB0      |        7088 |

## String References

- **7090**: Pay $7 gil and head through? [Yes./No.]

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

### Event 46

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 54 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    3B F0 FF FF 7F 01 00  02 00 03 00 02 02 00 00   ;..............
0010: 80 03 32 00 03 02 10 01  80 03 03 10 02 80 4A 0E  ..2...........J.
0020: 60 0F 01 F0 FF FF 7F 2B  0E 60 0F 01 03 80 23 01  `......+.`....#.
0030: 35 00 1A FD 00 21 00                              5....!.         
```

#### Opcodes

```
  0: 0x0001 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  1: 0x000C [0x02] IF !(ExtData[1]->WorkLocal[2] >= 57800*) GOTO 0x0032
  2: 0x0014 [0x03] Work_Zone[2] = 200*
  3: 0x0019 [0x03] Work_Zone[3] = 8*
  4: 0x001E [0x4A] Purequane (ID: 17784846/0x010F600E) looks at LocalPlayer
  5: 0x0027 [0x2B] Purequane (ID: 17784846/0x010F600E) [7087*]:
    → "This leads to departures. You'll need $6 and $0 gil to board."
  6: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002F [0x01] GOTO 0x0035
  8: 0x0032 [0x1A] CALL_SUBROUTINE(address=0x00FD)

SUBROUTINE_0035:
  9: 0x0035 [0x21] END_EVENT
 10: 0x0036 [0x00] END_REQSTACK()
```

### Event 38

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0037    |
| Data Size    | 154 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      3B  F0 FF FF 7F 01 00 02 00         ;........
0040: 03 00 02 02 00 00 80 03  CC 00 03 09 10 01 80 4A  ...............J
0050: 0E 60 0F 01 F0 FF FF 7F  2B 0E 60 0F 01 04 80 23  .`......+.`....#
0060: 24 05 80 06 80 07 80 25  02 00 10 07 80 00 C9 00  $......%........
0070: 42 27 0A F0 FF FF 7F 11  46 01 4C 45 08 80 F0 FF  B'......F.LE....
0080: FF 7F F0 FF FF 7F 63 6D  35 30 07 80 2A 0A F0 FF  ......cm50..*...
0090: FF 7F 4D 1C 09 80 45 01  80 F0 FF FF 7F F0 FF FF  ..M...E.........
00A0: 7F 66 64 6F 30 07 80 47  00 0A 80 0B 80 0C 80 0D  .fdo0..G........
00B0: 80 47 01 46 00 45 01 80  F0 FF FF 7F F0 FF FF 7F  .G.F.E..........
00C0: 66 64 69 30 07 80 01 C9  00 01 CF 00 1A FD 00 21  fdi0...........!
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x0037 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  1: 0x0042 [0x02] IF !(ExtData[1]->WorkLocal[2] >= 57800*) GOTO 0x00CC
  2: 0x004A [0x03] Work_Zone[9] = 200*
  3: 0x004F [0x4A] Purequane (ID: 17784846/0x010F600E) looks at LocalPlayer
  4: 0x0058 [0x2B] Purequane (ID: 17784846/0x010F600E) [7089*]:
    → "This leads to departures. You'll need $7 gil to board a flight."
  5: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0060 [0x24] CREATE_DIALOG(message_id=7090*, default_option=1*, option_flags=0*)
    → "Pay $7 gil and head through? [Yes./No.]"
  7: 0x0067 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0068 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C9
  9: 0x0070 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0071 [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x11)
 11: 0x0078 [0x46] CAMERA_CONTROL: Disable user control
 12: 0x007A [0x4C] EventEntity->StatusEvent = 8 // Open door
 13: 0x007B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm50" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 14: 0x008C [0x2A] GET_REQ_LEVEL(level=10, entity_id=LocalPlayer)
 15: 0x0092 [0x4D] EventEntity->StatusEvent = 9 // Close door
 16: 0x0093 [0x1C] WAIT(60* ticks)
 17: 0x0096 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x00A7 [0x47] UPDATE_PLAYER_POS(-77.064*, 59.341*, 8.001*, yaw=271.8°*)
 19: 0x00B1 [0x47] WAIT_PLAYER_POS_UPDATE
 20: 0x00B3 [0x46] CAMERA_CONTROL: Restore default settings
 21: 0x00B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x00C6 [0x01] GOTO 0x00C9

SUBROUTINE_00C9:
 23: 0x00C9 [0x01] GOTO 0x00CF
 24: 0x00CC [0x1A] CALL_SUBROUTINE(address=0x00FD)

SUBROUTINE_00CF:
 25: 0x00CF [0x21] END_EVENT
 26: 0x00D0 [0x00] END_REQSTACK()
```

### Event 42

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 62 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    3B F0 FF FF 7F 01 00  02 00 03 00 02 02 00 00   ;..............
00E0: 80 03 F8 00 4A 0E 60 0F  01 F0 FF FF 7F 2B 0E 60  ....J.`......+.`
00F0: 0F 01 0E 80 23 01 FB 00  1A FD 00 21 00 4A 0D 60  ....#......!.J.`
0100: 0F 01 F0 FF FF 7F 2B 0D  60 0F 01 0F 80 23 1B     ......+.`....#. 
```

#### Opcodes

```
  0: 0x00D1 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  1: 0x00DC [0x02] IF !(ExtData[1]->WorkLocal[2] >= 57800*) GOTO 0x00F8
  2: 0x00E4 [0x4A] Purequane (ID: 17784846/0x010F600E) looks at LocalPlayer
  3: 0x00ED [0x2B] Purequane (ID: 17784846/0x010F600E) [7107*]:
    → "I'm sorry, but your boarding rights have been temporarily revoked. Have a nice day."
  4: 0x00F4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00F5 [0x01] GOTO 0x00FB
  6: 0x00F8 [0x1A] CALL_SUBROUTINE(address=0x00FD)

SUBROUTINE_00FB:
  7: 0x00FB [0x21] END_EVENT
  8: 0x00FC [0x00] END_REQSTACK()

SUBROUTINE_00FD:
  9: 0x00FD [0x4A] Moulloie (ID: 17784845/0x010F600D) looks at LocalPlayer
 10: 0x0106 [0x2B] Moulloie (ID: 17784845/0x010F600D) [7088*]:
    → "This is the departures exit. You can't go out this way. Try the next door, please."
 11: 0x010D [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x010E [0x1B] RETURN
```
