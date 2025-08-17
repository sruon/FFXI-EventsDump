# 17977527 - Gilgamesh

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Reisenjima Sanctorium (ID: 293) |
| Block Size       | 208 bytes                       |
| Total Events     | 9                               |
| References Count | 15                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [6](#event-6)            | 0x0001       |      1 |              1 |
| [9](#event-9)            | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     22 |              6 |
| [65535.2](#event-655352) | 0x0019       |     22 |              6 |
| [65535.3](#event-655353) | 0x002F       |     14 |              4 |
| [65535.4](#event-655354) | 0x003D       |     24 |              6 |
| [11](#event-11)          | 0x0055       |      5 |              2 |
| [65535.5](#event-655355) | 0x005A       |      5 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFFFFD7  |  4294967255 |
|       2 | 0x25CE      |        9678 |
|       3 | 0x0F9F      |        3999 |
|       4 | 0x001E      |          30 |
|       5 | 0xFFFFFD20  |  4294966560 |
|       6 | 0x2E3B      |       11835 |
|       7 | 0xFFFFFFFF  |  4294967295 |
|       8 | 0x4458      |       17496 |
|       9 | 0xFFFFF8EA  |  4294965482 |
|      10 | 0x0B09      |        2825 |
|      11 | 0xFFFFF872  |  4294965362 |
|      12 | 0xFFFFE140  |  4294959424 |
|      13 | 0x099E      |        2462 |
|      14 | 0x058F      |        1423 |

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

### Event 9

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
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 1E F0 FF FF 7F 1C 04 80  00                       .........       
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.041*, Z=9.678*, Y=3.999*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0015 [0x1C] WAIT(30* ticks)
  5: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             32 00 80 1F 00 05 80           2......
0020: 06 80 03 80 1F 01 1E F0  FF FF 7F 1C 04 80 00     ............... 
```

#### Opcodes

```
  0: 0x0019 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.736*, Z=11.835*, Y=3.999*
  2: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0026 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x002B [0x1C] WAIT(30* ticks)
  5: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               32                 2
0030: 00 80 1F 00 07 80 08 80  03 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x002F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.001*, Z=17.496*, Y=3.999*
  2: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         32 00 80               2..
0040: 1F 00 09 80 0A 80 03 80  1F 01 1F 00 0B 80 0C 80  ................
0050: 03 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x003D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0040 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.814*, Z=2.825*, Y=3.999*
  2: 0x0048 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004A [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.934*, Z=-7.872*, Y=3.999*
  4: 0x0052 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0054 [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0055  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                B6 00 0D  80 00                         .....      
```

#### Opcodes

```
  0: 0x0055 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2462*)
  1: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005A  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                B6 00 0E 80 00               ..... 
```

#### Opcodes

```
  0: 0x005A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1423*)
  1: 0x005E [0x00] END_REQSTACK()
```
