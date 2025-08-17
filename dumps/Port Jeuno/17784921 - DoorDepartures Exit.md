# 17784921 - DoorDepartures Exit

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Port Jeuno (ID: 246) |
| Block Size       | 420 bytes            |
| Total Events     | 5                    |
| References Count | 17                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [45](#event-45)       | 0x0001       |     54 |             11 |
| [35](#event-35)       | 0x0037       |     44 |              9 |
| [37](#event-37)       | 0x0063       |    154 |             27 |
| [41](#event-41)       | 0x00FD       |     62 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xE1C8      |       57800 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0009      |           9 |
|       3 | 0x1BAF      |        7087 |
|       4 | 0x1CE9      |        7401 |
|       5 | 0x1BB1      |        7089 |
|       6 | 0x1BB2      |        7090 |
|       7 | 0x0001      |           1 |
|       8 | 0x0000      |           0 |
|       9 | 0x0092      |         146 |
|      10 | 0x003C      |          60 |
|      11 | 0xFFFFCCE3  |  4294954211 |
|      12 | 0xE7CD      |       59341 |
|      13 | 0x1F41      |        8001 |
|      14 | 0x0C15      |        3093 |
|      15 | 0x1BC3      |        7107 |
|      16 | 0x1BB0      |        7088 |

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

### Event 45

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
0010: 80 03 32 00 03 02 10 01  80 03 03 10 02 80 4A 2E  ..2...........J.
0020: 60 0F 01 F0 FF FF 7F 2B  2E 60 0F 01 03 80 23 01  `......+.`....#.
0030: 35 00 1A 29 01 21 00                              5..).!.         
```

#### Opcodes

```
  0: 0x0001 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  1: 0x000C [0x02] IF !(ExtData[1]->WorkLocal[2] >= 57800*) GOTO 0x0032
  2: 0x0014 [0x03] Work_Zone[2] = 200*
  3: 0x0019 [0x03] Work_Zone[3] = 9*
  4: 0x001E [0x4A] Illauvolahaut (ID: 17784878/0x010F602E) looks at LocalPlayer
  5: 0x0027 [0x2B] Illauvolahaut (ID: 17784878/0x010F602E) [7087*]:
    → "This leads to departures. You'll need $6 and $0 gil to board."
  6: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002F [0x01] GOTO 0x0035
  8: 0x0032 [0x1A] CALL_SUBROUTINE(address=0x0129)

SUBROUTINE_0035:
  9: 0x0035 [0x21] END_EVENT
 10: 0x0036 [0x00] END_REQSTACK()
```

### Event 35

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 44 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      3B  F0 FF FF 7F 01 00 02 00         ;........
0040: 03 00 02 02 00 00 80 03  5E 00 4A 2E 60 0F 01 F0  ........^.J.`...
0050: FF FF 7F 2B 2E 60 0F 01  04 80 23 01 61 00 1A 29  ...+.`....#.a..)
0060: 01 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0037 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  1: 0x0042 [0x02] IF !(ExtData[1]->WorkLocal[2] >= 57800*) GOTO 0x005E
  2: 0x004A [0x4A] Illauvolahaut (ID: 17784878/0x010F602E) looks at LocalPlayer
  3: 0x0053 [0x2B] Illauvolahaut (ID: 17784878/0x010F602E) [7401*]:
    → "This is the departure gate for airship passengers. If you have any questions, please inquire with Guddal."
  4: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x005B [0x01] GOTO 0x0061
  6: 0x005E [0x1A] CALL_SUBROUTINE(address=0x0129)

SUBROUTINE_0061:
  7: 0x0061 [0x21] END_EVENT
  8: 0x0062 [0x00] END_REQSTACK()
```

### Event 37

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0063    |
| Data Size    | 154 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          3B F0 FF FF 7F  01 00 02 00 03 00 02 02     ;............
0070: 00 00 80 03 F8 00 03 09  10 01 80 4A 2E 60 0F 01  ...........J.`..
0080: F0 FF FF 7F 2B 2E 60 0F  01 05 80 23 24 06 80 07  ....+.`....#$...
0090: 80 08 80 25 02 00 10 08  80 00 F5 00 42 27 0A F0  ...%........B'..
00A0: FF FF 7F 19 46 01 4C 45  09 80 F0 FF FF 7F F0 FF  ....F.LE........
00B0: FF 7F 6B 7A 30 30 08 80  2A 0A F0 FF FF 7F 4D 1C  ..kz00..*.....M.
00C0: 0A 80 45 01 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
00D0: 30 08 80 47 00 0B 80 0C  80 0D 80 0E 80 47 01 46  0..G.........G.F
00E0: 00 45 01 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 30  .E..........fdi0
00F0: 08 80 01 F5 00 01 FB 00  1A 29 01 21 00           .........).!.   
```

#### Opcodes

```
  0: 0x0063 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  1: 0x006E [0x02] IF !(ExtData[1]->WorkLocal[2] >= 57800*) GOTO 0x00F8
  2: 0x0076 [0x03] Work_Zone[9] = 200*
  3: 0x007B [0x4A] Illauvolahaut (ID: 17784878/0x010F602E) looks at LocalPlayer
  4: 0x0084 [0x2B] Illauvolahaut (ID: 17784878/0x010F602E) [7089*]:
    → "This leads to departures. You'll need $7 gil to board a flight."
  5: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008C [0x24] CREATE_DIALOG(message_id=7090*, default_option=1*, option_flags=0*)
    → "Pay $7 gil and head through? [Yes./No.]"
  7: 0x0093 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0094 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F5
  9: 0x009C [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x009D [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x19)
 11: 0x00A4 [0x46] CAMERA_CONTROL: Disable user control
 12: 0x00A6 [0x4C] EventEntity->StatusEvent = 8 // Open door
 13: 0x00A7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "kz00" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 14: 0x00B8 [0x2A] GET_REQ_LEVEL(level=10, entity_id=LocalPlayer)
 15: 0x00BE [0x4D] EventEntity->StatusEvent = 9 // Close door
 16: 0x00BF [0x1C] WAIT(60* ticks)
 17: 0x00C2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x00D3 [0x47] UPDATE_PLAYER_POS(-13.085*, 59.341*, 8.001*, yaw=271.8°*)
 19: 0x00DD [0x47] WAIT_PLAYER_POS_UPDATE
 20: 0x00DF [0x46] CAMERA_CONTROL: Restore default settings
 21: 0x00E1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x00F2 [0x01] GOTO 0x00F5

SUBROUTINE_00F5:
 23: 0x00F5 [0x01] GOTO 0x00FB
 24: 0x00F8 [0x1A] CALL_SUBROUTINE(address=0x0129)

SUBROUTINE_00FB:
 25: 0x00FB [0x21] END_EVENT
 26: 0x00FC [0x00] END_REQSTACK()
```

### Event 41

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FD   |
| Data Size    | 62 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                         3B F0 FF               ;..
0100: FF 7F 01 00 02 00 03 00  02 02 00 00 80 03 24 01  ..............$.
0110: 4A 2E 60 0F 01 F0 FF FF  7F 2B 2E 60 0F 01 0F 80  J.`......+.`....
0120: 23 01 27 01 1A 29 01 21  00 4A 2D 60 0F 01 F0 FF  #.'..).!.J-`....
0130: FF 7F 2B 2D 60 0F 01 10  80 23 1B                 ..+-`....#.     
```

#### Opcodes

```
  0: 0x00FD [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  1: 0x0108 [0x02] IF !(ExtData[1]->WorkLocal[2] >= 57800*) GOTO 0x0124
  2: 0x0110 [0x4A] Illauvolahaut (ID: 17784878/0x010F602E) looks at LocalPlayer
  3: 0x0119 [0x2B] Illauvolahaut (ID: 17784878/0x010F602E) [7107*]:
    → "I'm sorry, but your boarding rights have been temporarily revoked. Have a nice day."
  4: 0x0120 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0121 [0x01] GOTO 0x0127
  6: 0x0124 [0x1A] CALL_SUBROUTINE(address=0x0129)

SUBROUTINE_0127:
  7: 0x0127 [0x21] END_EVENT
  8: 0x0128 [0x00] END_REQSTACK()

SUBROUTINE_0129:
  9: 0x0129 [0x4A] Tautorie (ID: 17784877/0x010F602D) looks at LocalPlayer
 10: 0x0132 [0x2B] Tautorie (ID: 17784877/0x010F602D) [7088*]:
    → "This is the departures exit. You can't go out this way. Try the next door, please."
 11: 0x0139 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x013A [0x1B] RETURN
```
