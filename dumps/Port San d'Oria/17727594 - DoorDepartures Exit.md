# 17727594 - DoorDepartures Exit

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 240 bytes                 |
| Total Events     | 5                         |
| References Count | 9                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [604](#event-604)        | 0x0001       |      1 |              1 |
| [613](#event-613)        | 0x0002       |    160 |             28 |
| [65535.1](#event-655351) | 0x00A2       |      2 |              2 |
| [65535.2](#event-655352) | 0x00A4       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0400      |        1024 |
|       1 | 0x0C00      |        3072 |
|       2 | 0x0001      |           1 |
|       3 | 0x00C8      |         200 |
|       4 | 0x1DC1      |        7617 |
|       5 | 0x0000      |           0 |
|       6 | 0xFFFFD274  |  4294955636 |
|       7 | 0x6D0D      |       27917 |
|       8 | 0xFFFFE0C0  |  4294959296 |

## String References

- **7617**: Pay $0 gil and leave San d'Oria? [Yes./No.]

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

### Event 604

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 613

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 160 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       42 27 64 F0 FF FF  7F 26 2A 64 F0 FF FF 7F    B'd....&*d....
0010: 3A F0 FF FF 7F 00 00 02  00 00 00 80 02 2D 00 02  :............-..
0020: 00 00 01 80 03 2D 00 03  01 10 02 80 21 46 01 4A  .....-......!F.J
0030: 16 80 0E 01 F0 FF FF 7F  03 02 10 03 80 24 04 80  .............$..
0040: 02 80 05 80 25 02 00 10  05 80 00 9E 00 27 65 F0  ....%........'e.
0050: FF FF 7F 27 2A 65 F0 FF  FF 7F 4C 27 65 F0 FF FF  ...'*e....L'e...
0060: 7F 28 2A 65 F0 FF FF 7F  45 03 80 F0 FF FF 7F F0  .(*e....E.......
0070: FF FF 7F 66 64 6F 30 05  80 47 00 06 80 07 80 08  ...fdo0..G......
0080: 80 02 80 47 01 45 03 80  F0 FF FF 7F F0 FF FF 7F  ...G.E..........
0090: 66 64 69 30 05 80 03 01  10 05 80 01 9E 00 46 00  fdi0..........F.
00A0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0002 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0003 [0x27] REQ_SET(priority=0x64, entity_id=LocalPlayer, tag_num=0x26)
  2: 0x000A [0x2A] GET_REQ_LEVEL(level=100, entity_id=LocalPlayer)
  3: 0x0010 [0x3A] CONVERT_YAW_TO_BYTE(entity=LocalPlayer, result_destination=ExtData[1]->WorkLocal[0])
  4: 0x0017 [0x02] IF !(ExtData[1]->WorkLocal[0] <= 1024*) GOTO 0x002D
  5: 0x001F [0x02] IF !(ExtData[1]->WorkLocal[0] >= 3072*) GOTO 0x002D
  6: 0x0027 [0x03] Work_Zone[1] = 1*
  7: 0x002C [0x21] END_EVENT
  8: 0x002D [0x46] CAMERA_CONTROL: Disable user control
  9: 0x002F [0x4A] Anton (ID: 17727510/0x010E8016) looks at LocalPlayer
 10: 0x0038 [0x03] Work_Zone[2] = 200*
 11: 0x003D [0x24] CREATE_DIALOG(message_id=7617*, default_option=1*, option_flags=0*)
    → "Pay $0 gil and leave San d'Oria? [Yes./No.]"
 12: 0x0044 [0x25] WAIT_DIALOG_SELECT()
 13: 0x0045 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x009E
 14: 0x004D [0x27] REQ_SET(priority=0x65, entity_id=LocalPlayer, tag_num=0x27)
 15: 0x0054 [0x2A] GET_REQ_LEVEL(level=101, entity_id=LocalPlayer)
 16: 0x005A [0x4C] EventEntity->StatusEvent = 8 // Open door
 17: 0x005B [0x27] REQ_SET(priority=0x65, entity_id=LocalPlayer, tag_num=0x28)
 18: 0x0062 [0x2A] GET_REQ_LEVEL(level=101, entity_id=LocalPlayer)
 19: 0x0068 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x0079 [0x47] UPDATE_PLAYER_POS(-11.660*, 27.917*, -8.000*, yaw=0.1°*)
 21: 0x0083 [0x47] WAIT_PLAYER_POS_UPDATE
 22: 0x0085 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x0096 [0x03] Work_Zone[1] = 0*
 24: 0x009B [0x01] GOTO 0x009E

SUBROUTINE_009E:
 25: 0x009E [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x00A0 [0x21] END_EVENT
 27: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A2  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       4C 00                                         L.            
```

#### Opcodes

```
  0: 0x00A2 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A4  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             4D 00                                     M.          
```

#### Opcodes

```
  0: 0x00A4 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x00A5 [0x00] END_REQSTACK()
```
