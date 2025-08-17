# 17138557 - Five Moons

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | North Gustaberg [S] (ID: 88) |
| Block Size       | 168 bytes                    |
| Total Events     | 8                            |
| References Count | 10                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [6](#event-6)            | 0x0001       |      9 |              3 |
| [65535.1](#event-655351) | 0x000A       |      3 |              2 |
| [65535.2](#event-655352) | 0x000D       |      3 |              2 |
| [13](#event-13)          | 0x0010       |      7 |              2 |
| [65535.3](#event-655353) | 0x0017       |     26 |              7 |
| [65535.4](#event-655354) | 0x0031       |     16 |              5 |
| [65535.5](#event-655355) | 0x0041       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0xFFFC728F  |  4294734479 |
|       2 | 0x17B9B     |       97179 |
|       3 | 0x0000      |           0 |
|       4 | 0xFFFC70E1  |  4294734049 |
|       5 | 0x1BBFB     |      113659 |
|       6 | 0xFFFFFD90  |  4294966672 |
|       7 | 0x5DA12     |      383506 |
|       8 | 0x2A079     |      172153 |
|       9 | 0x09A6      |        2470 |

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

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F A4  01 00                     .........      
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  2: 0x0009 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000A  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                A5 01 00                     ...   
```

#### Opcodes

```
  0: 0x000A [0xA5] EventEntity->Flags3.BallistaTeam |= 0x08  // Set bit 3 of BallistaTeam
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         A5 00 00               ...
```

#### Opcodes

```
  0: 0x000D [0xA5] EventEntity->Flags3.BallistaTeam &= ~0x08  // Clear bit 3 of BallistaTeam
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0010 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      33  01 32 00 80 1F 00 01 80         3.2......
0020: 02 80 03 80 1F 01 1F 00  04 80 05 80 06 80 1F 01  ................
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0017 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0019 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  2: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=-232.817*, Z=97.179*, Y=0.000*
  3: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=-233.247*, Z=113.659*, Y=-0.624*
  5: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    33 01 32 00 80 1F 00  04 80 05 80 06 80 1F 01   3.2............
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0031 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0033 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  2: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-233.247*, Z=113.659*, Y=-0.624*
  3: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    32 00 80 1F 00 07 80  08 80 09 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0041 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=383.506*, Z=172.153*, Y=2.470*
  2: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004E [0x00] END_REQSTACK()
```
