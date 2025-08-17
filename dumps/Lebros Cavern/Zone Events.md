# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Lebros Cavern (ID: 63) |
| Block Size       | 300 bytes              |
| Total Events     | 8                      |
| References Count | 10                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [101](#event-101)     | 0x0002       |     26 |              7 |
| [102](#event-102)     | 0x001C       |     46 |              9 |
| [50](#event-50)       | 0x004A       |      9 |              4 |
| [103](#event-103)     | 0x0053       |     56 |             18 |
| [104](#event-104)     | 0x008B       |     35 |             12 |
| [105](#event-105)     | 0x00AE       |     35 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x00C9      |         201 |
|       4 | 0x008C      |         140 |
|       5 | 0x0001      |           1 |
|       6 | 0x1D20      |        7456 |
|       7 | 0x0002      |           2 |
|       8 | 0x1D21      |        7457 |
|       9 | 0x1D3E      |        7486 |

## String References

- **7456**: Take this male apkallu with you? [Yes./Not this one.]
- **7457**: Choose this female apkallu as a partner? [This is the one!/Not this one.]
- **7486**: You rrreally want to stop now? [Rrreally./Not rrreally.]

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
| Data Size    | 56 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          20 01 24 06 80  05 80 01 80 25 02 00 10      .$......%...
0060: 01 80 00 72 00 43 00 43  01 42 03 01 10 05 80 01  ...r.C.C.B......
0070: 87 00 02 00 10 05 80 00  87 00 43 00 43 01 42 03  ..........C.C.B.
0080: 01 10 07 80 01 87 00 20  00 21 00                 ....... .!.     
```

#### Opcodes

```
  0: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0055 [0x24] CREATE_DIALOG(message_id=7456*, default_option=1*, option_flags=0*)
    → "Take this male apkallu with you? [Yes./Not this one.]"
  2: 0x005C [0x25] WAIT_DIALOG_SELECT()
  3: 0x005D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0072
  4: 0x0065 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0067 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x0069 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x006A [0x03] Work_Zone[1] = 1*
  8: 0x006F [0x01] GOTO 0x0087
  9: 0x0072 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0087
 10: 0x007A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x007C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x007E [0x42] SET_CLI_EVENT_CANCEL_DATA()
 13: 0x007F [0x03] Work_Zone[1] = 2*
 14: 0x0084 [0x01] GOTO 0x0087

SUBROUTINE_0087:
 15: 0x0087 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0089 [0x21] END_EVENT
 17: 0x008A [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 35 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   20 01 24 08 80              .$..
0090: 05 80 01 80 25 02 00 10  01 80 00 AA 00 43 00 43  ....%........C.C
00A0: 01 42 03 01 10 05 80 01  AA 00 20 00 21 00        .B........ .!.  
```

#### Opcodes

```
  0: 0x008B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x008D [0x24] CREATE_DIALOG(message_id=7457*, default_option=1*, option_flags=0*)
    → "Choose this female apkallu as a partner? [This is the one!/Not this one.]"
  2: 0x0094 [0x25] WAIT_DIALOG_SELECT()
  3: 0x0095 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00AA
  4: 0x009D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x009F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x00A1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x00A2 [0x03] Work_Zone[1] = 1*
  8: 0x00A7 [0x01] GOTO 0x00AA

SUBROUTINE_00AA:
  9: 0x00AA [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00AC [0x21] END_EVENT
 11: 0x00AD [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 35 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            20 01                 .
00B0: 24 09 80 05 80 01 80 25  02 00 10 01 80 00 CD 00  $......%........
00C0: 43 00 43 01 42 03 01 10  05 80 01 CD 00 20 00 21  C.C.B........ .!
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00AE [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00B0 [0x24] CREATE_DIALOG(message_id=7486*, default_option=1*, option_flags=0*)
    → "You rrreally want to stop now? [Rrreally./Not rrreally.]"
  2: 0x00B7 [0x25] WAIT_DIALOG_SELECT()
  3: 0x00B8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00CD
  4: 0x00C0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x00C2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x00C4 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x00C5 [0x03] Work_Zone[1] = 1*
  8: 0x00CA [0x01] GOTO 0x00CD

SUBROUTINE_00CD:
  9: 0x00CD [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00CF [0x21] END_EVENT
 11: 0x00D0 [0x00] END_REQSTACK()
```
