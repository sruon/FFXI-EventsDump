# 17248937 - Morzivold

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 216 bytes                   |
| Total Events     | 5                           |
| References Count | 21                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [919](#event-919)        | 0x0001       |      7 |              2 |
| [920](#event-920)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     54 |             12 |
| [65535.2](#event-655352) | 0x0045       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x3B6CA     |      243402 |
|       2 | 0x487D      |       18557 |
|       3 | 0xFFFFEC54  |  4294962260 |
|       4 | 0x3B0FE     |      241918 |
|       5 | 0x3CC1      |       15553 |
|       6 | 0xFFFFED1C  |  4294962460 |
|       7 | 0x3A4E8     |      238824 |
|       8 | 0x2D01      |       11521 |
|       9 | 0xFFFFEE96  |  4294962838 |
|      10 | 0x38CEE     |      232686 |
|      11 | 0x2122      |        8482 |
|      12 | 0xFFFFEE89  |  4294962825 |
|      13 | 0x3289B     |      207003 |
|      14 | 0xFFFFF3E2  |  4294964194 |
|      15 | 0xFFFFEFA3  |  4294963107 |
|      16 | 0x397A7     |      235431 |
|      17 | 0x1970      |        6512 |
|      18 | 0xFFFFEFD8  |  4294963160 |
|      19 | 0x000A      |          10 |
|      20 | 0x0F92      |        3986 |

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

### Event 919

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 920

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 54 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               32                 2
0010: 00 80 1F 00 01 80 02 80  03 80 1F 01 1F 00 04 80  ................
0020: 05 80 06 80 1F 01 1F 00  07 80 08 80 09 80 1F 01  ................
0030: 1F 00 0A 80 0B 80 0C 80  1F 01 1F 00 0D 80 0E 80  ................
0040: 0F 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x000F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=243.402*, Z=18.557*, Y=-5.036*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=241.918*, Z=15.553*, Y=-4.836*
  4: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=238.824*, Z=11.521*, Y=-4.458*
  6: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=232.686*, Z=8.482*, Y=-4.471*
  8: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=207.003*, Z=-3.102*, Y=-4.189*
 10: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                32 00 80  1F 00 10 80 11 80 12 80       2..........
0050: 1F 01 1C 13 80 4B F8 FF  FF 7F 14 80 00           .....K.......   
```

#### Opcodes

```
  0: 0x0045 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0048 [0x1F] MOVE_ENTITY: EventEntity moves to X=235.431*, Z=6.512*, Y=-4.136*
  2: 0x0050 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0052 [0x1C] WAIT(10* ticks)
  4: 0x0055 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=21.9°*)
  5: 0x005C [0x00] END_REQSTACK()
```
