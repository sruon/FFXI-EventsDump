# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                               |
|------------------|-------------------------------------|
| Zone             | Mamool Ja Training Grounds (ID: 66) |
| Block Size       | 280 bytes                           |
| Total Events     | 7                                   |
| References Count | 13                                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [101](#event-101)     | 0x0002       |     26 |              7 |
| [102](#event-102)     | 0x001C       |     46 |              9 |
| [50](#event-50)       | 0x004A       |      9 |              4 |
| [103](#event-103)     | 0x0053       |     39 |             14 |
| [104](#event-104)     | 0x007A       |     60 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x00C9      |         201 |
|       4 | 0x008C      |         140 |
|       5 | 0x0001      |           1 |
|       6 | 0x1D7D      |        7549 |
|       7 | 0x1D7E      |        7550 |
|       8 | 0xCA73      |       51827 |
|       9 | 0xFFFB83E7  |  4294673383 |
|      10 | 0x06F0      |        1776 |
|      11 | 0x0800      |        2048 |
|      12 | 0x0014      |          20 |

## String References

- **7549**: There is a curious liquid here.
- **7550**: Take a sip? [I'll try anything once!/I have a weak stomach...]

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

### Event 65534

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

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 42 45 00 80  F0 FF FF 7F F0 FF FF 7F     .BE..........
0010: 66 64 6F 31 01 80 1C 02  80 30 21 00              fdo1.....0!.    
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0016 [0x1C] WAIT(60* ticks)
  4: 0x0019 [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x001A [0x21] END_EVENT
  6: 0x001B [0x00] END_REQSTACK()
```

### Event 102

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 46 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      20 01 42 9F               .B.
0020: 03 80 F8 FF FF 7F F8 FF  FF 7F 6D 61 69 6E 01 80  ..........main..
0030: 1C 04 80 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0040: 6F 31 01 80 1C 02 80 30  21 00                    o1.....0!.      
```

#### Opcodes

```
  0: 0x001C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x001E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x001F [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [EventEntity, EventEntity], work=[201*, 0*]
  3: 0x0030 [0x1C] WAIT(140* ticks)
  4: 0x0033 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x0044 [0x1C] WAIT(60* ticks)
  6: 0x0047 [0x30] SET_UCOFF_CONTINUE_ZERO()
  7: 0x0048 [0x21] END_EVENT
  8: 0x0049 [0x00] END_REQSTACK()
```

### Event 50

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 9 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                20 01 03 01 10 05             .....
0050: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x004A [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x004C [0x03] Work_Zone[1] = 1*
  2: 0x0051 [0x21] END_EVENT
  3: 0x0052 [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 39 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          20 01 48 06 80  23 24 07 80 05 80 01 80      .H..#$......
0060: 25 02 00 10 01 80 00 76  00 43 00 43 01 42 03 01  %......v.C.C.B..
0070: 10 05 80 01 76 00 20 00  21 00                    ....v. .!.      
```

#### Opcodes

```
  0: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0055 [0x48] [System] [7549*]:
    → "There is a curious liquid here."
  2: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0059 [0x24] CREATE_DIALOG(message_id=7550*, default_option=1*, option_flags=0*)
    → "Take a sip? [I'll try anything once!/I have a weak stomach...]"
  4: 0x0060 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0061 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0076
  6: 0x0069 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x006B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x006D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x006E [0x03] Work_Zone[1] = 1*
 10: 0x0073 [0x01] GOTO 0x0076

SUBROUTINE_0076:
 11: 0x0076 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0078 [0x21] END_EVENT
 13: 0x0079 [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 60 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                20 01 42 45 00 80             .BE..
0080: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 02  ........fdo1....
0090: 80 47 00 08 80 09 80 0A  80 0B 80 47 01 1C 0C 80  .G.........G....
00A0: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
00B0: 80 1C 02 80 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x007A [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x007C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x007D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x008E [0x1C] WAIT(60* ticks)
  4: 0x0091 [0x47] UPDATE_PLAYER_POS(51.827*, -293.913*, 1.776*, yaw=180.0°*)
  5: 0x009B [0x47] WAIT_PLAYER_POS_UPDATE
  6: 0x009D [0x1C] WAIT(20* ticks)
  7: 0x00A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x00B1 [0x1C] WAIT(60* ticks)
  9: 0x00B4 [0x21] END_EVENT
 10: 0x00B5 [0x00] END_REQSTACK()
```
