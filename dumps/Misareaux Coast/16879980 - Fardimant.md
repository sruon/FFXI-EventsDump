# 16879980 - Fardimant

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Misareaux Coast (ID: 25) |
| Block Size       | 208 bytes                |
| Total Events     | 10                       |
| References Count | 18                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [556](#event-556)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     14 |              4 |
| [65535.2](#event-655352) | 0x0010       |     14 |              4 |
| [557](#event-557)        | 0x001E       |      1 |              1 |
| [65535.3](#event-655353) | 0x001F       |     10 |              2 |
| [558](#event-558)        | 0x0029       |      1 |              1 |
| [65535.4](#event-655354) | 0x002A       |     10 |              2 |
| [65535.5](#event-655355) | 0x0034       |     14 |              4 |
| [65535.6](#event-655356) | 0x0042       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFDAC52  |  4294814802 |
|       2 | 0x9E40D     |      648205 |
|       3 | 0xFFFFC342  |  4294951746 |
|       4 | 0xFFFDA700  |  4294813440 |
|       5 | 0x9E132     |      647474 |
|       6 | 0xFFFFC32D  |  4294951725 |
|       7 | 0x0538      |        1336 |
|       8 | 0xFFFDB387  |  4294816647 |
|       9 | 0x9E304     |      647940 |
|      10 | 0xFFFFC32B  |  4294951723 |
|      11 | 0x0653      |        1619 |
|      12 | 0xFFFD9EEF  |  4294811375 |
|      13 | 0x9D798     |      645016 |
|      14 | 0xFFFFC2C0  |  4294951616 |
|      15 | 0xFFFE0861  |  4294838369 |
|      16 | 0x9B2D3     |      635603 |
|      17 | 0xFFFFC328  |  4294951720 |

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

### Event 556

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
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-152.494*, Z=648.205*, Y=-15.550*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 32 00 80 1F 00 04 80 05  80 06 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0010 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0013 [0x1F] MOVE_ENTITY: EventEntity moves to X=-153.856*, Z=647.474*, Y=-15.571*
  2: 0x001B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001D [0x00] END_REQSTACK()
```

### Event 557

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            00                   . 
```

#### Opcodes

```
  0: 0x001E [0x00] END_REQSTACK()
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
0020: 04 80 05 80 06 80 07 80  00                       .........       
```

#### Opcodes

```
  0: 0x001F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-153.856*, z=647.474*, y=-15.571*, direction=117.4°*
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 558

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             00                             .      
```

#### Opcodes

```
  0: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                37 08 80 09 80 0A            7.....
0030: 80 0B 80 00                                       ....            
```

#### Opcodes

```
  0: 0x002A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-150.649*, z=647.940*, y=-15.573*, direction=142.3°*
  1: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             32 00 80 1F  00 0C 80 0D 80 0E 80 1F      2...........
0040: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0034 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=-155.921*, Z=645.016*, Y=-15.680*
  2: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       32 00 80 1F 00 0F  80 10 80 11 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0042 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=-128.927*, Z=635.603*, Y=-15.576*
  2: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004F [0x00] END_REQSTACK()
```
