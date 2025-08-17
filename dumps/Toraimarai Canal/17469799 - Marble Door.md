# 17469799 - Marble Door

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Toraimarai Canal (ID: 169) |
| Block Size       | 496 bytes                  |
| Total Events     | 5                          |
| References Count | 12                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [70](#event-70)          | 0x0001       |     76 |             16 |
| [65535.1](#event-655351) | 0x004D       |    149 |             23 |
| [65535.2](#event-655352) | 0x00E2       |    183 |             32 |
| [69](#event-69)          | 0x0199       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x21DFD     |      138749 |
|       1 | 0x0002      |           2 |
|       2 | 0x0001      |           1 |
|       3 | 0x1D1B      |        7451 |
|       4 | 0x0000      |           0 |
|       5 | 0x1D1A      |        7450 |
|       6 | 0x00C8      |         200 |
|       7 | 0x003C      |          60 |
|       8 | 0x0012      |          18 |
|       9 | 0x00D3      |         211 |
|      10 | 0x0078      |         120 |
|      11 | 0x1D1D      |        7453 |

## String References

- **7450**: The door is sealed shut by some magical force.
- **7451**: A dreadful voice intones: "This door is guarded by the Four Servants."
- **7453**: Leave the Animastery? [Yes./No.]

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

### Event 70

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 76 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    3B F0 FF FF 7F 00 00  01 00 02 00 02 00 00 00   ;..............
0010: 80 02 1E 00 29 0E 67 91  0A 01 03 01 4B 00 02 05  ....).g.....K...
0020: 10 01 80 00 30 00 29 0E  67 91 0A 01 02 01 4B 00  ....0.).g.....K.
0030: 02 05 10 02 80 00 3F 00  48 03 80 23 01 4B 00 02  ......?.H..#.K..
0040: 05 10 04 80 00 4B 00 48  05 80 23 21 00           .....K.H..#!.   
```

#### Opcodes

```
  0: 0x0001 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x000C [0x02] IF !(ExtData[1]->WorkLocal[0] <= 138749*) GOTO 0x001E
  2: 0x0014 [0x29] REQ_SET_WAIT(priority=0x0E, entity_id=Marble Door (ID: 17469799/0x010A9167), tag_num=0x03)
  3: 0x001B [0x01] GOTO 0x004B
  4: 0x001E [0x02] IF !(Work_Zone[5] == 2*) GOTO 0x0030
  5: 0x0026 [0x29] REQ_SET_WAIT(priority=0x0E, entity_id=Marble Door (ID: 17469799/0x010A9167), tag_num=0x02)
  6: 0x002D [0x01] GOTO 0x004B
  7: 0x0030 [0x02] IF !(Work_Zone[5] == 1*) GOTO 0x003F
  8: 0x0038 [0x48] [System] [7451*]:
    → "A dreadful voice intones: "This door is guarded by the Four Servants.""
  9: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x003C [0x01] GOTO 0x004B
 11: 0x003F [0x02] IF !(Work_Zone[5] == 0*) GOTO 0x004B
 12: 0x0047 [0x48] [System] [7450*]:
    → "The door is sealed shut by some magical force."
 13: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_004B:
 14: 0x004B [0x21] END_EVENT
 15: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x004D    |
| Data Size    | 149 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         20 01 42                .B
0050: 46 01 45 06 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  F.E..........fdo
0060: 31 04 80 1C 07 80 38 08  80 29 0B F0 FF FF 7F 0A  1.....8..)......
0070: 29 0B F0 FF FF 7F 09 45  09 80 F8 FF FF 7F F8 FF  )......E........
0080: FF 7F 73 30 35 33 04 80  45 06 80 F0 FF FF 7F F0  ..s053..E.......
0090: FF FF 7F 66 64 69 31 04  80 4C 1C 0A 80 27 0B F0  ...fdi1..L...'..
00A0: FF FF 7F 0B 1C 0A 80 45  06 80 F0 FF FF 7F F0 FF  .......E........
00B0: FF 7F 66 64 6F 31 04 80  4D 1C 07 80 52 09 80 F8  ..fdo1..M...R...
00C0: FF FF 7F F8 FF FF 7F 73  30 35 33 45 06 80 F0 FF  .......s053E....
00D0: FF 7F F0 FF FF 7F 66 64  69 31 04 80 46 00 20 00  ......fdi1..F. .
00E0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x004D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x004F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0050 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0052 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0063 [0x1C] WAIT(60* ticks)
  5: 0x0066 [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
  6: 0x0069 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0A)
  7: 0x0070 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x09)
  8: 0x0077 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s053" with entities [EventEntity, EventEntity], work=[211*, 0*]
  9: 0x0088 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0099 [0x4C] EventEntity->StatusEvent = 8 // Open door
 11: 0x009A [0x1C] WAIT(120* ticks)
 12: 0x009D [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0B)
 13: 0x00A4 [0x1C] WAIT(120* ticks)
 14: 0x00A7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x00B8 [0x4D] EventEntity->StatusEvent = 9 // Close door
 16: 0x00B9 [0x1C] WAIT(60* ticks)
 17: 0x00BC [0x52] END_LOAD_SCHEDULER: End scheduler "s053" with entities [EventEntity, EventEntity], work=211*
 18: 0x00CB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x00DC [0x46] CAMERA_CONTROL: Restore default settings
 20: 0x00DE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 21: 0x00E0 [0x21] END_EVENT
 22: 0x00E1 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00E2    |
