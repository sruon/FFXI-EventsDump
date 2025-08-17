# 17162757 - Dantie-Corantie

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 160 bytes                    |
| Total Events     | 11                           |
| References Count | 10                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [126](#event-126)        | 0x0001       |      1 |              1 |
| [123](#event-123)        | 0x0002       |      1 |              1 |
| [124](#event-124)        | 0x0003       |      1 |              1 |
| [125](#event-125)        | 0x0004       |      1 |              1 |
| [65535.1](#event-655351) | 0x0005       |      1 |              1 |
| [127](#event-127)        | 0x0006       |      1 |              1 |
| [65535.2](#event-655352) | 0x0007       |     20 |              6 |
| [65535.3](#event-655353) | 0x001B       |     15 |              5 |
| [65535.4](#event-655354) | 0x002A       |     15 |              5 |
| [142](#event-142)        | 0x0039       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x1ACA      |        6858 |
|       2 | 0xFFFD889B  |  4294805659 |
|       3 | 0xFFFFEF67  |  4294963047 |
|       4 | 0x0E50      |        3664 |
|       5 | 0x06D6      |        1750 |
|       6 | 0x0000      |           0 |
|       7 | 0x041B      |        1051 |
|       8 | 0xFFFFF631  |  4294964785 |
|       9 | 0xFFFFFFF5  |  4294967285 |

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

### Event 126

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

### Event 123

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

### Event 124

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 125

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                00                                      .          
```

#### Opcodes

```
  0: 0x0005 [0x00] END_REQSTACK()
```

### Event 127

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   00                                    .         
```

#### Opcodes

```
  0: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      32  00 80 1F 00 01 80 02 80         2........
0010: 03 80 1F 01 6F 1E F0 FF  FF 7F 00                 ....o......     
```

#### Opcodes

```
  0: 0x0007 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000A [0x1F] MOVE_ENTITY: EventEntity moves to X=6.858*, Z=-161.637*, Y=-4.249*
  2: 0x0012 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0014 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0015 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   32 00 80 1F 00             2....
0020: 04 80 05 80 06 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x001B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=3.664*, Z=1.750*, Y=0.000*
  2: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                32 00 80 1F 00 07            2.....
0030: 80 08 80 09 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x002A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=1.051*, Z=-2.511*, Y=-0.011*
  2: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0037 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0038 [0x00] END_REQSTACK()
```

### Event 142

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0039  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             00                             .      
```

#### Opcodes

```
  0: 0x0039 [0x00] END_REQSTACK()
```
