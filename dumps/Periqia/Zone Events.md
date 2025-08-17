# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Periqia (ID: 56) |
| Block Size       | 228 bytes        |
| Total Events     | 6                |
| References Count | 11               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [101](#event-101)     | 0x0002       |     26 |              7 |
| [102](#event-102)     | 0x001C       |     46 |              9 |
| [50](#event-50)       | 0x004A       |      9 |              4 |
| [103](#event-103)     | 0x0053       |     60 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x00C9      |         201 |
|       4 | 0x008C      |         140 |
|       5 | 0x0001      |           1 |
|       6 | 0xFFFAB3DE  |  4294620126 |
|       7 | 0x5CC4F     |      379983 |
|       8 | 0xFFFFC44E  |  4294952014 |
|       9 | 0x0004      |           4 |
|      10 | 0x0014      |          20 |

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
| Data Size    | 60 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          20 01 42 45 00  80 F0 FF FF 7F F0 FF FF      .BE.........
0060: 7F 66 64 6F 31 01 80 1C  02 80 47 00 06 80 07 80  .fdo1.....G.....
0070: 08 80 09 80 47 01 1C 0A  80 45 00 80 F0 FF FF 7F  ....G....E......
0080: F0 FF FF 7F 66 64 69 31  01 80 1C 02 80 21 00     ....fdi1.....!. 
```

#### Opcodes

```
  0: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0055 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0056 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0067 [0x1C] WAIT(60* ticks)
  4: 0x006A [0x47] UPDATE_PLAYER_POS(-347.170*, 379.983*, -15.282*, yaw=0.4°*)
  5: 0x0074 [0x47] WAIT_PLAYER_POS_UPDATE
  6: 0x0076 [0x1C] WAIT(20* ticks)
  7: 0x0079 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x008A [0x1C] WAIT(60* ticks)
  9: 0x008D [0x21] END_EVENT
 10: 0x008E [0x00] END_REQSTACK()
```
