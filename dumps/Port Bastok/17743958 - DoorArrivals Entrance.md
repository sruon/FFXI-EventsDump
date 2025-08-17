# 17743958 - DoorArrivals Entrance

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 252 bytes             |
| Total Events     | 5                     |
| References Count | 12                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [140](#event-140)        | 0x0001       |    160 |             25 |
| [52](#event-52)          | 0x00A1       |      2 |              2 |
| [65535.1](#event-655351) | 0x00A3       |      2 |              2 |
| [306](#event-306)        | 0x00A5       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFEC780  |  4294887296 |
|       1 | 0xFFFFAFDA  |  4294946778 |
|       2 | 0x1068      |        4200 |
|       3 | 0x1DB9      |        7609 |
|       4 | 0x1DBA      |        7610 |
|       5 | 0x1DBB      |        7611 |
|       6 | 0x0001      |           1 |
|       7 | 0x0000      |           0 |
|       8 | 0x00CA      |         202 |
|       9 | 0x0064      |         100 |
|      10 | 0x00C8      |         200 |
|      11 | 0x001E      |          30 |

## String References

- **7611**: Go in? [Yes./No.]

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

### Event 140

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 160 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    3B F0 FF FF 7F 01 00  02 00 03 00 64 00 00 01   ;..........d...
0010: 00 02 00 00 80 01 80 02  00 00 02 80 03 33 00 4A  .............3.J
0020: 13 C0 0E 01 F0 FF FF 7F  2B 13 C0 0E 01 03 80 23  ........+......#
0030: 01 9F 00 4A 43 C0 0E 01  F0 FF FF 7F 2B 43 C0 0E  ...JC.......+C..
0040: 01 04 80 23 24 05 80 06  80 07 80 25 02 00 10 07  ...#$......%....
0050: 80 00 9F 00 27 0A F0 FF  FF 7F 13 46 01 4C 45 08  ....'......F.LE.
0060: 80 F0 FF FF 7F F0 FF FF  7F 63 30 36 69 09 80 2A  .........c06i..*
0070: 0A F0 FF FF 7F 45 0A 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0080: 66 64 6F 30 07 80 1C 0B  80 46 00 45 0A 80 F0 FF  fdo0.....F.E....
0090: FF 7F F0 FF FF 7F 66 64  69 30 07 80 01 9F 00 21  ......fdi0.....!
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  1: 0x000C [0x64] CALCULATE_DISTANCE: ExtData[1]->WorkLocal[0] = distance between point1(ExtData[1]->WorkLocal[1], ExtData[1]->WorkLocal[2]) and point2(4294887296*, 4294946778*)
  2: 0x0017 [0x02] IF !(ExtData[1]->WorkLocal[0] >= 4200*) GOTO 0x0033
  3: 0x001F [0x4A] Bartolomeo (ID: 17743891/0x010EC013) looks at LocalPlayer
  4: 0x0028 [0x2B] Bartolomeo (ID: 17743891/0x010EC013) [7609*]:
    → "You can't get out to the pier this way. Only arriving passengers may go through these doors. Please go around to the entrance on the west side."
  5: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0030 [0x01] GOTO 0x009F
  7: 0x0033 [0x4A] Aishah (ID: 17743939/0x010EC043) looks at LocalPlayer
  8: 0x003C [0x2B] Aishah (ID: 17743939/0x010EC043) [7610*]:
    → "If you enter Bastok, you must pay again to board the airship. Would you like to proceed?"
  9: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0044 [0x24] CREATE_DIALOG(message_id=7611*, default_option=1*, option_flags=0*)
    → "Go in? [Yes./No.]"
 11: 0x004B [0x25] WAIT_DIALOG_SELECT()
 12: 0x004C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x009F
 13: 0x0054 [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x13)
 14: 0x005B [0x46] CAMERA_CONTROL: Disable user control
 15: 0x005D [0x4C] EventEntity->StatusEvent = 8 // Open door
 16: 0x005E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "c06i" with entities [LocalPlayer, LocalPlayer], work=[202*, 100*]
 17: 0x006F [0x2A] GET_REQ_LEVEL(level=10, entity_id=LocalPlayer)
 18: 0x0075 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0086 [0x1C] WAIT(30* ticks)
 20: 0x0089 [0x46] CAMERA_CONTROL: Restore default settings
 21: 0x008B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x009C [0x01] GOTO 0x009F

SUBROUTINE_009F:
 23: 0x009F [0x21] END_EVENT
 24: 0x00A0 [0x00] END_REQSTACK()
```

### Event 52

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A1  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    4D 00                                           M.             
```

#### Opcodes

```
  0: 0x00A1 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A3  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          4C 00                                       L.           
```

#### Opcodes

```
  0: 0x00A3 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x00A4 [0x00] END_REQSTACK()
```

### Event 306

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                00                                      .          
```

#### Opcodes

```
  0: 0x00A5 [0x00] END_REQSTACK()
```
