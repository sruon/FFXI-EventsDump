# 17391858 - Overlord Bakgodek

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Monastic Cavern (ID: 150) |
| Block Size       | 180 bytes                 |
| Total Events     | 6                         |
| References Count | 18                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [8](#event-8)            | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     15 |              5 |
| [9](#event-9)            | 0x001A       |     10 |              2 |
| [65535.2](#event-655352) | 0x0024       |     15 |              5 |
| [65535.3](#event-655353) | 0x0033       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFDD9B7  |  4294826423 |
|       1 | 0xFFFFA39D  |  4294943645 |
|       2 | 0xFFFFDBFD  |  4294958077 |
|       3 | 0x011E      |         286 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFDD294  |  4294824596 |
|       6 | 0xFFFF9B4A  |  4294941514 |
|       7 | 0xFFFFDD49  |  4294958409 |
|       8 | 0xFFFDCC96  |  4294823062 |
|       9 | 0xFFFF957E  |  4294940030 |
|      10 | 0xFFFFDEF3  |  4294958835 |
|      11 | 0x0735      |        1845 |
|      12 | 0xFFFDC992  |  4294822290 |
|      13 | 0xFFFF9784  |  4294940548 |
|      14 | 0xFFFFDEEC  |  4294958828 |
|      15 | 0xFFFDDBB4  |  4294826932 |
|      16 | 0xFFFFA3D5  |  4294943701 |
|      17 | 0xFFFFDBC3  |  4294958019 |

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

### Event 8

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-140.873*, z=-23.651*, y=-9.219*, direction=25.1°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 07 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-142.700*, Z=-25.782*, Y=-8.887*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                37 08 80 09 80 0A            7.....
0020: 80 0B 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-144.234*, z=-27.266*, y=-8.461*, direction=162.2°*
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 04 80 1F  00 0C 80 0D 80 0E 80 1F      2...........
0030: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-145.006*, Z=-26.748*, Y=-8.468*
  2: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          32 04 80 1F 00  0F 80 10 80 11 80 1F 01     2............
0040: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0033 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-140.364*, Z=-23.595*, Y=-9.277*
  2: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0041 [0x00] END_REQSTACK()
```
