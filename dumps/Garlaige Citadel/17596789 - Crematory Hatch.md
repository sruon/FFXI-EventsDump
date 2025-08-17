# 17596789 - Crematory Hatch

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Garlaige Citadel (ID: 200) |
| Block Size       | 364 bytes                  |
| Total Events     | 3                          |
| References Count | 8                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [4](#event-4)         | 0x0001       |    134 |             22 |
| [5](#event-5)         | 0x0087       |    167 |             28 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0012      |          18 |
|       4 | 0x005E      |          94 |
|       5 | 0x0078      |         120 |
|       6 | 0x1C82      |        7298 |
|       7 | 0x0001      |           1 |

## String References

- **7298**: Leave the incinerator? [Yes./No.]

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

### Event 4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 134 bytes |
| Instructions | 22        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 46 01 42 45 00  80 F0 FF FF 7F F0 FF FF    .F.BE.........
0010: 7F 66 64 6F 31 01 80 1C  02 80 38 03 80 29 0B F0  .fdo1.....8..)..
0020: FF FF 7F 08 29 0B F0 FF  FF 7F 04 45 04 80 F0 FF  ....)......E....
0030: FF 7F F0 FF FF 7F 61 6C  30 31 01 80 45 00 80 F0  ......al01..E...
0040: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 4C 1C 05  .......fdi1..L..
0050: 80 27 0B F0 FF FF 7F 05  1C 05 80 45 00 80 F0 FF  .'.........E....
0060: FF 7F F0 FF FF 7F 66 64  6F 31 01 80 4D 1C 02 80  ......fdo1..M...
0070: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
0080: 80 46 00 20 00 21 00                              .F. .!.         
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0005 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0006 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0017 [0x1C] WAIT(60* ticks)
  5: 0x001A [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
  6: 0x001D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x08)
  7: 0x0024 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x04)
  8: 0x002B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "al01" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  9: 0x003C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x004D [0x4C] EventEntity->StatusEvent = 8 // Open door
 11: 0x004E [0x1C] WAIT(120* ticks)
 12: 0x0051 [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x05)
 13: 0x0058 [0x1C] WAIT(120* ticks)
 14: 0x005B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x006C [0x4D] EventEntity->StatusEvent = 9 // Close door
 16: 0x006D [0x1C] WAIT(60* ticks)
 17: 0x0070 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0081 [0x46] CAMERA_CONTROL: Restore default settings
 19: 0x0083 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 20: 0x0085 [0x21] END_EVENT
 21: 0x0086 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0087    |
| Data Size    | 167 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      24  06 80 07 80 01 80 25 02         $......%.
0090: 00 10 01 80 00 1F 01 46  01 42 03 01 10 07 80 45  .......F.B.....E
00A0: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 01 80  ..........fdo1..
00B0: 1C 02 80 38 03 80 29 0B  F0 FF FF 7F 09 29 0B F0  ...8..)......)..
00C0: FF FF 7F 06 45 04 80 F0  FF FF 7F F0 FF FF 7F 61  ....E..........a
00D0: 6C 30 31 01 80 45 00 80  F0 FF FF 7F F0 FF FF 7F  l01..E..........
00E0: 66 64 69 31 01 80 4C 1C  05 80 27 0B F0 FF FF 7F  fdi1..L...'.....
00F0: 07 1C 05 80 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0100: 64 6F 31 01 80 4D 1C 02  80 45 00 80 F0 FF FF 7F  do1..M...E......
0110: F0 FF FF 7F 66 64 69 31  01 80 46 00 01 2A 01 02  ....fdi1..F..*..
0120: 00 10 07 80 00 2A 01 01  2A 01 20 00 21 00        .....*..*. .!.  
```

#### Opcodes

```
  0: 0x0087 [0x24] CREATE_DIALOG(message_id=7298*, default_option=1*, option_flags=0*)
    → "Leave the incinerator? [Yes./No.]"
  1: 0x008E [0x25] WAIT_DIALOG_SELECT()
  2: 0x008F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x011F
  3: 0x0097 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0099 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x009A [0x03] Work_Zone[1] = 1*
  6: 0x009F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x00B0 [0x1C] WAIT(60* ticks)
  8: 0x00B3 [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
  9: 0x00B6 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x09)
 10: 0x00BD [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x06)
 11: 0x00C4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "al01" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 12: 0x00D5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x00E6 [0x4C] EventEntity->StatusEvent = 8 // Open door
 14: 0x00E7 [0x1C] WAIT(120* ticks)
 15: 0x00EA [0x27] REQ_SET(priority=0x0B, entity_id=LocalPlayer, tag_num=0x07)
 16: 0x00F1 [0x1C] WAIT(120* ticks)
 17: 0x00F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0105 [0x4D] EventEntity->StatusEvent = 9 // Close door
 19: 0x0106 [0x1C] WAIT(60* ticks)
 20: 0x0109 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x011A [0x46] CAMERA_CONTROL: Restore default settings
 22: 0x011C [0x01] GOTO 0x012A
 23: 0x011F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x012A
 24: 0x0127 [0x01] GOTO 0x012A

SUBROUTINE_012A:
 25: 0x012A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 26: 0x012C [0x21] END_EVENT
 27: 0x012D [0x00] END_REQSTACK()
```
