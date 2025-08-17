# 17965080 - Disjoined One

## Common Data

| Field            | Value                                 |
|------------------|---------------------------------------|
| Zone             | Desuetia - Empyreal Paradox (ID: 290) |
| Block Size       | 412 bytes                             |
| Total Events     | 9                                     |
| References Count | 15                                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [2](#event-2)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     14 |              4 |
| [4](#event-4)            | 0x0010       |      1 |              1 |
| [5](#event-5)            | 0x0011       |      1 |              1 |
| [6](#event-6)            | 0x0012       |      1 |              1 |
| [7](#event-7)            | 0x0013       |      1 |              1 |
| [65535.2](#event-655352) | 0x0014       |    256 |             26 |
| [65535.3](#event-655353) | 0x0114       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x7E90B     |      518411 |
|       2 | 0x85D44     |      548164 |
|       3 | 0xFFF85EE0  |  4294467296 |
|       4 | 0x0001      |           1 |
|       5 | 0x0000      |           0 |
|       6 | 0x00E6      |         230 |
|       7 | 0x0002      |           2 |
|       8 | 0x0003      |           3 |
|       9 | 0x0004      |           4 |
|      10 | 0x0005      |           5 |
|      11 | 0x0006      |           6 |
|      12 | 0x0007      |           7 |
|      13 | 0x0008      |           8 |
|      14 | 0x0184      |         388 |

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

### Event 2

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=518.411*, Z=548.164*, Y=-500.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0010 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    00                                              .              
```

#### Opcodes

```
  0: 0x0011 [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       00                                            .             
```

#### Opcodes

```
  0: 0x0012 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0013  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          00                                          .            
```

#### Opcodes

```
  0: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0014    |
| Data Size    | 256 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             29 10 F0 FF  FF 7F 02 02 02 10 04 80      )...........
0020: 80 3A 00 B6 0B 04 80 03  10 05 80 06 80 06 80 06  .:..............
0030: 80 06 80 05 80 05 80 01  13 01 02 02 10 07 80 80  ................
0040: 59 00 B6 0B 07 80 03 10  05 80 06 80 06 80 06 80  Y...............
0050: 06 80 05 80 05 80 01 13  01 02 02 10 08 80 80 78  ...............x
0060: 00 B6 0B 08 80 03 10 05  80 06 80 06 80 06 80 06  ................
0070: 80 05 80 05 80 01 13 01  02 02 10 09 80 80 97 00  ................
0080: B6 0B 09 80 03 10 05 80  06 80 06 80 06 80 06 80  ................
0090: 05 80 05 80 01 13 01 02  02 10 0A 80 80 B6 00 B6  ................
00A0: 0B 0A 80 03 10 05 80 06  80 06 80 06 80 06 80 05  ................
00B0: 80 05 80 01 13 01 02 02  10 0B 80 80 D5 00 B6 0B  ................
00C0: 0B 80 03 10 05 80 06 80  06 80 06 80 06 80 05 80  ................
00D0: 05 80 01 13 01 02 02 10  0C 80 80 F4 00 B6 0B 0C  ................
00E0: 80 03 10 05 80 06 80 06  80 06 80 06 80 05 80 05  ................
00F0: 80 01 13 01 02 02 10 0D  80 80 13 01 B6 0B 0D 80  ................
0100: 03 10 05 80 06 80 06 80  06 80 06 80 05 80 05 80  ................
0110: 01 13 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0014 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
  1: 0x001B [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x003A
  2: 0x0023 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  3: 0x0037 [0x01] GOTO 0x0113
  4: 0x003A [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0059
  5: 0x0042 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=2*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  6: 0x0056 [0x01] GOTO 0x0113
  7: 0x0059 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x0078
  8: 0x0061 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  9: 0x0075 [0x01] GOTO 0x0113
 10: 0x0078 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0097
 11: 0x0080 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 12: 0x0094 [0x01] GOTO 0x0113
 13: 0x0097 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x00B6
 14: 0x009F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 15: 0x00B3 [0x01] GOTO 0x0113
 16: 0x00B6 [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x00D5
 17: 0x00BE [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 18: 0x00D2 [0x01] GOTO 0x0113
 19: 0x00D5 [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x00F4
 20: 0x00DD [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 21: 0x00F1 [0x01] GOTO 0x0113
 22: 0x00F4 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x0113
 23: 0x00FC [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 24: 0x0110 [0x01] GOTO 0x0113

SUBROUTINE_0113:
 25: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             B6 0B 08 80  07 80 0E 80 06 80 06 80      ............
0120: 06 80 06 80 05 80 05 80  00                       .........       
```

#### Opcodes

```
  0: 0x0114 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=388*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  1: 0x0128 [0x00] END_REQSTACK()
```
