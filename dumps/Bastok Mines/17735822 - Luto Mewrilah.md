# 17735822 - Luto Mewrilah

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 268 bytes              |
| Total Events     | 7                      |
| References Count | 23                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [502](#event-502)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     15 |              3 |
| [65535.2](#event-655352) | 0x0011       |     17 |              5 |
| [65535.3](#event-655353) | 0x0022       |     15 |              3 |
| [65535.4](#event-655354) | 0x0031       |     37 |              5 |
| [65535.5](#event-655355) | 0x0056       |     44 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFB3D4  |  4294947796 |
|       1 | 0xFFFFCC23  |  4294954019 |
|       2 | 0xFFFFFFD4  |  4294967252 |
|       3 | 0x0882      |        2178 |
|       4 | 0x003C      |          60 |
|       5 | 0x000D      |          13 |
|       6 | 0xFFFFB79A  |  4294948762 |
|       7 | 0xFFFFD628  |  4294956584 |
|       8 | 0xFFFFFFD2  |  4294967250 |
|       9 | 0xFFFFCFE8  |  4294954984 |
|      10 | 0xFFFFCAE8  |  4294953704 |
|      11 | 0x04F9      |        1273 |
|      12 | 0x001C      |          28 |
|      13 | 0x0064      |         100 |
|      14 | 0xFFFFD904  |  4294957316 |
|      15 | 0xFFFFD939  |  4294957369 |
|      16 | 0xFFFFFFC8  |  4294967240 |
|      17 | 0xFFFFE2B5  |  4294959797 |
|      18 | 0xFFFFD8E5  |  4294957285 |
|      19 | 0xFFFFFFD6  |  4294967254 |
|      20 | 0xFFFFE947  |  4294961479 |
|      21 | 0xFFFFCEA3  |  4294954659 |
|      22 | 0x0000      |           0 |

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

### Event 502

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
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 80 8E A0 0E 01    7.............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-19.500*, z=-13.277*, y=-0.044*, direction=191.4°*
  1: 0x000B [0x80] LOAD_WAIT(entity=Luto Mewrilah (ID: 17735822/0x010EA08E))
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    1C 04 80 32 05 80 1F  00 06 80 07 80 08 80 1F   ...2...........
0020: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0011 [0x1C] WAIT(60* ticks)
  1: 0x0014 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0017 [0x1F] MOVE_ENTITY: EventEntity moves to X=-18.534*, Z=-10.712*, Y=-0.046*
  3: 0x001F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       37 09 80 0A 80 02  80 0B 80 80 F8 FF FF 7F    7.............
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0022 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-12.312*, z=-13.592*, y=-0.044*, direction=111.9°*
  1: 0x002B [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    66 0C 80 8E A0 0E 01  8E A0 0E 01 79 6B 6F 30   f..........yko0
0040: 1C 0D 80 66 0C 80 8E A0  0E 01 8E A0 0E 01 79 6B  ...f..........yk
0050: 6F 31 1C 0D 80 00                                 o1....          
```

#### Opcodes

```
  0: 0x0031 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "yko0" with entities [Luto Mewrilah (ID: 17735822/0x010EA08E), Luto Mewrilah (ID: 17735822/0x010EA08E)], work=28*
  1: 0x0040 [0x1C] WAIT(100* ticks)
  2: 0x0043 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "yko1" with entities [Luto Mewrilah (ID: 17735822/0x010EA08E), Luto Mewrilah (ID: 17735822/0x010EA08E)], work=28*
  3: 0x0052 [0x1C] WAIT(100* ticks)
  4: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   32 05  80 1F 00 0E 80 0F 80 10        2.........
0060: 80 1F 01 27 05 4F A0 0E  01 02 1C 04 80 1F 00 11  ...'.O..........
0070: 80 12 80 13 80 1F 01 1F  00 14 80 15 80 16 80 1F  ................
0080: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0056 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0059 [0x1F] MOVE_ENTITY: EventEntity moves to X=-9.980*, Z=-9.927*, Y=-0.056*
  2: 0x0061 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0063 [0x27] REQ_SET(priority=0x05, entity_id=Door:Boytz's Knickknacks (ID: 17735759/0x010EA04F), tag_num=0x02)
  4: 0x006A [0x1C] WAIT(60* ticks)
  5: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.499*, Z=-10.011*, Y=-0.042*
  6: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0077 [0x1F] MOVE_ENTITY: EventEntity moves to X=-5.817*, Z=-12.637*, Y=0.000*
  8: 0x007F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0081 [0x00] END_REQSTACK()
```
