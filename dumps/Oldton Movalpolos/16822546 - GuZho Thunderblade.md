# 16822546 - GuZho Thunderblade

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Oldton Movalpolos (ID: 11) |
| Block Size       | 160 bytes                  |
| Total Events     | 6                          |
| References Count | 12                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [60](#event-60)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     24 |              6 |
| [65535.2](#event-655352) | 0x0023       |     14 |              4 |
| [61](#event-61)          | 0x0031       |     10 |              2 |
| [65](#event-65)          | 0x003B       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFB2BF5  |  4294650869 |
|       1 | 0xFFFC04FC  |  4294706428 |
|       2 | 0x1FBC      |        8124 |
|       3 | 0x082D      |        2093 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFB272D  |  4294649645 |
|       6 | 0xFFFC0994  |  4294707604 |
|       7 | 0xFFFB231B  |  4294648603 |
|       8 | 0xFFFC0B27  |  4294708007 |
|       9 | 0xFFFB1256  |  4294644310 |
|      10 | 0xFFFC0B33  |  4294708019 |
|      11 | 0x1F2A      |        7978 |

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

### Event 60

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-316.427*, z=-260.868*, y=8.124*, direction=183.9°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 02 80 1F 01  1F 00 07 80 08 80 02 80  ................
0020: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-317.651*, Z=-259.692*, Y=8.124*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=-318.693*, Z=-259.289*, Y=8.124*
  4: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          32 04 80 1F 00  09 80 0A 80 0B 80 1F 01     2............
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0023 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=-322.986*, Z=-259.277*, Y=7.978*
  2: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0030 [0x00] END_REQSTACK()
```

### Event 61

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0031 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-316.427*, z=-260.868*, y=8.124*, direction=183.9°*
  1: 0x003A [0x00] END_REQSTACK()
```

### Event 65

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   37 00 80 01 80             7....
0040: 02 80 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x003B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-316.427*, z=-260.868*, y=8.124*, direction=183.9°*
  1: 0x0044 [0x00] END_REQSTACK()
```