| Data Size    | 183 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:       20 01 42 24 0B 80  02 80 04 80 25 02 00 10     .B$......%...
00F0: 04 80 00 F8 00 01 07 01  02 00 10 02 80 00 07 01  ................
0100: 20 00 21 00 01 07 01 46  01 45 06 80 F0 FF FF 7F   .!....F.E......
0110: F0 FF FF 7F 66 64 6F 31  04 80 1C 07 80 38 08 80  ....fdo1.....8..
0120: 29 0B F0 FF FF 7F 0D 29  0B F0 FF FF 7F 0C 45 09  )......)......E.
0130: 80 F8 FF FF 7F F8 FF FF  7F 73 30 35 33 04 80 45  .........s053..E
0140: 06 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 04 80  ..........fdi1..
0150: 4C 1C 0A 80 27 0B F0 FF  FF 7F 0E 1C 0A 80 45 06  L...'.........E.
0160: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 04 80 4D  .........fdo1..M
0170: 1C 07 80 52 09 80 F8 FF  FF 7F F8 FF FF 7F 73 30  ...R..........s0
0180: 35 33 45 06 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  53E..........fdi
0190: 31 04 80 46 00 20 00 21  00                       1..F. .!.       
```

#### Opcodes

```
  0: 0x00E2 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00E4 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00E5 [0x24] CREATE_DIALOG(message_id=7453*, default_option=1*, option_flags=0*)
    → "Leave the Animastery? [Yes./No.]"
  3: 0x00EC [0x25] WAIT_DIALOG_SELECT()
  4: 0x00ED [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F8
  5: 0x00F5 [0x01] GOTO 0x0107
  6: 0x00F8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0107
  7: 0x0100 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0102 [0x21] END_EVENT
  9: 0x0103 [0x00] END_REQSTACK()

SUBROUTINE_0107:
 10: 0x0107 [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0109 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x011A [0x1C] WAIT(60* ticks)
 13: 0x011D [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
 14: 0x0120 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0D)
 15: 0x0127 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0C)
 16: 0x012E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s053" with entities [EventEntity, EventEntity], work=[211*, 0*]
 17: 0x013F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0150 [0x4C] EventEntity->StatusEvent = 8 // Open door
 19: 0x0151 [0x1C] WAIT(120* ticks)
 20: 0x0154 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x0E)
 21: 0x015B [0x1C] WAIT(120* ticks)
 22: 0x015E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x016F [0x4D] EventEntity->StatusEvent = 9 // Close door
 24: 0x0170 [0x1C] WAIT(60* ticks)
 25: 0x0173 [0x52] END_LOAD_SCHEDULER: End scheduler "s053" with entities [EventEntity, EventEntity], work=211*
 26: 0x0182 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x0193 [0x46] CAMERA_CONTROL: Restore default settings
 28: 0x0195 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 29: 0x0197 [0x21] END_EVENT
 30: 0x0198 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0104 [0x01] GOTO 0x0107
```

### Event 69

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0199  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                             4D 00                          M.     
```

#### Opcodes

```
  0: 0x0199 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x019A [0x00] END_REQSTACK()
```
