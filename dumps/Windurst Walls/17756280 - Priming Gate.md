# 17756280 - Priming Gate

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 348 bytes                |
| Total Events     | 3                        |
| References Count | 10                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [395](#event-395)     | 0x0001       |    186 |             33 |
| [401](#event-401)     | 0x00BB       |     92 |             18 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2287      |        8839 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x0002      |           2 |
|       6 | 0x000A      |          10 |
|       7 | 0x00D4      |         212 |
|       8 | 0x0078      |         120 |
|       9 | 0x2288      |        8840 |

## String References

- **8839**: Pass through the gate? [Yes./No.]
- **8840**: Enter the gate? [Yes./No.]

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

### Event 395

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 186 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 24 00 80 01  80 02 80 25 02 00 10 02    .B$......%....
0010: 80 00 17 00 01 26 00 02  00 10 01 80 00 26 00 20  .....&.......&. 
0020: 00 21 00 01 26 00 46 01  45 03 80 F0 FF FF 7F F0  .!..&.F.E.......
0030: FF FF 7F 66 64 6F 31 02  80 1C 04 80 38 05 80 29  ...fdo1.....8..)
0040: 0B F0 FF FF 7F 3D 1C 06  80 29 0B F0 FF FF 7F 3E  .....=...).....>
0050: 45 07 80 F8 FF FF 7F F8  FF FF 7F 73 30 34 33 02  E..........s043.
0060: 80 45 03 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
0070: 02 80 4C 1C 08 80 45 03  80 F0 FF FF 7F F0 FF FF  ..L...E.........
0080: 7F 66 64 6F 31 02 80 1C  08 80 4D 29 0B F0 FF FF  .fdo1.....M)....
0090: 7F 3D 1C 08 80 52 07 80  F8 FF FF 7F F8 FF FF 7F  .=...R..........
00A0: 73 30 34 33 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  s043E..........f
00B0: 64 69 31 02 80 46 00 20  00 21 00                 di1..F. .!.     
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x24] CREATE_DIALOG(message_id=8839*, default_option=1*, option_flags=0*)
    → "Pass through the gate? [Yes./No.]"
  3: 0x000B [0x25] WAIT_DIALOG_SELECT()
  4: 0x000C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0017
  5: 0x0014 [0x01] GOTO 0x0026
  6: 0x0017 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0026
  7: 0x001F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0021 [0x21] END_EVENT
  9: 0x0022 [0x00] END_REQSTACK()

SUBROUTINE_0026:
 10: 0x0026 [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0028 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x0039 [0x1C] WAIT(60* ticks)
 13: 0x003C [0x38] SET_CLIENT_EVENT_MODE(mode=2*)
 14: 0x003F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x3D)
 15: 0x0046 [0x1C] WAIT(10* ticks)
 16: 0x0049 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x3E)
 17: 0x0050 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s043" with entities [EventEntity, EventEntity], work=[212*, 0*]
 18: 0x0061 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0072 [0x4C] EventEntity->StatusEvent = 8 // Open door
 20: 0x0073 [0x1C] WAIT(120* ticks)
 21: 0x0076 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0087 [0x1C] WAIT(120* ticks)
 23: 0x008A [0x4D] EventEntity->StatusEvent = 9 // Close door
 24: 0x008B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x3D)
 25: 0x0092 [0x1C] WAIT(120* ticks)
 26: 0x0095 [0x52] END_LOAD_SCHEDULER: End scheduler "s043" with entities [EventEntity, EventEntity], work=212*
 27: 0x00A4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 28: 0x00B5 [0x46] CAMERA_CONTROL: Restore default settings
 29: 0x00B7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 30: 0x00B9 [0x21] END_EVENT
 31: 0x00BA [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0023 [0x01] GOTO 0x0026
```

### Event 401

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 92 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   20 01 42 24 09              .B$.
00C0: 80 01 80 02 80 25 02 00  10 02 80 00 03 01 42 03  .....%........B.
00D0: 01 10 01 80 45 03 80 F8  FF FF 7F F8 FF FF 7F 66  ....E..........f
00E0: 64 6F 31 02 80 1C 08 80  29 08 F0 FF FF 7F 3C 45  do1.....).....<E
00F0: 03 80 F8 FF FF 7F F8 FF  FF 7F 66 64 69 31 02 80  ..........fdi1..
0100: 01 13 01 02 00 10 01 80  00 13 01 03 01 10 05 80  ................
0110: 01 13 01 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x00BB [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00BD [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00BE [0x24] CREATE_DIALOG(message_id=8840*, default_option=1*, option_flags=0*)
    → "Enter the gate? [Yes./No.]"
  3: 0x00C5 [0x25] WAIT_DIALOG_SELECT()
  4: 0x00C6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0103
  5: 0x00CE [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x00CF [0x03] Work_Zone[1] = 1*
  7: 0x00D4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  8: 0x00E5 [0x1C] WAIT(120* ticks)
  9: 0x00E8 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x3C)
 10: 0x00EF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 11: 0x0100 [0x01] GOTO 0x0113
 12: 0x0103 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0113
 13: 0x010B [0x03] Work_Zone[1] = 2*
 14: 0x0110 [0x01] GOTO 0x0113

SUBROUTINE_0113:
 15: 0x0113 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0115 [0x21] END_EVENT
 17: 0x0116 [0x00] END_REQSTACK()
```
