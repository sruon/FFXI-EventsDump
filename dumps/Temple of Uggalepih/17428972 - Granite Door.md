# 17428972 - Granite Door

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 364 bytes                     |
| Total Events     | 3                             |
| References Count | 9                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [46](#event-46)       | 0x0001       |    134 |             22 |
| [47](#event-47)       | 0x0087       |    164 |             28 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0012      |          18 |
|       4 | 0x00EA      |         234 |
|       5 | 0x0078      |         120 |
|       6 | 0x00B4      |         180 |
|       7 | 0x1CCF      |        7375 |
|       8 | 0x0001      |           1 |

## String References

- **7375**: Leave the room? [Yes./Not yet.]

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

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 134 bytes |
| Instructions | 22        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 46 01 42 45 00  80 F0 FF FF 7F F0 FF FF    .F.BE.........
0010: 7F 66 64 6F 31 01 80 1C  02 80 38 03 80 45 04 80  .fdo1.....8..E..
0020: F0 FF FF 7F F0 FF FF 7F  75 67 30 31 01 80 29 01  ........ug01..).
0030: F0 FF FF 7F 13 29 01 F0  FF FF 7F 15 45 00 80 F0  .....)......E...
0040: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 4C 1C 05  .......fdi1..L..
0050: 80 27 01 F0 FF FF 7F 17  1C 06 80 4D 45 00 80 F0  .'.........ME...
0060: FF FF 7F F0 FF FF 7F 66  64 6F 31 01 80 1C 02 80  .......fdo1.....
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
  6: 0x001D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ug01" with entities [LocalPlayer, LocalPlayer], work=[234*, 0*]
  7: 0x002E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x13)
  8: 0x0035 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x15)
  9: 0x003C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x004D [0x4C] EventEntity->StatusEvent = 8 // Open door
 11: 0x004E [0x1C] WAIT(120* ticks)
 12: 0x0051 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x17)
 13: 0x0058 [0x1C] WAIT(180* ticks)
 14: 0x005B [0x4D] EventEntity->StatusEvent = 9 // Close door
 15: 0x005C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x006D [0x1C] WAIT(60* ticks)
 17: 0x0070 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0081 [0x46] CAMERA_CONTROL: Restore default settings
 19: 0x0083 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 20: 0x0085 [0x21] END_EVENT
 21: 0x0086 [0x00] END_REQSTACK()
```

### Event 47

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0087    |
| Data Size    | 164 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      20  01 24 07 80 08 80 01 80          .$......
0090: 25 02 00 10 01 80 00 1C  01 46 01 42 45 00 80 F0  %........F.BE...
00A0: FF FF 7F F0 FF FF 7F 66  64 6F 31 01 80 1C 02 80  .......fdo1.....
00B0: 38 03 80 45 04 80 F0 FF  FF 7F F0 FF FF 7F 75 67  8..E..........ug
00C0: 30 32 01 80 29 01 F0 FF  FF 7F 14 29 01 F0 FF FF  02..)......)....
00D0: 7F 16 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
00E0: 31 01 80 4C 1C 05 80 27  01 F0 FF FF 7F 18 1C 06  1..L...'........
00F0: 80 4D 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  .ME..........fdo
0100: 31 01 80 1C 02 80 45 00  80 F0 FF FF 7F F0 FF FF  1.....E.........
0110: 7F 66 64 69 31 01 80 46  00 01 27 01 02 00 10 08  .fdi1..F..'.....
0120: 80 00 27 01 01 27 01 20  00 21 00                 ..'..'. .!.     
```

#### Opcodes

```
  0: 0x0087 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0089 [0x24] CREATE_DIALOG(message_id=7375*, default_option=1*, option_flags=0*)
    → "Leave the room? [Yes./Not yet.]"
  2: 0x0090 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0091 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x011C
  4: 0x0099 [0x46] CAMERA_CONTROL: Disable user control
  5: 0x009B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x009C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x00AD [0x1C] WAIT(60* ticks)
  8: 0x00B0 [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
  9: 0x00B3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ug02" with entities [LocalPlayer, LocalPlayer], work=[234*, 0*]
 10: 0x00C4 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x14)
 11: 0x00CB [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x16)
 12: 0x00D2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x00E3 [0x4C] EventEntity->StatusEvent = 8 // Open door
 14: 0x00E4 [0x1C] WAIT(120* ticks)
 15: 0x00E7 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x18)
 16: 0x00EE [0x1C] WAIT(180* ticks)
 17: 0x00F1 [0x4D] EventEntity->StatusEvent = 9 // Close door
 18: 0x00F2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0103 [0x1C] WAIT(60* ticks)
 20: 0x0106 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x0117 [0x46] CAMERA_CONTROL: Restore default settings
 22: 0x0119 [0x01] GOTO 0x0127
 23: 0x011C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0127
 24: 0x0124 [0x01] GOTO 0x0127

SUBROUTINE_0127:
 25: 0x0127 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 26: 0x0129 [0x21] END_EVENT
 27: 0x012A [0x00] END_REQSTACK()
```
