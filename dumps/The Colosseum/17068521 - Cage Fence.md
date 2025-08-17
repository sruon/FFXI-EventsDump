# 17068521 - Cage Fence

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | The Colosseum (ID: 71) |
| Block Size       | 244 bytes              |
| Total Events     | 3                      |
| References Count | 8                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     12 |              4 |
| [900](#event-900)        | 0x000D       |    169 |             27 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C40      |        7232 |
|       1 | 0x1C3F      |        7231 |
|       2 | 0x0000      |           0 |
|       3 | 0x00D9      |         217 |
|       4 | 0x0001      |           1 |
|       5 | 0x0002      |           2 |
|       6 | 0x0003      |           3 |
|       7 | 0x0004      |           4 |

## String References

- **7231**: Peer through the fence? [View the center./View the red corner./View the blue corner./View the entire cage./Quit.]
- **7232**: 

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 27 01 E9  71 04 01 02 00            H..#'..q....   
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7232*]:
    → ""
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x27] REQ_SET(priority=0x01, entity_id=Cage Fence (ID: 17068521/0x010471E9), tag_num=0x02)
  3: 0x000C [0x00] END_REQSTACK()
```

### Event 900

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000D    |
| Data Size    | 169 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         20 01 42                .B
0010: 46 01 24 01 80 02 80 02  80 25 02 00 10 02 80 00  F.$......%......
0020: 3D 00 45 03 80 F0 FF FF  7F F0 FF FF 7F 70 71 31  =.E..........pq1
0030: 30 02 80 27 01 E9 71 04  01 01 01 B5 00 02 00 10  0..'..q.........
0040: 04 80 00 60 00 45 03 80  F0 FF FF 7F F0 FF FF 7F  ...`.E..........
0050: 70 71 31 31 02 80 27 01  E9 71 04 01 01 01 B5 00  pq11..'..q......
0060: 02 00 10 05 80 00 83 00  45 03 80 F0 FF FF 7F F0  ........E.......
0070: FF FF 7F 70 71 31 32 02  80 27 01 E9 71 04 01 01  ...pq12..'..q...
0080: 01 B5 00 02 00 10 06 80  00 A6 00 45 03 80 F0 FF  ...........E....
0090: FF 7F F0 FF FF 7F 70 71  31 33 02 80 27 01 E9 71  ......pq13..'..q
00A0: 04 01 01 01 B5 00 02 00  10 07 80 00 B5 00 46 00  ..............F.
00B0: 21 00 01 B5 00 00                                 !.....          
```

#### Opcodes

```
  0: 0x000D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x000F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0010 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0012 [0x24] CREATE_DIALOG(message_id=7231*, default_option=0*, option_flags=0*)
    → "Peer through the fence? [View the center./View the red corner./View the blue corner./View the entire cage./Quit.]"
  4: 0x0019 [0x25] WAIT_DIALOG_SELECT()
  5: 0x001A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003D
  6: 0x0022 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "pq10" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
  7: 0x0033 [0x27] REQ_SET(priority=0x01, entity_id=Cage Fence (ID: 17068521/0x010471E9), tag_num=0x01)
  8: 0x003A [0x01] GOTO 0x00B5
  9: 0x003D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0060
 10: 0x0045 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "pq11" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 11: 0x0056 [0x27] REQ_SET(priority=0x01, entity_id=Cage Fence (ID: 17068521/0x010471E9), tag_num=0x01)
 12: 0x005D [0x01] GOTO 0x00B5
 13: 0x0060 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0083
 14: 0x0068 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "pq12" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 15: 0x0079 [0x27] REQ_SET(priority=0x01, entity_id=Cage Fence (ID: 17068521/0x010471E9), tag_num=0x01)
 16: 0x0080 [0x01] GOTO 0x00B5
 17: 0x0083 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x00A6
 18: 0x008B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "pq13" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 19: 0x009C [0x27] REQ_SET(priority=0x01, entity_id=Cage Fence (ID: 17068521/0x010471E9), tag_num=0x01)
 20: 0x00A3 [0x01] GOTO 0x00B5
 21: 0x00A6 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x00B5
 22: 0x00AE [0x46] CAMERA_CONTROL: Restore default settings
 23: 0x00B0 [0x21] END_EVENT
 24: 0x00B1 [0x00] END_REQSTACK()

SUBROUTINE_00B5:
 25: 0x00B5 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00B2 [0x01] GOTO 0x00B5
```
