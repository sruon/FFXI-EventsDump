# 17220138 - Telepoint

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Konschtat Highlands (ID: 108) |
| Block Size       | 204 bytes                     |
| Total Events     | 3                             |
| References Count | 6                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [101](#event-101)     | 0x0001       |     37 |              7 |
| [924](#event-924)     | 0x0026       |    111 |             25 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0002      |           2 |
|       2 | 0x0003      |           3 |
|       3 | 0x0004      |           4 |
|       4 | 0x0005      |           5 |
|       5 | 0x0006      |           6 |

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

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 37 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 00 00 02 10 2C  F8 FF FF 7F F0 FF FF 7F   B.....,........
0010: 62 69 6E 64 53 F8 FF FF  7F F0 FF FF 7F 62 69 6E  bindS........bin
0020: 64 1A 31 00 21 00                                 d.1.!.          
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  2: 0x0007 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "bind" with entities [EventEntity, LocalPlayer]
  3: 0x0014 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bind" with entities [EventEntity, LocalPlayer]
  4: 0x0021 [0x1A] CALL_SUBROUTINE(address=0x0031)
  5: 0x0024 [0x21] END_EVENT
  6: 0x0025 [0x00] END_REQSTACK()
```

### Event 924

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0026    |
| Data Size    | 111 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   42 03  00 00 02 10 1A 31 00 21        B......1.!
0030: 00 06 01 10 02 00 00 00  80 80 44 00 03 01 10 00  ..........D.....
0040: 80 01 94 00 02 00 00 01  80 80 54 00 03 01 10 01  ..........T.....
0050: 80 01 94 00 02 00 00 02  80 80 64 00 03 01 10 02  ..........d.....
0060: 80 01 94 00 02 00 00 03  80 80 74 00 03 01 10 03  ..........t.....
0070: 80 01 94 00 02 00 00 04  80 80 84 00 03 01 10 04  ................
0080: 80 01 94 00 02 00 00 05  80 80 94 00 03 01 10 05  ................
0090: 80 01 94 00 1B                                    .....           
```

#### Opcodes

```
  0: 0x0026 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0027 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  2: 0x002C [0x1A] CALL_SUBROUTINE(address=0x0031)
  3: 0x002F [0x21] END_EVENT
  4: 0x0030 [0x00] END_REQSTACK()

SUBROUTINE_0031:
  5: 0x0031 [0x06] Work_Zone[1] = 0
  6: 0x0034 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0044
  7: 0x003C [0x03] Work_Zone[1] = 1*
  8: 0x0041 [0x01] GOTO 0x0094
  9: 0x0044 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x0054
 10: 0x004C [0x03] Work_Zone[1] = 2*
 11: 0x0051 [0x01] GOTO 0x0094
 12: 0x0054 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x0064
 13: 0x005C [0x03] Work_Zone[1] = 3*
 14: 0x0061 [0x01] GOTO 0x0094
 15: 0x0064 [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x0074
 16: 0x006C [0x03] Work_Zone[1] = 4*
 17: 0x0071 [0x01] GOTO 0x0094
 18: 0x0074 [0x02] IF !(ExtData[1]->WorkLocal[0] == 5*) GOTO 0x0084
 19: 0x007C [0x03] Work_Zone[1] = 5*
 20: 0x0081 [0x01] GOTO 0x0094
 21: 0x0084 [0x02] IF !(ExtData[1]->WorkLocal[0] == 6*) GOTO 0x0094
 22: 0x008C [0x03] Work_Zone[1] = 6*
 23: 0x0091 [0x01] GOTO 0x0094

SUBROUTINE_0094:
 24: 0x0094 [0x1B] RETURN
```
