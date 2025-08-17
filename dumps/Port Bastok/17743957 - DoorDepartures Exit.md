# 17743957 - DoorDepartures Exit

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 344 bytes             |
| Total Events     | 3                     |
| References Count | 15                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [141](#event-141)     | 0x0001       |    174 |             27 |
| [142](#event-142)     | 0x00AF       |     79 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF081C  |  4294903836 |
|       1 | 0xFFFFE10F  |  4294959375 |
|       2 | 0x1068      |        4200 |
|       3 | 0x00C8      |         200 |
|       4 | 0x1DB7      |        7607 |
|       5 | 0x1DB8      |        7608 |
|       6 | 0x0001      |           1 |
|       7 | 0x0000      |           0 |
|       8 | 0x00CA      |         202 |
|       9 | 0x0064      |         100 |
|      10 | 0xFFFF1E66  |  4294909542 |
|      11 | 0x0768      |        1896 |
|      12 | 0x1DB6      |        7606 |
|      13 | 0x0008      |           8 |
|      14 | 0x1DB5      |        7605 |

## String References

- **7608**: Pay $7 gil? [Yes./No.]

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

### Event 141

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 174 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    3B F0 FF FF 7F 01 00  02 00 03 00 64 00 00 01   ;..........d...
0010: 00 02 00 00 80 01 80 02  00 00 02 80 03 9C 00 03  ................
0020: 09 10 03 80 4A 41 C0 0E  01 F0 FF FF 7F 2B 41 C0  ....JA.......+A.
0030: 0E 01 04 80 23 24 05 80  06 80 07 80 25 02 00 10  ....#$......%...
0040: 07 80 00 99 00 27 0A F0  FF FF 7F 14 46 01 4C 45  .....'......F.LE
0050: 08 80 F0 FF FF 7F F0 FF  FF 7F 63 30 36 69 09 80  ..........c06i..
0060: 2A 0A F0 FF FF 7F 45 03  80 F0 FF FF 7F F0 FF FF  *.....E.........
0070: 7F 66 64 6F 30 07 80 47  00 0A 80 01 80 0B 80 07  .fdo0..G........
0080: 80 47 01 46 00 45 03 80  F0 FF FF 7F F0 FF FF 7F  .G.F.E..........
0090: 66 64 69 30 07 80 01 99  00 01 AD 00 4A 42 C0 0E  fdi0........JB..
00A0: 01 F0 FF FF 7F 2B 42 C0  0E 01 0C 80 23 21 00     .....+B.....#!. 
```

#### Opcodes

```
  0: 0x0001 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  1: 0x000C [0x64] CALCULATE_DISTANCE: ExtData[1]->WorkLocal[0] = distance between point1(ExtData[1]->WorkLocal[1], ExtData[1]->WorkLocal[2]) and point2(4294903836*, 4294959375*)
  2: 0x0017 [0x02] IF !(ExtData[1]->WorkLocal[0] >= 4200*) GOTO 0x009C
  3: 0x001F [0x03] Work_Zone[9] = 200*
  4: 0x0024 [0x4A] Rajesh (ID: 17743937/0x010EC041) looks at LocalPlayer
  5: 0x002D [0x2B] Rajesh (ID: 17743937/0x010EC041) [7607*]:
    → "Those doors lead to the airship embarkation area. You must pay $7 gil to pass through."
  6: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0035 [0x24] CREATE_DIALOG(message_id=7608*, default_option=1*, option_flags=0*)
    → "Pay $7 gil? [Yes./No.]"
  8: 0x003C [0x25] WAIT_DIALOG_SELECT()
  9: 0x003D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0099
 10: 0x0045 [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x14)
 11: 0x004C [0x46] CAMERA_CONTROL: Disable user control
 12: 0x004E [0x4C] EventEntity->StatusEvent = 8 // Open door
 13: 0x004F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "c06i" with entities [LocalPlayer, LocalPlayer], work=[202*, 100*]
 14: 0x0060 [0x2A] GET_REQ_LEVEL(level=10, entity_id=LocalPlayer)
 15: 0x0066 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0077 [0x47] UPDATE_PLAYER_POS(-57.754*, -7.921*, 1.896*, yaw=0.0°*)
 17: 0x0081 [0x47] WAIT_PLAYER_POS_UPDATE
 18: 0x0083 [0x46] CAMERA_CONTROL: Restore default settings
 19: 0x0085 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0096 [0x01] GOTO 0x0099

SUBROUTINE_0099:
 21: 0x0099 [0x01] GOTO 0x00AD
 22: 0x009C [0x4A] Varden (ID: 17743938/0x010EC042) looks at LocalPlayer
 23: 0x00A5 [0x2B] Varden (ID: 17743938/0x010EC042) [7606*]:
    → "Only departing passengers may pass through these doors. Please go around to the entrance on the south side."
 24: 0x00AC [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00AD:
 25: 0x00AD [0x21] END_EVENT
 26: 0x00AE [0x00] END_REQSTACK()
```

### Event 142

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 79 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               3B                 ;
00B0: F0 FF FF 7F 01 00 02 00  03 00 64 00 00 01 00 02  ..........d.....
00C0: 00 00 80 01 80 02 00 00  02 80 03 EB 00 03 02 10  ................
00D0: 03 80 03 03 10 0D 80 4A  41 C0 0E 01 F0 FF FF 7F  .......JA.......
00E0: 2B 41 C0 0E 01 0E 80 23  01 FC 00 4A 42 C0 0E 01  +A.....#...JB...
00F0: F0 FF FF 7F 2B 42 C0 0E  01 0C 80 23 21 00        ....+B.....#!.  
```

#### Opcodes

```
  0: 0x00AF [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  1: 0x00BA [0x64] CALCULATE_DISTANCE: ExtData[1]->WorkLocal[0] = distance between point1(ExtData[1]->WorkLocal[1], ExtData[1]->WorkLocal[2]) and point2(4294903836*, 4294959375*)
  2: 0x00C5 [0x02] IF !(ExtData[1]->WorkLocal[0] >= 4200*) GOTO 0x00EB
  3: 0x00CD [0x03] Work_Zone[2] = 200*
  4: 0x00D2 [0x03] Work_Zone[3] = 8*
  5: 0x00D7 [0x4A] Rajesh (ID: 17743937/0x010EC041) looks at LocalPlayer
  6: 0x00E0 [0x2B] Rajesh (ID: 17743937/0x010EC041) [7605*]:
    → "These doors lead to the airship embarkation area. You need $6 and $0 gil to pass through."
  7: 0x00E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00E8 [0x01] GOTO 0x00FC
  9: 0x00EB [0x4A] Varden (ID: 17743938/0x010EC042) looks at LocalPlayer
 10: 0x00F4 [0x2B] Varden (ID: 17743938/0x010EC042) [7606*]:
    → "Only departing passengers may pass through these doors. Please go around to the entrance on the south side."
 11: 0x00FB [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00FC:
 12: 0x00FC [0x21] END_EVENT
 13: 0x00FD [0x00] END_REQSTACK()
```
