# 16986784 - Rughadjeen

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Wajaom Woodlands (ID: 51) |
| Block Size       | 376 bytes                 |
| Total Events     | 14                        |
| References Count | 31                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [12](#event-12)            | 0x0001       |      1 |              1 |
| [13](#event-13)            | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |     19 |              5 |
| [65535.2](#event-655352)   | 0x0016       |     33 |              7 |
| [65535.3](#event-655353)   | 0x0037       |     15 |              5 |
| [65535.4](#event-655354)   | 0x0046       |     20 |              6 |
| [65535.5](#event-655355)   | 0x005A       |     14 |              4 |
| [65535.6](#event-655356)   | 0x0068       |     14 |              4 |
| [65535.7](#event-655357)   | 0x0076       |     15 |              5 |
| [65535.8](#event-655358)   | 0x0085       |     14 |              4 |
| [65535.9](#event-655359)   | 0x0093       |     14 |              4 |
| [65535.10](#event-6553510) | 0x00A1       |      4 |              2 |
| [65535.11](#event-6553511) | 0x00A5       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFF0BB7  |  4294904759 |
|       2 | 0x6CD8      |       27864 |
|       3 | 0xFFFFE891  |  4294961297 |
|       4 | 0xFFFF0987  |  4294904199 |
|       5 | 0xB6C8      |       46792 |
|       6 | 0xFFFFE890  |  4294961296 |
|       7 | 0x0B54      |        2900 |
|       8 | 0xFFFF0627  |  4294903335 |
|       9 | 0xC2CD      |       49869 |
|      10 | 0xFFFF063F  |  4294903359 |
|      11 | 0xE033      |       57395 |
|      12 | 0xFFFF10E0  |  4294906080 |
|      13 | 0xF4D7      |       62679 |
|      14 | 0x000D      |          13 |
|      15 | 0xFFFF0AD8  |  4294904536 |
|      16 | 0x7BFF      |       31743 |
|      17 | 0xFFFFFE9A  |  4294966938 |
|      18 | 0xFFFFB256  |  4294947414 |
|      19 | 0x0000      |           0 |
|      20 | 0xFFFFFF46  |  4294967110 |
|      21 | 0xFFFFD6C3  |  4294956739 |
|      22 | 0x20D63     |      134499 |
|      23 | 0x054F      |        1359 |
|      24 | 0xFFFFF98D  |  4294965645 |
|      25 | 0x2040E     |      132110 |
|      26 | 0x0454      |        1108 |
|      27 | 0xFFFFFBE5  |  4294966245 |
|      28 | 0x00C8      |         200 |
|      29 | 0xFFFF5337  |  4294923063 |
|      30 | 0x7059      |       28761 |

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

### Event 12

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

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          7B A0 32 03 01  32 00 80 1F 00 01 80 02     {.2..2.......
0010: 80 03 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0003 [0x7B] Rughadjeen (ID: 16986784/0x010332A0) stops talking
  1: 0x0008 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=-62.537*, Z=27.864*, Y=-5.999*
  3: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   1E B1  32 03 01 37 04 80 05 80        ..2..7....
0020: 06 80 07 80 32 00 80 1F  00 08 80 09 80 03 80 1F  ....2...........
0030: 01 1E B1 32 03 01 00                              ...2...         
```

#### Opcodes

```
  0: 0x0016 [0x1E] EventEntity looks at Ovjang (ID: 16986801/0x010332B1) and starts talking
  1: 0x001B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-63.097*, z=46.792*, y=-6.000*, direction=254.9°*
  2: 0x0024 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-63.961*, Z=49.869*, Y=-5.999*
  4: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0031 [0x1E] EventEntity looks at Ovjang (ID: 16986801/0x010332B1) and starts talking
  6: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      32  00 80 1F 00 0A 80 0B 80         2........
0040: 06 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0037 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=-63.937*, Z=57.395*, Y=-6.000*
  2: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0044 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   1E B2  32 03 01 32 00 80 1F 00        ..2..2....
0050: 0C 80 0D 80 03 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0046 [0x1E] EventEntity looks at Aphmau (ID: 16986802/0x010332B2) and starts talking
  1: 0x004B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x004E [0x1F] MOVE_ENTITY: EventEntity moves to X=-61.216*, Z=62.679*, Y=-5.999*
  3: 0x0056 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0058 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                32 0E 80 1F 00 0F            2.....
0060: 80 10 80 06 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x005A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005D [0x1F] MOVE_ENTITY: EventEntity moves to X=-62.760*, Z=31.743*, Y=-6.000*
  2: 0x0065 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          32 0E 80 1F 00 11 80 12          2.......
0070: 80 13 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0068 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006B [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.358*, Z=-19.882*, Y=0.000*
  2: 0x0073 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   32 0E  80 1F 00 14 80 15 80 13        2.........
0080: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0076 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0079 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.186*, Z=-10.557*, Y=0.000*
  2: 0x0081 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0083 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                32 0E 80  1F 00 16 80 17 80 18 80       2..........
0090: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0085 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0088 [0x1F] MOVE_ENTITY: EventEntity moves to X=134.499*, Z=1.359*, Y=-1.651*
  2: 0x0090 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0092 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0093   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          32 0E 80 1F 00  19 80 1A 80 1B 80 1F 01     2............
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0093 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0096 [0x1F] MOVE_ENTITY: EventEntity moves to X=132.110*, Z=1.108*, Y=-1.051*
  2: 0x009E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A0 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A1  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    39 1C 80 00                                     9...           
```

#### Opcodes

```
  0: 0x00A1 [0x39] SET_ENTITY_DIRECTION(direction=1.1°*)
  1: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                32 00 80  1F 00 1D 80 1E 80 13 80       2..........
00B0: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x00A5 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00A8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-44.233*, Z=28.761*, Y=0.000*
  2: 0x00B0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B2 [0x00] END_REQSTACK()
```
