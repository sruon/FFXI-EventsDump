# 17387984 - Wall of Dark Arts

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Davoi (ID: 149) |
| Block Size       | 312 bytes       |
| Total Events     | 5               |
| References Count | 8               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [54](#event-54)       | 0x0001       |     76 |             15 |
| [55](#event-55)       | 0x004D       |     54 |             12 |
| [56](#event-56)       | 0x0083       |     56 |             10 |
| [57](#event-57)       | 0x00BB       |     56 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFEEEFB  |  4294897403 |
|       1 | 0x1CC6      |        7366 |
|       2 | 0x0000      |           0 |
|       3 | 0x1CC7      |        7367 |
|       4 | 0x1CC3      |        7363 |
|       5 | 0x0004      |           4 |
|       6 | 0x00C8      |         200 |
|       7 | 0x003C      |          60 |

## String References

- **7363**: The Orc barrier seals it shut.
- **7366**: Enter the cave? [Yes./No.]
- **7367**: Leave the cave? [Yes./No.]

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

### Event 54

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 76 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    3B F0 FF FF 7F 00 00  01 00 02 00 02 01 00 00   ;..............
0010: 80 02 31 00 24 01 80 02  80 02 80 25 02 00 10 02  ..1.$......%....
0020: 80 00 2E 00 29 03 D0 51  09 01 03 01 2E 00 01 4B  ....)..Q.......K
0030: 00 24 03 80 02 80 02 80  25 02 00 10 02 80 00 4B  .$......%......K
0040: 00 29 03 D0 51 09 01 04  01 4B 00 21 00           .)..Q....K.!.   
```

#### Opcodes

```
  0: 0x0001 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x000C [0x02] IF !(ExtData[1]->WorkLocal[1] <= 4294897403*) GOTO 0x0031
  2: 0x0014 [0x24] CREATE_DIALOG(message_id=7366*, default_option=0*, option_flags=0*)
    → "Enter the cave? [Yes./No.]"
  3: 0x001B [0x25] WAIT_DIALOG_SELECT()
  4: 0x001C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x002E
  5: 0x0024 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Wall of Dark Arts (ID: 17387984/0x010951D0), tag_num=0x03)
  6: 0x002B [0x01] GOTO 0x002E

SUBROUTINE_002E:
  7: 0x002E [0x01] GOTO 0x004B
  8: 0x0031 [0x24] CREATE_DIALOG(message_id=7367*, default_option=0*, option_flags=0*)
    → "Leave the cave? [Yes./No.]"
  9: 0x0038 [0x25] WAIT_DIALOG_SELECT()
 10: 0x0039 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004B
 11: 0x0041 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Wall of Dark Arts (ID: 17387984/0x010951D0), tag_num=0x04)
 12: 0x0048 [0x01] GOTO 0x004B

SUBROUTINE_004B:
 13: 0x004B [0x21] END_EVENT
 14: 0x004C [0x00] END_REQSTACK()
```

### Event 55

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 54 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         3B F0 FF               ;..
0050: FF 7F 00 00 01 00 02 00  02 01 00 00 80 02 67 00  ..............g.
0060: 48 04 80 23 01 81 00 24  03 80 02 80 02 80 25 02  H..#...$......%.
0070: 00 10 02 80 00 81 00 29  03 D0 51 09 01 04 01 81  .......)..Q.....
0080: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x004D [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x0058 [0x02] IF !(ExtData[1]->WorkLocal[1] <= 4294897403*) GOTO 0x0067
  2: 0x0060 [0x48] [System] [7363*]:
    → "The Orc barrier seals it shut."
  3: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0064 [0x01] GOTO 0x0081
  5: 0x0067 [0x24] CREATE_DIALOG(message_id=7367*, default_option=0*, option_flags=0*)
    → "Leave the cave? [Yes./No.]"
  6: 0x006E [0x25] WAIT_DIALOG_SELECT()
  7: 0x006F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0081
  8: 0x0077 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Wall of Dark Arts (ID: 17387984/0x010951D0), tag_num=0x04)
  9: 0x007E [0x01] GOTO 0x0081

SUBROUTINE_0081:
 10: 0x0081 [0x21] END_EVENT
 11: 0x0082 [0x00] END_REQSTACK()
```

### Event 56

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0083   |
| Data Size    | 56 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:          42 43 00 43 01  38 05 80 45 06 80 F0 FF     BC.C.8..E....
0090: FF 7F F0 FF FF 7F 66 64  6F 31 02 80 1C 07 80 29  ......fdo1.....)
00A0: 03 F0 FF FF 7F 09 45 06  80 F0 FF FF 7F F0 FF FF  ......E.........
00B0: 7F 66 64 69 31 02 80 1C  07 80 00                 .fdi1......     
```

#### Opcodes

```
  0: 0x0083 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0084 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  2: 0x0086 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  3: 0x0088 [0x38] SET_CLIENT_EVENT_MODE(mode=4*)
  4: 0x008B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x009C [0x1C] WAIT(60* ticks)
  6: 0x009F [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x09)
  7: 0x00A6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x00B7 [0x1C] WAIT(60* ticks)
  9: 0x00BA [0x00] END_REQSTACK()
```

### Event 57

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 56 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   42 43 00 43 01             BC.C.
00C0: 38 05 80 45 06 80 F0 FF  FF 7F F0 FF FF 7F 66 64  8..E..........fd
00D0: 6F 31 02 80 1C 07 80 29  03 F0 FF FF 7F 0A 45 06  o1.....)......E.
00E0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 02 80 1C  .........fdi1...
00F0: 07 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00BB [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00BC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  2: 0x00BE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  3: 0x00C0 [0x38] SET_CLIENT_EVENT_MODE(mode=4*)
  4: 0x00C3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x00D4 [0x1C] WAIT(60* ticks)
  6: 0x00D7 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x0A)
  7: 0x00DE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x00EF [0x1C] WAIT(60* ticks)
  9: 0x00F2 [0x00] END_REQSTACK()
```
