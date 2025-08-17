# 17375846 - Buu Xolo the Bloodfaced

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Balga's Dais (ID: 146) |
| Block Size       | 672 bytes              |
| Total Events     | 7                      |
| References Count | 16                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |    174 |             14 |
| [65535.2](#event-655352) | 0x00B0       |     99 |             10 |
| [65535.3](#event-655353) | 0x0113       |    213 |             22 |
| [32001](#event-32001)    | 0x01E8       |      1 |              1 |
| [65535.4](#event-655354) | 0x01E9       |     73 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00D3      |         211 |
|       1 | 0x0000      |           0 |
|       2 | 0x00B4      |         180 |
|       3 | 0x00C8      |         200 |
|       4 | 0x0082      |         130 |
|       5 | 0x00FA      |         250 |
|       6 | 0x003C      |          60 |
|       7 | 0x0002      |           2 |
|       8 | 0x001E      |          30 |
|       9 | 0x0050      |          80 |
|      10 | 0x0003      |           3 |
|      11 | 0x0004      |           4 |
|      12 | 0x0005      |           5 |
|      13 | 0x0006      |           6 |
|      14 | 0x0008      |           8 |
|      15 | 0x0064      |         100 |

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

### Event 32000

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

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 174 bytes |
| Instructions | 14        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       45 00 80 F8 FF FF  7F F8 FF FF 7F 73 30 36    E..........s06
0010: 30 01 80 1C 02 80 52 00  80 F8 FF FF 7F F8 FF FF  0.....R.........
0020: 7F 73 30 36 30 45 03 80  F8 FF FF 7F F8 FF FF 7F  .s060E..........
0030: 6F 76 6C 31 01 80 45 00  80 F8 FF FF 7F F8 FF FF  ovl1..E.........
0040: 7F 73 30 36 31 01 80 1C  04 80 52 00 80 F8 FF FF  .s061.....R.....
0050: 7F F8 FF FF 7F 73 30 36  31 45 03 80 F8 FF FF 7F  .....s061E......
0060: F8 FF FF 7F 6F 76 6C 31  01 80 45 00 80 64 22 09  ....ovl1..E..d".
0070: 01 64 22 09 01 73 30 36  35 01 80 1C 05 80 52 00  .d"..s065.....R.
0080: 80 64 22 09 01 64 22 09  01 73 30 36 35 45 03 80  .d"..d"..s065E..
0090: F0 FF FF 7F F0 FF FF 7F  6F 76 6C 31 01 80 45 00  ........ovl1..E.
00A0: 80 64 22 09 01 64 22 09  01 73 30 36 32 01 80 00  .d"..d"..s062...
```

#### Opcodes

```
  0: 0x0002 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s060" with entities [EventEntity, EventEntity], work=[211*, 0*]
  1: 0x0013 [0x1C] WAIT(180* ticks)
  2: 0x0016 [0x52] END_LOAD_SCHEDULER: End scheduler "s060" with entities [EventEntity, EventEntity], work=211*
  3: 0x0025 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  4: 0x0036 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s061" with entities [EventEntity, EventEntity], work=[211*, 0*]
  5: 0x0047 [0x1C] WAIT(130* ticks)
  6: 0x004A [0x52] END_LOAD_SCHEDULER: End scheduler "s061" with entities [EventEntity, EventEntity], work=211*
  7: 0x0059 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  8: 0x006A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s065" with entities [EVENTER (ID: 17375844/0x01092264), EVENTER (ID: 17375844/0x01092264)], work=[211*, 0*]
  9: 0x007B [0x1C] WAIT(250* ticks)
 10: 0x007E [0x52] END_LOAD_SCHEDULER: End scheduler "s065" with entities [EVENTER (ID: 17375844/0x01092264), EVENTER (ID: 17375844/0x01092264)], work=211*
 11: 0x008D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x009E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s062" with entities [EVENTER (ID: 17375844/0x01092264), EVENTER (ID: 17375844/0x01092264)], work=[211*, 0*]
 13: 0x00AF [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 99 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 45 00 80 F8 FF FF 7F F8  FF FF 7F 73 30 36 33 01  E..........s063.
00C0: 80 1C 06 80 62 07 80 66  22 09 01 66 22 09 01 6D  ....b..f"..f"..m
00D0: 61 69 6E 01 80 4E 00 66  22 09 01 1C 08 80 52 00  ain..N.f".....R.
00E0: 80 F8 FF FF 7F F8 FF FF  7F 73 30 36 33 45 03 80  .........s063E..
00F0: F0 FF FF 7F F0 FF FF 7F  6F 76 6C 31 01 80 45 00  ........ovl1..E.
0100: 80 F0 FF FF 7F F0 FF FF  7F 73 30 36 38 01 80 1C  .........s068...
0110: 06 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s063" with entities [EventEntity, EventEntity], work=[211*, 0*]
  1: 0x00C1 [0x1C] WAIT(60* ticks)
  2: 0x00C4 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [Buu Xolo the Bloodfaced (ID: 17375846/0x01092266), Buu Xolo the Bloodfaced (ID: 17375846/0x01092266)], work=[2*, 0*]
  3: 0x00D5 [0x4E] SET_ENTITY_HIDE_FLAG: Show Buu Xolo the Bloodfaced (ID: 17375846/0x01092266)
  4: 0x00DB [0x1C] WAIT(30* ticks)
  5: 0x00DE [0x52] END_LOAD_SCHEDULER: End scheduler "s063" with entities [EventEntity, EventEntity], work=211*
  6: 0x00ED [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x00FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s068" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
  8: 0x010F [0x1C] WAIT(60* ticks)
  9: 0x0112 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0113    |
| Data Size    | 213 bytes |
| Instructions | 22        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:          45 00 80 F8 FF  FF 7F F8 FF FF 7F 73 30     E..........s0
0120: 36 34 01 80 1C 09 80 52  00 80 F8 FF FF 7F F8 FF  64.....R........
0130: FF 7F 73 30 36 34 45 03  80 F0 FF FF 7F F0 FF FF  ..s064E.........
0140: 7F 6F 76 6C 31 01 80 02  09 10 0A 80 00 63 01 45  .ovl1........c.E
0150: 00 80 F0 FF FF 7F F0 FF  FF 7F 73 30 37 32 01 80  ..........s072..
0160: 01 E4 01 02 09 10 0B 80  00 7F 01 45 00 80 F0 FF  ...........E....
0170: FF 7F F0 FF FF 7F 73 30  37 33 01 80 01 E4 01 02  ......s073......
0180: 09 10 0C 80 00 9B 01 45  00 80 F0 FF FF 7F F0 FF  .......E........
0190: FF 7F 73 30 37 30 01 80  01 E4 01 02 09 10 0D 80  ..s070..........
01A0: 00 B7 01 45 00 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ...E..........s0
01B0: 37 30 01 80 01 E4 01 02  09 10 0E 80 00 D3 01 45  70.............E
01C0: 00 80 F0 FF FF 7F F0 FF  FF 7F 73 30 37 31 01 80  ..........s071..
01D0: 01 E4 01 45 00 80 F0 FF  FF 7F F0 FF FF 7F 73 30  ...E..........s0
01E0: 36 39 01 80 1C 09 80 00                           69......        
```

#### Opcodes

```
  0: 0x0113 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s064" with entities [EventEntity, EventEntity], work=[211*, 0*]
  1: 0x0124 [0x1C] WAIT(80* ticks)
  2: 0x0127 [0x52] END_LOAD_SCHEDULER: End scheduler "s064" with entities [EventEntity, EventEntity], work=211*
  3: 0x0136 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0147 [0x02] IF !(Work_Zone[9] == 3*) GOTO 0x0163
  5: 0x014F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s072" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
  6: 0x0160 [0x01] GOTO 0x01E4
  7: 0x0163 [0x02] IF !(Work_Zone[9] == 4*) GOTO 0x017F
  8: 0x016B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s073" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
  9: 0x017C [0x01] GOTO 0x01E4
 10: 0x017F [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x019B
 11: 0x0187 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s070" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
 12: 0x0198 [0x01] GOTO 0x01E4
 13: 0x019B [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x01B7
 14: 0x01A3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s070" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
 15: 0x01B4 [0x01] GOTO 0x01E4
 16: 0x01B7 [0x02] IF !(Work_Zone[9] == 8*) GOTO 0x01D3
 17: 0x01BF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s071" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
 18: 0x01D0 [0x01] GOTO 0x01E4
 19: 0x01D3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s069" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]

SUBROUTINE_01E4:
 20: 0x01E4 [0x1C] WAIT(80* ticks)
 21: 0x01E7 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01E8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                          00                               .       
```

#### Opcodes

```
  0: 0x01E8 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E9   |
| Data Size    | 73 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                             45 00 80 F8 FF FF 7F           E......
01F0: F8 FF FF 7F 73 30 37 34  01 80 1C 03 80 52 00 80  ....s074.....R..
0200: F8 FF FF 7F F8 FF FF 7F  73 30 37 34 45 03 80 F0  ........s074E...
0210: FF FF 7F F0 FF FF 7F 6F  76 6C 31 01 80 45 00 80  .......ovl1..E..
0220: F0 FF FF 7F F0 FF FF 7F  73 30 37 35 01 80 1C 0F  ........s075....
0230: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x01E9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s074" with entities [EventEntity, EventEntity], work=[211*, 0*]
  1: 0x01FA [0x1C] WAIT(200* ticks)
  2: 0x01FD [0x52] END_LOAD_SCHEDULER: End scheduler "s074" with entities [EventEntity, EventEntity], work=211*
  3: 0x020C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x021D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s075" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
  5: 0x022E [0x1C] WAIT(100* ticks)
  6: 0x0231 [0x00] END_REQSTACK()
```
