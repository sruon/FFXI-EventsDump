# 17830079 - Ari-Barali

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 224 bytes                 |
| Total Events     | 6                         |
| References Count | 18                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [5052](#event-5052)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     35 |              9 |
| [65535.2](#event-655352) | 0x0025       |     14 |              4 |
| [65535.3](#event-655353) | 0x0033       |     38 |             10 |
| [65535.4](#event-655354) | 0x0059       |     21 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFFFFF9  |  4294967289 |
|       2 | 0xFFFFA22F  |  4294943279 |
|       3 | 0x0000      |           0 |
|       4 | 0x0DAC      |        3500 |
|       5 | 0x003C      |          60 |
|       6 | 0x0AC1      |        2753 |
|       7 | 0x0028      |          40 |
|       8 | 0x000C      |          12 |
|       9 | 0xFFFFAFF5  |  4294946805 |
|      10 | 0xFFFFFC18  |  4294966296 |
|      11 | 0xFFFFDF53  |  4294958931 |
|      12 | 0x001E      |          30 |
|      13 | 0xFFFFFB24  |  4294966052 |
|      14 | 0xFFFFE19C  |  4294959516 |
|      15 | 0x0C24      |        3108 |
|      16 | 0xFFFFFC6F  |  4294966383 |
|      17 | 0xFFFFE1D4  |  4294959572 |

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

### Event 5052

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
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 4B F8 FF FF 7F 04 80 1C  05 80 4B F8 FF FF 7F 06  K.........K.....
0020: 80 1C 05 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.007*, Z=-24.017*, Y=0.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=19.2°*)
  5: 0x0017 [0x1C] WAIT(60* ticks)
  6: 0x001A [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=15.1°*)
  7: 0x0021 [0x1C] WAIT(60* ticks)
  8: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                32 07 80  1F 00 08 80 09 80 03 80       2..........
0030: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0025 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.012*, Z=-20.491*, Y=0.000*
  2: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 38 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          32 00 80 1F 00  0A 80 0B 80 03 80 1F 01     2............
0040: 6F 1C 0C 80 1F 00 0D 80  0E 80 03 80 1F 01 4B F8  o.............K.
0050: FF FF 7F 0F 80 1C 0C 80  00                       .........       
```

#### Opcodes

```
  0: 0x0033 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.000*, Z=-8.365*, Y=0.000*
  2: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0041 [0x1C] WAIT(30* ticks)
  5: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.244*, Z=-7.780*, Y=0.000*
  6: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x004E [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=17.1°*)
  8: 0x0055 [0x1C] WAIT(30* ticks)
  9: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             32 00 80 1F 00 10 80           2......
0060: 11 80 03 80 1F 01 4B F8  FF FF 7F 0F 80 00        ......K.......  
```

#### Opcodes

```
  0: 0x0059 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.913*, Z=-7.724*, Y=0.000*
  2: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0066 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=17.1°*)
  4: 0x006D [0x00] END_REQSTACK()
```
