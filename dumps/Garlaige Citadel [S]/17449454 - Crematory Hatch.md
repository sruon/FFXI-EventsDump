# 17449454 - Crematory Hatch

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Garlaige Citadel [S] (ID: 164) |
| Block Size       | 364 bytes                      |
| Total Events     | 3                              |
| References Count | 8                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10](#event-10)       | 0x0001       |    134 |             22 |
| [11](#event-11)       | 0x0087       |    166 |             29 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0012      |          18 |
|       4 | 0x005E      |          94 |
|       5 | 0x0078      |         120 |
|       6 | 0x1DDF      |        7647 |
|       7 | 0x0001      |           1 |

## String References

- **7647**: Leave the incinerator? [Yes./No.]

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

### Event 10

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
0010: 7F 66 64 6F 31 01 80 1C  02 80 38 03 80 29 01 F0  .fdo1.....8..)..
0020: FF FF 7F 07 29 01 F0 FF  FF 7F 03 45 04 80 F0 FF  ....)......E....
0030: FF 7F F0 FF FF 7F 61 6C  30 32 01 80 45 00 80 F0  ......al02..E...
0040: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 4C 1C 05  .......fdi1..L..
0050: 80 27 01 F0 FF FF 7F 04  1C 05 80 45 00 80 F0 FF  .'.........E....
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
  6: 0x001D [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x07)
  7: 0x0024 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)
  8: 0x002B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "al02" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  9: 0x003C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x004D [0x4C] EventEntity->StatusEvent = 8 // Open door
 11: 0x004E [0x1C] WAIT(120* ticks)
 12: 0x0051 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
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

### Event 11

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0087    |
| Data Size    | 166 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      24  06 80 07 80 01 80 25 02         $......%.
0090: 00 10 01 80 00 1E 01 43  00 43 01 46 01 42 45 00  .......C.C.F.BE.
00A0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 01 80 1C  .........fdo1...
00B0: 02 80 38 03 80 29 01 F0  FF FF 7F 08 29 01 F0 FF  ..8..)......)...
00C0: FF 7F 05 45 04 80 F0 FF  FF 7F F0 FF FF 7F 61 6C  ...E..........al
00D0: 30 32 01 80 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  02..E..........f
00E0: 64 69 31 01 80 4C 1C 05  80 27 01 F0 FF FF 7F 06  di1..L...'......
00F0: 1C 05 80 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0100: 6F 31 01 80 4D 1C 02 80  45 00 80 F0 FF FF 7F F0  o1..M...E.......
0110: FF FF 7F 66 64 69 31 01  80 46 00 01 29 01 02 00  ...fdi1..F..)...
0120: 10 07 80 00 29 01 01 29  01 20 00 21 00           ....)..). .!.   
```

#### Opcodes

```
  0: 0x0087 [0x24] CREATE_DIALOG(message_id=7647*, default_option=1*, option_flags=0*)
    → "Leave the incinerator? [Yes./No.]"
  1: 0x008E [0x25] WAIT_DIALOG_SELECT()
  2: 0x008F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x011E
  3: 0x0097 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  4: 0x0099 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  5: 0x009B [0x46] CAMERA_CONTROL: Disable user control
  6: 0x009D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x009E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x00AF [0x1C] WAIT(60* ticks)
  9: 0x00B2 [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
 10: 0x00B5 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x08)
 11: 0x00BC [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x00C3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "al02" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 13: 0x00D4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x00E5 [0x4C] EventEntity->StatusEvent = 8 // Open door
 15: 0x00E6 [0x1C] WAIT(120* ticks)
 16: 0x00E9 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x06)
 17: 0x00F0 [0x1C] WAIT(120* ticks)
 18: 0x00F3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0104 [0x4D] EventEntity->StatusEvent = 9 // Close door
 20: 0x0105 [0x1C] WAIT(60* ticks)
 21: 0x0108 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0119 [0x46] CAMERA_CONTROL: Restore default settings
 23: 0x011B [0x01] GOTO 0x0129
 24: 0x011E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0129
 25: 0x0126 [0x01] GOTO 0x0129

SUBROUTINE_0129:
 26: 0x0129 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 27: 0x012B [0x21] END_EVENT
 28: 0x012C [0x00] END_REQSTACK()
```
