# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ghoyu's Reverie (ID: 129) |
| Block Size       | 236 bytes                 |
| Total Events     | 6                         |
| References Count | 8                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [15](#event-15)       | 0x0002       |     41 |              5 |
| [16](#event-16)       | 0x002B       |     38 |              4 |
| [10001](#event-10001) | 0x0051       |     26 |              7 |
| [10000](#event-10000) | 0x006B       |     54 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x008C      |         140 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x0002      |           2 |
|       6 | 0x00AA      |         170 |
|       7 | 0x005A      |          90 |

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

### Event 15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       62 00 80 F0 FF FF  7F F0 FF FF 7F 6D 61 69    b..........mai
0010: 6E 01 80 1C 02 80 45 03  80 F0 FF FF 7F F0 FF FF  n.....E.........
0020: 7F 66 64 6F 31 01 80 1C  04 80 00                 .fdo1......     
```

#### Opcodes

```
  0: 0x0002 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  1: 0x0013 [0x1C] WAIT(140* ticks)
  2: 0x0016 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0027 [0x1C] WAIT(60* ticks)
  4: 0x002A [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 38 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   45 03 80 F0 FF             E....
0030: FF 7F F0 FF FF 7F 66 64  69 31 01 80 62 05 80 F0  ......fdi1..b...
0040: FF FF 7F F0 FF FF 7F 6D  61 69 6E 01 80 1C 06 80  .......main.....
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x002B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  1: 0x003C [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
  2: 0x004D [0x1C] WAIT(170* ticks)
  3: 0x0050 [0x00] END_REQSTACK()
```

### Event 10001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    20 01 42 45 03 80 F0  FF FF 7F F0 FF FF 7F 66    .BE..........f
0060: 64 6F 31 01 80 1C 04 80  30 21 00                 do1.....0!.     
```

#### Opcodes

```
  0: 0x0051 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0053 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0054 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0065 [0x1C] WAIT(60* ticks)
  4: 0x0068 [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x0069 [0x21] END_EVENT
  6: 0x006A [0x00] END_REQSTACK()
```

### Event 10000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 54 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   20 01 42 02 09              .B..
0070: 10 01 80 00 8A 00 62 00  80 F0 FF FF 7F F0 FF FF  ......b.........
0080: 7F 6D 61 69 6E 01 80 1C  07 80 45 03 80 F0 FF FF  .main.....E.....
0090: 7F F0 FF FF 7F 66 64 6F  31 01 80 1C 04 80 30 21  .....fdo1.....0!
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x006B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x006D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x006E [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x008A
  3: 0x0076 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  4: 0x0087 [0x1C] WAIT(90* ticks)
  5: 0x008A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x009B [0x1C] WAIT(60* ticks)
  7: 0x009E [0x30] SET_UCOFF_CONTINUE_ZERO()
  8: 0x009F [0x21] END_EVENT
  9: 0x00A0 [0x00] END_REQSTACK()
```
