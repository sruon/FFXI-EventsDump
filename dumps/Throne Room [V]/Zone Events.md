# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Throne Room [V] (ID: 229) |
| Block Size       | 340 bytes                 |
| Total Events     | 7                         |
| References Count | 6                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1000](#event-1000)   | 0x0001       |     68 |             12 |
| [1001](#event-1001)   | 0x0045       |      8 |              5 |
| [10000](#event-10000) | 0x004D       |     54 |             10 |
| [10001](#event-10001) | 0x0083       |     26 |              7 |
| [1002](#event-1002)   | 0x009D       |    112 |             16 |
| [65534](#event-65534) | 0x010D       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x005A      |          90 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x0002      |           2 |

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

### Event 1000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 68 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    02 09 10 00 80 01 0F  00 4E 01 F0 FF FF 7F 20   ........N..... 
0010: 01 42 02 09 10 00 80 00  2E 00 62 01 80 F0 FF FF  .B........b.....
0020: 7F F0 FF FF 7F 6D 61 69  6E 00 80 1C 02 80 45 03  .....main.....E.
0030: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 00 80 1C  .........fdo1...
0040: 04 80 30 21 00                                    ..0!.           
```

#### Opcodes

```
  0: 0x0001 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x000F
  1: 0x0009 [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
  2: 0x000F [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x0011 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0012 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x002E
  5: 0x001A [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  6: 0x002B [0x1C] WAIT(90* ticks)
  7: 0x002E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x003F [0x1C] WAIT(60* ticks)
  9: 0x0042 [0x30] SET_UCOFF_CONTINUE_ZERO()
 10: 0x0043 [0x21] END_EVENT
 11: 0x0044 [0x00] END_REQSTACK()
```

### Event 1001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                20 01 42  1C 04 80 21 00                 .B...!.   
```

#### Opcodes

```
  0: 0x0045 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0047 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0048 [0x1C] WAIT(60* ticks)
  3: 0x004B [0x21] END_EVENT
  4: 0x004C [0x00] END_REQSTACK()
```

### Event 10000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 54 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         20 01 42                .B
0050: 02 09 10 00 80 00 6C 00  62 01 80 F0 FF FF 7F F0  ......l.b.......
0060: FF FF 7F 6D 61 69 6E 00  80 1C 02 80 45 03 80 F0  ...main.....E...
0070: FF FF 7F F0 FF FF 7F 66  64 6F 31 00 80 1C 04 80  .......fdo1.....
0080: 30 21 00                                          0!.             
```

#### Opcodes

```
  0: 0x004D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x004F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0050 [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x006C
  3: 0x0058 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  4: 0x0069 [0x1C] WAIT(90* ticks)
  5: 0x006C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x007D [0x1C] WAIT(60* ticks)
  7: 0x0080 [0x30] SET_UCOFF_CONTINUE_ZERO()
  8: 0x0081 [0x21] END_EVENT
  9: 0x0082 [0x00] END_REQSTACK()
```

### Event 10001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0083   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:          20 01 42 45 03  80 F0 FF FF 7F F0 FF FF      .BE.........
0090: 7F 66 64 6F 31 00 80 1C  04 80 30 21 00           .fdo1.....0!.   
```

#### Opcodes

```
  0: 0x0083 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0085 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0086 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0097 [0x1C] WAIT(60* ticks)
  4: 0x009A [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x009B [0x21] END_EVENT
  6: 0x009C [0x00] END_REQSTACK()
```

### Event 1002

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x009D    |
| Data Size    | 112 bytes |
| Instructions | 16        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         03 00 00               ...
00A0: 02 10 03 01 00 03 10 03  02 00 04 10 03 03 00 05  ................
00B0: 10 42 62 01 80 F0 FF FF  7F F0 FF FF 7F 6D 61 69  .Bb..........mai
00C0: 6E 00 80 1C 02 80 45 03  80 F0 FF FF 7F F0 FF FF  n.....E.........
00D0: 7F 66 64 6F 31 00 80 1C  04 80 47 00 00 00 02 00  .fdo1.....G.....
00E0: 01 00 03 00 47 01 45 03  80 F0 FF FF 7F F0 FF FF  ....G.E.........
00F0: 7F 66 64 69 31 00 80 62  05 80 F0 FF FF 7F F0 FF  .fdi1..b........
0100: FF 7F 6D 61 69 6E 00 80  1C 02 80 21 00           ..main.....!.   
```

#### Opcodes

```
  0: 0x009D [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x00A2 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x00A7 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  3: 0x00AC [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  4: 0x00B1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x00B2 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  6: 0x00C3 [0x1C] WAIT(90* ticks)
  7: 0x00C6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x00D7 [0x1C] WAIT(60* ticks)
  9: 0x00DA [0x47] UPDATE_PLAYER_POS(ExtData[1]->WorkLocal[0], ExtData[1]->WorkLocal[2], ExtData[1]->WorkLocal[1], yaw=ExtData[1]->WorkLocal[3])
 10: 0x00E4 [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x00E6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x00F7 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
 13: 0x0108 [0x1C] WAIT(90* ticks)
 14: 0x010B [0x21] END_EVENT
 15: 0x010C [0x00] END_REQSTACK()
```

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         00                     .  
```

#### Opcodes

```
  0: 0x010D [0x00] END_REQSTACK()
```
