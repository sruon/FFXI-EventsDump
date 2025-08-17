# 17748092 - Viresefilant

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 216 bytes            |
| Total Events     | 8                    |
| References Count | 20                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [802](#event-802)        | 0x0001       |      1 |              1 |
| [805](#event-805)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     14 |              4 |
| [65535.2](#event-655352) | 0x0011       |     14 |              4 |
| [65535.3](#event-655353) | 0x001F       |     10 |              2 |
| [65535.4](#event-655354) | 0x0029       |     21 |              5 |
| [65535.5](#event-655355) | 0x003E       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000A      |          10 |
|       1 | 0x20788     |      133000 |
|       2 | 0xFFFF7748  |  4294932296 |
|       3 | 0xFFFFB5C8  |  4294948296 |
|       4 | 0x0014      |          20 |
|       5 | 0x1D4C0     |      120000 |
|       6 | 0xFFFFAA10  |  4294945296 |
|       7 | 0xFFFFBD98  |  4294950296 |
|       8 | 0x180CD     |       98509 |
|       9 | 0x3269      |       12905 |
|      10 | 0xFFFFB136  |  4294947126 |
|      11 | 0x0AB6      |        2742 |
|      12 | 0x16B48     |       93000 |
|      13 | 0x2AF8      |       11000 |
|      14 | 0xFFFFB127  |  4294947111 |
|      15 | 0x000F      |          15 |
|      16 | 0x15F90     |       90000 |
|      17 | 0x15BA8     |       89000 |
|      18 | 0x2328      |        9000 |
|      19 | 0x0FA0      |        4000 |

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

### Event 802

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

### Event 805

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=133.000*, Z=-35.000*, Y=-19.000*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 20* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=120.000*, Z=-22.000*, Y=-17.000*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               37                 7
0020: 08 80 09 80 0A 80 0B 80  00                       .........       
```

#### Opcodes

```
  0: 0x001F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=98.509*, z=12.905*, y=-20.170*, direction=241.0°*
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             36 0C 80 0D 80 0E 80           6......
0030: 32 0F 80 1F 00 10 80 0D  80 0E 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0029 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=93.000*, pos_z=11.000*, pos_y=-20.185*)
  1: 0x0030 [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  2: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=90.000*, Z=11.000*, Y=-20.185*
  3: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            32 0F                2.
0040: 80 1F 00 11 80 12 80 0E  80 1F 01 1F 00 11 80 13  ................
0050: 80 0E 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x003E [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x0041 [0x1F] MOVE_ENTITY: EventEntity moves to X=89.000*, Z=9.000*, Y=-20.185*
  2: 0x0049 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=89.000*, Z=4.000*, Y=-20.185*
  4: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0055 [0x00] END_REQSTACK()
```
