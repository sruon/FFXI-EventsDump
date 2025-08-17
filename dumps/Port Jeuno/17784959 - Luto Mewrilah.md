# 17784959 - Luto Mewrilah

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Port Jeuno (ID: 246) |
| Block Size       | 212 bytes            |
| Total Events     | 8                    |
| References Count | 16                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [309](#event-309)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     14 |              4 |
| [65535.2](#event-655352) | 0x0010       |     22 |              6 |
| [65535.3](#event-655353) | 0x0026       |     19 |              5 |
| [65535.4](#event-655354) | 0x0039       |     15 |              3 |
| [65535.5](#event-655355) | 0x0048       |     14 |              4 |
| [65535.6](#event-655356) | 0x0056       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFFC264  |  4294951524 |
|       2 | 0x22DB      |        8923 |
|       3 | 0x0000      |           0 |
|       4 | 0xFFFFC39A  |  4294951834 |
|       5 | 0x1C9E      |        7326 |
|       6 | 0x001E      |          30 |
|       7 | 0xFFFFC1F1  |  4294951409 |
|       8 | 0x1E47      |        7751 |
|       9 | 0x3927      |       14631 |
|      10 | 0xFFFFFBF8  |  4294966264 |
|      11 | 0x003F      |          63 |
|      12 | 0x5022      |       20514 |
|      13 | 0xFFFFFB04  |  4294966020 |
|      14 | 0x75C7      |       30151 |
|      15 | 0xFFFFF9D7  |  4294965719 |

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

### Event 309

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
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-15.772*, Z=8.923*, Y=0.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 32 00 80 1F 00 04 80 05  80 03 80 1F 01 1E 7E 60  2.............~`
0020: 0F 01 1C 06 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0010 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0013 [0x1F] MOVE_ENTITY: EventEntity moves to X=-15.462*, Z=7.326*, Y=0.000*
  2: 0x001B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001D [0x1E] EventEntity looks at Palometa (ID: 17784958/0x010F607E) and starts talking
  4: 0x0022 [0x1C] WAIT(30* ticks)
  5: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   32 00  80 1F 00 07 80 08 80 03        2.........
0030: 80 1F 01 1E 7E 60 0F 01  00                       ....~`...       
```

#### Opcodes

```
  0: 0x0026 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0029 [0x1F] MOVE_ENTITY: EventEntity moves to X=-15.887*, Z=7.751*, Y=0.000*
  2: 0x0031 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0033 [0x1E] EventEntity looks at Palometa (ID: 17784958/0x010F607E) and starts talking
  4: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             37 09 80 0A 80 03 80           7......
0040: 0B 80 80 F8 FF FF 7F 00                           ........        
```

#### Opcodes

```
  0: 0x0039 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=14.631*, z=-1.032*, y=0.000*, direction=5.5°*
  1: 0x0042 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          32 00 80 1F 00 0C 80 0D          2.......
0050: 80 03 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0048 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=20.514*, Z=-1.276*, Y=0.000*
  2: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   32 00  80 1F 00 0E 80 0F 80 03        2.........
0060: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0056 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0059 [0x1F] MOVE_ENTITY: EventEntity moves to X=30.151*, Z=-1.577*, Y=0.000*
  2: 0x0061 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0063 [0x00] END_REQSTACK()
```
