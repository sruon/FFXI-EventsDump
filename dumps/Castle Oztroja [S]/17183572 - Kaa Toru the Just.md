# 17183572 - Kaa Toru the Just

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Castle Oztroja [S] (ID: 99) |
| Block Size       | 196 bytes                   |
| Total Events     | 8                           |
| References Count | 14                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [101](#event-101)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     23 |              7 |
| [65535.2](#event-655352) | 0x001F       |     14 |              4 |
| [102](#event-102)        | 0x002D       |      7 |              2 |
| [103](#event-103)        | 0x0034       |      7 |              2 |
| [65535.3](#event-655353) | 0x003B       |     15 |              5 |
| [65535.4](#event-655354) | 0x004A       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000F      |          15 |
|       1 | 0xFFFDDF15  |  4294827797 |
|       2 | 0x190BB     |      102587 |
|       3 | 0x00F9      |         249 |
|       4 | 0x001E      |          30 |
|       5 | 0x000D      |          13 |
|       6 | 0xFFFF15AF  |  4294907311 |
|       7 | 0xFFFF2646  |  4294911558 |
|       8 | 0xFFFFFD8B  |  4294966667 |
|       9 | 0xFFFDD7BF  |  4294825919 |
|      10 | 0x1883D     |      100413 |
|      11 | 0xFFFDCA88  |  4294822536 |
|      12 | 0x1873A     |      100154 |
|      13 | 0x0127      |         295 |

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

### Event 101

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 6F 1E 53  33 06 01 1C 04 80 00     .....o.S3...... 
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=-139.499*, Z=102.587*, Y=0.249*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0016 [0x1E] EventEntity looks at Boo Kyeko the Ironfaith (ID: 17183571/0x01063353) and starts talking
  5: 0x001B [0x1C] WAIT(30* ticks)
  6: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 05 80 1F 00 06 80 07 80  08 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=-59.985*, Z=-55.738*, Y=-0.629*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x00] END_REQSTACK()
```

### Event 102

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         92 01 F8               ...
0030: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x002D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0033 [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0034  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x0034 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   32 05 80 1F 00             2....
0040: 09 80 0A 80 03 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x003B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=-141.377*, Z=100.413*, Y=0.249*
  2: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0048 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                32 05 80 1F 00 0B            2.....
0050: 80 0C 80 0D 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x004A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=-144.760*, Z=100.154*, Y=0.295*
  2: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0057 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0058 [0x00] END_REQSTACK()
```
